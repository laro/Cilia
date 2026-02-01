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
- 
- `Int x = 42`
- `var x = 42`
- `const x = 42`
- `String[] words`
- `Set<String> names`
- `ContactInfo[String] contactInfoForID`
- 
- `func multiply(Int a, b) -> Int { return a * b }`
- `func print(ContactInfo a) { ... }`
- `func concat(String a, b) -> String { return a + b }`
- 
- `for i in 1..10 { ... }`
- `for i in 0..<words.size() { ... }`
- `for i in [5, 7, 11, 13] { ... }`
- `for word in words { ... }`

Corresponding examples for C++, Cpp2, Carbon, Rust, Swift, and Kotlin are given [separately](/comparison/).
