# Cilia
**C++ with CamelCase Style**  
I'd like to have the standard library roughly in the [style of Qt](https://wiki.qt.io/Qt_Coding_Style). In addition to being my personal favourite, this could also attract many developers currently using Java, JavaScript/TypeScript, Kotlin, Swift.

**C++ with Simplified Syntax**  
Many of C++'s shortcomings stem from the fact that it inherited from C or that backwards compatibility with existing code must be guaranteed.
Cilia can call into C++ (and vice versa), but is a separate language, so its _syntax_ does not need to be backwards compatible with C++.


## By Example
Cilia is, in my opinion, a collection of quite obvious ideas (and mostly taken from other programming languages, of course):
- **Cilia**
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


## Introduction
- Ideas / a wish list for an "improved" C++, a "thought experiment",
    - with a **simplified syntax**,
    - roughly **in the [style of Qt](https://wiki.qt.io/Qt_Coding_Style)**, Java, JavaScript/TypeScript, Kotlin, Swift.
    - Isomorphic mapping of all C++ functionality to Cilia shall be possible
        - only with other/better/shorter "expression".
- C++ "Successor Language / Syntax"
    - similar to [CppFront/Cpp2](https://github.com/hsutter/cppfront#cppfront), [Carbon](https://github.com/carbon-language/carbon-lang), or [Circle](https://github.com/seanbaxter/circle),
    - a bit like
        - Java and Kotlin,
        - Objective-C and Swift.
- Uses the same compiler backend as C++ (clang comes to mind)  
  with an own / a new compiler frontend.
    - Or a precompiler, like Cpp2, if that is significantly easier to do.
- So _no_ garbage collection,  
  instead in Cilia you use, as in C++:
    - automatic/stack variables,
    - **RAII** (Resource Acquisition is Initialization)
        - I'd like to call it "RROD" (Resource Release on Object Destruction)
    - shared pointers (`T^`).
- Why a new language, not extending C++?
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
- The names [D](https://dlang.org/), [C2](http://c2lang.org/), [C3](https://c3-lang.org), and [Cpp2](https://github.com/hsutter/cppfront#cppfront) were already taken,  
  as well as [Cone](https://cone.jondgoodwin.com/) and many others `¯\_(ツ)_/¯`.


## C++ Compatibility / Interoperability
- **Compatible to C++** and maybe other languages of this "**language family**" / "**ecosystem**",
    - as with
        - Java and Kotlin, Scala, Groovy, Clojure, Fantom, Ceylon, Jython, JRuby ...
        - C# and C++/CLI, Visual Basic .NET, F#, A# (Ada), IronPython, IronRuby ...
        - Objective-C and Swift
    - Bi-directional interoperability, so (with a hypothetical C++/Cilia compiler) it is possible to include
        - C++ headers and modules from Cilia,
        - Cilia headers and modules from C++.
    - Can call C functions, access C structs (as C++ can do).
    - The compiler recognizes the language (C, C++, or Cilia) by:
        - Marked blocks
            - `lang "C++" { ... }`
            - `lang "Cilia" { ... }`
            - ~~`lang "C" { ... }`~~
            - TODO Limited to top level?
            - Limited to languages where the scope is marked with `{ }`.
        - File extension
            - Cilia: `*.cil`, `*.hil`
            - C++: `*.cpp`, `*.hpp` or `*.cxx`, `*.hxx`
                - Even `*.h`, but that is a problem, as the header could be C or C++ code.  
                  So use of `*.hpp` is recommended for C++ code.  
                  This can probably best be solved using path based rules.
            - C: `*.c` `*.h`
        - Path based rules,
            - to handle C or C++ standard headers in certain directories.
        - File specific configuration,
            - can be set in the IDE or on the command line,  
              for each file individually.


## CamelCase Style
Roughly in the style of Qt, Java, JavaScript, TypeScript, Kotlin, Swift.

- All types and **classes** in **upper CamelCase** ("PascalCase").
    - `Bool`, `Int`, `Int32`, `UInt`, `BigInt`, `Float`
    - `String`, `Array`, `Map`, `ForwardList`, `UnorderedMap`, `ValueType`

- **Variables**/instances/objects in **lower camelCase**
    - `Int i`
    - `String word`
    - `String[] words`
    - `ContactInfo[String] contactInfoForID`
    - Feel free to bend/break this rule, e.g. name matrices as `Matrix M, R, L`
      
- **Functions** in **lower camelCase**
    - `str.findFirstOf(...)`
    - `arr.pushBack(...)`
    - `Thread::hardwareConcurrency()`

- **Global constants** in **upper CamelCase**
    - `Pi`, `Euler` (feel free to bend/break this rule, e.g. define a constant `const e = Euler`)
    - Constant-like keywords
        - `NullPtr`
        - `True`, `False`
        - `NaN`, `Infinity`
    - But keep _local_ constants in lower camelCase:  
        - `const Int lastIndex = 100` instead of ~~`const Int LastIndex = 100`~~

- Namespaces fully lowercase 
    - `cilia`
    - `cilia::lapack`
    - `cilia::geometry`
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
    - `Int` == `Int32` on 32 bit systems only (i.e. old/small platforms), `Int` == `Int16` on 8 and 16 bit systems (i.e. old/small microcontrollers).
    - As in Swift and Go.
    - _No_ ~~`Size`~~, ~~`SSize`~~, nor ~~`PtrDiff`~~, simply use `Int` instead.
    - _No_ ~~`Long`~~ nor ~~`Lonmg Long`~~, simply use `Int` instead.
    - `Int8`, `Int16`, `Int32`, `Int64`
    - `UInt`, `UInt8`, `UInt16`, `UInt32`, `UInt64`
- `Byte` == `UInt8` (Alias, i.e. the same type for parameter overloading)
- `Float`
    - `Float` == `Float32`
        - This is how it is in C/C++.
        - Is faster than Float64 and good enough most of the time.
    - `Float16`, `Float32`, `Float64` (half, single, double precision floating point)


## Variable Declaration
`Int i` as variable declaration, very much as in C/C++.
- `TypeName variableName`
- Some simplifications and restrictions:
    - The type definition is completely on the left-hand side,
        - i.e. before the variable name, also for arrays and bit fields.
    - `const` always binds to the right.
    - All variables in a multiple-variable declarations are of the exact same type.

- Examples:
    - `Int i`
    - `Int i = 0`
    - `Int x, y`
    - `Int x = 99, y = 199`
    - `Int[3] position`  // Array of three integers (instead of `Int position[3]`)
    - `Float* m, n`   // m _and_ n are pointers (contrary to C/C++)
    - `Float& m, n`   // m _and_ n are references (contrary to C/C++)
    - `Image image(width, height, 0.0)`
    - `const Float* pointerToConstantFloat`
    - `const Float const* constPointerToConstantFloat`
        - `const` always binds to the right (contrary to C/C++).
    - `Complex<Float>& complexNumber = complexNumberWithOtherName`

- Not allowed / a syntax error is:
    - ~~`Float* m, &n`~~
        - Type variations within multiple-variable declarations are _not_ allowed.
        - It has to be the exact same type.
    - ~~`Float*m`~~
        - Whitespace _between_ type specification and variable name is mandatory.
    - ~~`Image image { width, height, 0.0 }`~~
        - No list initialization _for plain constructors_, as there is no need anymore.
        - There are generally _no_ unsafe integral promotions and _no_ implicit narrowing conversions.
        - See [Misc](#misc) / Mixed arithmetic and [https://stackoverflow.com/a/18222927](https://stackoverflow.com/a/18222927)
- **Type inference** with `var` / `const`:
    - `var i = 3` instead of ~~`auto i = 3;`~~
    - `const i = 3` instead of ~~`const auto i = 3;`~~ (`const var` would be a contradiction in terms, as there is no such thing as a "constant variable".)
- Bit fields
  ```
  UInt32:1  sign
  UInt32:8  exponent
  UInt32:23 significand // AKA mantissa
  ```
  (instead of `UInt32 sign : 1`)


## Classes
- Quite as in C++
  ```
  class MyArrayOfInt {
      Int* numbers = NullPtr
      Int size = 0
  }
  ```
- Default access specifier is `public`.
- Not ~~`struct`~~, as it is just too similar to `class` with no real benefit.
   - Keep as a reserved keyword for future use.


## Functions
```
func multiplyAdd(Int x, y, Float z) -> Float {
    return x * y  +  z
}
```
- Function declarations start with the keyword `func`,
    - as in Swift.
    - Easier parsing due to clear distinction between function declaration vs. variable declaration,  
      avoiding the [most vexing parse](https://en.wikipedia.org/wiki/Most_vexing_parse).
- Function parameters are given as `TypeName parameterName`, as with variable declarations.
- Multiple function parameters of the (exact) same type can be combined to e.g. `TypeName parameter1, parameter2`.
    - `func multiply(`**`Int x, y`**`) -> Int` // x _and_ y are Int
- Always and only in the trailing return type syntax (using `-> ReturnType`),
    - but void functions are written _without_ trailing `->` (i.e. no ~~`-> Void`~~),  
      e.g. `func print(String line) { ... }`
- **Lambdas**
    - `[](Int i) -> Float { i * 3.14 }`  
      as in C++
- **`constexpr`** and `consteval`
  ```
  constexpr multiply(Int x, y) -> Int {
      return x * y
  }
  consteval multiply(Int x, y) -> Int {
      return x * y
  }
  ```
    - TODO Would `constfunc` be the better keyword?
- **Function pointers**
    - Trying to maintain consistency between declarations of functions, function pointers, functors and lambdas.
    - Examples:
        - **`func(Int, Int -> Int)* pointerToFunctionOfIntAndIntToInt`**
        - **`func(Int)* pointerToFunctionOfInt`**
        - `func(Int, Int -> Int)& referenceToFunctionOfIntAndIntToInt` // Can't be zero
        - `func(Int)& referenceToFunctionOfInt`

          
## Operators
- Power function
    - **`a^x`** for `pow(a, x)` (as in Julia),
    - "raise a to the power of x".
- Boolean operators
    - **`and`**, **`or`**, **`nand`**, **`nor`**, **`xor`** in addition to `&&`/`&`, `||`/`|`, ...
        - similar to [Python](https://www.w3schools.com/python/python_operators.asp),
          [Carbon](https://www.naukri.com/code360/library/operators-and-precedence-in-carbon)
        - Used for both
            - boolean operation (when used on Bool)
                - `aBool`**`and`**`anotherBool` -> `Bool`
            - bitwise operation (when used on integers)
                - `anInt`**`and`**`anotherInt` -> `Int`
            - No mixed types allowed (you need to explicitly cast one side instead).
        - Words like `and` and `or` IMHO are a bit clearer than `&&`/`&` and `||`/`|`, so they are recommended.
        - Still _also_ use `&` and `|` for bitwise operation,
            - as C/C++/Java/C# programmers are used to it,
            - as we keep `&=` and `|=` anyway.
        - Still _also_ use `&&` and `||` for boolean operation,
            - as C/C++/Java/C# programmers are used to it,
                - even [Swift](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/#Logical-Operators)
                  and [Kotlin](https://www.w3schools.com/kotlin/kotlin_operators.php) keep `&&` and `||`,
            - as we want `&&=` and `||=` anyway.
            - Defined on `Bool` only (_not_ on integers).
    - **`not`** in addition to `!` (for boolean negation)
        - `not` is a bit clearer than `!` (especially as many modern languages like Rust and Swift use `!` also for error handling).
        - Still _also_ `!` for negation (in addition to `not`), as we keep `!=` for "not equal" anyways.  
          (We could use `<>` instead of `!=`, but that's really not familiar to C/C++ programmers.)
        - Still use `~` for bitwise negation,
            - as C/C++/Java/C# programmers are used to it,
            - as we keep `~T` for the destructor anyway.
    - **`xor`** _instead_ of `^`  
      because we want `^` for the power function.
- Equality
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
- **Range operator** `..` and `..<`
    - `1..10` and `0..<10` are ranges
        - as in [Kotlin](https://kotlinlang.org/docs/ranges.html)
        - Similar, but diffentent:
            - Swift would be ~~`1...10`~~ and ~~`0..<10`~~
            - Rust would be ~~`1..=10`~~ and ~~`0..10`~~
            - Cpp2 would be ~~`1..=10`~~ and ~~`0..<10`~~ (as of recently)
    - Different kinds of ranges:
        - `1..3` – 1, 2, 3
            - `Range(1, 3)`
        - `0..<3` – 0, 1, 2
            - `RangeExclusiveEnd(0, 3)`
        - Range with step (especially to **iterate with the given step size in the `for` loop**)
            - `1..6:2` – 1, 3, 5
                - `RangeByStep(1, 6, 2)`
            - `0..<6:2` – 0, 2, 4
                - `RangeExclusiveEndByStep(0, 6, 2)`
        - Downwards iterating range (especially to **iterate downwards in the `for` loop**).  
          Step size is mandatory here (to make it clear that we are counting down, to avoid wrong conclusions).
            - `8..0:-1` – 8, 7, 6, 5, 4, 3, 2, 1, 0
                - `RangeByStep(8, 0, -1)`
                - Not ~~`8..0`~~, as `Range(8, 0)` is always empty (it is counting up, not down!)
                - Not `8..<0:-1`
                    - With staticAssert in `RangeExclusiveEndByStep` that `step > 0`:  
                      "The range operator with exclusive end (`..<`) is not compatible with negative increments, because when counting downwards it would be necessary/logical to write `..>` and that is not available."
                    - It simply would be too much, IMHO.
                    - Use `8..1:-1` instead.
        - If both start and end of the range are compile time constants, then it may be warned when the range contains no elements at all (e.g. when `start >= end` with `step > 0`).
        - Incomplete ranges (need lower and/or upper bounds to be set before use)  
            - `..2` – ..., 1, 2
                - `RangeTo(2)`
            - `..<3` – ..., 1, 2
                - `RangeToExclusiveEnd(3)`
            - `0..` – 0, 1, 2, ...
                - `RangeFrom(0)`
            - `..`
                - `RangeFull()`
            - Incomplete range with step
                - `..2:2` – `RangeToByStep(2, 2)`
                - `..<3:2` – `RangeToExclusiveEndByStep(3, 2)`
                - `0..:2` – `RangeFromByStep(0, 2)`
                - `..:2` – `RangeFullByStep(2)`
        - See Rust [Ranges](https://doc.rust-lang.org/std/ops/index.html#structs) and [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- Bit-Shift & Rotation
    - `>>` Shift right (logical shift with unsigned integers, arithmetic shift with signed integers)
    - `<<` Shift left (here a logical shift left with unsigned integers is the same as an arithmetic shift left with signed integers)
    - `>>>` Rotate right (circular shift right, only defined for unsigned integers)
    - `<<<` Rotate left (circular shift left, only defined for unsigned integers)
- Operator declaration
    - Keyword **`operator`** instead of `func`.
    - As with normal functions: Parameters are passed as `in` by default (i.e. `const T&` or `const T`).
    - Assignment operator
      ```
      class Int256 {
          operator =(Int256 other) { ... }
      }
      ```
        - No return of this-reference,
            - [as in Swift](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/),
            - so `if a = b { ... }` is _not_ accidentally allowed.
        - Move assignment
          ```
          class Int256 {
              operator =(move Int256 other) { ... }
          }
          ```
    - Arithmetic operators
      ```
      operator +(Int256 a, b) -> Int256 { ... }
      operator -(Int256 a, b) -> Int256 { ... }
      operator *(Int256 a, b) -> Int256 { ... }
      operator /(Int256 a, b) -> Int256 { ... }
      operator %(Int256 a, b) -> Int256 { ... }
      ```
    - Shift and rotate operators
      ```
      operator <<(Int256 a, Int shiftCount) -> Int256 { ... }
      operator >>(Int256 a, Int shiftCount) -> Int256 { ... }
      operator <<<(UInt256 a, Int shiftCount) -> UInt256 { ... }
      operator >>>(UInt256 a, Int shiftCount) -> UInt256 { ... }
      ```
    - Compound assignment operators
      ```
      class Int256 {
          operator +=(Int256 other) { ... }
          operator -=(Int256 other) { ... }
          operator *=(Int256 other) { ... }
          operator /=(Int256 other) { ... }
          operator %=(Int256 other) { ... }
          operator <<=(Int shiftCount) { ... }
          operator >>=(Int shiftCount) { ... }
          operator &=(Int256 other) { ... }
          operator |=(Int256 other) { ... }
      }
      class UInt256 {
          operator <<<=(Int shiftCount) { ... }
          operator >>>=(Int shiftCount) { ... }
      }
      ```
        - Not ~~`operator ^=(Int256 other) { ... }`~~
    - Increment and decrement operators
      ```
      class Int256 {
          operator ++() -> Int256& { ... }
          operator ++(Int dummy) -> Int256 { ... } // post-increment
          operator --() -> Int256& { ... }
          operator --(Int dummy) -> Int256 { ... } // post-decrement
      }
      ```
    - Relational and comparison operators
      ```
      operator ==(Int256 a, b) -> Bool { ... }
      operator !=(Int256 a, b) -> Bool { ... }
      operator <(Int256 a, b) -> Bool { ... }
      operator >(Int256 a, b) -> Bool { ... }
      operator <=(Int256 a, b) -> Bool { ... }
      operator >=(Int256 a, b) -> Bool { ... }
      operator <=>(Int256 a, b) -> Int { ... }
      ```
    - Logical operators
        - Boolean operators
          ```
          operator and(Bool a, b) -> Bool { ... }
          operator or(Bool a, b) -> Bool { ... }
          operator nand(Bool a, b) -> Bool { ... }
          operator nor(Bool a, b) -> Bool { ... }
          operator xor(Bool a, b) -> Bool { ... }
          operator not(Bool a) -> Bool { ... }
          operator &&(Bool a, b) -> Bool { return a and b }
          operator ||(Bool a, b) -> Bool { return a or b }
          operator !(Bool a) -> Bool { return not a }
          operator ∧(Bool a, b) -> Bool { return a and b }
          operator ∨(Bool a, b) -> Bool { return a or b }
          operator ⊼(Bool a, b) -> Bool { return a nand b }
          operator ⊽(Bool a, b) -> Bool { return a nor b }
          operator ⊻(Bool a, b) -> Bool { return a xor b }
          ```
            - Defined for _`Bool`_,
            - operators `!`, not `~`,
                - `&&` and `||`, not `&` and `|`.
        - Bitwise operators
          ```
          operator and(Int256 a, b) -> Int256 { ... }
          operator or(Int256 a, b) -> Int256 { ... }
          operator nand(Int256 a, b) -> Int256 { ... }
          operator nor(Int256 a, b) -> Int256 { ... }
          operator xor(Int256 a, b) -> Int256 { ... }
          operator not(Int256 a) -> Int256 { ... }
          operator &(Int256 a, b) -> Int256 { return a and b }
          operator |(Int256 a, b) -> Int256 { return a or b }
          operator ~(Int256 a) -> Int256 { return not a }
          operator ∧(Int256 a, b) -> Int256 { return a and b }
          operator ∨(Int256 a, b) -> Int256 { return a or b }
          operator ⊼(Int256 a, b) -> Int256 { return a nand b }
          operator ⊽(Int256 a, b) -> Int256 { return a nor b }
          operator ⊻(Int256 a, b) -> Int256 { return a xor b }
          ```
            - Defined for _integers_ (not for `Bool`),
            - operators `~`, not `!`,
                - `&` and `|`, not `&&` and `||`.
    - Subscript/bracket/parenthesis/functor operators:
      ```
      class MyImage<type T> {
          // Array subscript
          operator [Int i] -> T& {
              return data[i]
          }
    
          // 2D array (i.e. image like) subscript
          operator [Int x, y] -> T& {
              return data[x + y*stride]
          }
          
          // Functor call
          operator (Int a, Float b, String c) {
              ...
          }
      }
      ```
    - Exotic operators (e.g. Unicode)
        - ⊕, ⊖, ⊗, ⊘, ⊙, ⊛, ⊞, ⊟, ∪, ∩, ∖, ∈, ∉, ∋, ∌, ∧, ∨, ¬, ∷, ∶, ∝, ∼, ≈, ≉, ≠, ≤, ≥, ≪, ≫, ⊂, ⊃, ⊆, ⊇, ∅, ∇, ∂, ∞, ∑, ∏, ∫, ∮, ∵, ∴, ∗, ∘, ∙, ∟, ∥, ∦, ∠, ⟂, ≜, ≝, ≔, ≕
        - Reserved for future use, as it could get complicated and confusing.
            - Especially to differentiate
                - operator precedence and
                - unary (prefix, postfix) or binary (infix) operators.
            - Many seem more suitable for a computer algebra system (CAS), not for a general purpose programming language.
        - `|x|` for `abs(x)`?
            - `||x||` for `norm(x)`?
                - This would interfere with `||` as logical `or`.
            - This form is called as "enclosing operator", "delimited form", "bracketed expression", or informally as a paired prefix/postfix or "sandwich operator".
            - More variants?
                - `≪...≫`
                - `‹...›` , `«...»`
                - `⦅...⦆` , `〚...〛` , `⦃...⦄`
                - `（...）`, `［...］`, `｛...｝`, `｟...｠`
                - `「...」`, `『...』`, `〈...〉`, `《...》`, `【...】`, `〖...〗`, `〔...〕`, `〘...〙`, `⦗...⦘`
            - Some may be used in reversed order: `≫...≪`
            - Also see [Unicode Math Brackets](http://xahlee.info/comp/unicode_math_brackets.html)



## Branches & Loops
No braces around the condition clause (as in Python, Swift, Go, Ruby).
- **if**
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
        - chained comparison as in Cpp2 (Herb Sutter), Python, Julia
- **while**
  ```
  while a > b {
      // ...
  }
  ```
- **do-while**
  ```
  do {
      // ...
  } while a > b
  ```
- **for-in**
    - as in Swift, Rust
    - Write
      ```
      for str in ["a", "b", "c"] {
          // ...
      }
      ```
      instead of `for (... : ...)` (AKA range-for in C++, `for each` in C++/CLI, `foreach` in C#)
    - Use the **range operator** to write          
        - `for i in 1..10 { ... }`  
          instead of ~~`for (Int i = 1; i <= 10; ++i) { ... }`~~,  
          translates to `for i in Range(1, 10) { ... }`.
        - `for i in 0..<10 { ... }`  
          instead of ~~`for (Int i = 0; i < 10; ++i) { ... }`~~,  
          translates to `for i in RangeExclusiveEnd(0, 10) { ... }`.
        - `for i in 10..1:-1 { ... }`  
          instead of ~~`for (Int i = 10; i >= 1; --i) { ... }`~~,  
          translates to `for i in RangeByStep(10, 1, -1) { ... }`.
        - I find this for-loop-syntax so intriguing that I accept the somewhat complex details of the range operator (with all its variants).
    - The loop variable is declared "with the loop", with its type inferred from the range, array, etc. used (similar to `var` but only with the options `in` (the default), `inout`, `copy`, `move`),  
      so `for i in 0..<10 { <Body> }` is equivalent to:
      ```
      {
          var i = 0
          while i < 10 {
              <Body>
              ++i
          }
      }
      ```
    - In general you can replace the (overly) powerful C/C++ for-loop like
      ```
      for (<Initialization>; <Condition>; <Increment>) {
          <Body>
      }  
      ```
      with a while-loop:
      ```
      {
          <Initialization>
          while <Condition> {
              <Body>
              <Increment>
          }
      }
      ```
- **switch/case** with `fallthrough` instead of ~~`break`~~,  
  like in Swift
    - ```
      switch i {
      case 1:
          print("1")
          // implicit break
      
      case 2, 3:
          print("Either 2 or 3")
          // implicit break
      
      case 4:
          // do something
          fallthrough
      case 5:
          // do something more
          print("4 or 5")
          // implicit break
      
      default:
          print("default")
      }
      ```
        - Old behaviour on demand
            - ```
              switch i fallthrough {
              case 1:
                  print("1")
                  break
              
              case 2, 3:
                  print("Either 2 or 3")
                  break
              
              case 4:
                  // do something
                  // implicit fallthrough
              case 5:
                  // do something more
                  print("4 or 5")
                  break
              
              default:
                  print("default")
              }
              ```

## Aliasing
Create an alias with `using`, for:
- Member **variables**  
  `using var x = data[0]`  
  `using var y = data[1]`  
    - Not quite possible in C++.
        - With `T& x = data[0]` unfortunately memory is created for the reference (the pointer).
        - And this indeed is necessary here, because the reference could be assigned differently in the constructor, so it is not possible to optimize it away.
- Member **functions**
    - `using func f(String) = g(String)` to alias the function `g(String)`.
    - `using func f = g` to alias _all_ overloads of the function `g`.
- **Types**
    - `using InParameterType = const StringView`  
      (no ~~`typedef`~~)


## Type Extension
To add "member like" types, functions/methods, constants (and maybe static variables) to "third party" classes/types.  
In case of conflicts, in-class definitions (inside the class) have priority (and a warning is issued).
- **Extension methods**
    - Can be called like normal member functions, but they but do not have access to private or protected members themselves.
    - Also possible for basic/arithmetic types, e.g.:  
      `Int i`  
      `i.toString()`  
      based on  
      `func Int::toString() -> String { ... }`  // as in Kotlin
- **Externally defined alias** (with `using`) for members:
    - **Variables**  
      `using var Vector2::x = Vector2::data[0]`  
      `using var Vector2::y = Vector2::data[1]`  
    - **Functions**  
      `using func Array::pushBack(String) = Array::push_back(String)` to alias the function `push_back(String)`.  
      `using func Array::pushBack = Array::push_back` to alias _all_ overloads of the function `g`.
    - **Types**  
      `using StringView::InParameterType = const StringView`
- Static constants, typically for type traits
  ```
  const Bool Float32::IsFloatingPoint = True
  const Bool Float64::IsFloatingPoint = True
  ```
    - TODO: Allow external static _variables_ (i.e. mutable), too?
        - Why not. But for what would it be useful?
        - `Int ContactInfo::numOfInstances = 0`


## (Smart) Pointers
- **Short Smart Pointer Syntax**
    - “Make simple things simple” (or at least short to write),  
      encourage use of smart pointers.
    - **`Type+ pointer`**
        - `T+` is short for **`UniquePtr<T>`** (i.e. a unique pointer to a single object)
        - `T[0]+` is short for **`UniquePtr<T[0]>`** (i.e. a unique pointer to a C/C++ array of fixed but unknown size, `0` is just a dummy here)
            - TODO `UniquePtr<T[]>` seems possible in C++ (it is an "incomplete type"). But in Cilia `T[]` is an `Array<T>`, so we use `T[0]` instead.
        - **`makeUnique<T>(...)`**,
            - `ContactInfo+ contactInfoUniquePtr = makeUnique<ContactInfo>()`.
            - `ContactInfo[0]+ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()`  
              not ~~`ContactInfo+ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()`~~ (there is no array-to-single-element-pointer decay possible with `UniquePtr`, as that is a necessary distinction in its type).
    - **`Type^ pointer`**
        - `T^` is short for **`SharedPtr<T>`**
        - Inspired by C++/CLI (so its a proven possiblilty), _but_  
           - Sean Baxter is also using `T^` for Rust-style references in Circle (so there may be a conflict in the future).
            - And there is an inconsistency in its usage:
                - A normal pointer `T* pointer` is dereferenced with `*pointer`.
                - A smart pointer `T^ pointer` is dereferenced also with `*pointer` (not `^pointer`).
                - So maybe use `T*^` and `T*+` instead?
        - **`makeShared<T>(...)`**,
            - `ContactInfo^ contactInfoSharedPtr = makeShared<ContactInfo>()`.
            - `ContactInfo^ contactInfoSharedArrayPtr = makeShared<ContactInfo[10]>()`  
              also possibler (but not recommended) is ~~`ContactInfo[0]^ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()`~~ (whether it is a single-element- or an array-pointer is stored in the SharedPtrInfo).
        - `T^`/`SharedPtr<T>` can take over the pointer from _rvalue_ `T+`/`UniquePtr<T>` and `T[0]+`/`UniquePtr<T[0]>` (as in C/C++):
            - `ContactInfo^ contactInfoSharedPtr = new ContactInfo`
            - `ContactInfo^ contactInfoSharedPtr = move(contactInfoUniquePtr)`
                - The `contactInfoUniquePtr` is a `NullPtr` afterwards.
- A classical C/C++ "raw" pointer is still possible, but unsafe.
    - `ContactInfo* contactInfoPtr = new ContactInfo`  
      `delete contactInfoPtr` (with classical/raw pointers you need to free the objects yourself)
    - `ContactInfo* contactInfoPtr = new ContactInfo[10]`  
      `delete[] contactInfoPtr` (you need to distinguish single-element- and array-pointers yourself)
- Redefine `T^` and `T+` for special cases / **interoperability with other languages**:
    - `T^` is defined via type traits `SharedPtrType`,  
        - For C++/Cilia classes `T^` is `SharedPtr<T>`:
            - `using<type T> T::SharedPtrType = SharedPtr<T>`
        - Objective-C/Swift classes use their reference counting mechanism:
            - `using ObjectiveCObject::SmartPtrType = ObjectiveCRefCountPtr`
        - C#/.NET classes use garbage collected memory for instance/object allocation, add instance/object-pointers to the global list of C#/.NET instance pointers (with GCHandle and/or gcroot).   
            - `using DotNetObject::SmartPtrType = DotNetGCPtr`
            - Access/dereferencing creates a temporary `DotNetGCPinnedPtr`, that pins the object (so the garbage collector cannot move it during access).
        - Java classes use garbage collected memory, add pointers to the global list of Java instance pointers.  
            - `using JavaObject::SmartPtrType = JavaGCPtr`
            - Probably very similar to C#/.NET.
    - `T+` is defined via type traits `UniquePtrType`.
        - For C++/Cilia classes `T+` is `UniquePtr<T>`:
            - `using<type T> T::UniquePtrType = UniquePtr<T>`


## Templates
The basic new idea is, to define templates (classes and functions) mostly the same as they are used.  
Similar as in Java, C#, Swift and Rust.
- **Class** templates  
  The template parameters (`<...>`) are given after the class name, so that the definition is similar to the usage (in a variable declaration).
  ```
  class MyArray<Number T> {
      T* numbers = NullPtr
      Int size = 0
  }
  ```
    - Template specialization
      ```
      class MyUniquePtr<type T> {
          ... destructor calls delete ...
      }
      class MyUniquePtr<type T[Int N]> {
          ... destructor calls delete[] ...
      }
      ```
    - Partial template specialization
      ```
      class KeyValuePair<type TKey, type TValue> {
          ...
      }
      class KeyValuePair<Int, type TValue> {
          ...
      }
      class KeyValuePair<type TKey, String> {
          ...
      }
      ```
- **Function** templates
    - _Automatic_ function templates
        - If the type of (at least) one of the function parameters is a concept, then the function is (in fact) a function template.
            - Concept `Number`:
              ```
              func sq(Number x) -> Number {
                   return x * x
              }
              ```
                - However, the return type could be a _different_ type than `x` is (but it needs to satisfy the concept `Number`)
                - With `func add(Number a, b) -> Number` even `a` and `b` could be of a different type (but both need to satisfy the concept `Number`)
            - Concept `Real` (real numbers as `Float16`/`32`/`64`/`128` or `BigFloat`):
              ```
              func sqrt(Real x) -> Real {
                  // ... a series development ...
                  // (with number of iterations determined from the size of the mantissa)
              }
              ```
        - Like abbreviated function templates in C++ 20, only without `auto`.
    - _Explicit_ function templates for cases where a common type is required.  
        - The template parameters (`<...>`) are given after the function name, so that the function definition is similar to the function call.
          ```
          func add<Number T>(T x, y) -> T {
               return x + y
          }
          ```
    - For extension function templates it is necessary to know the _type_-specific template parameter(s) even before we write the function name, where the function-specific template parameters are given.  
      Therefore we write
        - `func<type T, Int N> T[N]::size() -> Int { return N }`
        - `func<type T, Int N> T[N]::convertTo<type TOut>() -> TOut[N] { ... }`  
            - Not ~~`func T[N]::convertTo<type T, Int N, type TOut>() { ... }`~~, as  
                - then T and N would be used even before they were declared, and
                - with `Float[3] arrayOfThreeFloat = [1.0, 2.0, 3.0]` we want to write  
                  `Int[3] arrayOfThreeInt = arrayOfThreeFloat.convertTo<Int>()` (not ~~`...convertTo<Float, 3, Int>()`~~)
            - The template parameters `T` and `N` belong to the type of the object `arrayOfThreeFloat` and are determined already. It would not be possible to change them in the call of `convertTo<>()`, so it is not desired to specify them here at all.

- Further restrict the type with `requires` (as in C++):
    - ```
      func sq<Number T>(T x) -> T
      requires (T x) { x * x }
      {
           return x * x
      }
      ```
    - ```
      class SlidingAverage<type T, type TSum = T>
      requires (T x, TSum sum) {
          sum = 0   // requires assignment of 0
          sum += x  // requires addition of type T to type TSum
          sum -= x  // requires subtraction of type T from type TSum
          sum / 1   // requires to divide sum by 1 (i.e. an Int)
      } {
          T+ numbers
          Int size = 0
          Int sizeMax = 0
          Int index = 0
          TSum sum = 0
      public:
          SlidingAverage(Int size) {
             sizeMax = size
             numbers = new T[sizeMax]
          }
          func append(T value) { ... }
          func average() -> TSum { ... }
          func reset() { ... }
          func reset(Int newSize) { ... }
      }
      ```
- Template **type alias** with `using` (not ~~`typedef`~~)
    - `using<type T> T::InParameterType = const T&`
- Template static constants as type traits
    - ```
      const<type T> Bool          T::IsFloatingPoint = False
      const         Bool    Float32::IsFloatingPoint = True
      const         Bool    Float64::IsFloatingPoint = True
      const<type T> Bool Complex<T>::IsFloatingPoint = T::IsFloatingPoint
      ```


## Arrays & ArrayViews
- `Int[] dynamicArrayOfIntegers`
    - „Dynamic array“ with **dynamic size**
      ```
      Int[] array = [0, 1, 2]
      array[0] = 0
      array[1] = 0
      array[2] = 0
      array[3] = 0  // Runtime error, no compile time bounds check
      ```
    - "Make simple things simple",  
      having a short and traditional syntax for dynamic arrays should encourage people to use it.
    - `T[] arr` is the short form of `cilia::Array<T> arr`
        - TODO Also `[T] arr`, as in Swift or Rust, has some merits.  
          But I don't like `[T;3] arr`.
    - The long form is called `Array<T>`, not ~~`Vector<T>`~~, because
        - that's the more traditional wording,
        - by using the word "vector", the purpose of this class is not immediately clear (especially not for users of many languages other than C++, not even C),
        - `Vector` could too easily collide with the mathematical vector (as used in linear algebra or geometry).
    - "Raw" C/C++ arrays are handled with `T*` instead.
    - `std::array` is called `cilia::StaticArray` instead.
    - In C/C++ `T[]` means "array of certain (inferred) size",
        - but that can be replaced with `T*` and `T[N]`.
        - Also see [https://cplusplus.com/forum/beginner/267321/#msg1150228](https://cplusplus.com/forum/beginner/267321/#msg1150228)
- `Int[3] arrayOfThreeIntegers`  
  (instead of ~~`Int arrayOfThreeIntegers[3]`~~ in C/C++)
    - „Static array“ with **fixed size**
      ```
      Int[3] array = [0, 1, 2]
      array[0] = 0
      array[1] = 0
      array[2] = 0
      array[3] = 0  // Compilation error, due to compile time bounds check
      ```
    - `arrayOfThreeIntegers.size()` -> `3`
        - realized as extension function  
          `func<type T, Int N> T[N]::size() -> Int { return N }`
- Use `T+`/`UniquePtr<T>` for "raw" C/C++ arrays of arbitrary size.  
  But array subscript with `Int+` is unsafe.
    - ```
      Int+ array = new Int[3]  // Array-to-pointer decay possible
      unsafe {
          array[0] = 0
          array[1] = 0
          array[2] = 0
          array[3] = 0  // Undefined behaviour, no bounds check at all
      }
      ```
    - Using `Int*` for arrays is possible but generally unsafe.
        - ```
          Int+ uniquePtrToArray = new Int[3]  // Array-to-pointer decay possible
          unsafe {
              Int* array = uniquePtrToArray.release()
              array[0] = 0
              array[1] = 0
              array[2] = 0
              array[3] = 0  // Undefined behaviour, no bounds check at all
              delete[] array
          }
          ```
        - ```
          unsafe {
              Int* array = reinterpretCastTo<Int*>(malloc(3 * sizeof(Int)))
              array[0] = 0
              array[1] = 0
              array[2] = 0
              array[3] = 0  // Undefined behaviour, no bounds check at all
              free(array)
          }
          ```
    - Actually this is how to handle pointer to array of `Int` "properly":  
      ```
      Int[3]+ arrayPtr = new Int[3]
      *arrayPtr[0] = 0
      *arrayPtr[1] = 0
      *arrayPtr[2] = 0
      *arrayPtr[3] = 0  // Compilation error, due to compile time bounds check
      ```
        - But raw pointer access is still `unsafe`:  
          ```
          unsafe {
              Int[3]* arrayPtr = (new Int[3]).release()
              *arrayPtr[0] = 0
              *arrayPtr[1] = 0
              *arrayPtr[2] = 0
              *arrayPtr[3] = 0  // Compilation error, due to compile time bounds check
              delete[] arrayPtr
          }
          ```
- Examples:
    - `Int[] dynamicArrayOfInt`
    - `Int[3] arrayOfThreeInt`
    - `Int[3]& referenceToArrayOfThreeInt`
    - `Int[3]* pointerToArrayOfThreeInt`
    - `Int[3][]& referenceToDynamicArrayOfArrayOfThreeInt`
    - `String*[] dynamicArrayOfPointersToString`
- ArrayViews AKA Slices AKA Subarrays
    - `var subarray = array[1..2]`
    - `var subarray = array[1..<3]`
    - Incomplete ranges (need lower and/or upper bounds before use) are
      typcally implemented as inline functions that determine the concrete bounds and then call `array[start..end]` (or one of the exclusive counterparts).
        - `var subarray = array[..2]`
        - `var subarray = array[..]`
    - See Rust [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- Multidimensional arrays
    - dynamic size
        - `Int[,] dynamic2DArray`  
            - `T[,] array` is the short form of `cilia::MDArray<2, T> array`
        - `Int[,,] multidimensionalDynamicArray`  
            - `T[,,] array` is the short form of `cilia::MDArray<3, T> array`
        - and so on:  
            - `cilia::MDArray<N, T>`
    - static size
        - `Int[3, 2, 200]`
            - Multidimensional static array  
              ```
              Int[3, 2, 200] intArray3D
              intArray3D[2, 1, 199] = 1
              ```
            - `cilia::StaticMDArray<Int, 3, 2, 200> intArray3D`
- Mixed forms of static and dynamic array
    - `Int[3][,] dynamic2DArrayOfArrayOfThreeInt`
    - `Int[3,4][] dynamicArrayOfThreeByFourArrayOfInt`


## Signed Size
`Int` (i.e. signed) as type for `*.size()`
- Because mixed integer arithmetic ("signed - unsigned") and "unsigned - unsigned" is difficult to handle.
    - In C/C++ `aUInt - 1 >= 0` is _always_ true (even if `aUInt` is `0`)
- When working with sizes, calculating the difference is common; Then you are limited to `Int`/`SSize`/`PtrDiff` (i.e. signed integer) anyway.
- Anyone who needs more than 2GB of data in a single "byte array", should please use a 64 bit platform.
- For bounds checking, the two comparisons `x >= 0` and  `x < width` may very well be reduced to a single `UInt(x) < width` _by the compiler_ in an optimization step. 
- Then types ~~`Size`~~ and ~~`SSize`~~/~~`PtrDiff`~~ are not necessary anymore, so two types less.
    - We simply use `Int` instead.
    - `UInt` is used in rare cases (i.e. hardware registers, masks, flags), surely _not_ for sizes.
- See also Going Native 2012, Day 2, Interactive Panel: Ask Us Anything
    - [42:41 - 45:28](https://youtu.be/Puio5dly9N8?feature=shared&t=2561)
    - [1:02:51 - 1:03:14](https://youtu.be/Puio5dly9N8?feature=shared&t=3771)


## Associative Arrays
- AKA Maps (or Dictionaries)
- `TValue[TKey]` as short form of `Map<TKey, TValue>`
    - e.g. `ContactInfo[String] contactInfoForID` as short form  
      of `Map<String, ContactInfo> contactInfoForID`,
    - as [in D](https://dlang.org/spec/hash-map.html).
- "Make simple things simple",  
  having a short syntax for associative arrays so they are easy to use.
- Maybe partial template specialization:
    - `Map<Int, ...>` is a `HashMap`
    - `Map<String, ...>` is a `SortedMap`


## Function/Loop Parameter Passing
The basic idea is to have the most efficient/appropriate parameter passing mode as the _default_, and to give more the intent than the technical realization.  
Taken from [Cpp2 / Herb Sutter](https://hsutter.github.io/cppfront/cpp2/functions/) (who extended/generalized the `out` parameters of C#).
- **Default is passing as `in`**-parameter.
    - So if no parameter passing keyword is given, `in` parameter passing is used.
    - All other parameter passing methods need to be explicitly given.
- Function call parameters are passed as either **`in`**, **`inout`**, **`out`**, **`copy`**, **`move`**, or **`forward`**.
    - Wording fits nicely for function parameters: How does the parameter get into the function body (or out of it).
- The loop variable of `for ... in` is passed as either **`in`**, **`inout`**, **`copy`**, or **`move`**  
  (`out` and `forward` are not applicable here).
    - With `for` loops these keywords describe how the information (i.e. the variable) gets into the body of the loop (or out of it).
- Parameter passing methods/keywords:
    - **`in`**
        - to mark parameters used as input.
        - Is the default if no parameter passing keyword is given.
        - Suitable for most basic functions, like `print(Int count, String text)`.
        - Technically either `const X&` (a constant reference) or `const X` (a constant copy), sometimes `const XView` (a view type, e.g. a slice).
            - `const X&` as default, suitable for most, medium to large types:
                - `add(BigInt a, BigInt b)`
                    - is effectively translated to `add(const BigInt& a, const BigInt& b)`  
                - `BigInt[] bigIntArray = ...`  
                  `for i in bigIntArray { ... }`
                    - `i` is `const BigInt&`  
            - `const X` for "small types" (like `Int`, `Float`, etc.):
                - `for i in [1, 2, 3] { ... }`
                    - `i` is `const Int`
                - `for str in ["a", "b", "c"] { ... }`
                    - `str` is `const StringView` (a string-literal like `"a"` forms a `const StringView`, therefore `["a", "b", "c"]` is a `const StringView[3]`)
            - `const XView` for types `X` that have a corresponding view type:
                - `concat(String first, String second)`
                    - is effectively translated to `concat(const StringView first, const StringView second)`
                - `String[] stringArray = ...`  
                  `for str in stringArray { ... }`
                    - `str` is `const StringView`
    - **`inout`**
        - to mark parameters used as input (so they need to be initialized at the caller) _and_ as output.
        - Technically a non-const/mutable reference (`X&`)
        - Suitable for e.g. `swap(inout Int a, inout Int b)`.
        - Keyword `inout` is also to be given at the caller: `swap(inout a, inout b)`
        - Examples:
            - `for inout str in stringArray { ... }`
                - `str` is `String&`
            - `for inout i in intArray { ... }`
                - `i` is `Int&`
    - **`out`**
        - to mark output parameters (is initialized at the callee).
        - Technically, like `inout`, a non-const/mutable reference (`X&`), but without prior initialization.
        - Keyword `out` is also to be given at the caller:
          ```
          String errorDetails
          if not open("...", out errorDetails) {
              cout << errorDetails
          }
          ```
        - Maybe even with ad-hoc declaration of the out variable:
          ```
          if not open("...", out String errorDetails) {
              cout << errorDetails
          }
          ```
        - Maybe even with broader scope:
          ```
          if open("...", out String errorDetails) {
              // ...
          } else {
              cout << errorDetails
          }
          ```
    - **`copy`**
        - to create a (mutable) copy (i.e. pass "by value"). 
        - Technically a non-const/mutable value (`X`), sometimes the "full class" `X` of a view class `XView`.
        - Examples:
            - `for copy i in [1, 2, 3] { ... }`
                - `i` is `Int`
            - `for copy str in stringArray { ... }`
                - `str` is `String`
            - `for copy str in ["an", "array", "of", "words"] { ... }`
                - `str` is `String` (not ~~`StringView`~~, due to the `X`/`XView`-copy-trick)
    - **`move`**
        - for move sematics.
        - Technically a right-value reference (`X&&`)
    - **`forward`**
        - for perfect forwarding.
        - TODO Technically a right-value reference (`X&&`), too?
- Type traits **`InParameterType`** to determine the concrete type to be used for `in`-passing.
    - The rule of thumb is:
        - Objects that are POD (Plain Old Data, i.e. with no pointers) with a size less than or equal to the size of two `Int` (i.e. up to 16 bytes on 64 bit platforms) are passed by value.
        - Larger objects (or non-POD) are passed by reference.
    - So as general default use _const reference_,
        - `using<type T> T::InParameterType = const T&`  
    - and use a "list of exceptions" for the "const _value_ types".
        - ```
          using       Bool::InParameterType = const Bool
          using       Int8::InParameterType = const Int8
          using      Int16::InParameterType = const Int16
          using      Int32::InParameterType = const Int32
          using      Int64::InParameterType = const Int64
          ...
          using     UInt64::InParameterType = const UInt64
          using    Float32::InParameterType = const Float32
          using    Float64::InParameterType = const Float64
          using StringView::InParameterType = const StringView
          using  ArrayView::InParameterType = const ArrayView
          ...
          ```
        - `using<type T> Complex<T>::InParameterType = T::InParameterType`
            - A generic rule: `Complex<T>` is passed the same way as `T`,
            - could be further refined/corrected with  
              `using Complex<Float128>::InParameterType = const Complex<Float128>&`  
              as `sizeof(Complex<Float128>)` is 32 bytes (so pass by reference), despite `sizeof(Float128)` is 16 bytes (so pass by value would be the default).
        - This way developers only need to extend this list if they create a _small_ class (and if they need or want maximum performance). And I expect most custom classes to be larger than 16 bytes (so nothing to do for those).
- Special **trick for types with views**
    - Applicable only for types `X` that have an `XView` counterpart where
        - `X` can implicitly be converted to `XView`,
        - `XView` can (explicitly) be converted to `X`, and
        - `XView` has the same "interface" as `const X` (i.e. contiguous memory access).
    - like:  
        - `String` - `StringView`
        - `Array` - `ArrayView`
        - `Vector` - `VectorView`
    - As example, with `String`/`StringView`:
        - `using String::InParameterType = const StringView`  
          i.e. **for an `in String` _in fact_ a `const StringView`** is used as parameter type.
        - So all functions with a `String` (AKA `in String`) parameter would _implicitly_ accept
            - a `String` (as that can implicitly be converted to `StringView`) 
            - a `StringView` (that somehow is the more versatile variant of `const String&`),
            - and therefore also _every third-party string_ class (as long as it is implicitly convertable to `StringView`).
        - This way people do not necessarily need to understand the concept of a `StringView`. They simply write `String` and still cover all these cases.
        - Example:
            - `concat(String first, String second)`
                - is short for `concat(in String first, in String second)`
                - and extends to `concat(const StringView first, const StringView second)`
        - For cases where you need to _change_ the string parameter, an **`in`**`String` (whether it is a `const String&` or a `const StringView`) is not suitable anyway. And all other parameter passing modes (`inout`, `out`, `copy`, `move`, `forward`) are based on real `String`s.
        - Though I don't see any advantage with respect to the `for ... in` loop, I would still apply the same rules just to ensure consistency.
        - Example:
            - `String[] stringArray = ["a", "b", "c"]`  
              `for str in stringArray { ... }`
                - `str` is `const StringView`
    - This is not possible with every view type, as some views do not guarantee contiguous memory access (typically when they do support stride):
        - ~~`Matrix` - `MatrixView`~~
        - ~~`Image` - `ImageView`~~
        - ~~`MDArray` - `MDArrayView` (AKA MDSpan?)~~
        - Maybe having some `XBasicView` instead, explicitly _without_ stride support,  
          that can cut off at start and end, but no slicing:
            - `Matrix` - `MatrixBasicView`
            - `Image` - `ImageBasicView`
            - `MDArray` - `MDArrayBasicView`
    - Small `...View`-classes with a size of up to 16 bytes (such as `StringView`, `ArrayView`, and `VectorView`) will be passed by value:
        - ```
          using String::InParameterType = const StringView
          using  Array::InParameterType = const ArrayView
          using Vector::InParameterType = const VectorView
          ```
    - Bigger `...View`-classes with a size of _more_ than 16 bytes (such as `MatrixBasicView`, `ImageBasicView`, and `MDArrayBasicView`) will be passed by reference:
        - ```
          using  Matrix::InParameterType = const MatrixBasicView&
          using   Image::InParameterType = const ImageBasicView&
          using MDArray::InParameterType = const MDArrayBasicView&
          ```
- Type trait **`CopyParameterType`**
    - of a type `T` typically simply is `T`  
      `using<type T> T::CopyParameterType = T`  
    - but for `View`-types it is the corresponding "full" type:
      ```
      using       StringView::CopyParameterType = String
      using        ArrayView::CopyParameterType = Array
      using       VectorView::CopyParameterType = Vector
      using       MatrixView::CopyParameterType = Matrix
      using  MatrixBasicView::CopyParameterType = Matrix
      using        ImageView::CopyParameterType = Image
      using   ImageBasicView::CopyParameterType = Image
      using      MDArrayView::CopyParameterType = MDArray
      using MDArrayBasicView::CopyParameterType = MDArray
      ```
    - The idea is to get a _mutable copy_ of the object, even without understanding the concept of a `View`.
    - Example:
        - `for copy str in ["an", "array", "of", "words"] { ... }`
            - `str` is `String` (not ~~`StringView`~~)
            - This way people do not necessarily need to understand the concept of a `StringView` literal. They simply write `copy` to get a `String` with a copy of the content of the `StringView`.
            - (This is currently the only useful example I can think of.)


## Literals
- `True`, `False` are Bool,
    - as in Python,
    - uppercase as they are constants.  
- `NullPtr` is the null pointer,
    - it is of the type `NullPtrType`,
    - explicit cast necessary to convert any pointer to `Int`.
- `123` is an integer literal of arbitrary precision
    - Can be converted to any integer type it fits into (signed and unsigned)
        - `Int8 a = 1`    // Works because `1` fits into `Int8`
        - `Int8 b = 127`  // Works because `127` fits into `Int8`
        - `Int8 c = 128`  // _Error_ because 128 does _not_ fit into `Int8`
        - `Int8 d = -128` // Works because `-128` fits into `Int8`
        - `Int8 e = -129` // _Error_ because `-129` does _not_ fit into `Int8`
        - `UInt8 f = 255` // Works because `255` fits into `UInt8`
        - `UInt8 g = 256` // _Error_ because `256` does _not_ fit into `UInt8`
        - `UInt8 h = -1`  // _Error_ because `-1` does _not_ fit into `UInt8`
        - `Int16 i = 32767` // Works
        - `Int32 j = 2'147'483'647` // Works
        - `Int64 k = 9'223'372'036'854'775'807` // Works
        - `Int l = a`     // Works because `Int8` fits into `Int32`
        - `UInt m = l`    // _Error_ because `Int` does _not always_ fit into `UInt`
            - `UInt m = UInt(l)` // Works
        - `Int n = m`     // Error because `UInt` does _not always_ fit into `Int`
            - `Int n = Int(m)`   // Works
    - Small integer literals like `123` are interpreted as `Int`
    	- in case of type inferring, parameter overloading and template matching.
        - Big integer literals are interpreted as `Int64`, `Int128`, `Int256`, `BigInt`, if required due to the size.
    - Difficult: Constexpr constructor that accepts an arbitrary precision integer literal and can store that in ROM
        - Store as array of `Int`
    - `123u` is `UInt`
    	- `-123u` is an error.
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
    - Difficult: Constexpr constructor that accepts an arbitrary precision float literal and can store that in ROM
        - Store the mantissa as arbitrary precision integer (i.e. array of `Int`), plus the exponent as as arbitrary precision integer (i.e. array of `Int`, most always only a single `Int`)
    - Small floating point literals like `1.0` are interpreted as `Float`
        - in case of type inferring, parameter overloading and template matching.
        - Big floating point literals are interpreted as `Float64`, `Float128`, `Float256`, `BigFloat`, if required due to the size/precision.
    - `1.0f` is always `Float32`
    - `1.0d` is always `Float64`
- `Infinity`/`-Infinity` is a floating point literal of arbitrary precision for infinity values
    - Can be converted to any float type.
    - Is interpreted as `Float`
        - in case of type inferring, parameter overloading and template matching.
- `NaN` is a floating point literal of arbitrary precision for NaN ("not a number") values
    - Can be converted to any float type
    - Is interpreted as `Float`
        - in case of type inferring, parameter overloading and template matching.
- `"Text"` is a `StringView` with UTF-8 encoding.
    - No null termination.
        - If necessary
            - use `"Text"sz`, `"Text\0“`  or
            - convert using `StringZ("Text")`.
    - Data is typically stored in read-only data segments (".rodata") or ROM.
    - A Cilia-to-C++-transpiler would translate every string literal to a C++ string_view-literal:
        - `"Text"` -> `u8"Text"sv`
        - (`"Text"sv` as to avoid null termination, and `u8"Text"` as to have UTF-8 encoding.)
    - A StringView starts like a String does: pointer to first character plus length,
        - so slicing of String to StringView is possible.
        - TODO This would probably not work with small string optimization (SSO), so it is of limited use.
  
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
    - `f"M[{i},{j}] = {M[i, j]}"`
        - like f-strings in Python.
    - ~~Or `$"M[{i},{j}] = {M[i, j]}"` like in C#?~~
    - Curly braces (`{}`) are used in std::format already.
    - TODO Any reason to use/prefer any other syntax?
- Alternative string literals
    - ~~`"Text"utf8` (but UTF-8 is the default anyway, so just "Text" is also UTF-8)~~
    - ~~`"Text"utf16`~~
    - ~~`"Text"utf32`~~
    - ~~`"Text"ascii`~~
        - ~~Syntax error, if one of the characters is not ASCII.~~
    - ~~`"Text"latin1`~~
        - ~~Syntax error, if one of the characters is not Latin-1.~~
    - TODO C++ uses
        - prefixes
            - `u8"..."` and `u8'...'` for UTF-8
            - `u"..."` and `u'...'` for UTF-16
            - `U"..."` and `U'...'` for UTF-32
        - and user defined string suffixes
            - `"..."s` for `std::string`
            - `"..."sv` for `std::string_view`.
        - So as to avoid conflicts we should drop the Cilia string literals.
    - `u8"Text"` (but UTF-8 is the default anyway, so just "Text" is also UTF-8)
    - ~~`"Text"sz` is a zero terminated string (as used in C)~~
        - ~~Problem: How to combine e.g. `"..."ascii` and `"..."sz`?~~
            - Workaround: Use `"Text\0"ascii` instead.
    - All these available for multiline string literals and interpolated strings, too.
        - TODO Any reason, not to? 
- `[1, 2, 3]` is an array (here an `Int[3]`),
    - all elements have the same type.
- `{1, "Text", 3.0}` is an initialization list.
    - e.g. for `Tuple`
- `String[String]` (AKA `Map<String,String>`) is initialized with
  ```
  {
      "Key1": "Value1"
      "Key2": "Value2"
      "Key3": "Value3"
      "Key4": "Value4"
  }
  ```
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
    - `xor` in addition to `!=`
    - `not` in addition to `!`
- `Int32` instead of `int32_t` or `qint32`,
    - so no prefix "q" nor postfix "_t", and in CamelCase.
- When translating C++ code to Cilia then change conflicting names, e.g.
    - `int var` -> `Int __variable_var`
    - `class func` -> `class __class_func`
    - `yield()` -> `func __function_yield()`


## Safety and Security
- **Range & Validation Checks**
	- The low hanging fruit would be to enable _by default_, also in release builds (not only in debug):
		- range checks, to detect **buffer overflows** or similar,
		- safe iterators, to detect invalid iterators.
			- So every safe iterator would have a pointer to the element _and_ a pointer to the container.
				- Naive: check at every dereferencing
				- Optimized: check at first dereferencing, but thereafter only after a call to a non-const member function of the container (or if such a call cannot be excluded).
    - This should fix the majority of C/C++ security issues.  
      To achieve maximum performance in all cases, there could be a third build configuration for even faster, but potentially unsafe builds.  
    - So we would have:
        - **Debug**
            - for debugging,
            - with range checks,
            - with line by line debug info, and
            - often with a modified memory layout (to find more types of errors).
        - **Release**
            - for deployment,
            - _with_ range checks,
            - suitable for most situations,
            - by default using _safe_ containers (with safe iterators),
                - optionally using unsafe containers (with unsafe iterators),
            - with memory layout compatible to ~~EvenFasterBut~~UnsafeRelease.
        - ~~EvenFasterBut~~**UnsafeRelease**
            - for deployment,
            - _without_ range checks (for even better performance),
            - by default still using _safe_ containers (with safe iterators),
                - so memory layout is compatible to Release,
            - _optionally_ using unsafe containers (with unsafe iterators, for even better performance).
- **Initialization**
    - No initialization means random values. In this case they are in fact often zero, but _not always_.
    - Initializing large arrays (e.g. `Array`, `Image`, `Vector`, or `Matrix` with many elements) takes a noticeable amount of time, so we don't want to always initialize everything.
        - With virtual memory it could actually be (almost) "free" to initialize _large_ arrays with zero. But only when using heap memory directly. Small memory regions, that were used before, still need to be overwritten with zeros.
    - We could warn (or maybe even consider it an error) if not initialized,  
      and use a keyword `noinit` to avoid that warning/error.  
      ```
      Int i         // Warning
      Int j noinit  // No warning
      Int j = 1     // No warning
      ```
    - Classes / custom types
        - Mark constructors with `noinit` when they do not initialize their values, so `noinit` should be used when calling them consciously.
        - ```
          class Array<type T> {
              Array(Int size) noinit { ... }
              Array(Int size, T value) { ... }
          }
          Array<Float> anArray(10)         // Warning
          Array<Float> anArray(10) noinit  // No warning
          Array<Float> anArray(10, 1.0)    // No warning
          ```
    - Also for free memory/heap
        - ```
          var arrayPtr = new Array<Float>(10)         // Warning
          var arrayPtr = new Array<Float>(10) noinit  // No warning
          var arrayPtr = new Array<Float>(10, 1.0)    // No warning
          ```
- **`safe`** as default, **`unsafe`** code blocks as escape.
    - Mainly to guide developers:
        - to signal what to do and what not to do,
        - `unsafe` is not regularly used, normally you just use the already _existing_, carefully developed and tested abstractions (like `Array`, `Vector`, `Matrix`, ...).
    - Not allowed in safe code:
        - Subscript access to pointers,
        - `reinterpretCastTo<T>(...)`,
        - calling functions marked as `unsafe`,
        - use of `noinit`.
    - Still allowed/undetected in unsafe code:
        - Integer overflow (checking that all the time seems too costly)
    - `unsafe` code is _necessary_ to implement certain abstractions (like container classes):
        - ```
          operator[Int i] -> T& {
              if CHECK_BOUNDS and (i < 0 or i >= size) {
                  terminate()
              }
              unsafe {
                  return data[i]
              }
          }
          ```
    - A function with unsafe code does not necessarily has to be marked as `unsafe` itself.
        - `unsafe` is a marker for those parts (subfunctions or code blocks) that are not safe (i.e. dangerous) and need to be checked carefully.
        - Functions containing unsafe code enclosed in an `unsafe` block _do not_ have to be marked with `unsafe` themselves.
        - Only functions containing unsafe code _not_ enclosed in an `unsafe` block have to be marked with `unsafe` themselves.
        - Unsafe is transitive (from an `unsafe` inner function to the outer function), but limited to the scope of `unsafe` blocks.
- `cilia::safe::Int`
    - Like `cilia::Int`, but with **overflow check** for all operations,
        - may throw OverflowException (or abort the program).
    - Generally considered to be too costly, even in languages that are otherwise considered as "safe".
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
        - `objPtr is T*` instead of `dynamic_cast<T*>(objPtr) != NullPtr`
        - `obj is cilia::Array` (i.e. a template)
        - `obj is cilia::Integer` (i.e. a concept)
    - TODO Also support value query?
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


## `cilia` Standard Library
Standard library in namespace `cilia` (instead of `std` to avoid naming conflicts and to allow easy parallel use).
- With a Cilia version of each standard class/concept (i.e. CamelCase class names and camelCase function and variable names)
    - `cilia::String` instead of `std::string`
    - `Map` instead of `map`
        - `Dictionary` as alias with deprecation warning, as a hint for C# programmers.
    - `ForwardList` instead of `forward_list`
    - `UnorderedMap` instead of `unordered_map`
    - `ValueType` instead of `value_type`
    - Some exceptions/variations:
        - `Array` instead of `vector`
        - `StringStream` instead of `stringstream`
            - `TextStream`, `ByteStream`, ...
- Mostly a shallow wrapper,
    - e.g. `class cilia::String : public std::string { ... }`
    - with "**aliases**" for 
        - member variables  
          `using var x = data[0]`  
          `using var y = data[1]`
        - member functions  
          `using func pushBack = push_back`
    - A wrapper is not strictly necessary, Cilia can access/call every C/C++ class/function without.  
      But only _with_ wrapper we have
        - a Cilia standard library in the "idiomatic" Cilia style (i.e. CamelCase),
        - whose types/classes are also used with existing C++ APIs (i.e. using Int, Int32, String and StringView instead of int, int32_t, string and string_view).
- Matrix & Vector
    - Geometry
        - Static/fixed size
        - For small, fixed size vectors & matrices ,
            - as typically used in geometry (i.e. 2D, 3D, 4D).
        - `cilia::Vector<Int size, T = Float>`
            - `cilia::Vector2<T = Float>`
            - `cilia::Vector3<T = Float>`
            - `cilia::Vector4<T = Float>`
        - `cilia::Matrix<Int rows, Int columns, T = Float>`
            - `cilia::Matrix22<T = Float>`
            - `cilia::Matrix33<T = Float>`
            - `cilia::Matrix44<T = Float>`
    - Linear Algebra
        - Dynamic/variable size
        - For large, dynamically sized vectors & matrices,
            - as typically used in linear algebra: BLAS (Basic Linear Algebra Subprograms)
        - `cilia::Vector<T = Float>`
        - `cilia::Matrix<T = Float>`
            - Stored column-major, like:
              ```
              0 3 6
              1 4 7
              2 5 8
              ```
        - `cilia::MDArray<Int dimensions, T = Float>`
            - also see `MDSpan`
          
- Image
    - `cilia::Image<T = Float>`
    - Almost like `cilia::Matrix`, but stored row-major, like:
      ```
      0 1 2
      3 4 5
      6 7 8
      ```
      
- Views, Slices
    - `ArrayView`
    - `VectorView`
    - `MatrixView`
    - `ImageView`
    - `MDArrayView`


## String, Char & CodePoint
- `cilia::String` with _basic/standard_ unicode support.
    - Based on UTF-8, as that IMHO is (among all the Unicode formats)
        - the most widespread nowadays,
        - the most compatible (as it is ASCII based),
        - the most efficient, at least for "western" use (and you are free to use UTF16- or UTF32String otherwise).
    - Iteration over a `String` or `StringView` by:
        - **grapheme clusters**
            - represented by `StringView`.
            - This is the _default form of iteration_ over a `String` or `StringView`
            - A single grapheme cluster will often consist of multiple code units   
              and may even consist of multiple code points.
            - `for graphemeCluster in "abc 🥸👮🏻"`
                - "a", "b", "c", " ", "🥸", "👮🏻"
                - "\x61", "\x62", "\x63", "\x20", "\xf0\x9f\xa5\xb8", "\xf0\x9f\x91\xae\xf0\x9f\x8f\xbb"
            - A bit slow, as it has to find grapheme cluster boundaries.
            - It is recommended to mostly use the standard functions for string manipulation anyway. But if you need to iterate manually over a Unicode-String, then grapheme-cluster-based iteration is the safe/right way. 
            - Additional/alternative names?
                - `for graphemeCluster in text.asGraphemeClusters()`?
        - **code points**
            - represented by `UInt32`,
                - independent of the encoding (i.e. the same for UTF-8, UTF-16, and UTF-32 strings).
                - Called "auto decoding" in D.
            - `for codePoint in "abc 🥸👮🏻".asCodePoints()`
                - 0x00000061, 0x00000062, 0x00000063, 0x00000020, &nbsp; 0x0001F978, &nbsp; 0x0001F46E, 0x0001F3FB 
            - **Note:** _Not_ even with UTF-32 do all grapheme clusters fit into a single code point,  
              so not:
        	    - emoji with modifier characters like skin tone or variation selector,
        	    - diacritical characters (äöü..., depending on the normal form chosen),
        	    - surely some more ...
            - A bit faster than iteration over grapheme clusters, but still slow, as it has to find code point boundaries in UTF-8/16 strings.
            - Fast with UTF-32 strings, but UTF-32 strings in general are often slower than UTF-8, simply due to their size (cache, memory bandwidth).
        - **code units**
            - represented by
                - `Char` for `String`
                    - it is `Char`==`Char8`==`Byte`==`UInt8` and `String`==`UTF8String`
                - `Char16` for `UTF16String`
                - `Char32` for `UTF32String`
            - `for aChar8 in "abc 🥸👮🏻".asArray()`
                - 0x61, 0x62, 0x63, 0x20,  &nbsp;  0xf0, 0x9f, 0xa5, 0xb8,  &nbsp;  0xf0, 0x9f, 0x91, 0xae, 0xf0, 0x9f, 0x8f, 0xbb
                - same for
                    - `for aChar8 in u8"abc 🥸👮🏻".asArray()`
                    - `for aChar8 in UTF8String("abc 🥸👮🏻").asArray()`
            - `for aChar16 in u"abc 🥸👮🏻".asArray()`
                - 0x0061, 0x0062, 0x0063, 0x0020,  &nbsp;  0xD83E, 0xDD78,  &nbsp;  0xD83D, 0xDC6E, 0xD83C, 0xDFFB
                - same for `for aChar16 in UTF16String("abc 🥸👮🏻").asArray()`
            - `for aChar32 in U"abc 🥸👮🏻".asArray()`
                - 0x00000061, 0x00000062, 0x00000063, 0x00000020,  &nbsp;  0x0001F978,  &nbsp;  0x0001F46E , 0x0001F3FB
                - same for `for aChar32 in UTF32String("abc 🥸👮🏻").asArray()`
    - `string.toUpper()`, `string.toLower()`
        - `toUpper(String) -> String`, `toLower(String) -> String`
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
            - `for aChar in a"abc"`
                - 0x61, 0x62, 0x63
                - 'a', 'b', 'c'
                - Compilation error, if string literal contains non-ASCII characters.
                - same for `for aChar in ASCIIString("abc")`
                    - but Exception thrown, if string contains non-ASCII characters.
        - Implicitly convertable to `String`==`UTF8String`.
            - Very fast conversion, as all characters have the same binary representation.
    - `Latin1String`, a string containing only Latin-1 (ISO 8859-1) characters.
        - Iteration over an `Latin1String` or `Latin1StringView` by `Char`==`Char8`==`Byte`
            - `for aChar in l"äßç"`
                - 0xe4, 0xdf, 0xe7
                - 'ä', 'ß', 'ç'
                - Compilation error, if string literal contains non-Latin-1 characters.
                - same for `for aChar in Latin1String("abc")`
                    - but Exception thrown, if string contains non-Latin1 characters.
        - Explicitly convertable to `String`==`UTF8String`.
            - Not as fast a conversion as ASCIIString to String, because typically some characters need to be translated into _two_ UTF-8 code units.
- `Char8`, `Char16`, `Char32`
    - are considered as _different_ types for parameter overloading,
    - but otherwise are like `UInt8`, `UInt16`, `UInt32`,

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
            - lines
                - `for line in text.asLines()`
            - sentences (needs list of abbreviations, like "e.g.", "i.e.", "o.ä.")
                - `for sentence in text.asSentences()`
        - Depending on locale
            - `string.toUpper(locale)`, `string.toLower(locale)`
                - `toUpper(String, locale) -> String`, `toLower(String, locale) -> String`
            - `stringArray.sort(locale)`
                - `sort(Container<String>, locale) -> Container<String>`
            - `compare(stringA, stringB, locale) -> Int`
     

## Misc 
- Two-Pass Compiler
    - so no forward declarations necessary,
    - as with C# and Java (but unlike C/C++, due to its single-pass compiler).

- **Mixed arithmetic**
    - Mixing signed with unsigned integer
        - `Signed + - * / Unsigned` is an error
            - you have to cast explicitly,
            - i.e. no implicit cast (neither ~~`UInt` -> `Int`~~ nor ~~`Int` -> `UInt`~~).
            - `Int` (i.e. signed) is almost always used anyways.
        - Error with `if aUInt < anInt`
            - you have to cast
        - Error with `if aUInt < 0`
            - if the literal on the right is `<= 0`
    - Mixing integer with float
        - `1 * aFloat` is possible
            - Warning, if the integer literal cannot be reproduced exactly as `Float32`/`64`
        - `anInt * aFloat` is possible
            - Warning that the integer variable may not be reproduced exactly as `Float32`/`64`,  
              i.e. with
                - `aFloat32 * anInt8`  // OK
                - `aFloat32 * anInt16` // OK
                - `aFloat32 * anInt32` // Warning
                    - `aFloat32 * Float32(anInt32)` // OK
                - `aFloat32 * anInt64` // Warning
                    - `aFloat32 * Float32(anInt64)` // OK
                - `aFloat64 * anInt8`  // OK
                - `aFloat64 * anInt16` // OK
                - `aFloat64 * anInt32` // OK
                - `aFloat64 * anInt64` // Warning
                    - `aFloat64 * Float64(anInt64)` // OK

- [Endianness](https://en.wikipedia.org/wiki/Endianness)
    - Big Endian (Motorola)
        - `cilia::be::Int`, `Int8`, `Int16`, `Int32`, `Int64`
        - MSB first (most significant byte first), starting with the "big end"
        - MSb first (most significant bit first)
        - classical "[network byte order](https://en.wikipedia.org/wiki/Endianness#Networking)"
    - Little Endian (Intel)
        - `cilia::le::Int`, `Int8`, `Int16`, `Int32`, `Int64`
        - LSB first (least significant byte first), starting with the "little end"
        - LSb first (least significant bit first)
        - "[USB byte order](http://cholla.mmto.org/computers/usb/endian.html)"

- Extended & Arbitrary Precision Integer & Float
    - `Int128`, `Int256`
    - `UInt128`, `UInt256` e.g. for SHA256
    - `BigInt` – Arbitrary Precision Integer
        - for cryptography, maybe computer algebra, numerics
        - see [Boost.Multiprecision](https://www.boost.org/doc/libs/1_79_0/libs/multiprecision/doc/html/index.html), [GMP](https://gmplib.org)
    - `BFloat16` (Brain Floating Point)
    - `Float128`
    	- 1 bit sign, 15 bit exponent, 112 bit significand
    	- `Float256`?
    - `DDFloat`, `TDFloat`, `QDFloat`
        - double-double/triple-double/quad-double arithemtic
        - [wiki.org/Double-Double Arithmetic](https://en.wikipedia.org/w/index.php?title=Quadruple-precision_floating-point_format)
        - [https://stackoverflow.com/a/6770329](https://stackoverflow.com/a/6770329)
        - Problem: Is saved incompatible to the IEEE 754 format for 128/256/512 bit float.
    - `BigFloat<>` for arbitrary precision float,
        - see [GMP](https://gmplib.org), [MPFR](https://www.mpfr.org)
        - The precision is arbitrary but fixed, either
          - statically, i.e. at compile time, as part of the BigFloat type, or
          - dynamically, i.e. at runtime, as property of a BigFloat variable.

- Integer operations **with carry** (flag or UInt)  
  (to implement `Int128`, `Int256` etc.)
    - Add with carry (flag, i.e. one bit only)
        - `UInt c = add(UInt a, UInt b, inout Bool carryFlag)`
            - `c = bits63..0(a + b + carryFlag)`  
              `carryFlag = bit64(a + b + carryFlag)`
        - `a.add(UInt b, inout Bool carryFlag)`
            - `a = bits63..0(a + b + carryFlag)`  
              `carryFlag = bit64(a + b + carryFlag)`
    - Mutiply with carry (high data, i.e. one UInt)
        - `UInt c = multiply(UInt a, UInt b, out UInt cHigh)`
            - `c = bits63..0(a * b)`  
              `cHigh = bit127..64(a * b)`
        - `a.multiply(UInt b, out UInt aHigh)`
            - `a = bits63..0(a * b)`  
              `aHigh = bit127..64(a * b)`
        - Mutiply-Add with carry (high data, i.e. one UInt)
            - `UInt d = multiplyAdd(UInt a, UInt b, UInt c, out UInt dHigh)`
                - `d = bits63..0(a * b + c)`  
                  `dHigh = bit127..64(a * b)`
            - `a.multiplyAdd(UInt b, UInt c, out UInt aHigh)`
                - `a = bits63..0(a * b + c)`  
                  `aHigh = bit127..64(a * b + c)`
    - Shift
        - `b = shiftLeftAdd(UInt a, Int steps, inout UInt addAndHigh)`
        - `a.shiftLeftAdd(Int steps, inout UInt addAndHigh)`
        - `b = shiftOneLeft(UInt a, inout Bool carryFlag)`
        - `a.shiftOneLeft(inout carryFlag)`
      
- `cilia::saturating::Int`
    - Like `cilia::Int`, but with **saturation** for all operations.
        - Limit to maximum, no wrap around.
        - Typically using SIMD (as those „media/DSP instructions“ do support saturation natively).
    - see [https://en.wikipedia.org/wiki/Saturation_arithmetic](https://en.wikipedia.org/wiki/Saturation_arithmetic)
    - `saturating::Int8`/`Int16`/`Int32`/`Int64`
    - `saturating::Uint`
        - `saturating::UInt8`/`UInt16`/`UInt32`/`UInt64`

- Reserved keywords for _future_ use (maybe, maybe not).
    - `parallel` for `parallel for ...`
    - `interface` for pure abstract base classes or similar constructs?
    - `struct` for some variant of C++ strcuts/classes?
    - `Null` instead of `NullPtr`? (But actually it always is a pointer in our context.)
    - `template`, as it still is unclear, if the "new", shorter template expressions are really better.
    - `let` for `const` variable declarations?
    - `constfunc` instead of `constexpr` or `consteval`?

- Versioning of the Cilia source code
    - Via file ".cilVersion" in a (project) directory,
        - similar to ".clang_format",
        - also possible file by file: "Matrix.cilVersion" (for "Matrix.cil").
    - Via file extension: 
        - "*.cil" – always the latest language version (if not overridden via ".cilVersion")
        - "*.2024.cil" – version from the year 2024
        - "*.2024b.cil" – second version from the year 2024

- No [function-like macros](https://www.geeksforgeeks.org/cpp-macros/), just object-like:
    - `#define`
    - `#if`
    - `#else`
    - `#endif`

- TODO OpenMP-like parallel programming?
    - ```
      Floar[] arr = ...
      for i in 0..<arr.size() {
          arr[i] = 2 * arr[i]
      }
      ```
    - ```
      Floar[] arr = ...
      for i in 0..<arr.size() parallel {
          arr[i] = 2 * arr[i]
      }
      ```
    - ```
      Floar[] arr = ...
      for i in 0..<arr.size()
      parallel batch(1024) {
          arr[i] = 2 * arr[i]
      }
      ```
    - ```
      Floar[] arr = ...
      for i in 0..<arr.size()
      parallel if arr.size() > 65535 {
          arr[i] = 2 * arr[i]
      }
      ```
    - ```
      Floar[] arr = ...
      Float sum = 0.0
      for i in 0..<arr.size() parallel reduce(sum: +) {
          sum += arr[i]
      }
      ```
