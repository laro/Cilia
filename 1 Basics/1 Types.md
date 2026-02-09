---
permalink: /basics/types/
---

## Basic / Arithmetic Types

- `Bool`
- `Int` == `Int64`
    - `Int8`, `Int16`, `Int32`, `Int64`
- `UInt`
    - `UInt8`, `UInt16`, `UInt32`, `UInt64`
- `Byte`
- `Float` == `Float64`  
    - `Float16`, `Float32`, `Float64`


### Notes

It is `Bool`, not ~~`bool`~~ nor ~~`Boolean`~~.

Simply use `Int` == `Int64`, as in Swift and Go,
- _not_ ~~`Size`~~, ~~`SSize`~~, nor ~~`PtrDiff`~~,
- _not_ ~~`Long`~~ nor ~~`LongLong`~~.

`Int` == `Int32` on systems with a 32-bit address bus only (i.e. old/small platforms, like Win32, Amiga, Atari, in general Motorola 68K, Intel 386, old SPARC, MIPS, POWER),  
`Int` == `Int16` on systems with a 16-bit address bus (i.e. very old/small microcontrollers like AVR/ATmega328/Arduino Uno, in general 6502 or Z80 CPUs of classic 8-bit home computers).

`Byte` == `std::byte`, i.e. _not_ the same type as `UInt8` for parameter overloading.

`Float` == `Float64`, so it is double precision, like Python, unlike C/C++.  
`Float` == `Float32` on old/small platforms only (i.e. those with hardware support for `Float32` but not for `Float64`).  
With modern processors double precision is very fast.
When concerned with memory bandwidth, cache size, and SIMD performance, choose one of the smaller floating-point types like `Float32`
or (if available) `BFloat16`, `Float8`, or even `Float4`.
