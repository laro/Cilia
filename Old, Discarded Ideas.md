# Old, discarded ideas for Cilia
For several topics thwre are alternative ideas, that were discarded but are still worth mentioning.


## No Trailing Semicolons
- As this is difficult & unclear/disputed: Keep C++ semicolons for now?
- Implicitly/clever multiline expressions as in Swift, Kotlin and JavaScript?  
  (Actually I don't remember the rules anymore.)


## Better Readable Keywords
- Cilia could have
    - `class ... extends ...` instead of `class ... : ...`
        - `class ... implements ...` instead of `class ... : ...` for pure abstract classes (like interfaces)


## Basic / Arithmetic Types
- `Float` could be 64-bit float: `Float` == `Float64`
    - Among other things because already in C/C++ `1.0` == `Float64` (while `1.0f` == `Float32`)
    - `Float32` only on certain platforms


## Variable Declaration
- Very short variable declaration:
    - Maybe possible to simply write `i = 3`?
    - Maybe `i := 3`?
- More verbose syntax,
    - as having `func` for function declaration, but not `var` for variable declaration, may still not be clear enough.
    - Examples:
        - `var Int i`
        - `var i : Int`
    - Swift, Kotlin and Circle always start variable declarations with `var`.
    - Not starting with `var` could be problematic in connection with omitting the trailing semicolons.
  

## Arrays & ArrayViews
Mixed forms of static and dynamic array maybe useful:
- `Int[3,,]`
- `Int[3,4,]`


## Signed Size
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


## Functions
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

          
## Operators
- Possible, alternative syntax for `pow(a, x)`:
  `a**x` (as Python)
- Maybe remove `++i`, `--i`, `i++`, `i--`?
    - as Python
    - only offer/allow `i += 1`, `i -= 1`
      oven `i = i + 1`, `i = i - 1`


## Templates
- **Function** templates
    - _Explicit_ function templates could be written as:
      `func<Number T> add(T x, y) -> T { return x + y }`
    - Extension function templates could be written as  
        - `template<type T, Int N> func T[N]::size() -> Int { return N }`
        - `template<type T, Int N> func T[N]::convertTo<type TOut>() -> TOut[N] { ... }`
- Template **type alias** could be written as:
    - `template<type T> using T::InArgumentType = const T&`?


## Literals
- `true`, `false` are Bool
- `NullPtr` could be the null pointer, and `NullPtrType` its type.


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
                - `toUpper(String, locale) -> String`, `toLower(String, locale) -> String`
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
            - Stored column-major, like:
              ```
              0 3 6
              1 4 7
              2 5 8
              ```
        - `cilia::numerics::MDArray<T = Float, Int dimensions>`
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
