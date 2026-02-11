---
permalink: /advanced/safety/
---

## Safety

### **No Implicit Downcasts**
Standard conversions only apply when no information is lost.

~~Not OK~~ or OK is
- `Int8` ->
    - `Int8`, `Int16`, `Int32`, `Int64`, `Int128`, `Int256`, `BigInt`
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`~~
    - `Float16`, `Float32`, `Float64`, `Float128`, `Float256`, `BigFloat`
- `UInt8` ->
    - `UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`
    - ~~`Int8`,~~ `Int16`, `Int32`, `Int64`, `Int128`, `Int256`, `BigInt`
    - `Float16`, `Float32`, `Float64`, `Float128`, `Float256`, `BigFloat`
- `Int16` ->
    - ~~`Int8`,~~ `Int16`, `Int32`, `Int64`, `Int128`, `Int256`, `BigInt`
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`~~
    - ~~`Float16`,~~ `Float32`, `Float64`, `Float128`, `Float256`, `BigFloat`
- `UInt16` ->
    - ~~`UInt8`,~~ `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`
    - ~~`Int8`, `Int16`,~~ `Int32`, `Int64`, `Int128`, `Int256`, `BigInt`
    - ~~`Float16`,~~ `Float32`, `Float64`, `Float128`, `Float256`, `BigFloat`
- `Int32` ->
    - ~~`Int8`, `Int16`,~~ `Int32`, `Int64`, `Int128`, `Int256`, `BigInt`
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`~~
    - ~~`Float16`, `Float32`,~~ `Float64`, `Float128`, `Float256`, `BigFloat`
- `UInt32` ->
    - ~~`UInt8`, `UInt16`,~~ `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`
    - ~~`Int8`, `Int16`, `Int32`,~~ `Int64`, `Int128`, `Int256`, `BigInt`
    - ~~`Float16`, `Float32`,~~ `Float64`, `Float128`, `Float256`, `BigFloat`
- `Int64` ->
    - ~~`Int8`, `Int16`, `Int32`,~~ `Int64`, `Int128`, `Int256`, `BigInt`
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`~~
    - ~~`Float16`, `Float32`, `Float64`,~~ `Float128`, `Float256`, `BigFloat`
- `UInt64` ->
    - ~~`UInt8`, `UInt16`, `UInt32`,~~ `UInt64`, `UInt128`, `UInt256`, `BigUInt`
    - ~~`Int8`, `Int16`, `Int32`, `Int64`,~~ `Int128`, `Int256`, `BigInt`
    - ~~`Float16`, `Float32`, `Float64`,~~ `Float128`, `Float256`, `BigFloat`
- `Int128` ->
    - ~~`Int8`, `Int16`, `Int32`, `Int64`, `Int128`,~~ `Int256`, `BigInt`
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`~~
    - ~~`Float16`, `Float32`, `Float64`, `Float128`,~~ `Float256`, `BigFloat`
- `UInt128` ->
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`,~~ `UInt128`, `UInt256`, `BigUInt`
    - ~~`Int8`, `Int16`, `Int32`, `Int64`, `Int128`,~~ `Int256`, `BigInt`
    - ~~`Float16`, `Float32`, `Float64`, `Float128`,~~ `Float256`, `BigFloat`
- `Int256` ->
    - ~~`Int8`, `Int16`, `Int32`, `Int64`, `Int128`,~~ `Int256`, `BigInt`
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`~~
    - ~~`Float16`, `Float32`, `Float64`, `Float128`, `Float256`,~~ `BigFloat`
- `UInt256` ->
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`,~~ `UInt256`, `BigUInt`
    - ~~`Int8`, `Int16`, `Int32`, `Int64`, `Int128`, `Int256`,~~ `BigInt`
    - ~~`Float16`, `Float32`, `Float64`, `Float128`, `Float256`,~~ `BigFloat`
- `BigInt` ->
    - ~~`Int8`, `Int16`, `Int32`, `Int64`, `Int128`, `Int256`,~~ `BigInt`
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `BigUInt`~~
    - ~~`Float16`, `Float32`, `Float64`, `Float128`, `Float256`,~~ `BigFloat`
- `BigUInt` ->
    - ~~`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`,~~ `BigUInt`
    - ~~`Int8`, `Int16`, `Int32`, `Int64`, `Int128`, `Int256`,~~ `BigInt`
    - ~~`Float16`, `Float32`, `Float64`, `Float128`, `Float256`,~~ `BigFloat`

### Signed Size
Using [**signed `Int` as size**](/cilia/basics/signed-size/)

### **Range & Validation Checks**
The low hanging fruit would be to enable _by default_, also in release builds (not only in debug):
- range checks, to detect **buffer overflows** or similar,
- safe iterators, to detect invalid iterators.
    - So every safe iterator would have a pointer to the element _and_ a pointer to the container.
        - Naive: check at every dereferencing
        - Optimized: check at first dereferencing, but thereafter only after a call to a non-const member function of the container (or if such a call cannot be excluded).

