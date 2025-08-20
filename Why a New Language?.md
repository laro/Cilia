# Why a new language, why not extending C++?
- The [CamelCase style](#camelcase-style) could basically be archieved in C++, too
- C++ could be extended by some features:
    - Aliasing of member names (functions and variables) seems necessary for having a CamelCase standard library, that is realized as a shallow but "perfect" wrapper for the C++ standard library (i.e. a translation layer).
- Some parts are impossible – or at least extremely unlikely – to include in a future C++ standard:
   - [Const reference as default type](#functionloop-parameter-passing) for function parameters
   - [Fixing C++ "wrong defaults"](Interesting%20Ideas%20from%20Other%20Languages.md#circle)
       - Restricting integral promotions and no implicit narrowing conversions, etc.
   - New array declaration (`Int[3] array` instead of `Int array[3]`, `Int[] array` instead of `vector<Int> array`)
   - [New/simplified keywords](#better-readable-keywords)
   - [No trailing semicolons](#no-trailing-semicolons)

# Why "Cilia"?
- The names [D](https://dlang.org/), [C2](http://c2lang.org/), [C3](https://c3-lang.org), and [Cpp2](https://github.com/hsutter/cppfront#cppfront) were already taken,  
  as well as [Cone](https://cone.jondgoodwin.com/) and many others `¯\_(ツ)_/¯`.
