---
permalink: /basics/types/
---

## Basic / Arithmetic Types

- `Bool`
- `Int` == `Int64`
    - `Int8`, `Int16`, `Int32`, `Int64`
    - `UInt`, `UInt8`, `UInt16`, `UInt32`, `UInt64`
- `Byte`
- `Float` == `Float64`  
    - `Float16`, `Float32`, `Float64`


### Notes

It is `Bool`, not ~~`bool`~~ nor ~~`Boolean`~~.

Simply use `Int` == `Int64`, as in Swift and Go,
- _not_ ~~`Size`~~, ~~`SSize`~~, nor ~~`PtrDiff`~~,
- _not_ ~~`Long`~~ nor ~~`LongLong`~~.

`Int` == `Int32` on 32 bit systems only (i.e. old/small platforms),  
`Int` == `Int16` on 8 and 16 bit systems (i.e. very old/small microcontrollers with 16 bit addresses, like AVR, Atmel ATmega328, Arduino Uno, or old home computers with 6502, Z80).

`Byte` == `std::byte`, i.e. _not_ the same type as UInt8 for parameter overloading.

`Float` == `Float64`, so it is double precision, like Python, unlike C/C++.  
`Float` == `Float32` on old/small platforms only (i.e. those with hardware support for `Float32` but not for `Float64`),
With modern processors double precision is very fast.
When concerned with memory bandwith, cache size, and SIMD performance, choose one of the smaller floating-point types.
But then (when available) `BFloat16`, `Float8`, or even `Float4` might be even better than `Float32`.
