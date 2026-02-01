---
title: Cilia
permalink: /
order: 0
---

# Cilia

This is a collection of ideas for a language that is based on C++, but with
- **CamelCase Style**  
I'd like to have the standard library roughly in the style of Java or [Qt](https://wiki.qt.io/Qt_Coding_Style). In addition to being my personal favourite, this could also attract many developers currently using those languages (to a lesser degree also C#, JavaScript/TypeScript, Kotlin, Swift).
- **Simplified Syntax**  
Many of C++'s shortcomings stem from the fact that it inherited from C or that backwards compatibility with existing code must be guaranteed. Cilia can call into C++ (and vice versa), but is a separate language, so its _syntax_ does not need to be backwards compatible with C++.

Cilia is mainly a new syntax for C++, so it has the same core features:
- compiled to machine code,
- statically typed,
- high performance & low-level control,
- object-oriented (with classes, inheritance, polymorphism),
- generic programming (with templates, concepts),
- memory & resource management with [RAII](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization) & smart pointers (instead of garbage collection),
- exceptions, const correctness,
- compile-time computation, coroutines, static reflection.

Furthermore it is a collection of – in my opinion – quite obvious ideas. And mostly taken from other programming languages, of course.

Currently it is more of a wish list, a "thought experiment".
But a transpiler seems to be feasible (like Herb Sutter is doing it with Cpp2).
In the long run one could imagine a Cilia parser/frontend, producing an AST for the common backend of an existing C++ compiler (like clang).


## Cilia by Example
- `Int`, `Int32`, `Int64`, `Float`
- `Int x = 42`
    - `var x = 42`
    - `const x = 42`
    - `String[] words`
    - `Set<String> names`
    - `ContactInfo[String] contactInfoForID`
- `func multiply(Int a, b) -> Int { return a * b }`
    - `func print(ContactInfo a) { ... }`
    - `func concat(String a, b) -> String { return a + b }`
- `for i in 1..10 { ... }`
    - `for i in 0..<words.size() { ... }`
    - `for i in [5, 7, 11, 13] { ... }`
    - `for word in words { ... }`

Corresponding examples for C++, Cpp2, Carbon, Rust, Swift, and Kotlin are given [separately](/comparison/).


## CamelCase Style
Roughly in the style of Qt and Java (or JavaScript, TypeScript, Kotlin, Swift).

- All types and **classes** in **UpperCamelCase** (AKA PascalCase).
    - `Bool`, `Int`, `Int32`, `UInt`, `BigInt`, `Float`
    - `String`, `Array`, `Map`, `ForwardList`, `UnorderedMap`, `ValueType`

- **Variables**/instances/objects in **lowerCamelCase**
    - `Int i`
    - `String word`
    - `String[] words`
    - `ContactInfo[String] contactInfoForID`
    - Feel free to bend/break this rule, e.g. name matrices as `Matrix M, R, L`

- **Functions** in **lowerCamelCase**
    - `str.findFirstOf(...)`
    - `arr.pushBack(...)`
    - `Thread::hardwareConcurrency()`

- **Global constants** in **UpperCamelCase**.
    - `Pi`, `SpeedOfLight`, `Euler` (feel free to bend/break this rule, e.g. define a constant `const e = Euler`)
    - Constant-like keywords
        - `True`, `False`
        - `NullPtr`
        - `NaN`, `Infinity`
    - But keep _local_ constants in lowerCamelCase:  
        - `const Int lastIndex = 100` instead of ~~`const Int LastIndex = 100`~~

- Namespaces fully lowercase
    - `cilia`
    - `cilia::gui`, `cilia::cli`
    - `cilia::lapack`, `cilia::geometry`
    - I don't think this is that important, but it helps to differentiate between classes and namespaces.


## No Trailing Semicolons
For better readability.  
When we are at it, after a quick look at Python, Kotlin, Swift, JavaScript, Julia.
- Typically a statement or expression ends with the end of a line.
- Multiline expressions:
    - Explicitly via `\` at end of line,
        - it is no whitespace after this continuation-backslash allowed
        - (as in Python).
    - Up to closing of `(...)` or `[...]`
        - (also as in Python).
- Multiple expressions in a single line _are_ separated by semicolon.  
  `x += offset; y += offset`
- Disadvantages:
    - Errors are less easily recognized (Walter Bright / D: „Redundancy helps“)
    - Probably a completely new parser must be written, as the one from clang (for C++) no longer fits at all.
- Only in REPL:
    - Trailing semicolon used to suppress evaluation output,  
      as in Matlab, Python, Julia.
    - See [cling](https://root.cern/cling/)


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

## Better Readable Keywords
C++ has a "tradition" of complicated names, keywords or reuse of keywords, simply as to avoid compatibility problems with old code, which may have used one of the new keywords as name (of a variable, function, class, or namespace). Cilia can call into C++ (and vice versa), but is a separate language, so its syntax does not need to be backwards compatible.

- Cilia has
    - `var` instead of ~~`auto`~~
    - `func` instead of ~~`auto`~~
    - `type` instead of ~~`typename`~~
    - `await` instead of ~~`co_await`~~
    - `yield` instead of ~~`co_yield`~~
    - `return` instead of ~~`co_return`~~
    - `and`, `or` in addition to `&&`/`&`, `||`/`|`
    - `xor` in addition to `!=`/`^`
    - `not` in addition to `!`
- `Int32` instead of `int32_t` or `qint32`,
    - so no postfix "_t" nor prefix "q", and in CamelCase.
- When translating C++ code to Cilia then change conflicting names, e.g.
    - `int var` -> `Int __variable_var`
    - `class func` -> `class __class_func`
    - `yield()` -> `func __function_yield()`

## More topics
- [Details](/cilia/details/)
- [Misc](/cilia/misc/)

