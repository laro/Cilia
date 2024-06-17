# Cilia
**C++ with CamelCase Style**  
I'd like to have the standard library in the [style of Qt](https://wiki.qt.io/Qt_Coding_Style), and (a variant of) Qt with the standard library classes as base (and with exceptions, and with namespaces instead of the prefix "Q").
  
**C++ with Simplified Syntax**  
Many of C++'s shortcomings stem from the fact that it inherited from C or that backwards compatibility with existing code must be guaranteed.
Cilia can call into C++ (and vice versa), but is a separate language, so its _syntax_ does not need to be backwards compatible.

**C++ without Semicolons**  
When we are at it, after a quick look at Julia and Python. 


## Introduction
- Ideas / a wish list for an "improved" C++
    - with a **simplified** syntax,
    - in the **[style of Qt](https://wiki.qt.io/Qt_Coding_Style)**, Objective-C, Java, JavaScript, Kotlin, Swift
    - Isomorphic mapping of all C++ functionality to Cilia possible
        - only with other/better/shorter "expression".
- C++ "Successor Language / Syntax"
    - like [CppFront/Cpp2](https://github.com/hsutter/cppfront#cppfront), [Carbon](https://github.com/carbon-language/carbon-lang), or [Circle](https://github.com/seanbaxter/circle)
    - Similar to C -> C++, Java -> Kotlin, Objective-C -> Swift, JavaScript -> TypeScript
- While "[C++11 feels like a new language](https://www.stroustrup.com/tour2preface.pdf)",  
  Clilia should feel like (a modernized) C++.
- Uses the same compiler backend as C++ (clang, gcc, ...)  
  with an own / a new compiler frontend (or a precompiler).
- So _no_ garbage collection,  
  instead in Cilia you use, as in C++,
    - automatic/stack variables
    - **RAII** (Resource Acquisition is Initialization)
        - I'd like to call it "RROD" (Resource Release on Object Destruction)
    - `SharedPtr<T>` / `T^` etc.
- The names [D](https://dlang.org/), [C2](http://c2lang.org/), and [Cpp2](https://github.com/hsutter/cppfront#cppfront) were already taken,  
  as well as [Cone](https://cone.jondgoodwin.com/) and many others `¯\_(ツ)_/¯`.
    - "Cilia" signals something in between [C](https://en.wikipedia.org/wiki/C_(programming_language))/[C++](https://en.wikipedia.org/wiki/C%2B%2B) and [Julia](https://julialang.org)  
      (so maybe I could add some more of Julias interesting features to this wish list).
- Why a new language, not extending C++?
    - The [CamelCase style](#style) could basically be archieved in C++, too
    - C++ could be extended by some features:
        - Aliasing of member names (functions and variables) seems necessary for having a CamelCase standard library, that is realized as a shallow wrapper for the C++ standard library (i.e. a translation layer).
    - Some parts are impossible or at least extremely unlikely, to include in a future C++ standard:
       - [Const reference as default type](#const-reference-as-default-type) for function arguments
       - [Fixing C++ "wrong defaults"](#fix-c-wrong-defaults)
           - Restricted integral promotions and implicit narrowing conversions, etc.
       - New array declaration (`Int[] array` instead of `Int array[]`)
       - [New/simplified keywords](#better-readable-keywords)
       - [No trailing semicolons](#No-trailing-semicolons)


## Comparison with C++, Cpp2, and Carbon
Cilia is, in my opinion, a collection of quite obvious ideas, but tastes and opinions differ:  
Carbon and Cpp2 ("C++ syntax 2") are based on the same basic idea, a new syntax with C++ interoperability, but both with a syntax more resembling Rust than C++.  

[Bjarne Stroustrup in an interview (2000):](https://www.stroustrup.com/devXinterview.html)
> Today, I'd look for a much simpler syntax—and probably clash with people's confusion between the familiar and the simple.

I don't know what exact syntax Bjarne Stroustrup would prefer today, but indeed Cpp2 and Carbon do not feel familiar to me. 
I like many aspects especially of Cpp2, but _not_ its `name: Type` syntax.
IMHO it is not necessary to go from the "most vexing parse" right to the "most easy parse".

- Cilia
    - `Int`, `Int32`, `Int64`, `Float`
    - `Int x = 42`
        - `var x = 42`
        - `Circle[] circles` (short form for `Array<Circle> circles`)
        - `Map<String, Circle> mapStringsToCircles`
    - `func multiply(Int x, y) -> Int { return x * y }`
    - `for i in 1..10 { ... }`
    - `for i in 0..<words.size() { ... }`
    - `for i in [5, 7, 11, 13] { ... }`
- C++
    - `int`, `int32_t`, `int64_t`, `float`
    - `int x = 42;`
        - `auto x = 42;`
        - `vector<Circle> circles;`
        - `map<string, Circle> mapStringsToCircles`
    - `auto multiply(int x, int y) -> int { return x * y; }`
    - `for (int i = 1; i <= 10; ++i) { ...; }`
    - `for (int i = 0; i < words.ssize(); ++i) { ...; }`
    - `for (int i : {5, 7, 11, 13}) { ...; }`
- Cpp2
    - `int`, `i32`, `i64`, `f32`
    - `x: int = 42;`
        - `x := 42;`
        - `circles: vector<Circle>;`
        - `mapStringsToCircles: map<string, Circle>;`
    - `multiply: (x: int, y: int) -> int = x * y;`
    - `i := 1;`  
      `while i <= 10 next i++ { ...; } `          
    - `i := 0;`  
      `while i < words.ssize() next i++ { ...; } `          
    - `for (5, 7, 11, 13) do (i) { ...; }`
- Carbon
    - `i32`, `i64`, `f32`
    - `var x: i64 = 42;`
        - `var x: auto = 42;`
        - `var circles: Array(Circle);`
        - `var mapStringsToCircles: HashMap(String, Circle);`
    - `fn multiply(x: i64, y: i64) -> i64 { return x * y; }`
    - `var i: i64 = 1;`  
      `while (i <= 10) { ...; ++i; }`
    - `var i: i64 = 0;`  
      `while (i < words.ssize()) { ...; ++i; } `          
    - `for (i:i64 in (5, 7, 11, 13)) { ...; }`


## C++ Language Family
- **Compatible to C++**, C and maybe other languages of this "**language family**" / "**ecosystem**", even future ones,
    - as with
        - Java: Kotlin, Scala, Groovy, Clojure, Fantom, Ceylon, Jython, JRuby ...
        - C#: C++/CLI, Visual Basic .NET, F#, A# (Ada), IronPython, IronRuby ...
        - Objective-C: Swift
    - Bi-directional interoperability, so it is possible to include
        - C++ headers and modules from Cilia,
        - Cilia headers and modules from C++.
    - The compiler recognises the language (C, C++, or Cilia) by
        - the file extension
            - Cilia: `*.cilia` `*.hilia`  &nbsp;  `*.cl` `*.hl`
            - C++: `*.cpp` `*.hpp` &nbsp; `*.cxx` `*.hxx` &nbsp; `*.h`
                - `*.h` is of course a problem, as the header could be C or C++ code.  
                  So use of `*.hpp` is recommended for C++ code.  
                  This can probably best be solved using path based rules.
            - C: `*.c` `*.h`
        - path based rules
            - to handle C or C++ standard headers in certain directories 
        - can be set in IDE
            - for each file individually 


## CamelCase Style
Roughly in the style of Qt, Objective-C/C++, Java, JavaScript, TypeScript, Kotlin, Swift

- All types and **classes in upper CamelCase**.
    - Basic/arithmetic types
        - `Bool`
        - `Int`, `Int8`, `Int16`, `Int32`, `Int64`, `UInt`, `BigInt`
        - `Byte`, `Char`
        - `Float`, `Float32`, `Float64`, `BFloat16`, `BigFloat`
    - Cilia standard library (`cilia::` instead of `std::`)
        - `cilia::String` instead of `std::string`
        - `Array`, `Map`, `ForwardList`, `UnorderedMap`, `ValueType`

- **Functions in lower camelCase**
    - `str.findFirstOf(...)`
    - `vec.pushBack(...)`

- Namespaces fully lowercase 
    - `cilia`
    - `cilia::numerics`
    - `cilia::geometry`
    - I don't think this is that important, but it helps to differentiate between classes and namespaces.


## No Trailing Semicolons
As in Python, Kotlin, Swift, JavaScript, Julia.
- Advantage:
    - Better readability
- Disadvantage:
    - Errors are less easily recognized
        - Walter Bright / D: „Redundancy helps“
    - This probably means that a completely new parser must be written, as the one from clang (for C++) no longer fits at all.
        - ~~As this is difficult & unclear/disputed: Keep C++ semicolons for now?~~
- Multiline expressions:
    - Explicitly via `\` or `(...)` / `[...]` / `{...}` as in Python
    - ~~Implicitly/clever as in Swift, Kotlin and JavaScript?~~
- Multiple expressions in a single line _are_ separated by semicolon.  
  `x += offset; y += offset`
- Only in REPL:
    - Trailing semicolon used to suppress evaluation output,
        - as in Matlab, Python, Julia.


## Better Readable Keywords
C++ has a "tradition" of complicated names, keywords or reuse of keywords, simply as to avoid compatibility problems with old code, which may have used one of the new keywords as name (of a variable, function, class, or namespace). Cilia can call into C++ (and vice versa), but is a separate language, so its syntax does not need to be backwards compatible.

- Cilia has
    - `var` instead of `auto`
    - `func` instead of `auto`
    - ~~`class ... extends ...` instead of `class ... : ...`~~
        - ~~`class ... implements ...` instead of `class ... : ...` for pure abstract classes (like interfaces)~~
    - `type` instead of `typename`
    - `await` instead of `co_await`
    - `yield` instead of `co_yield`
    - `return` instead of `co_return`
    - `and`, `or`, `xor`, `not` instead of `&&`, `||`, `^`, `!`
        - as in Python, Carbon
        - Used for both
            - boolean operation
                - `aBool`**`and`**`anotherBool` -> `Bool`
            - bitwise operation
                - `anInt`**`and`**`anotherInt` -> `Int`
- `Int32` instead of `int32_t` or `qint32`,
    - so no prefix "q" nor postfix "_t".
- When translating C++ code to Cilia then change conflicting names, e.g.
    - `int var` -> `Int __variable_var`
    - `class func` -> `class __class_func`
    - `yield()` -> `func __function_yield()`


## Basic / Arithmetic Types
- `Bool`
    - not ~~`bool`~~ nor ~~`Boolean`~~
- `Int`, `UInt`
    - `Int` == `Int64`
        - `Int` == `Int32` on 32 bit systems only (i.e. old/small platforms).
        - _No_ ~~`Size`~~ or ~~`SSize`~~, use `Int` instead.
    - `Int8`, `Int16`, `Int32`, `Int64`
        - like `int32_t` or `qint32`, but no prefix "q" nor postfix "_t", and in CamelCase
        - maybe `Int128`, `Int256`
    - `UInt8`, `UInt16`, `UInt32`, `UInt64`
        - maybe `UInt128`, `UInt256` e.g. for SHA256
- `Byte` == `UInt8` (Alias, i.e. the same type for parameter overloading)
- `BigInt` – Arbitrary Precision Integer
    - for cryptography, maybe computer algebra, numerics
    - see [Boost.Multiprecision](https://www.boost.org/doc/libs/1_79_0/libs/multiprecision/doc/html/index.html), [GMP](https://gmplib.org)
- `Float`
    - `Float` == `Float32`
        - Among other things because this is how it works in C/C++
        - Is faster than Float64 and good enough most of the time
    - ~~`Float` == `Float64`~~
        - ~~Among other things because already in C/C++ `1.0` == `Float64` and `1.0f` == `Float32`~~
        - ~~`Float32` only on certain platforms~~
    - `Float16`, `Float32`, `Float64` (half, single, double precision floating point)
        - maybe `Float128`, `Float256`
            - typically probably realized as double-double respectively double-double-double-double
            - [https://stackoverflow.com/a/6770329](https://stackoverflow.com/a/6770329)
    - `BFloat16` (Brain Floating Point)
    - Mixed arithmetic:
        - `1 * aFloat` is possible
            - Warning, if the integer literal cannot be reproduced exactly as `Float32`/`64`
        - `anInt * aFloat` is possible
            - Warning that the integer variable may not be reproduced exactly as `Float32`/`64`, i.e. with
                - `aFloat32 * anInt8`  // OK
                - `aFloat32 * anInt16` // OK
                - `aFloat32 * anInt32` // Warning
                - `aFloat32 * anInt64` // Warning
                - `aFloat64 * anInt8`  // OK
                - `aFloat64 * anInt16` // OK
                - `aFloat64 * anInt32` // OK
                - `aFloat64 * anInt64` // Warning
    - `BigFloat<>` for arbitrary precision float,
        - see [GMP](https://gmplib.org), [MPFR](https://www.mpfr.org)
        - The precision is arbitrary but fixed, either
          - statically, i.e. at compile time, as part of the BigFloat type, or
          - dynamically, i.e. at runtime, as property of a BigFloat variable.


## Variable Declaration
`Int i` as variable declaration, just as in C/C++.
- `var i = 3` only for type inference  
  instead of ~~`auto i = 3;`~~
    - ~~Maybe possible to simply write `i = 3`?~~
    - ~~Maybe `i := 3`?~~
- Not
    - ~~`var Int i`~~
    - ~~`var i : Int`~~
    - ~~Or is having `func` for function declaration, but not `var` for variable declaration, still not clear enough?~~
        - ~~Swift, Kotlin and Circle always start variable declarations with `var`.~~
        - ~~Not starting with `var` could be problematic in connection with omitting the trailing semicolons.~~
- Examples:
    - `Int anInt`
    - **`Float* i, j`   // i _and_ j are pointers**
        - contrary to C/C++.
    - `const Complex<Float>& complexNumber = complexNumberWithOtherName`
    - `const Float*`
    - `const Float const*`
- Not allowed / syntax error is:
    - ~~`Float* i, &j`~~
        - Type variations within multiple-variable declarations are _not_ allowed.
        - It has to be the exactly same type.
    - ~~`Float*i`~~
        - Whitespace _between_ type specification and variable name is mandatory.


## Classes
- Quite as in C++
  ```
  class MyVectorOfInt {
  public:
      Int* numbers = Null
      Int size = 0
  }
  ```


## Arrays & ArrayViews
- `Int[] dynamicArrayOfIntegers`
    - „Dynamic array“ with **dynamic size**
      ```
      Int[] array(3)
      array[2] = 0
      array[3] = 0  // Runtime error, no compile time bounds check
      ```
    - `T[] array` is the short form of `cilia::Array<T> array`
        - Not called `cilia::Vector<T>`, because this could easily collide with the mathematical (numerical/geometric) Vector.
          (See Matrix & Vector, even though they are in other sub-namespaces.)
    - May be confusing because it is so similar to fixed-size arrays,  
      **but** IMHO the inconsistency is already in C/C++:
        - while in C/C++ function declarations:
            - `int[]` and `int*` are actually the same,
        - for local variables in C/C++ you write:
            - `int array[3]` and `int array[] = { 1, 2, 3 }` for in-place arrays,  
              but `int* array = new int[3]` for an int-array of unknown size, so
            - `int[]` and `int*` mean different things.
- `Int[3] arrayOfThreeIntegers`  
  (instead of ~~`Int arrayOfThreeIntegers[3]`~~ in C/C++)
    - „Static array“ with **fixed size**
      ```
      Int[3] array
      array[2] = 0
      array[3] = 0  // Compilation error, due to compile time bounds check
      ```
    - `arrayOfThreeIntegers.size()` -> `3`
        - realized as extension function `func<type T, Int N> T[N]::size() -> Int { return N }`
- Use `Int*` for "raw" C/C++ arrays of arbitrary size  
  ```
  Int* array = new Int[3]  // Array-to-pointer decay possible
  array[2] = 0
  array[3] = 0  // Undefined behaviour, no bounds check at all
  ```
    - Recommended to _not_ use subscript for raw pointers anyway,  
      except for implementation of abstractions (like Array, Vector, Matrix, ...).
- Actually this is how to handle pointer to array of Int "correctly":
  ```
  Int[3]* arrayPtr = new Int[3]
  *arrayPtr[2] = 0
  *arrayPtr[3] = 0  // Compilation error, due to compile time bounds check
  ```
- Examples:
    - `Int[] dynamicArrayOfInt`
    - `Int[3] arrayOfThreeInt`
    - `Int[3]* pointerToArrayOfThreeInt`
    - `Int[3][]* pointerToDynamicArrayOfArrayOfThreeInt`
    - `String*[] dynamicArrayOfPointersToString`
- ArrayViews AKA Slices AKA Subarrays
    - `var subarray = array[1..2]`
    - `var subarray = array[1..<3]`
    - Incomplete ranges (need lower and/or upper bounds before use) are
      typcally implemented as inline functions that determine the concrete bounds an then call `array[start..end]` (or one of the exclusive counterparts).
        - `var subarray = array[..2]`
        - `var subarray = array[..]`
    - See Rust [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- Multidimensional arrays
    - dynamic size
        - `Int[,] dynamic2DArray`  
            - `T[,] array` is the short form of `cilia::MDArray<T, 2> array`
        - `Int[,,] multidimensionalDynamicArray`  
            - `T[,,] array` is the short form of `cilia::MDArray<T, 3> array`
        - and so on:  
            - `cilia::MDArray<T, N>`
    - static size
        - `Int[3, 2, 200]`
            - Multidimensional static array  
              ```
              Int[3, 2, 200] intArray3D
              intArray3D[2, 1, 199] = 1
              ```
- Mixed forms of static and dynamic array
    - `Int[3][,] dynamic2DArrayOfArrayOfThreeInt`  
       ~~not `Int[3,,]`~~
    - `Int[3,4][] dynamicArrayOfThreeByFourArrayOfInt`  
       ~~not `Int[3,4,]`~~


## Signed Size
`Int` (i.e. signed) as type for `*.size()`
- Because mixed integer arithmetic ("signed - unsigned") and "unsigned - unsigned" is difficult to handle.
    - In C/C++ `aUInt - 1 >= 0` is _always_ true (even if `aUInt` is `0`)
- When working with sizes, calculating the difference is common; Then you are limited to `PtrDiff` (i.e. signed integer) anyway.
- Who needs more than 2GB of data in a single "array", should please use a 64 bit platform.
- For bounds checking, the two comparisons `x >= 0` and  `x < width` may very well be reduced to a single `UInt(x) < width` _by the compiler_ in an optimization step. 
- Then types `Size` and `SSize`/`PtrDiff` are not necessary anymore, so two types less.
    - We simply use `Int` instead. Or `UInt` in rare cases.
- Restricted rules for mixed integer arithmetic:
    - `Unsigned +-*/ Signed` is an error
        - you have to cast
        - `Int` (i.e. signed) is almost always used anyways
    - Error with `if aUInt < 0`
        - if the literal on the right is `<= 0`
    - Error with `if aUInt < anInt`
        - you have to cast
- Not:
    - ~~`UInt` as type for `*.size()` (i.e. still unsigned)~~  
      ~~but with new rules for mixed integer arithmetic:~~
        - ~~Unsigned +-*/ Signed -> Signed.~~
            - ~~Signed is therefore considered the "larger" type compared to unsigned~~
            - ~~`1` is `Int` (signed)~~
                - ~~`1u` is `UInt` (unsigned)~~
            - ~~Therefore `if aUInt - 1 >= 0` is a useful expression (as `1` is signed, `aUInt - 1` is signed, too)~~
            - ~~But then also `aUInt + 1 == anInt`~~
    - ~~Or~~
        - ~~`Size` - `Size` -> `SSize`~~
            - ~~Problem: `-` results in `SSize`, but `+` results in `Size`?!~~
        - ~~The conversion of a negative number into `Size` leads to an error instead of delivering a HUGE size.~~


## Functions
- Function declarations start with the keyword `func`:
  ```
  func multiplyAdd(Int x, y, Float z) -> Float {
      return x * y  +  z
  }
  ```
    - `func` as in Swift
    - ~~or `fn` (Rust, Carbon, New Circle), `fun` (Kotlin), `function` (Julia)~~
    - Easier parsing due to clear distinction between function vs. variable declaration.
- Always and only in the trailing return type syntax.
- `func function2(`**`Int x, y`**`) -> Float` // x _and_ y are Int
- **Lambdas**
    - `[](Int i) -> Float { i * 3.14 }`  
      as in C++
- **Extension methods**
    - To add "member like" functions to "third party" classes/types.
    - Can be called like normal member functions, but they but do not have access to private or protected members themselves.
    - Also possible for arithmetic types (like `Int i; i.toString()`)
        - `func Int::toString() -> String { ... }`  // as in Kotlin
            - ~~or `func toString (Int this) -> String` ~~
- **Function pointers**
    - Difficult to maintain consistency between declarations of functions, function pointers, functors and lambdas.
    - Variant A:
        - **`func(Int, Int -> Int)* pointerToFunctionOfIntAndIntToInt`**
        - **`func(Int)* pointerToFunctionOfInt`**
        - `func(Int, Int -> Int)& referenceToFunctionOfIntAndIntToInt` // Can't be zero; is that useful?
        - `func(Int)& referenceToFunctionOfInt`
    - ~~Variant B:~~
        - ~~`func((Int, Int) -> Int)* pointerToFunctionOfIntAndIntToInt`  // Closer to the function declaration but (too) many brackets~~
    - ~~Variant C:~~
        - ~~`(Int, Int -> Int)` [Functions are only available as pointers, so you can omit "*"?]~~
    - ~~Variant D:~~
        - ~~`func*(Int->Int) pointerToFunctionOfIntAndIntToInt`~~
        - ~~`func*(Int) pointerToFunctionOfInt`~~
    - ~~Variant E:~~
        - ~~`func*(Int, Int)->Int pointerToFunctionOfIntAndIntToInt`~~
        - ~~`(func*(Int, Int)->Int)[] arrayOfPointersToFunctionOfIntAndIntToInt`~~

          
## Operators
- `a^x` for `pow(a, x)` (as Julia)
    - ~~or `a**x`? (as Python)~~
- ~~Remove `++i`, `--i`, `i++`, `i--`?~~
    - ~~as Python~~
    - ~~only offer/allow `i += 1`, `i -= 1`~~
- Default `operator==`
    - If not defined, then
        - use negated `operator!=` (if defined), or
        - use `operator<=>` (if defined), or
        - use elementwise comparison with `==`
            - Only possible if all elements themselves offer the `operator==`.
            - Optimization for simple types: Byte-by-byte comparison.
- Default `operator!=`
    - If not defined, then
        - use negated `operator==` (if defined), or
        - use `operator<=>` (if defined), or
        - use negated generated `operator==`.
- `>>` Shift right (logical shift with UInt, arithmetic shift with Int)
- `<<` Shift left (here a logical shift with UInt is the same as arithmetic shift with Int)
- `>>>` Rotate right (circular shift right)
- `<<<` Rotate left (circular shift left)


## `if`, `while`, `for ... in` Branches & Loops
No braces around the condition clause.
- if
    - ```
      if a > b {
          // ...
      }
      ```
    - ```
      if a > b {
          // ...
      } else {
          // ...
      }
      ```
    - ```
      if a > b {
          // ...
      } else if a > c {
          // ...
      } else {
          // ...
      }
      ```
    - `if 1 <= x <= 10 { ... }`
        - as in Python, Julia, Cpp2 (Herb Sutter)
- while
  ```
  while a > b {
      // ...
  }
  ```
- do ... while
  ```
  do {
      // ...
  } while a > b
  ```
- `for ... in ...`
    - as in Rust, Swift
    - Write
      ```
      for str in ["a", "b", "c"] {
          // ...
      }
      ```
      instead of `for (... : ...)` (AKA C++ range-for, C++/CLI `for each`, C# `foreach`)
    - The loop variable is declared "in the loop", with its type inferred from the range, array, etc. used (similar to `var`).
    - Use the range literal to write          
      `for i in 0..<10  { ... }`  
      instead of `for (Int i = 0; i < 10; ++i) { ... }`
        - `for i in 1..10 { ... }`  
          translates to `for i in Range(1, 10) { ... }`
        - `for i in 1..<10 { ... }`  
           translates to `for i in RangeExclusiveEnd(1, 10) { ... }`
        - Write  
          `for i in 10..1:-1  { ... }`  
          instead of `for (Int i = 10; i > 0; --i)  { ... }`
        - Translates to `for i in RangeWithStep(10, 1, -1) { ... }`
        - Alternatively write
            - `for i in (1..10).reversed()`
            - `for i in RangeWithStep(10..1, -1)`
    - In general you can replace a C/C++ `for`-loop
      ```
      for (<Initialization>; <Condition>; <Increment>) {
          <Body>
      }  
      ```
      with `while`
      ```
      <Initialization>
      while <Condition> {
          <Body>
          <Increment>
      }
      ```
      (OK, curly braces around all of this are necessary to be a perfect replacement.)


## Templates
- **Class** templates
  ```
  class MyVector<Number T> {
      T* numbers = Null
      Int size = 0
  }
  ```
- **Function** templates
    - _Automatic_ function templates
        - If (at least) one of the function arguments is a concept, then the function is (in fact) a function template.
            - Concept `Number`:
              ```
              func sq(Number x) -> Number {
                   return x * x
              }
              ```
                - However, the return type could be a different type than `x` is (as long as it satisfies the concept `Number`)
            - `func add(Number a, b) -> Number`
                - Even `a` and `b` (and of course the return type) could each be a _different_ type (as long as they satisfy the concept `Number`)
            - Concept `Real` (real numbers as `Float16`/`32`/`64`/`128` or `BigFloat`):
              ```
               func sqrt(Real x) -> Real {
                   // ... a series development ...
                  // (with number of iterations determined from the size of the mantissa)
              }
              ```
        - Like abbreviated function templates in C++ 20, only without `auto`.
    - _Explicit_ function templates for cases where a common type is required.
        - ```
          func add<Number T>(T x, y) -> T {
               return x + y
          }
          ```
        - Not ~~`func<Number T> add(T x, y) -> T { return x + y }`~~
    - For extension function templates it is necessary to know the template parameter(s) for the type that shall be extended, before we write the function name.  
      Therefore we write
        - `func<type T, Int N> T[N]::size() -> Int { return N }`
            - Not ~~`func T[N]::size<type T, Int N>() -> Int { return N }`~~
            - Maybe `template<type T, Int N> func T[N]::size() -> Int { return N }`?
            - ~~Maybe `class<type T, Int N> func T[N]::size() -> Int { return N }`?~~
                - `T[N]` is not even a `class`, it's a type.
        - `func<type T, Int N> T[N]::convertTo<type TOut>() -> TOut[N] { ... }`  
            - Not ~~`func T[N]::convertTo<type T, Int N, type TOut>() { ... }`~~  
              as with  
              `Float[3] arrayOfThreeFloat = { 1.0, 2.0, 3.0 }`  
              we would write  
              `Int[3] arrayOfThreeInt = arrayOfThreeFloat.convertTo<Int>()`  
              not  
              ~~`Int[3] arrayOfThreeInt = arrayOfThreeFloat.convertTo<Float, 3, Int>()`~~  
            - The template parameters `T` and `N` belong to the type of the object `arrayOfThreeFloat` and are determined already. It would not be possible to change them in the call of `convertTo<>()`, so it is not desired to specify them here at all.
            - Maybe `template<type T, Int N> func T[N]::convertTo<type TOut>() -> TOut[N] { ... }`?
            - ~~Maybe `class<type T, Int N> func T[N]::convertTo<type TOut>() -> TOut[N] { ... }`?~~
                - `T[N]` is not even a `class`, it's a type.

    - `requires` for further restricting the type.
        - ```
          func sq<Number T>(T x) -> T requires (T x) { x * x } {
               return x * x
          }
          ```
        - TODO Really this syntax: `{ ... } { ... }`?
- Template **type alias** (with `using`, not ~~`typedef`~~)
    - `using<type T> T::InArgumentType = const T&`
    - ~~Or `template<type T> using T::InArgumentType = const T&`?~~


## Function/Loop Parameter Passing
- Function call arguments and the loop variable of "for ... in" are **by default passed as `in`**.
- Explicit override with keywords **`inout`**, **`out`**, **`copy`**, **`move`**, **`forward`**.
- Wording fits nicely for function arguments,  
  and also for `for` loops, then these words describe how the information (i.e. the variable) gets into the body of the loop (or out of it).
- Parameter passing keywords:
    - **`in`**
        - Is the default if no parameter passing keyword is given.
        - Technically either `const X&` or `const X` (sometimes `const XView`)
            - `const X&` as default:
                - **`concat(String first, String second)`**  
                    - is effectively translated to `concat(const String& first, const String& second)`  
                      (or to `concat(const StringView first, const StringView second)`, if the `X`/`XView`-trick is implemented)
                - **`String[] stringArray = ["a", "b", "c"]`**  
                  **`for str in stringArray { ... }`**
                    - `str` is `const String&`  
                      (or `const StringView`, if the `X`/`XView`-trick is implemented)
            - `const X` for "small types":
                - `for i in [1, 2, 3] { ... }`
                    - `i` is `const Int`
                - `for i in 1..<10 { ... }`
                    - `i` is `const Int`
                - `for str in ["a", "b", "c"] { ... }`
                    - `str` is `const StringView` (a string-literal like `"a"` is a `const StringView`, therefore `["a", "b", "c"]` is a `StringView[]`)
    - **`inout`**
        - to mark as mutable/non-const reference.
        - Technically a non-const/mutable reference (`X&`)
        - Also at the caller `swap(inout a, inout b)`
        - Examples:
            - `for inout str in stringArray { ... }`
                - `str` is `String&`
            - `for inout i in [1, 2, 3] { ... }`
                - `i` is `Int&`
    - **`out`**
        - to mark as (non-const) reference.
        - Technically, like `inout`, a non-const/mutable reference (`X&`), but without prior initialization.
        - Also at the caller
          ```
          String errorDetails
          if not open("...", out errorDetails) {
              cout << errorDetails
          }
          ```
    - **`copy`**
        - to create a (mutable) copy (i.e. pass "by value"). 
        - Technically a non-const/mutable value (`X`)
        - Examples:
            - `for copy str in stringArray { ... }`
                - `str` is `String`
            - `for copy i in [1, 2, 3] { ... }`
                - `i` is `Int`
    - **`move`**
        - for move sematics.
        - Technically a right-value reference (`X&&`)
    - **`forward`**
        - for perfect forwarding.
        - Technically a right-value reference (`X&&`)?
- Type traits `InArgumentType` to determine the concrete type to be used for `in`-passing.
    - Use const _reference_ (`const&`) as general default.
        - `using<type T> T::InArgumentType = const T&`  
    - A "list of exceptions" for the "const _value_ types" (`const X`).
        - ```
          using Bool::InArgumentType       = const Bool
          using Int32::InArgumentType      = const Int32
          using Int64::InArgumentType      = const Int64
          using Float32::InArgumentType    = const Float32
          using Float64::InArgumentType    = const Float64
          using StringView::InArgumentType = const StringView
          ```
        - `using<type T> Complex<T>::InArgumentType = T::InArgumentType`
            - A generic rule.
            - Could be further refined/corrected  
              `using Complex<Float128>::InArgumentType = const Complex<Float128>&`
    - Special trick for **types with views**, e.g. `String`/`StringView`:  
      `using String::InArgumentType = const StringView`,  
      so _all_ functions with an `in String` parameter would implicitly accept a `String` and _also_ a `StringView`. So people do not necessarily need to understand the concept of a `StringView`, they simply write `String`, and nonetheless there is no need to define two functions (one for `String` and one for `StringView`).  
      If you want to change the string argument, a `in String` AKA `const StringView` is not suitable anyway.
        - Example:
            - **`concat(String first, String second)`**  
                - extends to `concat(const StringView first, const StringView second)`
            - **`String[] stringArray = ["a", "b", "c"]`**  
              **`for str in stringArray { ... }`**
                - `str` is `const StringView`
        - Applicable only for types `X` that can implicitly be converted/reduced to `XView`,  
          like:  
            - `String` -> `StringView`
            - `Array` -> `ArrayView`
            - `Vector` -> `VectorView`
            - `Matrix` -> `MatrixView`
            - `Image` -> `ImageView`
            - `MDArray` -> `MDArrayView` (AKA MDSpan?)
    - If you want even the basic type to be different:
        - `for Double d in [1, 2, 3] { ... }`
            - `d` is `const Double`
        - `for String str in ["a", "b", "c"] { ... }`
            - `str` is `const String&` (not `const StringView&`)
        - `for inout String str in ["a", "b", "c"] { ... }`
            - `str` is `String&`
        - `for copy String str in ["a", "b", "c"] { ... }`
            - `str` is `String`


## Literals
- `True`, `False` are Bool,
    - as in Python,
    - as they are constants.  
    - ~~`true`, `false` are Bool~~
- `Null` is the null pointer,
    - it is of the type `NullPtr`,
        - (or should `NullPtr` be the null pointer, and `NullPtrType` its type?)
    - explicit cast necessary to convert any pointer to `Int`.
- `123` is an integer literal of arbitrary precision
    - Can be converted to any integer type it fits into (signed and unsigned)
        - `Int8 a = 1`    // Works because `1` fits into `Int8`
        - `Int8 b = 127`  // Works because `127` fits into `Int8`
        - `Int8 c = 128`  // _Error_ because 128 does _not_ fit into `Int8`
        - `Int8 d = -128` // Works because `-128` fits into `Int8`
        - `Int8 e = -129` // _Error_ because `-129` does _not_ fit into `Int8`
        - `UInt8 f = 255` // Works because `255` fits into `UInt8`
        - `UInt8 g = 256` // _Error_ because `256` does _not_ fit into `Int8`
        - `UInt8 h = -1`  // _Error_ because `-1` does _not_ fit into `UInt8`
        - `Int16 i = 32767` // Works
        - `Int32 j = 2'147'483'647` // Works
        - `Int64 k = 9'223'372'036'854'775'807` // Works
        - `Int l = a`     // Works because `Int8` fits into `Int32`
        - `UInt m = l`    // _Error_ because `Int` does _not always_ fit into `UInt`
            - `UInt m = UInt(l)` // Works
        - `Int n = m`     // Error because `UInt` does _not always_ fit into `Int`
            - `Int n = Int(m)`   // Works
    - `123` is interpreted as `Int`
        - in case of type inferring, parameter overloading and template matching.
    - Difficult: Constexpr constructor that accepts an arbitrary precision integer literal and can store that in ROM
        - Store as array of `Int`
    - `123u` is `UInt`
    - `-123` is always `Int` (signed)
- `0xffffffff` is `UInt` in hexadecimal
- `0b1011` is `UInt` in binary
- `0o123` is `UInt` in octal
    - as in Python
    - not `0123`, as that is confusing/unexpected, even if it is C++ standard
- `Int` vs. `Bool`
    - ~~`Int a = True`~~      // Error,
        - because `Bool` is _not_ an `Int`
        - because a `Bool` should not be accidentally interpreted as an `Int`
        - cast if necessary: `Int a = Int(True)`
    - ~~`Bool a = 1`~~      // Error,
        - because `Int` is not a `Bool`
        - because an `Int` should not be accidentally interpreted as a `Bool`
        - cast if necessary: `Bool a = Bool(1)` 
- `1.0` is a floating point literal of arbitrary precision
    - Can be converted to any float type into which it fits exactly
        - otherwise explicit cast necessary: `Float16(3.1415926)`
    - Difficult: Constexpr constructor that accepts an arbitrary precision float literal  and can store that in ROM
        - Store the mantissa as arbitrary precision integer (i.e. array of `Int`), plus the exponent as as arbitrary precision integer (i.e. array of `Int`, most always only a single `Int`)
    - `1.0` is interpreted as `Float`
        - in case of type inferring, parameter overloading and template matching.
    - `1.0f` is always `Float32`
    - `1.0d` is always `Float64`
- `Infinity`/`-Infinity` is a floating point literal of arbitrary precision for infinity values
    - Can be converted to any float type
    - Is interpreted as `Float`
        - in case of type inferring, parameter overloading and template matching.
- `NaN` is a floating point literal of arbitrary precision for NaN ("not a number") values
    - Can be converted to any float type
    - Is interpreted as `Float`
        - in case of type inferring, parameter overloading and template matching.
- `1..10` and `1..<10` are range literals
    - as in Kotlin
    - Similar, but diffentent:
        - Swift would be ~~`1...10`~~ and ~~`1..<10`~~
            - I like `...` to be reserved for ellipsis in human language like comments.
        - Rust would be ~~`1..=10`~~ and ~~`1..10`~~
    - Different kinds of ranges:
        - `1..2` – Range(1, 2)
        - `1..<3` – RangeExclusiveEnd(1, 3)
        - `0<..2` – RangeExclusiveStart(0, 2)
        - Incomplete ranges (need lower and/or upper bounds to be set before use)  
            - `..2` – RangeTo(2)
            - `..<2` – RangeToExclusiveEnd(2)
            - `1..` – RangeFrom(1)
            - `0<..` – RangeFromExclusiveStart(0)
            - `..` – RangeFull()
        - Range with step, also used for downwards iterating ranges.  
            - `2..1:-1` – RangeWithStep(2, 1, -1)
            - `2..>0:-1` – RangeWithStepExclusiveEnd(2, 0, -1)
            - `3>..1:-1` – RangeWithStepExclusiveStart(3, 1, -1)
            - Incomplete ranges
                - `..1:-1` – RangeWithStepTo(1, -1)
                - `..>0:-1` – RangeWithStepToExclusiveEnd(1, -1)
                - `2..:-1` – RangeWithStepFrom(2, -1)
                - `3>..:-1` – RangeWithStepFromExclusiveStart(3, -1)
                - `..:-1` – RangeWithStepFull(-1)
            - Wheather (with the exclusive ranges) `<` or `>` is used (i.e. the direction) does not matter.
            - Compile time checks:
                - In case the step value is a compile time constant, then it may be _warned_
                    - if `>` ("greater than") is used for positive steps (i.e. for `1`), or
                    - if `<` ("less than") is used for negative steps (e.g. for `-1`).
                - If both start and end of the range are compile time constants, then it may be warned when the range contains no elements at all (e.g. when start >= end ans step > 0).
        - See Rust [Ranges](https://doc.rust-lang.org/std/ops/index.html#structs) and [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- `"Text"` is a `StringView`
    - Pointer to first character and pointer after the last character
        - in C++ tradition, but length would also work, of course
    - No null termination
        - If necessary
            - use `"Text\0“`  or
            - convert using `StringZ(...)`.
    - Data is typically stored in read-only data segments or ROM.
- Multiline String Literal
    - ```
      """
      First line
      Second line
      """
      ```
    - Removes indentation as in the last line
    - Removes first newline (if the opening """ is on a separate line)
    - Removes last newline (if the closing """ is on a separate line)
    - Similar to Swift, Julia, late Java, ...
    - Also as single line string literal with very few restrictions, good for RegEx
        - `"""(.* )whatever(.*)"""`
- Interpolated Strings
    - `$“M[{i},{j}] = {M[i, j]}"`
        - as in C#
        - Any reason to use/prefer any other syntax?
- Alternative string literals
    - `"Text"utf8` (but UTF-8 is the default anyway)
    - `"Text"utf16`
    - `"Text"utf32`
    - `"Text"ascii`
        - Syntax error, if one of the characters is not ASCII
    - `"Text"latin1`
        - Syntax error, if one of the characters is not Latin-1
    - ~~`"Text"sz` is a zero terminated string (as used in C)~~
        - ~~Problem: How to combine e.g. `"..."ascii` and `"..."sz`?~~
            - Workaround: Use `"Text\0"ascii` instead
    - All these available for multiline string literals and interpolated strings, too.
        - Any reason, not to? 
- `[1, 2, 3]` is an array (here an `Int[]`),
    - all elements have the same type.
- `{1, "Text", 3.0}` is an initialization list
    - e.g. for `Tuple`
- ```
  {
      "Key1": "Value1"
      "Key2": "Value2"
      "Key3": "Value3"
      "Key4": "Value4"
  }
  ```
    - is a `Map<String,String>`
- Rules for user defined literals
    - as in C++.


## Comments
- Single-line comments
    - ```
      // if a < b {
      //   TODO
      // }
      ```
- Block comments can be _nested_
    - ```
      /* This
      /* (and this) */
         is a comment */ 
      ```


## String, Char & CodePoint
- `cilia::String` with _basic/standard_ unicode support.
    - Iteration over a `String` or `StringView` by:
        - **grapheme clusters**
            - represented by `StringView`.
            - This is the _default form of iteration_ over a `String` or `StringView`
            - A single grapheme cluster will typically consist of multiple code units   
              and may even consist of multiple code points.
            - `for graphemeCluster in "abc 🥸👮🏻"`
                - "a", "b", "c", " ", "🥸", "👮🏻"
                - "\x61", "\x62", "\x63", "\x20", "\xf0\x9f\xa5\xb8", "\xf0\x9f\x91\xae\xf0\x9f\x8f\xbb"
            - A bit slow, as it has to find grapheme cluster boundaries.
            - It is recommended to mostly use the standard functions for string manipulation anyway. But if you need to iterate manually over a Unicode-String, then grapheme-cluster-based iteration is the safe/right way. 
            - Additional/alternative names?
                - `for graphemeCluster in text.asGraphemeClusters()`?
                - ~~`for graphemeCluster in text.byGraphemeCluster()`?~~
        - **code points**
            - represented by `UInt32`,
                - independent of the encoding (i.e. the same for UTF-8, UTF-16, and UTF-32 strings).
                - Called "auto decoding" in D.
                - ~~`CodePoint` == `UInt32`~~
                    - ~~No distinct type for code points necessary, or would it be useful?~~
            - `for codePoint in "abc 🥸👮🏻".asCodePoints()`
                - 0x00000061, 0x00000062, 0x00000063, 0x00000020, &nbsp; 0x0001F978, &nbsp; 0x0001F46E, 0x0001F3FB 
            - ~~`for codePoint in text.byCodePoint()`?~~
            - A bit faster than iteration over grapheme clusters, but still slow, as it has to find code point boundaries in UTF-8/16 strings.
            - Fast with UTF-32, **but** even with UTF-32 not all grapheme clusters fit into a single code point,
                - so not:
                    - emoji with modifier characters like skin tone or variation selector,
                    - diacritical characters (äöü..., depending on the normal form chosen),
                    - surely some more ...
                - Often slower than UTF-8, simply due to its size (cache, memory bandwidth).
        - **code units**
            - represented by
                - `Char` for `String`
                    - it is `Char`==`Char8`==`Byte`==`UInt8` and `String`==`UTF8String`
                - `Char16` for `UTF16String`
                - `Char32` for `UTF32String`
            - `for aChar8 in "abc 🥸👮🏻".asArray()`
                - 0x61, 0x62, 0x63, 0x20,  &nbsp;  0xf0, 0x9f, 0xa5, 0xb8,  &nbsp;  0xf0, 0x9f, 0x91, 0xae, 0xf0, 0x9f, 0x8f, 0xbb
                - same for
                    - `for codeUnit in "abc 🥸👮🏻"utf8.asArray()`
                    - `for codeUnit in UTF8String("abc 🥸👮🏻").asArray()`
                    - ? `for codeUnit in "abc 🥸👮🏻".asCodeUnits()`
                    - ~~`for codeUnit in text.byCodeUnit()`?~~
                    - ~~`for codeUnit in text.byChar()`?~~
            - `for aChar16 in "abc 🥸👮🏻"`**`utf16`**`.asArray()`
                - 0x0061, 0x0062, 0x0063, 0x0020,  &nbsp;  0xD83E, 0xDD78,  &nbsp;  0xD83D, 0xDC6E, 0xD83C, 0xDFFB
                - same for `for aChar16 in UTF16String("abc 🥸👮🏻").asArray()`
            - `for aChar32 in "abc 🥸👮🏻"`**`utf32`**`.asArray()`
                - 0x00000061, 0x00000062, 0x00000063, 0x00000020,  &nbsp;  0x0001F978,  &nbsp;  0x0001F46E , 0x0001F3FB
                - same for `for aChar32 in UTF32String("abc 🥸👮🏻").asArray()`
    - `string.toUpper()`, `string.toLower()`
        - `toUpper(Sting) -> String`, `toLower(Sting) -> String`
    - `stringArray.sort()`
        - `sort(Container<String>) -> Container<String>`
    - `compare(stringA, stringB) -> Int`
- `ByteString` to represent the strings with single byte encoding (i.e. the classical strings consisting of one-byte characters),
    - like
        - ASCII
        - Latin-1
        - ANSI (mostly identical to Latin-1)
        - almost every one of the "code pages"
    - Encoding is not defined.
        - The user has to take care of this,
        - or a subclass with known encoding has to be used (`ASCIIString`, `Latin1String`). 
    - `ASCIIString`, a string containing only ASCII characters.
        - Iteration over an `ASCIIString` or `ASCIIStringView` by `Char`==`Char8`==`Byte`
            - `for aChar in "abc"ascii`
                - 0x61, 0x62, 0x63
                - 'a', 'b', 'c'
                - Compilation error, if string literal contains non-ASCII characters.
                - same for `for aChar in ASCIIString("abc")`
                    - but Exception thrown, if string contains non-ASCII characters.
        - Implicitly convertable to `String`==`UTF8String`.
            - Very fast conversion, as all characters have the same binary representation.
    - `Latin1String`, a string containing only Latin-1 (ISO 8859-1) characters.
        - Iteration over an `Latin1String` or `Latin1StringView` by `Char`==`Char8`==`Byte`
            - `for aChar in "äbc"latin1`
                - 0xe4, 0x62, 0x63
                - 'ä', 'b', 'c'
                - Compilation error, if string literal contains non-Latin-1 characters.
                - same for `for aChar in ASCIIString("abc")`
                    - but Exception thrown, if string contains non-Latin1 characters.
        - Explicitly convertable to `String`==`UTF8String`.
            - Not as fast conversion as with ASCIIString, as typically some characters need to be translated into two UTF-8 code units.
- `Char8`, `Char16`, `Char32`
    - are considered as _different_ types for parameter overloading,
    - but otherwise are like `UInt8`, `UInt16`, `UInt32`,
- So no ~~`WideChar`~~
    - ~~Or is it useful for portable code (Linux `UInt32` <-> Windows `UInt16`)?~~
        - ~~You may use `wchar_t` then.~~

- [**ICU**](https://unicode-org.github.io/icu/userguide/icu4c/) ("International Components for Unicode") for advanced Unicode support.
    - "The ICU libraries provide support for:
        - The latest version of the Unicode standard
        - Character set conversions with support for over 220 codepages
        - Locale data for more than 300 locales
        - Language sensitive text collation (sorting) and searching based on the Unicode Collation Algorithm (=ISO 14651)
        - Regular expression matching and Unicode sets
        - Transformations for normalization, upper/lowercase, script transliterations (50+ pairs)
        - Resource bundles for storing and accessing localized information
        - Date/Number/Message formatting and parsing of culture specific input/output formats
        - Calendar specific date and time manipulation
        - Text boundary analysis for finding characters, word and sentence boundaries"
    - `import icu` adds extension methods for `cilia::String`
        - Allows iteration over:
            - words (important/difficult for Chinese, Japanese, Thai or Khmer, needs list of words)
                - `for word in text.asWords()`
                - ~~`for word in text.byWord()`~~
            - lines
                - `for line in text.asLines()`
                - ~~`for line in text.byLine()`~~
            - sentences (needs list of abbreviations, like "e.g.", "i.e.", "o.ä.")
                - `for sentence in text.asSentences()`
                - ~~`for sentence in text.bySentence()`~~
        - Depending on locale
            - `string.toUpper(locale)`, `string.toLower(locale)`
                - `toUpper(Sting, locale) -> String`, `toLower(Sting, locale) -> String`
            - `stringArray.sort(locale)`
                - `sort(Container<String>, locale) -> Container<String>`
            - `compare(stringA, stringB, locale) -> Int`
     

## `cilia` Standard Library
Standard library in namespace `cilia` (instead of `std` to avoid naming conflicts and to allow easy parallel use).
- With Cilia version of every standard class/concept (i.e. CamelCase class names and camelCase function and variable names)
    - `cilia::String` instead of `std::string`
    - `Map` instead of `map`
        - `Dictionary` as alias with deprecation warning, as a hint for C# programmers.
    - `ForwardList` instead of `forward_list`
    - `UnorderedMap` instead of `unordered_map`
    - `ValueType` instead of `value_type`
    - Maybe some exceptions/variations:
        - `Array` instead of `vector`
        - `Stringstream` or `StringStream` instead of `stringstream`?
            - `Textstream` or `TextStream`, `Bytestream` or `ByteStream`, ...
        - `Multimap` or `MultiMap` instead of `multimap`?
- Shallow wrapper,
    - e.g. `cilia::String : public std::string`
- "**Alias**" for 
    - member variables  
      `using x = data[0]`  
      `using y = data[1]`  
        - ~~or `alias x = data[0]`?~~
        - Not quite possible in C++.
            - With ...  
              `Float& imaginary = im`  
              or  
              `T& x = data[0]`  
              ... unfortunately memory is created for the reference (the pointer).
            - And this indeed is necessary here, because the reference could be assigned differently in the constructor, so it is not possible to optimize it away.
    - member functions
        - `using f() = g()`
        - ~~Or is perfect forwarding enough?~~
            - ~~https://stackoverflow.com/a/9864472~~
            - This would not work for virtual functions

- Matrix & Vector
    - Geometry
        - Static/fixed size
        - For small, fixed size vectors & matrices ,
            - as typically used in geometry (i.e. 2D, 3D, 4D).
        - `cilia::geometry::Vector<T = Float, Int size>`
            - `cilia::geometry::Vector2<T = Float>`
            - `cilia::geometry::Vector3<T = Float>`
            - `cilia::geometry::Vector4<T = Float>`
        - `cilia::geometry::Matrix<T = Float, Int rows, Int columns>`
            - `cilia::geometry::Matrix22<T = Float>`
            - `cilia::geometry::Matrix33<T = Float>`
            - `cilia::geometry::Matrix44<T = Float>`
    - Numerics
        - Dynamic/variable size
        - For large, dynamically sized vectors & matrices,
            - as typically used in numerics: BLAS (Basic Linear Algebra Subprograms)
        - `cilia::numerics::Vector<T = Float>`
        - `cilia::numerics::Matrix<T = Float>`
            - stored column-major
        - `cilia::numerics::MDArray<T = Float, Int dimensions>`
            - also see `MDSpan`
          
- Image
    - `cilia::Image<T = Float>`
    - Almost like `cilia::Matrix`, but stored row-major.
      
- Views, Slices
    - `ArrayView`
    - `VectorView`
    - `MatrixView`
    - `ImageView`
    - `MDArrayView`


## Short Smart Pointer Syntax 
- `Type^ instance`, inspired by C++/CLI.
    - `T^` by default is `SharedPtr<T>`
        - for C++/Cilia classes,
        - defined via type traits `SmartPtrType`:  
          `using<type T> T::SmartPtrType = SharedPtr<T>`
    - Possible to redefine for interoperability with other languages:
        - Objective-C/Swift classes: Use their reference counting mechanism.
        - C#/Java classes: Use garbage collected memory, manage a global list of C#/Java instance pointers.


## Safety and Security
- **Range Checks**
    - The low hanging fruit would be to enable range checks _by default_, also in release builds (not only in debug), to detect **buffer overflows** or similar. This should fix the majority of C/C++ security issues.  
      To achieve maximum performance in all cases, there could be a third build configuration for even faster, but potentially unsafe builds.  
      So we would have:
        - Debug (for debugging with line by line debug info, and with range checks)
        - Release (for deployment, with range checks, suitable for most situations)
        - ~~EvenFasterBut~~UnsafeRelease (for deployment when maximum performance is desired, _without_ range checks)
- **Initialization**
    - No initialization means random values. In this case they are in fact often zero, but _not always_.
    - Initializing large arrays (e.g. `Array`, `Image`, `Vector`, or `Matrix` with many elements) takes a noticeable amount of time, so we don't always want to initialize everything.
        - But with virtual memory, it is actually (almost) "free" to initialize with zero.
    - We could warn (or maybe even consider it an error) if not initialized,  
      and use a keyword `noinit` to avoid that warning/error.  
      ```
      Int i         // Warning
      Int j noinit  // No warning
      Int j = 1     // No warning
      ```
    - How to handle classes?
        - Mark constructors with `noinit` when they do not initialize their values, so `noinit` should be used when calling them consciously.
        - ```
          template<typename T>
          class Array {
              Array(Int size) noinit { ... }
              Array(Int size, T value) { ... }
          }
          Array<Float> anArray(10)         // Warning
          Array<Float> anArray(10) noinit  // No warning
          Array<Float> anArray(10, 1.0)    // No warning
          ```
    - Only for stack variables or also for free memory/heap?
        - ```
          var array = new Array<Float>(10)         // Warning
          var array = new Array<Float>(10) noinit  // No warning
          var array = new Array<Float>(10, 1.0)    // No warning
          ```
- `cilia::safe::Int`
    - Like `cilia::Int`, but with **overflow check** for all operations,
        - may throw OverflowException (or abort the program).
    - `safe::Int8`/`Int16`/`Int32`/`Int64`
    - `safe::Uint`
        - `safe::UInt8`/`UInt16`/`UInt32`/`UInt64`
- No further security features planned beyond C++
    - not as in [Rust](https://www.rust-lang.org/) or [Hylo](https://www.hylo-lang.org/),
        - that is just out of scope,
    - no _additional_ thread safety measures
        - A thread safety issue can easily lead to a deadlock or crash, but that is a reliabilty problem, usually IMHO not a security problem.
        - While thread safety can be a hard problem, there are currently no plans to extend the possibilities beyond plain C++ here (just because I am not aware of / familiar with better solutions than already available/recommended in C++).


## `is`, `as`, Casting
- `is` (type query)
    - See Cpp2 [is](https://hsutter.github.io/cppfront/cpp2/expressions/#is-safe-typevalue-queries):
        - `obj is Int` (i.e. a type)
        - `objPtr is T*` instead of `dynamic_cast<T*>(objPtr) != Null`
        - `obj is cilia::Array` (i.e. a template)
        - `obj is cilia::Integer` (i.e. a concept)
    - Also support value query?
- `as`
    - See Cpp2 [as](https://hsutter.github.io/cppfront/cpp2/expressions/#as-safe-casts-and-conversions)
        - `obj as T` instead of `T(obj)`
        - `objPtr as T*` instead of `dynamic_cast<T*>(objPtr)`
        - With `Variant v` where T is one alternative:  
          `v as T` instead of`std::get<T>(v)`
        - With `Any a`:  
          `a as T` instead of `std::any_cast<T>(a)`
        - With `Optional<T> o`:  
          `o as T` instead of `o.value()`
- Constructor casting
    - `Float(3)`
    - no classic C-style casting: ~~`(Float) 3`~~
    - but also
        - ~~const_cast<>~~
        - mutable_cast<>
        - reinterpret_cast<>
        - static_cast<>?
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
    - Multiple inheritance is problematic here:
        - In Cilia/C++, an object can be an instance of several base classes at once, whereby the pointer (sometimes) changes during casting.
        - What if you still want/need to access the functions for a `Type obj` after `if obj is ParentA`?
            - Workaround: Cast back with `Type(obj).functionOfA()`
        - ~~Therefore maybe better: `if obj is String str ...`~~
            - ~~as in C#~~


## Misc
- Two-Pass Compiler
    - no forward declarations necessary  
      as in C#, Java
    - no single-pass as in C/C++

- `cilia::saturating::Int`
    - Like `cilia::Int`, but with **saturation** for all operations.
        - Limit to maximum, no wrap around.
        - Typically using SIMD (as those „media/DSP instructions“ do support saturation natively).
    - see https://en.wikipedia.org/wiki/Saturation_arithmetic 
    - `saturating::Int8`/`Int16`/`Int32`/`Int64`
    - `saturating::Uint`
        - `saturating::UInt8`/`UInt16`/`UInt32`/`UInt64`

- Operations with carry flag  
  (to implement `Int128`, `Int256` etc.)
    - `c = add(a, b, inout carry)`
    - `a.add(b, inout carry)`
    - `d = multiplyAdd(a, b, c, inout dHigh)`
    - `a.multiplyAdd(b, c, inout aHigh)`
    - `b = shiftLeftAdd(a, Int steps, inout addAndHigh)`
    - `a.shiftLeftAdd(Int steps, inout addAndHigh)`
    - `b = shiftOneLeft(a, inout carry)`
    - `a.shiftOneLeft(inout carry)`

- Versioning of the Cilia source code
    - Via file ".ciliaVersion" ~~".cilia_version"~~ in a (project) directory,
        - similar to ".clang_format",
        - also possible file by file: Matrix.ciliaVersion (for Matrix.cilia).
    - Via file extension: 
        - "*.cilia" – always the latest language version (if not overridden via ".ciliaVersion")
        - "*.2024.cilia" – Version from the year 2024
        - "*.2024b.cilia" – Second version from the year 2024
        - ~~"*.cilia2024" – Version from the year 2024~~
        - ~~"*.cilia2024b" – Second version from the year 2024~~
        - ~~"*.cilia_2024" – Version from the year 2024~~
        - ~~"*.cilia_2024b" – Second version from the year 2024~~
        - ~~"*.ciliaA"~~
        - ~~"*.ciliaB"~~


## Interesting Ideas from Other Languages
- Circle
    - [Versioning with feature directives](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#versioning-with-feature-directives)
        - Standardization is better than having multiple different language "dialects"  
          **but** for
            - for transitioning of existings source code  and
            - for the evolution of a language
        - it is a very interesting idea to selectively enable new language features or defaults.
    - [Circle C++ with Memory Safety](https://www.circle-lang.org/site/index.html)
        - Extending C++ for Rust-level safety. 
    - **Fix C++ "wrong defaults"**
        [Sean Baxter](https://x.com/seanbax), creator of [Circle](https://github.com/seanbaxter/circle), [writes about C++'s wrong defaults](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#to-err-is-human-to-fix-divine):
        > C++ has a number of "wrong defaults," design decisions either inherited from C or specific to C++ which many programmers consider mistakes.
        > They may be counter-intuitive, go against expected practice in other languages, leave data in undefined states, or generally be prone to misuse.
        
        I am not familiar with all these issues, but in a new language we certainly coud fix a lot of it.
        
        1. [Uninitialized automatic variables.](http://eel.is/c++draft/dcl.init#general-7.3)
            - See [Safety and Security](#safety-and-security)/Initialization
        2. [Integral promotions.](http://eel.is/c++draft/conv.prom)
            - Only allow safe ones,  
              otherwise an explicit cast is necessary.
        3. [Implicit narrowing conversions.](http://eel.is/c++draft/conv.integral#3)
            - Not allowed,  
              only implicit widening is allowed.
            - Assigment of integer and float literals to variables of certain precision only possible if "it fits".
        4. [Switches should break rather than fallthrough.](http://eel.is/c++draft/stmt.switch#6)
            - Use the keyword `fallthrough` instead, as in Swift.
        5. [Operator precedence is complicated and wrong.](http://eel.is/c++draft/expr.compound#expr.bit.and)
            - If the [suggestion](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#simpler_precedence) of Circle (Sean Baxter) works well, then that would be fine.
            - Cpp2 (Herb Sutter) has [this precedence](https://hsutter.github.io/cppfront/cpp2/common/?h=operator#binary-operators).
        6. [Hard-to-parse declarations and the most vexing parse.](http://eel.is/c++draft/dcl.pre#nt:simple-declaration)
            - Use `func` (but not typically `var`)
        7. [Template brackets `< >` are a nightmare to parse.](http://eel.is/c++draft/temp.names#nt:template-argument-list)
            - I would not like to change this, only if it _really_ has to be.
            - Cpp2 / Herb Sutter kept `< >` after all.
        8. [Forwarding parameters and `std::forward` are error prone.](http://eel.is/c++draft/temp.deduct#call-3)
           - I am not familiar with the problem(s), but Cpp2 / Herb Sutter offers the `forward` keyword.
        10. [Braced initializers can choose the wrong constructor.](http://eel.is/c++draft/dcl.init.list#2)
            - Do without braced initializers altogether.
            - With `func` there is now a clear distinction between function declaration and variable declaration with initialization.
            - The classic initialization via `(...)`, ultimately a function call of the constructor, fits better.
            - Curly brackets only for initializer lists, i.e. for tuples, lists etc.
            - Square brackets for arrays.
        11. [`0` shouldn't be a null pointer constant.](http://eel.is/c++draft/expr#conv.ptr-1)
            - Not allowed, use `Null`.
        12. [`this` shouldn't be a pointer.](http://eel.is/c++draft/expr.prim.this#1)
            - Better it is a reference.
- Cpp2 (Herb Sutter)
    - [is](https://hsutter.github.io/cppfront/cpp2/expressions/#is-safe-typevalue-queries)
    - [as](https://hsutter.github.io/cppfront/cpp2/expressions/#as-safe-casts-and-conversions)
    -  [Function](https://hsutter.github.io/cppfront/cpp2/functions/) [Parameter Passing](https://hsutter.github.io/cppfront/cpp2/functions/#parameters)
        - `in`, `inout`, `out`, `move`, `copy`, `forward`
            - `in` – const reference (`const X&`) or const value (`const X`)
            - `inout` – non-const/mutable reference (`X&`)
            - `out` – ?
            - `move` – right-value reference (`X&&`)
            - `copy` – non-const/mutable value (`X`)
            - `forward` – ? `X&&`
        - Sounds nice for function arguments.
        - Also works for `for` loops, then these words decribe how the information (i.e. the variables) get into the body of the loop (or out of it).
    - [Labelled `break` and `continue`](https://github.com/ntrel/cpp2?tab=readme-ov-file#labelled-break-and-continue) (i.e. multi-level)
      ```
      outer: while true {
          j := 0;
          while j < 3 next j++ {
              if done() {
                  break outer;
              }
          }
      }
      ```
    - `for words next i++ do (word) { ... word & i ... }` iterates over all words and with an index, at the same time.
    - [Uniform Call Syntax](https://github.com/ntrel/cpp2?tab=readme-ov-file#uniform-call-syntax)
      for member functions and free functions.
    - [Function Bodies](https://github.com/ntrel/cpp2?tab=readme-ov-file#function-bodies)
        - `multiply: (x: int, y: int) -> int = x * y;`
        - `multiply: (x: int, y: int) x * y;` (not even an `=` anymore?)
        - `multiply: (x: int, y: int) -> int = return x * y;`
        - Nice and short, as in math, but in the end it is one more kind of notation for functions.
    - [Unified `operator=` for assignment, constructor, and destructor)](https://github.com/ntrel/cpp2?tab=readme-ov-file#operator).
        - Takes a bit of getting used to.
    - [Implicit Move on Last Use](https://github.com/ntrel/cpp2?tab=readme-ov-file#implicit-move-on-last-use)
        - So resources are freed even earlier than in C++.
    - [Named Return Values](https://github.com/ntrel/cpp2?tab=readme-ov-file#named-return-values)
    - [Inspect](https://github.com/ntrel/cpp2?tab=readme-ov-file#inspect),
      a kind of pattern matching.
- Rust
    - Security, of course: borrow checker etc.
- [Julia](https://julialang.org/)
  has very strong math support. Some of its features should be easy to copy.
    - `b = 2a` as short form of `b = 2*a`
    - `x ÷ y`, integer divide, like `x / y`, truncated to an integer
    - `sqrt(x)`, `√x`
    - `cbrt(x)`, `∛x`
    - `!=`, `≠`
    - `<=`, `≤`
    - `>=`, `≥`
    - Operator overloading
        - See:
            - [https://www.geeksforgeeks.org/operator-overloading-in-julia/](https://www.geeksforgeeks.org/operator-overloading-in-julia/)
                - „Precedence and associativity:  When defining new operators or overloading existing ones, you can also specify their precedence and associativity, which determines the order in which they are evaluated.“
                    - That seems quite complicated to parse?!
                    - I cannot find any other reference to this feature, I assume it is a misunderstanding.
            - [https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm](https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm)
        - Much more operators
            - [https://stackoverflow.com/a/60321302](https://stackoverflow.com/a/60321302)
    - Many kinds of brackets?
        - [https://stackoverflow.com/a/33357311](https://stackoverflow.com/a/33357311)
        - Problem: some of the brackets are also conceivable as operators.
