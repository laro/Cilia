---
permalink: /more/other-ideas/
order: 1
---

## Other Ideas, Good & Bad
### **Circle**
- **Fix C++'s "wrong defaults"**  
    [Sean Baxter](https://x.com/seanbax) ([Circle](https://github.com/seanbaxter/circle)), [writes about C++'s wrong defaults](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#to-err-is-human-to-fix-divine):
    > C++ has a number of "wrong defaults," design decisions either inherited from C or specific to C++ which many programmers consider mistakes.
    > They may be counter-intuitive, go against expected practice in other languages, leave data in undefined states, or generally be prone to misuse.
    
    I am not familiar with all of these issues, but in a new language we certainly coud fix a lot of it.
    
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
        - Use the keyword `func` (but not typically `var`, unless you want type inferring)
    7. [Template brackets `< >` are a nightmare to parse.](http://eel.is/c++draft/temp.names#nt:template-argument-list)
        - I would not like to change this, only if it _really_ has to be.
        - Cpp2 / Herb Sutter kept `< >` after all.
    8. [Forwarding parameters and `std::forward` are error prone.](http://eel.is/c++draft/temp.deduct#call-3)
       - I am not familiar with the problem(s), but Cpp2 / Herb Sutter offers the `forward` keyword.
    9. [Braced initializers can choose the wrong constructor.](http://eel.is/c++draft/dcl.init.list#2)
        - Do without braced initialization altogether.
            - With the keyword `func` there is now a clear distinction between function declaration and variable declaration with initialization.
            - The classic initialization via `(...)`, ultimately a function call of the constructor, is a better fit anyway.
        - Braces / curly brackets only for initializer lists,
            - only when a constructor or assignment operator is defined, with `InitializerList` as input parameter,
            - i.e. for tuples, lists etc.
    10. [`0` shouldn't be a null pointer constant.](http://eel.is/c++draft/expr#conv.ptr-1)
        - Not allowed, use `NullPtr` or explicit casting.
    11. [`this` shouldn't be a pointer.](http://eel.is/c++draft/expr.prim.this#1)
        - Better `this` is a reference.
- [Versioning with feature directives](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#versioning-with-feature-directives)
    - Standardization is better than having multiple different language "dialects"  
      **but**
        - for transitioning of existings source code  and
        - for the evolution of a language
    - it is a very interesting idea to selectively enable new language features or defaults.
- [Circle C++ with Memory Safety](https://www.circle-lang.org/site/index.html)
    - Extending C++ for Rust-level safety.

### **Cpp2** (Herb Sutter)
- [is](https://hsutter.github.io/cppfront/cpp2/expressions/#is-safe-typevalue-queries)
- [as](https://hsutter.github.io/cppfront/cpp2/expressions/#as-safe-casts-and-conversions)
-  [Function](https://hsutter.github.io/cppfront/cpp2/functions/) [Parameter Passing](https://hsutter.github.io/cppfront/cpp2/functions/#parameters)
    - `in`, `inout`, `out`, `move`, `copy`, `forward`
    - I like this and therefore "copied" it. Admittedly without fully understanding the difference between `move` and `forward`.
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
    - Nice and short, as in math, but
        - actually not quite as in math, as math usually does not denote the type,
        - in the end it is _one more kind_ of notation for functions.
- [Implicit Move on Last Use](https://github.com/ntrel/cpp2?tab=readme-ov-file#implicit-move-on-last-use)
    - So resources are freed even earlier than in C++.
- [Named Return Values](https://github.com/ntrel/cpp2?tab=readme-ov-file#named-return-values)
- [Inspect](https://github.com/ntrel/cpp2?tab=readme-ov-file#inspect),
  a kind of pattern matching.
- [Unified `operator=` for assignment, constructor, and destructor)](https://github.com/ntrel/cpp2?tab=readme-ov-file#operator).
    - Takes a bit of getting used to.

### **Rust**
- Security, of course: borrow checker etc.
- Ranges

### [**Julia**](https://julialang.org/)
- "Cilia" sounds like something in between [C](https://en.wikipedia.org/wiki/C_(programming_language))/[C++](https://en.wikipedia.org/wiki/C%2B%2B) and [Julia](https://julialang.org), so maybe I could/should add some more of Julias interesting features to the Cilia wish list.
- Julia has very strong math support. Some of its features should be easy to copy.
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
                - „Precedence and associativity: When defining new operators or overloading existing ones, you can also specify their precedence and associativity, which determines the order in which they are evaluated.“
                    - That seems quite complicated to parse?!
                    - I cannot find any other reference to this feature, I assume it is a misunderstanding.
            - [https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm](https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm)
        - Much more operators
            - [https://stackoverflow.com/a/60321302](https://stackoverflow.com/a/60321302)
    - Many kinds of brackets?
        - [https://stackoverflow.com/a/33357311](https://stackoverflow.com/a/33357311)
        - TODO: Are these "unusual" brackets meant to be used as operators?


## Unfinished Ideas

- OpenMP-like parallel programming?
    - Serial code
      ```
      Floar[] arr = ...
      for i in 0..<arr.size() {
          arr[i] = 2 * arr[i]
      }
      ```
    - Parallel code
        - ```
          for i in 0..<arr.size() parallel { .. }
          ```
          ```
          for i in 0..<arr.size()
          parallel batch(1024) { .. }
          ```
          ```
          for i in 0..<arr.size()
          parallel if arr.size() > 65535 { .. }
          ```
          ```
          for i in 0..<arr.size()
          parallel if arr.size() > 65535 { .. }
          ```
          ```
          for i in 0..<arr.size() parallel reduce(sum: +) { .. }
          ```
          ```
          for i in 0..<arr.size()
          parallel
          if arr.size() > 65535
          reduce(sum: +)
          schedule(dynamic, 65536) { .. }
          ```
        - TODO Syntactically this is not a good solution.
            - We avoid brackets in `if` and `while`, but then use it for `reduce` and `schedule`...
            - Syntax should be better, clearer, or more powerful than plain OpenMP, otherwise better use just that.


## Old, Discarded Ideas for Cilia
For several topics there are alternative ideas, that were discarded but are still worth mentioning.


### No Trailing Semicolons
- As this is difficult & unclear/disputed: Keep C++ semicolons for now?
- Implicitly/clever multiline expressions as in Swift, Kotlin and JavaScript?  
  (Actually I don't know / remember the rules anymore.)


### Better Readable Keywords
- Instead of `class ... : ...` Cilia could have
    - `class ... extends ...` 
       - good for extending base classes
    - `class ... implements ...`
       - good fit for implementing pure abstract base classes (like interfaces)
- But then we would have two different keywords. And what about mixed cases, i.e. abstract classes with partly function implementation? (Probably best to use `implements` then, but still not nice.)

### Basic / Arithmetic Types
- `Float` could be 32-bit float: `Float` == `Float32`,
    - like in C++.
    - Then `Float` == `Float32` on all platforms.


### Variable Declaration
- Very short variable declaration:
    - Maybe possible to simply write `i = 3`?
    - Maybe `i := 3`?
- `let i = 0` instead of `const i = 0`
    - similar to Swift and Carbon.
    - In Rust `let mut` is used for variables,
    - in JavaScript `let` and `const` are very similar with slight differences.
- Always starting with keyword `var`
    - Examples:
        - `var Int i`
        - `var i : Int`
    - In case `func` for function declaration, but not `var` for variable declaration, is still not clear enough.
    - Swift, Kotlin and Circle always start variable declarations with `var`.
    - Not starting with `var` could be especially problematic in connection with omitting the trailing semicolons.


### Bitfields
One could define the order of bit in a bitfield.
- MSB (Most Significant Bit) first.
    - This way you can use
      ```
      class Float32Equivalent {
          UInt32:1  signIsNegative
          UInt32:8  exponent
          UInt32:23 significand // AKA mantissa
      }
      ```
      to read/interpret `Float32`,
    - and with
      ```
      class SignBitOfInt64 {
          UInt64:1 signIsNegative
      }
      ```
      signIsNegative is true for negative Int64.
    - Bits are left-aligned, so the first element always covers the most-significant bit:
      ```
      class MostSignificantThreeBits {
          UInt8:1 bit7
          UInt8:1 bit6
          UInt8:1 bit5
          // ...
      }
      ```
    - This is what typical "MSB-first" C++ compilers do (on big-endian PowerPC, MIPS, SPARC).
        - CiliaC may have to reverse the order of bit field elements and add some padding `UInt32:... __filler_for_right_alignment` (when using typical "LSB-first" C++ compilers like GCC x86).
    - Add your own filler (padding bits) to shift field elements/members on demand, e.g.
      ```
      class Sign {
          UInt32:1  filler
          UInt32:31 bit0
      }
      ```


### Arrays & ArrayViews
- `Int[] dynamicArrayOfIntegers`
    - May be confusing because it is so similar to fixed-size arrays,  
      but IMHO the inconsistency is **already in C/C++**:  
        - in function declarations
            - `int[]` and `int*` are actually the same,
        - but for local variables
            - `int[]` and `int*` mean different things:
                - `int array[3]` and `int array[] = { 1, 2, 3 }` are used for in-place arrays,
                - `int* array = new int[3]` is used for an int-array of _unknown size_.
- Mixed forms of static and dynamic array maybe useful:
    - `Int[3,,]`
    - `Int[3,4,]`


### Signed Size
- `UInt` as type for `*.size()` (i.e. still unsigned)  
  but with new rules for mixed integer arithmetic:
    - Unsigned +-*/ Signed -> Signed.
        - Signed is therefore considered the "larger" type compared to unsigned
        - `1` is `Int` (signed)
            - `1u` is `UInt` (unsigned)
        - Therefore `if aUInt - 1 >= 0` is a useful expression (as `1` is signed, `aUInt - 1` is signed, too)
        - But then also `aUInt + 1 == anInt`
- Or
    - `Size` - `Size` -> `SSize`
        - Problem: `-` results in `SSize`, but `+` results in `Size`?!
    - The conversion of a negative number into `Size` leads to an error instead of delivering a HUGE size.
    - Note: In the end this just didn't work out.

### Functions
- Function declarations could start with the keyword
    - `fn` (Rust, Carbon, New Circle),
    - `fun` (Kotlin), or
    - `function` (Julia)
- **Extension methods**
    - Possible, alternative syntax:  
      `func toString (Int this) -> String`
- **Function pointers**
    - Possible, alternative syntax variants:
    - Variant B:
        - `func((Int, Int) -> Int)* pointerToFunctionOfIntAndIntToInt`  // Closer to the function declaration but (too) many brackets
    - Variant C:
        - `(Int, Int -> Int)` [Functions are only available as pointers, so you can omit "*"?]
    - Variant D:
        - `func*(Int->Int) pointerToFunctionOfIntAndIntToInt`
        - `func*(Int) pointerToFunctionOfInt`
    - Variant E:
        - `func*(Int, Int)->Int pointerToFunctionOfIntAndIntToInt`
        - `(func*(Int, Int)->Int)[] arrayOfPointersToFunctionOfIntAndIntToInt`

          
### Operators
- Possible, alternative syntax for `pow(a, x)`:  
  `a**x` (as Python did)
- Some more kinds of range literals could be useful:
    - `8>..0:-1` – 7, 6, 5, 4, 3, 2, 1, 0
        - RangeExclusiveStartByStep(8, 0, -1)
    - `8>..0:-3` – 7, 4, 1
        - RangeExclusiveStartByStep(8, 0, -3)
    - `8..>0:-1` – 8, 7, 6, 5, 4, 3, 2, 1
        - RangeExclusiveEndByStep(8, 0, -1)
    - `8..>0:-1` – 8, 7, 6, 5, 4, 3, 2, 1
        - RangeDownwardsExclusiveEndByStep(8, 0, -1)
    - Incomplete ranges
        - `0<..` – RangeFromExclusiveStart(0)
    - Incomplete range with step
        - `8>..:-1` – RangeFromExclusiveStartByStep(8, -1)
        - `8>..:-2` – RangeFromExclusiveStartByStep(8, -2)
    - `0<..2` – RangeExclusiveStart(0, 2)
    - Range with negative step used for downwards iterating ranges: 
        - `2..0:-1` – RangeWithStep(2, 0, -1)
        - `3>..0:-1` – RangeExclusiveStartWithStep(3, 0, -1)
        - Incomplete ranges with negative step: 
            - `..1:-1` – RangeToWithStep(1, -1)
            - `2..:-1` – RangeFromWithStep(2, -1)
            - `3>..:-1` – RangeFromExclusiveStartWithStep(3, -1)
            - `..:-1` – RangeFullWithStep(-1)
    - Note: Too complicated for too little benefit.
- Maybe remove `++i`, `--i`, `i++`, `i--`?
    - as Python
    - only offer/allow `i += 1`, `i -= 1`  
      or even only `i = i + 1`, `i = i - 1`
    - Note: No, Cilia is a C++ descendant after all.


### Templates
- **Class** templates  
    - Partial template specialization could be written
      ```
      class<type T, Int N> MyUniquePtr<T[N]> {
          ... destructor calls delete[] ...
      }
      ```
- **Function** templates
    - _Explicit_ function templates could be written as:
      `func<Number T> add(T x, y) -> T { return x + y }`
    - Extension function templates could be written as  
        - `template<type T, Int N> func T[N]::size() -> Int { return N }`
        - `template<type T, Int N> func T[N]::convertTo<type TOut>() -> TOut[N] { ... }`
- Template **type alias** could be written as:
    - `template<type T> using T::InArgumentType = const T&`


### Function/Loop Parameter Passing
- If you want even the basic type to be different, we could write:
    - `for Double d in [1, 2, 3] { ... }`
        - `d` is `const Double`
    - `for String str in ["a", "b", "c"] { ... }`
        - `str` is `const String` (not `const StringView&`)
        - ~~`str` is `const String&` (not `const StringView&`)~~
            - TODO This dosnn't actually make sense here, you can not get a (const) reference to a string, when the underlying array is in fact a `StringView[]`.
    - `for inout String str in ["a", "b", "c"] { ... }`
        - `str` is `String&`
        - TODO This dosnn't actually make sense here, you can not get a (mutable/non-const) reference to a string, when the underlying array is in fact a `StringView[]`.
    - `for copy String str in ["a", "b", "c"] { ... }`
        - `str` is `String`


### Literals
- `true`, `false` are Bool
- `Null` could be the null pointer, and `NullType` its type.
    - Shorter and more similar to C `NULL`.


### String, Char & CodePoint
- **Code points** could be represented by `UInt32` or by an distinct type `CodePoint` (== `UInt32`).
    - Would it be useful?
- `WideChar` could be useful for portable code (Linux `UInt32` <-> Windows `UInt16`)
    - But you may use `wchar_t` then.
- Alternative names/syntax to iterate over strings:
    - `for codeUnit in "abc 🥸👮🏻".asCodeUnits()` (a bit more explicit/clear than `.asArray()`)
    - Is `byWord()` (like in "word by word") a better naming?
        - `for graphemeCluster in text.byGraphemeCluster()`
        - `for codePoint in text.byCodePoint()`
        - `for codeUnit in text.byCodeUnit()`
        - `for codeUnit in text.byChar()`
        - `for word in text.byWord()`
        - `for line in text.byLine()`
        - `for sentence in text.bySentence()`
     

### Cilia Standard Library
- "**Alias**" for 
    - member variables could be written as  
       `alias x = data[0]`,
    - member functions could use perfect forwarding,
        - see https://stackoverflow.com/a/9864472
        - but that would not work for virtual functions.


### (Smart) Pointers
- **`Type- pointer`**
    - `T-` is short for `UniquePtr<T[0]>` (i.e. a unique pointer to a C/C++ array of fixed but unknown size)
- `new T` returns a `T+`/`UniquePtr<T>`,
    - so `T+`/`UniquePtr<T>` is the "default type" for pointers,  
      e.g. `ContactInfo+ contactInfoUniquePtr = new ContactInfo`.
    - `T[0]+`/`UniquePtr<T[0]>` is the "default type" for pointers to array,  
      e.g. `ContactInfo[0]+ contactInfoUniqueArrayPtr = new ContactInfo[10]`.
- A classical C/C++ "raw" pointer is still possible, but inconvenient to use.
    - `ContactInfo* contactInfoPtr = (new ContactInfo).release()`  
      `delete contactInfoPtr` (with classical/raw pointers you need to free the objects yourself)
    - `ContactInfo* contactInfoPtr = (new ContactInfo[10]).release()`  
      `delete[] contactInfoPtr` (you need to distinguish single-element- and array-pointers yourself)
- Other conceivable variants, may be used for `UniquePtr<T>`, `WeakPtr<T>`, ...:
    - ASCII
        - **`Type+ pointer`** ("plus pointer", my favourite, maybe even better than `Type^ pointer`)
        - `Type> pointer` (IMHO nice idea for a pointer, but very difficult to read with template types, e.g. `Matrix<Float64>> matrix`)
        - `Type~ pointer` (IMHO nice for `WeakPtr<T>`, but also used for binary not and destructor syntax, so not a perfect fit)
        - `Type# pointer`
        - `Type% pointer`
        - `Type§ pointer`
    - Latin-1 (but a character that is difficult to find on the keyboard would not actaully encourage people to use this syntax)
        - `Type° pointer` (for `SmartPtr<T>`)
        - `Type¹ pointer` (for `UniquePtr<T>`)
        - `Type• pointer`
        - `Type› pointer`
    - Multiple, combined characters
        - `Type*° pointer` (for `SmartPtr<T>`)
        - `Type*¹ pointer` (for `UniquePtr<T>`)
        - `Type*+ pointer` (for `WeakPtr<T>`?)
        - `Type*> pointer` (for `SmartPtr<T>`?)
        - `Type*1> pointer` (for `UniquePtr<T>`)
        - `Type*¹> pointer` (for `UniquePtr<T>`)


### `is`, `as`, Casting
- Automatic casts
    - As multiple inheritance is problematic here:
        - In Cilia/C++, an object can be an instance of several base classes at once, whereby the pointer (sometimes) changes during casting.
        - What if you still want/need to access the functions for a `Type obj` after `if obj is ParentA`?
        - Therefore maybe better: `if obj is String str ...`
            - as in C#


### Misc
- Versioning of the Cilia source code could alternatively be done
    - via file ".cilia_version" in a (project) directory,
    - via file extension: 
        - "*.cilia2024" – Version from the year 2024
        - "*.cilia2024b" – Second version from the year 2024
        - "*.cilia_2024" – Version from the year 2024
        - "*.cilia_2024b" – Second version from the year 2024
        - "*.ciliaA"
        - "*.ciliaB"
