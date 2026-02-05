---
permalink: /basics/control-flow/
---

## Control Flow

Branches, loops, and exceptions,  
without braces around the condition clause (as in Python, Swift, Go, Ruby).

### Conditional Branches
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

Chained comparison as in Cpp2 (Herb Sutter), Python, Julia
```
if 1 <= x <= 10 { ... }
```

### Loops
- **while**
  ```
  while a > b {
      // ...
  }
  ```

- **do-while**
  ```
  do {
      // ...
  } while a > b
  ```

- **for-in**
    - as in Swift, Rust
    - Write
      ```
      for str in ["a", "b", "c"] {
          // ...
      }
      ```
      instead of ~~`for (... : ...)`~~ AKA range-for in C++, ~~`for each`~~ in C++/CLI, or ~~`foreach`~~ in C#.
    - Use the **range operator** to write
        - `for i in 1..10 { ... }`  
          instead of ~~`for (Int i = 1; i <= 10; ++i) { ... }`~~,  
          translates to `for i in Range(1, 10) { ... }`.
        - `for i in 0..<10 { ... }`  
          instead of ~~`for (Int i = 0; i < 10; ++i) { ... }`~~,  
          translates to `for i in RangeExclusiveEnd(0, 10) { ... }`.
        - `for i in 10..1:-1 { ... }`  
          instead of ~~`for (Int i = 10; i >= 1; --i) { ... }`~~,  
          translates to `for i in RangeByStep(10, 1, -1) { ... }`.
        - I find this for-loop-syntax so intriguing that I accept the somewhat complex details of the range operator (with all its variants).
    - The variable is declared "with the loop", with its type inferred from the range, array, etc. used (similar to `var`, but only with the options `in` (the default), `inout`, `copy`, `move`),  
      so `for i in 0..<10 { <Body> }` is equivalent to:
      ```
      {
          var i = 0
          while i < 10 {
              <Body>
              ++i
          }
      }
      ```
    - _Not every_ C/C++ for-loop can be expressed as a Cilia for-loop,  
      but in general, any C/C++ for-loop can be converted into a while-loop.
        - ```
          for (<Initialization>; <Condition>; <Increment>) {
              <Body>
          }  
          ```
          can be written as
          ```
          {
              <Initialization>
              while <Condition> {
                  <Body>
                  <Increment>
              }
          }
          ```
        - IMHO the code is even more clear when written as while-loop.
        - Note: When the `<Condition>` is empty, then it needs to be replaced with `True`,
            - e.g. `for (;;) { ... }` is translated to `while True { ... }`.

### Switch / Case
With implicit ~~`break`~~, i.e `break` is the default, and it is not necessary to explicitly write it (like in Swift). Use `fallthrough` if necessary.
- ```
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

### Exceptions
```
try {
    // ...
} catch Exception ex {
    print(ex)
}
```
```
try {
    // ...
} catch Exception ex {
    print(ex)
} catch {
    print("An unknown exception has occured")
}
```
