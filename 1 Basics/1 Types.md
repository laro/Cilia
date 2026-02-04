---
permalink: /basics/types/
---

## Basic / Arithmetic Types

### Bool
`Bool`, not ~~`bool`~~ nor ~~`Boolean`~~.

### Int
Simply use `Int` == `Int64`, as in Swift and Go,
- _not_ ~~`Size`~~, ~~`SSize`~~, nor ~~`PtrDiff`~~,
- _not_ ~~`Long`~~ nor ~~`LongLong`~~.

Fixed width:
- `Int8`, `Int16`, `Int32`, `Int64`
- `UInt`, `UInt8`, `UInt16`, `UInt32`, `UInt64`

`Int` == `Int32` on 32 bit systems only (i.e. old/small platforms),  
`Int` == `Int16` on 8 and 16 bit systems (i.e. very old/small microcontrollers with 16 bit addresses, like AVR / Atmel ATmega328 / Arduino Uno, or old home computers with 6502, Z80).

### Byte
`Byte` == `std::byte`, i.e. _not_ the same type as UInt8 for parameter overloading.

### Float
`Float` == `Float64`, i.e. double precision is "standard".  
Like Python. Unlike C/C++, where `float` is single precision.

Fixed precision:
- `Float16`, `Float32`, `Float64` (half, single, double precision floating point)

With modern processors double precision is very fast.
When concerned with memory bandwith, cache size, and SIMD performance, choose one of the smaller floating-point types.
But then `BFloat16`, `Float8`, or even `Float4` might be better than `Float32`.

"[Every language is a child of its time](https://www.stroustrup.com/devXinterview.html)":
`Float` == `Float32` on old/small platforms only (i.e. those with hardware support for `Float32` but not for `Float64`),
