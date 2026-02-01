---
title: Basics
permalink: /basics/
order: 1
---

# Basics

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

### Signed Size
`Int` (i.e. signed) as type for `*.size()`
- Because mixing signed and unsigned integer (e.g. "signed - unsigned") and even calculating "unsigned - unsigned" is difficult to handle.
    - Problem in C/C++: `aUInt - 1 >= 0` is _always_ true (even if `aUInt` is `0`)
- When working with sizes, calculating the difference is common; Then you are limited to `Int`/~~`SSize`~~/~~`PtrDiff`~~ (i.e. signed integer) anyway.
- Anyone who needs more than 2GB of data in a single "byte array", should please use a 64 bit platform.
- For bounds checking, the two comparisons `x >= 0` and  `x < width` may very well be reduced to a single `UInt(x) < width` _by the compiler_ in an optimization step.
- Then types ~~`Size`~~ and ~~`SSize`~~/~~`PtrDiff`~~ are not necessary anymore, so two types less.
    - We simply use `Int` instead.
    - `UInt` is used in rare cases (i.e. hardware registers, masks, flags), surely _not_ for sizes.
- See also Going Native 2012, Day 2, Interactive Panel: Ask Us Anything
    - [42:41 - 45:28](https://youtu.be/Puio5dly9N8?feature=shared&t=2561)
        - Bjarne Stroustrup and Herb Sutter recommend using _signed_ integer.
    - [1:02:51 - 1:03:14](https://youtu.be/Puio5dly9N8?feature=shared&t=3771)
        - Herb Sutter and Chandler Carruth about _unsigned_ `size_t` in the C++ STL containers: "They are wrong", "We are sorry"
