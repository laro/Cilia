---
permalink: /basics/control-flow/
description: "Cilia control flow: if/else, switch, for, while without braces around conditions. Exceptions, break, continue."
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
> I am not very fond of this syntax,  
> _but_ in an `if` / `else if` chain it is more efficient, and much more compact, than nesting `if … else { if … else … }`.  
> Also C#, Java, Swift, and Rust all have it.

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
while var pt = stmt->getParent() {
    // ...
}
```
instead of ~~`while (auto pt = stmt->getParent()) { ... }`~~.

```
while Stmt* pt = stmt->getParent() {
    // ...
}
```
instead of ~~`while (Stmt* pt = stmt->getParent()) { ... }`~~.


## Switch / Case

With implicit ~~`break`~~ (like in Swift), i.e `break` is the default, and it is not necessary to explicitly write it. Use `fallthrough` if necessary.
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
