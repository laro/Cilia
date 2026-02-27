---
permalink: /basics/types/
description: "Cilia basic types: Bool, Int (Int8–Int64), UInt, Byte, Float. Int defaults to Int64 like Swift and Go."
---

# Basic / Arithmetic Types

- `Bool`
- `Int`
    - `UInt`, `Byte`
- `Float`  


## Width-Specified Types

| Int   | UInt   | Float   |
|-------|--------|---------|
| Int8  | UInt8  |         |
| Int16 | UInt16 | Float16 |
| Int32 | UInt32 | Float32 |
| Int64 | UInt64 | Float64 |


## Notes

It is `Bool`, not ~~`bool`~~ nor ~~`Boolean`~~.

Simply use `Int` (that is `Int64`, like in Swift and Go),
- _not_ ~~`Size`~~, ~~`SSize`~~, nor ~~`PtrDiff`~~,
- _not_ ~~`Long`~~ nor ~~`LongLong`~~.

`Int` is `Int32` on systems with a 32-bit address bus only (i.e. old/small platforms, like Win32/x86),  
`Int` is `Int16` on systems with a 16-bit address bus (i.e. very old/small microcontrollers like AVR/ATmega328/Arduino Uno, 6502, Z80).

`Byte` is `std::byte`, i.e. _not_ the same type as `UInt8` for parameter overloading.

`Float` is `Float64` / double precision (like in Python, unlike C/C++).  
`Float` is `Float32` on old/small platforms only (i.e. those with hardware support for `Float32` but not for `Float64`).  
With modern processors double precision is very fast.
When concerned with memory bandwidth, cache size, and SIMD performance, choose one of the smaller floating-point types like `Float32`
or (if available) `BFloat16`, `Float8`, maybe even `Float4`.
