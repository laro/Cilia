---
permalink: /advanced/is-as-casting/
description: "Cilia is/as: type queries (obj is Int), safe casts (obj as T). Replaces dynamic_cast, std::get, value()."
---

# `is`, `as`, Casting

- `is` (type query)
    - See Cpp2 [is](https://hsutter.github.io/cppfront/cpp2/expressions/#is-safe-typevalue-queries):
        - `obj is Int` (i.e. a type)
        - `objPtr is T*` instead of `dynamic_cast<T*>(objPtr) != NullPtr`
        - `obj is cilia::Array` (i.e. a template)
        - `obj is cilia::Integer` (i.e. a concept)
    - TODO Also support value query?
- `as`
    - See Cpp2 [as](https://hsutter.github.io/cppfront/cpp2/expressions/#as-safe-casts-and-conversions)
        - `obj as T` instead of `T(obj)`
        - `objPtr as T*` instead of `dynamic_cast<T*>(objPtr)`
        - With `Variant v` where T is one alternative:  
          `v as T` instead of `std::get<T>(v)`
        - With `Any a`:  
          `a as T` instead of `std::any_cast<T>(a)`
        - With `Optional<T> o`:  
          `o as T` instead of `o.value()`
- Constructor casting
    - `Float(3)`
    - Casting via constructor is `explicit` by default, `implicit` as option.
    - No classic C-style casting: ~~`(Float) 3`~~
    - but also
        - `castToMutable<T>(...)` or `mutableCastTo<T>(...)`
            - instead of ~~`constCastTo<>(...)`~~
        - `reinterpretCastTo<T>(...)`
        - `staticCastTo<T>(...)`?
- Automatic casts
    - as in Kotlin,
    - for template types, references and pointers.
    - ```
      func getStringLength(Type obj) -> Int {
          if obj is String {
              // "obj" is automatically cast to "String" in this branch
              return obj.length
           }
          // "obj" is still a "Type" outside of the type-checked branch
          return 0
      }
      ```
    - ```
      func getStringLength(Type obj) -> Int {
          if not obj is String
              return 0
          // "obj" is automatically cast to "String" in this branch
          return obj.length
      }
      ```
    - ```
      func getStringLength(Type obj) -> Int {
          // "obj" is automatically cast to "String" on the right-hand side of "and"
          if obj is String  and  obj.length > 0 {
              return obj.length
          }
          return 0
      }
      ```
    - TODO Multiple inheritance is problematic here:
        - In Cilia/C++, an object can be an instance of several base classes at once, whereby the pointer (sometimes) changes during casting.
        - What if you still want/need to access the functions for a `Type obj` after `if obj is ParentA`?
            - Workaround:
                - In case of multiple inheritance there is no automatic casting.
                - ~~Cast back with `Type(obj).functionOfA()`~~
