---
permalink: /advanced/is-as-casting/
description: "Cilia is/as: type queries (obj is Int), safe casts (obj as T). Replaces dynamic_cast, std::get, value()."
---

# `is`, `as`, Casting


## `is` (Type Query)

See Cpp2 [is](https://hsutter.github.io/cppfront/cpp2/expressions/#is-safe-typevalue-queries):
- `obj is Int` (i.e. a type)
- `objPtr is T*` instead of `dynamic_cast<T*>(objPtr) != NullPtr`
- `obj is cilia::Array` (i.e. a template)
- `obj is cilia::Integer` (i.e. a concept)

> **TODO**
> Also support value query?


## `as`
See Cpp2 [as](https://hsutter.github.io/cppfront/cpp2/expressions/#as-safe-casts-and-conversions)
- `obj as T` instead of `T(obj)`
- `objPtr as T*` instead of `dynamic_cast<T*>(objPtr)`
- With `Variant v` where T is one alternative:  
    `v as T` instead of `std::get<T>(v)`
- With `Any a`:  
    `a as T` instead of `std::any_cast<T>(a)`
- With `Optional<T> o`:  
    `o as T` instead of `o.value()`


## Constructor Casting

- `Float(3)`
- Casting via constructor is `explicit` by default, `implicit` as option.
- No classic C-style casting: ~~`(Float) 3`~~


## Classical C++ Casts

All of these also work for smart pointers (`T^`, `T+`, `T-`), replacing ~~`std::*_pointer_cast`~~.

- `staticCastTo<T>(...)`
    - instead of ~~`static_cast<T>(...)`~~
- `dynamicCastTo<T>(...)`
    - instead of ~~`dynamic_cast<T>(...)`~~
    - But typically `objPtr as T*` is preferred.
- `castToMutable<T>(...)` or `castToMutable(...)`
    - instead of ~~`const_cast<T>(...)`~~
- `reinterpretCastTo<T>(...)`
    - instead of `reinterpret_cast<T>(...)`
- `castTo<T>(...)`?
    - A general, safe cast, i.e. like `as`, but in function syntax.
- Other casts of the C++ standard library (and GSL):
    - `bitCastTo<T>(...)` instead of ~~`std::bit_cast<T>(...)`~~
    - `anyCastTo<T>(a)` instead of ~~`std::any_cast<T>(a)`~~
        - But typically `a as T` is preferred.
    - `durationCastTo<T>(d)` instead of ~~`std::chrono::duration_cast<T>(d)`~~
    - `timePointCastTo<T>(t)` instead of ~~`std::chrono::time_point_cast<T>(t)`~~
    - `narrowCastTo<T>(...)` instead of ~~`gsl::narrow_cast<T>(...)`~~ (unchecked)
    - `narrowTo<T>(...)` instead of ~~`gsl::narrow<T>(...)`~~ (checked)