This should fix the majority of C/C++ security issues.  
To achieve maximum performance in all cases, there could be a third build configuration for even faster, but potentially unsafe builds.

So we would have:
- **Debug**
    - for debugging,
    - with range checks,
    - with line by line debug info, and
    - often with a modified memory layout (to find more types of errors).
- **Release**
    - for deployment,
    - _with_ range checks,
    - suitable for most situations,
    - by default using _safe_ containers (with safe iterators),
        - optionally using unsafe containers (with unsafe iterators),
    - with memory layout compatible to ~~EvenFasterBut~~UnsafeRelease.
- ~~EvenFasterBut~~**UnsafeRelease**
    - for deployment,
    - _without_ range checks (for even better performance),
    - by default still using _safe_ containers (with safe iterators),
        - so memory layout is compatible to Release,
    - _optionally_ using unsafe containers (with unsafe iterators, for even better performance).

### **Initialization**
- No initialization means random values. In this case they are in fact often zero, but _not always_.
- Initializing large arrays (e.g. `Array`, `Image`, `Vector`, or `Matrix` with many elements) takes a noticeable amount of time, so we don't want to always initialize everything.
    - With virtual memory it could actually be (almost) "free" to initialize _large_ arrays with zero. But only when using heap memory directly. Small memory regions, that were used before, still need to be overwritten with zeros.
- We could consider it an error (or at least warn) if not initialized,  
  and use a keyword `noinit` to avoid that warning/error.  
  ```
  Int i         // Error
  Int j noinit  // Ok
  Int j = 1     // Ok
  ```
- Classes / custom types
    - Mark constructors with `noinit` when they do not initialize their values, so `noinit` should be used when calling them consciously.
    - ```
      class Array<type T> {
          Array(Int size) noinit { ... }
          Array(Int size, T value) { ... }
      }
      Array<Float> anArray(10)         // Warning
      Array<Float> anArray(10) noinit  // No warning
      Array<Float> anArray(10, 1.0)    // No warning
      ```
- Also for free memory/heap
    - ```
      var arrayPtr = new Array<Float>(10)         // Warning
      var arrayPtr = new Array<Float>(10) noinit  // No warning
      var arrayPtr = new Array<Float>(10, 1.0)    // No warning
      ```

### Safe / Unsafe
**`safe`** code blocks as default, **`unsafe`** as escape.  
Mainly to guide developers:
- to signal what to do and what not to do,
- `unsafe` is not regularly used, normally you just use the already _existing_, carefully developed and tested abstractions (like `Array`, `Vector`, `Matrix`, ...).

Not allowed in safe code:
- Subscript access to pointers,
- `reinterpretCastTo<T>(...)`,
- calling functions marked as `unsafe`,
- use of `noinit`.

Still allowed/undetected in unsafe code:
- Integer overflow (checking that all the time seems too costly)

`unsafe` code is _necessary_ to implement certain abstractions (like container classes):
```
operator[Int i] -> T& {
  if CHECK_BOUNDS and (i < 0 or i >= size) {
      terminate()
  }
  unsafe {
      return data[i]
  }
}
```
A function with unsafe code does not necessarily have to be marked as `unsafe` itself. `unsafe` is a marker for those parts (subfunctions or code blocks) that are not safe (i.e. dangerous) and need to be checked carefully.

Functions containing unsafe code enclosed in an `unsafe` block _do not_ have to be marked with `unsafe` themselves. Only functions containing unsafe code _not_ enclosed in an `unsafe` block have to be marked with `unsafe` themselves. Unsafe is transitive (from an `unsafe` inner function to the outer function), but limited to the scope of `unsafe` blocks.

### Int with Overflow Check
`cilia::safe::Int` is like `cilia::Int`, but with **overflow check** for all operations, may throw OverflowException (or abort the program).
- `safe::Int8`/`Int16`/`Int32`/`Int64`
- `safe::UInt`
    - `safe::UInt8`/`UInt16`/`UInt32`/`UInt64`

Generally considered to be too costly for "normal" integers, even in languages that are otherwise considered as "safe".

### Not like Rust
No further safety features planned beyond C++:
- Not as in [Rust](https://www.rust-lang.org/) or [Hylo](https://www.hylo-lang.org/),
    - that is just out of scope.
- No _additional_ thread safety measures.
    - A thread safety issue can easily lead to a deadlock or crash, and sometimes can even be a security problem.
    - But while thread safety can be a hard problem, there are currently no plans to extend the possibilities beyond plain C++ here (mainly because I am not aware of / familiar with better solutions than already available/recommended in C++).
