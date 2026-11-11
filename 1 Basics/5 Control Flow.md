---
permalink: /basics/control-flow/
description: "Cilia control flow: if/else, switch, for, while without parentheses around conditions. Exceptions, break, continue."
---

# Control Flow

Branches, loops, and exceptions, without parentheses around the condition clause (as in Python, Swift, Go, Ruby).

`if`, `for`, and `while`/`do` _always_ take a `{...}` body, even for a single statement.

That can still be one line:
```
if a > b { return a }
```


## Conditional Branches
```
if a > b {
    // ...
}
```
```
if a > b {
    // ...
} else {
    // ...
}
```
```
if a > b {
    // ...
} else if a > c {
    // ...
} else {
    // ...
}
```

Chained comparison as in Cpp2 (Herb Sutter), Python, Julia.
```
if 1 <= x <= 10 { ... }
```


## Loops

### While

```
while a > b {
    // ...
}
```


### Loop

Simpler syntax (as in Rust) for cases with complex termination criteria.
```
Int i = 0
loop {
    i = str.find("...", i)
    if i == String.NPos {
        break
    }
    // ...
}
```
instead of ~~`while True { ... }`~~.


### Do-While

```
do {
    // ...
} while a > b
```


### For-In

```
for str in ["a", "b", "c"] {
    // ...
}
```
As in Swift, Rust.  
Instead of ~~`for (... : ...)`~~ AKA range-for in C++, ~~`for each`~~ in C++/CLI, or ~~`foreach`~~ in C#.  

Use the **range operator** to write:  
```
for i in 1..10 { ... }
```
instead of ~~`for (Int i = 1; i <= 10; ++i) { ... }`~~,  
translates to `for i in Range(1, 10) { ... }`.

```
for i in 0..<10 { ... }
```
instead of ~~`for (Int i = 0; i < 10; ++i) { ... }`~~,  
translates to `for i in RangeExclusiveEnd(0, 10) { ... }`.

```
for i in 10..1:-1 { ... }
```
instead of ~~`for (Int i = 10; i >= 1; --i) { ... }`~~,  
translates to `for i in RangeByStep(10, 1, -1) { ... }`.

I find this for-loop-syntax so intriguing that I accept the somewhat complex details of the range operator (with all its variants).

The variable is declared "with the loop", with its type inferred from the range, array, etc. used as source (similar to `var`, but only with the options `in`, `inout`, `copy`, `move`; see [Parameter Passing](https://cilialang.org/advanced/parameter-passing/#loop-variables)).  
So `for i in start..<end { <body> }` is equivalent to:
```
{
    var i = start
    while i < end {
        <body>
        ++i
    }
}
```

_Not every_ C/C++ for-loop can be expressed as a Cilia for-loop,  
but then it (and in general, _any_ C/C++ for-loop) can be converted into a while-loop.
```
for (<initialization>; <condition>; <increment>) {
    <body>
}
```
can be written as
```
{
    <initialization>
    while <condition> {
        <body>
        <increment>
    }
}
```

IMHO the code is even more clear when written as while-loop (though not so dense).
> **Note**  
> When the `<condition>` is empty, then it needs to be replaced with `True`,
> so `for (;;) { ... }` is translated to `while True { ... }`.


## Condition Declaration

The condition of `if` and `while` may itself be a declaration.  
The declared variable is the condition, contextually converted to `Bool`, as in C++.  
A null pointer is `False`.  
The name is in scope in the body, and for `if` also in the `else` branch.

```
if var pt = stmt->getParent() {
    // ...
}
```
instead of ~~`if (auto pt = stmt->getParent()) { ... }`~~.
```
if Stmt* pt = stmt->getParent() {
    // ...
}
```
instead of ~~`if (Stmt* pt = stmt->getParent()) { ... }`~~.


> **Note**  
> I am not particularly fond of this syntax, _but_ in an `if` / `else if` chain it is
> - more efficient, as the function is called only if the else branch is really taken, or
> - much more concise, when compared to the exact equivalent code.
> 
> Also:
> - C++ has it,
> - Swift and Rust have the equivalent `if let`,
> - C# and Java a pattern-based variant (`is` / `instanceof`).

In an `if` / `else if` chain, the next declaration is evaluated only when the previous condition was false:
```
if var pt = stmt->getParent() {
    // ...
} else if var prev = stmt->getPrevious() {
    // ...
} else {
    // ...
}
```
instead of the more verbose and complicated
```
var pt = stmt->getParent()
if pt {
    // ...
} else {
    var prev = stmt->getPrevious()
    if prev {
        // ...
    } else {
        // ...
    }
}
```

<br>
With `while`, the declaration runs again on every iteration:
```
while var task = queue.tryPop() {
    // ...
}
```
instead of ~~`while (auto task = queue.tryPop()) { ... }`~~.

```
while Task* task = queue.tryPop() {
    // ...
}
```
instead of ~~`while (Task* task = queue.tryPop()) { ... }`~~.


## Compile-Time Control Flow

### Consteval If

The condition is evaluated at compile time; the discarded branch is not instantiated.
```
func toString<type T>(T value) -> String {
    consteval if T is Integer {
        return formatInteger(value)
    } else if T is FloatingPoint {
        return formatFloat(value)
    } else {
        return value.toString()
    }
}
```
instead of ~~`if constexpr ( ... ) { ... }`~~.

`consteval` applies to the whole `if` / `else if` chain, so every condition must be a compile-time constant.

> **Note**  
> Not to be confused with C++23 `if consteval { ... }` (which checks whether the code is currently being evaluated at compile time).
> That is possible in Cilia, too.


### Consteval For

The loop is unrolled at compile time, the body is instantiated once per element.  
Useful for iterating over heterogeneous sequences, like tuples, parameter packs, or (static reflection) members of a class.
```
consteval for value in (1, 2.5, "three") {
    print(value)  // `value` has a different type in each iteration
}
```
instead of ~~`template for ( ... ) { ... }`~~ (C++26 expansion statements),
or ~~`std::apply([](auto... v) { ... }, ...)`~~ (fold expressions).


## Switch / Case

With implicit ~~`break`~~ (like in Swift), i.e. `break` is the default, and it is not necessary to explicitly write it. Use `fallthrough` if necessary.
```
switch i {
case 1:
    print("1")
    // implicit break

case 2, 3:
    print("Either 2 or 3")
    // implicit break

case 4:
    // do something
    fallthrough
case 5:
    // do something more
    print("4 or 5")
    // implicit break

default:
    print("default")
}
```


## Exceptions

```
try {
    // ...
} catch Exception ex {
    print(ex)
} catch {
    print("An unknown exception has occurred")
}
```
No ~~`finally`~~, use RAII/RROD instead.
