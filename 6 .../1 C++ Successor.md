---
permalink: /more/cpp-successor/
---

## C++ "Successor" Language / Syntax

Cilia is similar to
- [Cpp2/CppFront](https://github.com/hsutter/cppfront#cppfront),
- [Carbon](https://github.com/carbon-language/carbon-lang), or
- [Circle](https://github.com/seanbaxter/circle),

and a bit like the evolution
- from Java to Kotlin,
- from Objective-C to Swift.


### Why a new language, why not extending C++?

- The [CamelCase style](/#camelcase-style) could basically be archieved in C++, too
- C++ could be extended by some features:
    - Aliasing of member names (functions and variables) seems necessary for having a CamelCase standard library, that is realized as a shallow but "perfect" wrapper for the C++ standard library (i.e. a translation layer).
- Some parts are impossible – or at least extremely unlikely – to include in a future C++ standard:
    - [Const reference as default type](/basics/functions/#function-parameter-passing-modes) for function parameters
    - [Fixing C++ "wrong defaults"](/more/other-ideas/#circle)
        - Restricting integral promotions and no implicit narrowing conversions, etc.
    - New array declaration (`Int[3] array` instead of `Int array[3]`, `Int[] array` instead of `vector<Int> array`)
    - [New/simplified keywords](/#better-readable-keywords)
    - [No trailing semicolons](/#no-trailing-semicolons)


### Why "Cilia"?

Starting with "C" is a kind of tradition.  
All the most obvious names (like [D](https://dlang.org/), [C2](http://c2lang.org/), [C3](https://c3-lang.org), [Cpp2](https://github.com/hsutter/cppfront#cppfront), [Cone](https://cone.jondgoodwin.com/)) and many others were already taken `¯\_(ツ)_/¯`.  
[Julia](https://julialang.org) is a nice language,
so now Cilia got a "[cute](https://forum.qt.io/topic/132893/qt-pronunciation)" name.  
"C/Celia" comes to mind, too 🤠.
