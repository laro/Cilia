---
title: Basics.Types
permalink: /basics/types/
order: 0
---

## Basic / Arithmetic Types
- `Bool`
    - not ~~`bool`~~ nor ~~`Boolean`~~
- `Int` == `Int64`
    - As in Swift and Go.
    - `Int` == `Int32` on 32 bit systems only (i.e. old/small platforms),
        - `Int` == `Int16` on 8 and 16 bit systems (i.e. very old/small microcontrollers with 16 bit addresses, like AVR / Atmel ATmega328 / Arduino Uno, or old home computers with 6502, Z80).
    - `Int8`, `Int16`, `Int32`, `Int64`
    - `UInt`, `UInt8`, `UInt16`, `UInt32`, `UInt64`
    - Simply use `Int`,
        - _not_ ~~`Size`~~, ~~`SSize`~~, nor ~~`PtrDiff`~~,
        - _not_ ~~`Long`~~ nor ~~`LongLong`~~.
- `Byte` == `std::byte` (i.e. _not_ the same type as UInt8 for parameter overloading)
- `Float`
    - `Float` == `Float64`, i.e. double precision is "standard"
        - Like Python. Unlike C/C++, where `float` is single precision.
        - "[Every language is a child of its time](https://www.stroustrup.com/devXinterview.html)"
            - With modern processors double precision is very fast.
            - When concerned with memory bandwith, cache size, and SIMD performance, choose one of the smaller floating-point types.  
            But then `BFloat16`, `Float8`, or even `Float4` maybe better than `Float32`.
        - `Float` == `Float32` on old/small platforms only (i.e. those with hardware support for `Float32` but not for `Float64`),
    - `Float16`, `Float32`, `Float64` (half, single, double precision floating point)
