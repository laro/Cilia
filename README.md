# Cilia
# Cilia (programming language)
**C++ with CamelCase Style**  
I'd like to have the standard library / STL roughly in the [style of Qt](https://wiki.qt.io/Qt_Coding_Style), and (a variant of) Qt with the standard library / STL classes as base (and with exceptions, and with namespaces instead of the prefix "Q").
  
**C++ with Simplified Syntax**  
Many of C++'s shortcomings stem from the fact that it inherited from C or that backwards compatibility with existing code must be guaranteed.
Cilia can call into C++ (and vice versa), but is a separate language, so its syntax does not need to be backwards compatible.

**C++ without Semicolons**  
When we are at it, after a quick look at Julia and Python. 


## Introduction
- "Improved" C++
    - with a **simplified** syntax,
    - in the **[style of Qt](https://wiki.qt.io/Qt_Coding_Style)**, Objective-C, Java, JavaScript, Kotlin, Swift
    - Isomorphic mapping of all C++ functionality to Cilia possible
        - only with other/better/shorter "expression".
- C++ "Successor Language"
    - like [Carbon](https://github.com/carbon-language/carbon-lang) or [Circle](https://github.com/seanbaxter/circle),  
      but [CppFront/Cpp2](https://github.com/hsutter/cppfront#cppfront) seems to be a fully backwards compatible syntax, so it's a bit different.
    - Similar C -> C++, Java -> Kotlin, Objective-C -> Swift, JavaScript -> TypeScrtipt
- Uses the same compiler backend as C++ (clang, gcc, …)  
  with an own / a new compiler frontend (or a precompiler).
- So _no_ garbage collection,  
  instead in Cilia you use, as in C++,
    - automatic/stack variables
    - **RAII** (Resource Acquisition is Initialization)
        - **RROD** (Resource Release on Object Destruction)
    - `SharedPtr<T>` / `T^` etc.
- The names [D](https://dlang.org/), [C2](http://c2lang.org/), and [Cpp2](https://github.com/hsutter/cppfront#cppfront) were already taken,  
  as well as [Cone](https://cone.jondgoodwin.com/) and many others `¯\_(ツ)_/¯`.
    - "Cilia" signals something in between [C](https://en.wikipedia.org/wiki/C_(programming_language))/[C++](https://en.wikipedia.org/wiki/C%2B%2B) and [Julia](https://julialang.org) (so maybe I could add some more of Julias interesting features to this wish list).


- **Compatible to C++**, C and maybe other languages of this "**language family**" / "**ecosystem**", even future ones,
    - as with
        - Java: Kotlin, Scala, Groovy, Clojure, Fantom, Ceylon, Jython, JRuby …
        - C#: C++/CLI, Visual Basic .NET, F#, A# (Ada), IronPython, IronRuby …
        - Objective-C: Swift
    - Possible to include
        - C++ headers and modules from Cilia
        - Cilia headers and modules from C++
    - The compiler recognises the language (C, C++, or Cilia) by
        - the file extension
            - Cilia: `*.cl` `*.hl`  &nbsp;  ~~`*.cilia` `*.hilia`~~
            - C++: `*.cpp` `*.hpp` &nbsp; `*.cxx` `*.hxx` &nbsp; `*.h`
                - `*.h` is of course a problem, as the header could be C or C++ code.  
                  So use of `*.hpp` is recommended for C++ code.  
                  This can probably best be solved using path based rules.
            - C: `*.c` `*.h`
        - path based rules
            - to handle C or C++ standard headers in certain directories 
        - can be set in IDE
            - for each file individually 


## Style
- All types and **classes in upper CamelCase** (even the standard/STL classes).
    - Style similar to Kotlin, Swift
    - Cilia standard library (`cilia::` instead of `std::`)
        - `cilia::String` instead of `std::string`
        - `Array`, `Map`, `ForwardList`, `UnorderedMap`, `ValueType`
    - Arithmetic types
        - `Bool`
        - `Int`
            - `Int8`, `Int16`, `Int32`, `Int64`
        - `UInt`
            - `UInt8`, `UInt16`, `UInt32`, `UInt64`
        - `Byte` == `UInt8`
        - `Char` == `Char8`, `Char16`, `Char32`~~, `CodePoint` == `UInt32`~~
        - `BigInt` (Arbitrary Precision Integer)
        - `Float`
            - `Float16`, `Float32`, `Float64` (Half, Single, Double Precision Floating Point)
            - `BFloat16` (Brain Floating Point)
            - `BigFloat` (Arbitrary Precision Float)

- **Functions in lower camelCase**
    - Roughly in the style of Qt, Objective-C/C++, Java, JavaScript, TypeScript, Kotlin, Swift

- Namespaces fully lowercase 
    - Standard namespace `cilia`
    - I am not sure about this, I don't think it's important. But this helps to differentiate between classes and namespaces.


## Arithmetic Types
- `Bool`
    - not ~~`bool`~~ nor ~~`Boolean`~~
- `Int`, `UInt`
    - `Int` == `Int64`
        - `Int` == `Int32` on 32 bit systems only (i.e. old/small platforms)
            - therefore it is _not_ necessary to have ~~`Size`~~ or ~~`SSize`~~
    - `Int8`, `Int16`, `Int32`, `Int64`
        - like `int32_t` or `qint32`, but no prefix "q" nor postfix "_t", and in CamelCase
        - maybe `Int128`, `Int256`
    - `UInt8`, `UInt16`, `UInt32`, `UInt64`
        - maybe `UInt128`, `UInt256` e.g. for SHA256
    - `cilia::safe::Int`
        - Like `cilia::Int`, but with **overflow check** for all operations,
            - may throw OverflowException.
        - `safe::Int8`/`Int16`/`Int32`/`Int64`
        - `safe::Uint`
            - `safe::UInt8`/`UInt16`/`UInt32`/`UInt64`
    - `cilia::saturating::Int`
        - Like `cilia::Int`, but with **saturation** for all operations.
            - Limit to maximum, no wrap around.
            - Typically using SIMD (as those „media/DSP instructions“ do support saturation natively).
        - see https://en.wikipedia.org/wiki/Saturation_arithmetic 
        - `saturating::Int8`/`Int16`/`Int32`/`Int64`
        - `saturating::Uint`
            - `saturating::UInt8`/`UInt16`/`UInt32`/`UInt64`
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
            - https://stackoverflow.com/a/6770329
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


## Signed Size
`Int` (i.e. signed) as type for `*.size()`
- Because mixed integer arithmetic ("signed - unsigned") and "unsigned - unsigned" is difficult to handle.
    - In C/C++ `anUInt - 1 >= 0` is _always_ true (even if `anUInt` is `0`)
- When working with sizes, calculating the difference is common; Then you are limited to `PtrDiff` (i.e. signed integer) anyway.
- Who needs more than 2GB of data in an "array", should please use a 64 bit platform.
- For bounds checking, the two comparisons `x >= 0` and  `x < width` may very well be reduced to a single `UInt(x) < width` _by the compiler_ in an optimization step. 
- Then types `Size` and `SSize`/`PtrDiff` are not necessary anymore, so two types less.
    - We simply use Int instead. Or `UInt` in rate cases.
- Restricted rules for mixed integer arithmetic:
    - `Unsigned +-*/ Signed` is an error
        - you have to cast
        - `Int` (i.e. signed) is almost always used anyways
    - Error with `if anUInt < 0`
        - if the literal on the right is `<= 0`
    - Error with `if anUInt < anInt`
        - you have to cast
- Not:
    - ~~`Size` AKA `UInt` as type for `*.size()` (i.e. still unsigned)~~
        - ~~`Size` reads IMHO better than `UInt`~~
            - ~~`Size` would not really be necessary~~
        - ~~New rules for mixed integer arithmetic:~~
            - ~~Unsigned +-*/ Signed -> Signed.~~
                - ~~Signed is therefore considered the "larger" type compared to unsigned~~
                - ~~`1` is `Int` (signed)~~
                    - ~~`1u` is `UInt` (unsigned)~~
                - ~~Therefore `if anUInt - 1 >= 0` is a useful expression (`1` is signed)~~
                - ~~But also `anUInt + 1 == anInt`~~
    - ~~Or~~
        - ~~`Size` - `Size` -> `SSize`~~
            - ~~Problem: `-` results in `SSize`, but `+` results in `Size`?!~~
        - ~~The conversion of a negative number into `Size` leads to an error instead of delivering a HUGE size ~~


## String, Char & CodePoint
- `cilia::String` with
    - _basic/standard_ unicode support.
        - Iteration over a `String` or `StringView` by:
            - **grapheme clusters**
                - represented by `StringView`.
                - This is the _default form of iteration_ over a `String` or `StringView`
                - A grapheme cluster may consist of multiple code points.
                - `for graphemeCluster in "abc 🥸👮🏻"`
                    - "a", "b", "c", " ", "🥸", "👮🏻"
                    - "\x61", "\x62", "\x63", "\x20", "\xf0\x9f\xa5\xb8", "\xf0\x9f\x91\xae\xf0\x9f\x8f\xbb"
                - A bit slow, as it has to find grapheme cluster boundaries.
                - It is recommended to mostly use the standard functions for string manipulation anyway, you seldomly need grapheme-cluster-based iteration. But when you do, this probably is the correct way. 
                - additional/alternative names?
                    - `for graphemeCluster in text.asGraphemeClusters()`?
                    - ~~`for graphemeCluster in text.byGraphemeCluster()`?~~
            - **code points**
                - represented by `UInt32`,
                    - independent of the encoding (so, the same for UTF-8, UTF-16, and UTF-32 strings).
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
                        - diacritical characters (äöü…, depending on the normal form chosen),
                        - surely some more …
                    - Often slower than UTF-8, simply due to its size (cache, memory bandwidth).
            - **code units**
                - represented by
                    - `Char` for `String`
                    -   `Char`==`Char8`==`Byte`, `String`==`UTF8String`
                    - `Char16` with `UTF16String`
                    - `Char32` with `UTF32String`
                - `for char8 in "abc 🥸👮🏻".asArray()`
                    - 0x61, 0x62, 0x63, 0x20,  &nbsp;  0xf0, 0x9f, 0xa5, 0xb8,  &nbsp;  0xf0, 0x9f, 0x91, 0xae, 0xf0, 0x9f, 0x8f, 0xbb
                    - same for
                        - `for codeUnit in "abc 🥸👮🏻"utf8.asArray()`
                        - `for codeUnit in UTF8String("abc 🥸👮🏻").asArray()`
                        - ? `for codeUnit in "abc 🥸👮🏻".asCodeUnits()`
                        - ~~`for codeUnit in text.byCodeUnit()`?~~
                        - ~~`for codeUnit in text.byChar()`?~~
                - `for char16 in "abc 🥸👮🏻"`**`utf16`**`.asArray()`
                    - 0x0061, 0x0062, 0x0063, 0x0020,  &nbsp;  0xD83E, 0xDD78,  &nbsp;  0xD83D, 0xDC6E, 0xD83C, 0xDFFB
                    - same for `for char16 in UTF16String("abc 🥸👮🏻").asArray()`
                - `for char32 in "abc 🥸👮🏻"`**`utf32`**`.asArray()`
                    - 0x00000061, 0x00000062, 0x00000063, 0x00000020,  &nbsp;  0x0001F978,  &nbsp;  0x0001F46E , 0x0001F3FB
                    - same for `for char32 in UTF32String("abc 🥸👮🏻").asArray()`
    - Advanced support based on [ICU](https://unicode-org.github.io/icu/userguide/icu4c/) ("International Components for Unicode", "ICU4C").
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
    - `string.toUpper()`, `string.toLower()`
        - `toUpper(Sting)` -> `String`
        - `toLower(Sting)` -> `String`
    - Sorting
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
            - `for char in "abc"ascii`
                - 0x61, 0x62, 0x63
                - 'a', 'b', 'c'
                - Compilation error, if string literal contains non-ASCII characters.
                - same for `for char in ASCIIString("abc")`
                    - but Exception thrown, if string contains non-ASCII characters.
        - Implicitly convertable to `String`==`UTF8String`.
            - Very fast conversion, as all characters have the same binary representation.
    - `Latin1String`, a string containing only Latin-1 (ISO 8859-1) characters.
        - Iteration over an `Latin1String` or `Latin1StringView` by `Char`==`Char8`==`Byte`
            - `for char in "äbc"latin1`
                - 0xe4, 0x62, 0x63
                - 'ä', 'b', 'c'
                - Compilation error, if string literal contains non-Latin-1 characters.
                - same for `for char in ASCIIString("abc")`
                    - but Exception thrown, if string contains non-Latin1 characters.
        - Explicitly convertable to `String`==`UTF8String`.
            - Not so fast conversion as with ASCIIString, as typically some characters need to be translated into two UTF-8 code units.
- `Char8`, `Char16`, `Char32`
    - are like `UInt8`, `UInt16`, `UInt32`,
    - but considered as _different_ types for parameter overloading.
- So no ~~`WideChar`~~
    - ~~Or is it useful for portable code (Linux `UInt32` <-> Windows `UInt16`)?~~
        - ~~You may use `wchar_t` then.~~


## Namespace `cilia`
Cilia standard library in namespace `cilia` (instead of `std`).
- With Cilia version of every standard class/concept (i.e. CamelCase class names and camelCase function and variable names)
    - `cilia::String` instead of `std::string`
    - `Map` instead of `map`
        - `Dictionary` as typedef with deprecation warning, as a hint for C# programmers.
    - `ForwardList` instead of `forward_list`
    - `UnorderedMap` instead of `unordered_map`
    - `ValueType` instead of `value_type`
    - Maybe some exceptions/variations:
        - `Array` instead of `vector`
        - `Stringstream` or `StringStream` instead of `stringstream`?
            - `Textstream` or `TextStream`, `Bytestream` or `ByteStream`, …
        - `Multimap` or `MultiMap` instead of `multimap`?
- Shallow wrapper,
    - e.g. `cilia::String : protected std::string`
- "**Alias**" for 
    - member variables  
      `using x = data[0]`  
      `using y = data[1]`  
        - ~~or `alias x = data[0]`?~~
        - Not quite possible in C++.
            - With …  
              `Float& imaginary = im`  
              `T& x = data[0]`  
              … unfortunately memory is created for the reference (the pointer).
            - And this indeed is necessary here, because the reference could be assigned differently in the constructor,
                - so it is not possible to optimize it away.
    - member functions
        - `using f() = g()`
        - ~~Or is perfect forwarding enough?~~
            - ~~https://stackoverflow.com/a/9864472~~
            - This would not work for virtual functions


## Const Reference as Default Type
Const reference/value as default type for function call arguments and for "for-in" (AKA "for-each", "foreach").
- `mutable`, to mark as changeable
    - Also at the caller `swap(mutable a, mutable b)`
    - ~~Or `inout`?~~
- `value`, to mark as value (not reference) 
    - `mutable value`
    - Is not specified when calling the function, as a copy is created here.
- `reference`, to mark as reference (not value)
- RValue references still as `&&`
- Type traits `DefaultArgumentType`
    - As const _value_:
        - `Int`, `Float`, `Bool` etc.
        - Small classes (as `Complex<Float>`, `StringView`) 
    - As const _reference_:
        - All other cases
    - Therefore probably best to have const reference as general default, "list of exceptions" for the "value types".
    - ~~Or (similar to C# and Swift) const-reference for `classes`, const-value for `structs`?~~
        - ~~At least as default?~~
- Examples:
    - `concat(String first, String second)`
        - instead of `concat(const String& first, const String& second)`
    - `String[] stringArray = ["a", "b", "c"]`  
      `for str in stringArray { … }`
        - `str` is `const String&`
        - If you want to have it differently:
            - `for mutable str in stringArray { … }`
                - `str` is `String&`
            - `for value str in stringArray { … }`
                - `str` is `const String`
            - `for mutable value str in stringArray { … }`
                - `str` is `String`
    - `for str in ["a", "b", "c"] { … }`
        - `str` is `const StringView`
    - `for i in [1, 2, 3] { … }`
        - `i` is `const Int`
        - If you want to have it differently:
            - `for mutable i in [1, 2, 3] { … }`
                - `i` is `Int`
            - `for reference i in [1, 2, 3] { … }`
                - `i` is `const Int&`
            - `for mutable reference i in [1, 2, 3] { … `}"
                - `i` is `Int&`
    - If you want even the basic type to be different:
        - `for Double d in [1, 2, 3] { … }`
            - `d` is `const Double`
        - `for String str in ["a", "b", "c"] { … }`
            - `str` is `const String&` (not `const StringView&`)
        - `for mutable String str in ["a", "b", "c"] { … }`
            - `str` is `String&`
        - `for value String str in ["a", "b", "c"] { … }`
            - `str` is `const String`
        - `for mutable value String str in ["a", "b", "c"] { … }`
            - `str` is `String`
    - `for i in 1..<10 { … }`
        - `i` is `const Int`


## Better Readable Keywords
C++ has a "tradition" of complicated names, keywords or reuse of keywords, simply as to avoid compatibility problems with old code, which may have used one of the new keywords as name (of a variable, function, class, or namespace).
- Cilia has
    - `var` instead of `auto`
    - `func` instead of `auto`
    - `for … in …` instead of `for (… : …)`
        - `for i in 0..<10` instead of `for (int i = 0; i < 10; ++i)`
    - `class … extends …` instead of `class … : …`
        - or better `implements`?
    - `await` instead of `co_await`
    - `yield` instead of `co_yield`
    - `return` instead of `co_return`
    - `and`, `or`, `xor`, `not` instead of `&&`, `||`, `^`, `!`
        - as in Python, Carbon
        - Used for both
            - boolean operation
                - `anBool`**`and`**`anotherBool` -> `Bool`
            - bitwise operation
                - `anInt`**`and`**`anotherInt` -> `Int`
- `Int32` instead of `int32_t` or `qint32`,
  - so no prefix "q" nor postfix "_t".
- When translating C++ code to Cilia then change conflicting names, e.g.
    - `int var` -> `Int __variable_var`
    - `class func` -> `class __class_func`
    - `yield()` -> `func __function_yield()`


## No Trailing Semicolons
As in Python, Kotlin, Swift, JavaScript, Julia
- Advantage:
    - Better readability
- Disadvantage:
    - Errors are less easily recognized
        - Walter Bright / D: „Redundancy helps“
    - This probably means that a completely new parser must be written, as the one from clang (for C++) no longer fits at all.
        - As this is difficult & unclear/disputed: Keep C++ semicolons for now?
- Multiline expressions:
    - Explicitly via `\` or `(…)` / `[…]` / `{…}` as in Python
    - ~~Implicitly/clever as in Swift, Kotlin and JavaScript?~~
- Only in REPL:
    - Trailing semicolon used to suppress evaluation output,
        - as in Matlab, Python, Julia.
     
## Functions
- `func aFunction(Int i) -> Float { return i * 3.14 }`
    - ~~or `fn` (Rust, Carbon, New Circle), `fun` (Kotlin), `function` (Julia)~~
    - Easier parsing due to clear distinction between function vs. variable declaration.
    - Always and only in the trailing return type syntax.
- `func function2(`**`Int x, y`**`) -> Float` // x _and_ y are Int
- Lambdas
    - `[](Int i) -> Float { i * 3.14 }`
        - as in C++
- Function pointers
    - Difficult to maintain consistency between declarations of functions, function pointers, functors and lambdas.
    - Variant A:
        - **`func(Int, Int -> Int)* pointerToFunctionOfIntToInt`**
        - **`func(Int)* pointerToFunctionOfInt`**
        - `func(Int, Int -> Int)& referenceToFunctionOfIntToInt` // Can't be zero; is that useful?
        - `func(Int)& referenceToFunctionOfInt`
    - ~~Variant B:~~
        - ~~`func((Int, Int) -> Int)* pointerToFunctionOfIntToInt`  // Closer to the function declaration but (too) many brackets~~
    - ~~Variant C:~~
        - ~~`(Int, Int -> Int)` [Functions are only available as pointers, so you can omit "*"?]~~
    - ~~Variant D:~~
        - ~~`func*(Int->Int) pointerToFunctionOfIntToInt`~~
        - ~~`func*(Int) pointerToFunctionOfInt`~~
    - ~~Variant E:~~
        - ~~`func*(Int, Int)->Int pointerToFunctionOfIntAndIntToInt`~~
        - ~~`(func*(Int, Int)->Int)[] arrayOfPointersToFunctionOfIntAndIntToInt`~~
- Extension methods
    - Also possible for arithmetic types (like `Int i; i.toString()`)
        - `func Int::toString() -> String { … }`  // as in Kotlin
            - ~~or `func toString (Int this) -> String` ~~


## Variable Declaration
Variable declaration still simply as `Int i`, as in C/C++.
- Or is having `func` for function declaration, but not `var` for variable declaration, still not clear enough?
    - Could be problematic in connection with omitting the trailing semicolons,
    - Swift, Kotlin and Circle always start variable declarations with `var`.
- Not
    - ~~`var Int i`~~
    - ~~`var i : Int`~~
- `var i = 3` only for type inference
    - ~~Maybe possible to simply write `i = 3`?~~
    - ~~Maybe `i := 3`?~~
- Examples:
    - `Int anInt`
    - `Int[] arrayOfInt`
    - `Int[3] arrayOfThreeInt`
    - `Int[3]* pointerToArrayOfThreeInt`
    - `Int[3][]* pointerToDynamicArrayOfArrayOfThreeInt`
    - `String*[] dynamicArrayOfPointersToString`
    - **`Float* i, j`   // i _and_ j are pointers**
        - contrary to C/C++.
- Not allowed / syntax error is:
    - ~~`Float* i, &j`~~
        - Type variations are _not_ allowed.
    - ~~`Float *i`~~
        - No whitespace _whithin_ type specification allowed.
    - ~~`Float*i`~~
        - Whitespace _between_ type specification and variable name is mandatory.


## Casting
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
          if obj not is String
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
        - In Cilia/C++, an object can be an instance of several base classes at once, whereby the pointer (typically) changes during casting.
        - What if you still want/need to access the functions for a `Type obj` after `if obj is ParentA`?
            - Workaround: Cast back with `Type(obj).functionOfA()`
        - ~~Therefore maybe better: `if obj is String str ...`~~
            - ~~as in C#~~


## Comments
- One line comments
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

     
## Literals
- `True`, `False` are Bool,
    - as in Python,
    - as they are constants.  
    - ~~`true`, `false` are Bool~~
- `Null` is the null pointer
    - it is of the type `NullPtr` 
    - explicit cast necessary to convert any pointer to Int
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
        - for type inferring, parameter overloading and template matching.
    - Difficult: Constexpr constructor that accepts an arbitrary precision integer literal  and can store that in ROM
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
        - for type inferring, parameter overloading and template matching.
    - `1.0f` is always `Float32`
    - `1.0d` is always `Float64`
- `"Text"` is a `StringView`
    - Pointer to first character and pointer after the last character
        - in C++ tradition, but length would also work, of course
    - No null termination
        - If necessary
            - use `"Text\0“`  or
            - convert using `StringZ(…)`.
    - Data is typically stored in read-only data segments or ROM.
- Multiline String Literal
    - ```
      """
      First line
      Second line
      """
      ```
    - Removes indentation as in the last line
    - Removes first newline
    - As in Swift, Julia
    - Also as single line string literal with very few restrictions, good for RegEx
        - `"""(.* )whatever(.*)"""`
- Interpolated Strings
    - `$“M[{i},{j}] = {M[i, j]}"`
        - like in C#
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
- Range literals `1..10` and `1..<10`
    - as in Kotlin
    - ~~Swift would be `1...10`~~
        - I like `...` to be reserved for ellipsis in human language like comments.
- Rules for user defined literals
    - as in C++.


## Short Smart Pointer Syntax 
- `Type^ instance`
    - `T^` by default is `SharedPtr<T>`
        - for C++/Cilia,
        - defined via type traits `DefaultCircumflexType`.
    - Possible to redefine for interoperability with other languages:
        - Objective-C/Swift: Use their reference counting mechanism
        - C#/Java: Use garbage collected memory
    - ~~`T^^` by default is `WeakPtr<T>`~~
        - ~~defined via type traits `DefaultCircumflexCircumflexType`.~~
        - ~~`SharedPtr<SharedPtr<T>>` just doesn't work like that, doesn’t really make sense anyway.~~
        - Do we really need a short expression for `WeakPtr<T>`?


## Automatic Templates
- If the type of a function argument is a concept, then the function is a template.
    - Concept `Number`:
        - ```
          func sq(Number x) -> Number {
               return x * x
           }
          ```
        - However, the return type could be a different type than `x` is (as long as it satisfies the concept `Number`)
    - `func add(Number a, b) -> Number`
        - `a`, `b` and the return type could each be a _different_ type (as long as it satisfies the concept `Number`)
    - Concept `Real` (real numbers as `Float16`/`32`/`64`/`128` or `BigFloat`):
      ```
       func sqrt(Real x) -> Real {
           // … a series development …
      }
      ```
- Like abbreviated function templates in C++ 20, only without `auto`.
- `template<typename T>` for cases where a common type is required.
- `requires` for further restricting the type.

          
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
- `<<` Shift left (here a logical shift with UInt is the same as arithmetic shift with Int)
- `>>` Shift right (logical shift with Uint, arithmetic shift with Int)
- `<<<` Rotate left (circular shift left)
- `>>>` Rotate right (circular shift right)
  

## Misc
- Operations with carry flag  
  (to implement `Int128`, `Int256` etc.)
    - `c = add(a, b, inout carry)`
    - `a.add(b, inout carry)`
    - `d = multiplyAdd(a, b, inout c)`
    - `a.multiplyAdd(b, inout c)`
    - `b = shiftLeft(a, Int steps, mutable carry)`
    - `a.shiftLeft(Int steps, mutable carry)`
 

- For-in loop (instead of `for (… : …)` or `foreach`)
    - as in Rust, Swift
    - With range literal also used instead of `for (Int i = 0; i < 10; ++i) { … }`
        - `for i in 1..10`
            - translates to `for i in Range(1, 10)`
        - `for i in 1..<10`
            - translates to `for i in RangeExclusiveEnd(1, 10)`
        - Not recommended, but possible to write
            - `for i in Range(1, 10)`
            - `for i in Range(1, 10, 1)`
        - Instead of `for (Int i = 10; i > 0; --i) { … }` use
            - `for i in 10..1:-1`
            - ? `for i in 10..>0:-1`
            - `for i in (1..10).reversed()`
            - Not recommended, but possible
                - `for i in Range(10, 1, -1)`
                - `for i in Range(10..1, -1)`
                - ~~`for i in 10 downTo 1 step 1`~~
                - ~~`for i in 10..1 by -1`~~
                - ~~`for i in 10..1 step -1`~~


-  `if 1 <= x <= 10 { … }`
    - as in Python, Julia, Cpp2 (Herb Sutter)
 
    
- Arrays
    - `Int[3] arrayOfThreeIntegers`
        - „Static array“ – fixed size, same as C/C++
        - arrayOfThreeIntegers.size() -> 3 (realised as extension function)
    - `Int[] arrayOfIntegers`
        - „Dynamic array“ – dynamic size
        - Translated to `Array<T>` (normally `cilia::Array<T>` will be used)
        - `cilia::Array<Int>`
            - not called `cilia::Vector<Int>`, because this could easily collide with the mathematical (numerical/geometric) Vector.
            - (See Matrix & Vector, even if they are in other sub-namespaces.)
        - Problem: Confusing because so similar to fixed-size arrays?
        - Use `Int*` for C/C++ arrays of arbitrary size  
          ```
          Int* array = new Int[4]
          array[3] = 0
          array[4] = 0  // Runtime error, no static bounds check
          ```
    - `Int[3,2,200]`
        - Multidimensional array  
          ```
          Int[3,2,200] intArray3D
          intArray3D[2, 1, 199] = 1
          ```
    - `int[,,]`
        - Multidimensional dynamic array
        - `cilia::NArray<Int, 3>`
        - or `Int[*,*,*]`?
        - TODO Mixed forms?
            - `Int[3,*,*]` 
            - `Int[3,4,*]`
         
        
- Matrix & Vector
    - BLAS (Basic Linear Algebra Subprograms)
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
            - as typically used in numerics.
        - `cilia::numerics::Vector<T = Float>`
        - `cilia::numerics::Matrix<T = Float>`
            - stored column-major
        - `cilia::numerics::NArray<T = Float, Int dimensions>`
          
- Image
    - `cilia::Image<T = Float>`
    - Almost like `cilia::Matrix`, but stored row-major.
      
- Views, Slices
    - `ArrayView`
    - `VectorView`
    - `MatrixView`
    - `NArrayView`
 
      
## Two-Pass Compiler
- no forward declarations necessary 
    - as in C#, Java
- no single-pass as in C/C++
 
      
## Versioning of the Cilia source code
- Via file ".ciliaVersion" ".cilia_version" in a (project) directory,
    - similar to ".clang_format",
    - also possible file by file: Matrix.ciliaVersion (for Matrix.cilia).
- Via file extension: 
    - "*.cilia" – always the latest language version (if not defined otherwise via ".ciliaVersion")
    - "*.2024.cilia" – Version from the year 2024
    - "*.2024b.cilia" – Second version from the year 2024
    - ~~"*.cilia2024" – Version from the year 2024~~
    - ~~"*.cilia2024b" – Second version from the year 2024~~
    - ~~"*.cilia_2024" – Version from the year 2024~~
    - ~~"*.cilia_2024b" – Second version from the year 2024~~
    - ~~"*.c1a"~~
    - ~~"*.c1b"~~
    - ~~"*CiliaA"~~
        - ~~"*.CiliaB"~~
         
              
## Fix C++ "wrong defaults"
[Sean Baxter](https://x.com/seanbax), creator of [Circle](https://github.com/seanbaxter/circle), [writes about C++'s wrong defaults](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#to-err-is-human-to-fix-divine):
> C++ has a number of "wrong defaults," design decisions either inherited from C or specific to C++ which many programmers consider mistakes.
> They may be counter-intuitive, go against expected practice in other languages, leave data in undefined states, or generally be prone to misuse.

I am not familiar with all these issues, but in a new language we certainly coud fix a lot of it.

1. Uninitialized automatic variables.
    - Unclear - haven't people gotten used to it?
    - Then there should be a keyword `noinit`,
        - at least for large arrays.
    - Only for stack variables or also for free memory/heap?
        - With virtual memory, this is actually "free".
2. Integral promotions.
    - Only allow safe ones,
    - otherwise explicit cast necessary.
3. Implicit narrowing conversions.
    - Not allowed
4. Switches should break rather than fallthrough.
    - Keyword `fallthrough` instead
5. Operator precedence is complicated and wrong.
    - If the suggestion of Sean Baxter / Circle works well, then that would be fine.
6. Hard-to-parse declarations and the most vexing parse.
    - `func` but not `var`
7. Template brackets `< >` are a nightmare to parse.
    - I would not like to change this.
    - Only if it _really_ has to be.
8. Forwarding parameters and std::forward are error prone.
9. Braced initializers can choose the wrong constructor.
    - Do without braced initializers altogether.
    - With `func` there is now a clear distinction between function declaration and variable declaration with initialization.
    - The classic initialization via `(...)`, ultimately a function call of the constructor, fits better.
    - Curly brackets only for initializer lists, i.e. for tuples, lists etc.
    - Square brackets for arrays.
10. `0` shouldn't be a null pointer constant.
    - Not allowed, use `Null`.
11. `this` shouldn't be a pointer.
    - Better it is a reference.
       
        
## Capabilities of Julia
[Julia](https://julialang.org/) has very strong math support. Some of its features should be easy to copy.
- `b = 2a` as short form of `b = 2*a`
- `x ÷ y`, integer divide, like `x / y`, truncated to an integer
- `sqrt(x)`, `√x`
- `cbrt(x)`, `∛x`
- `!=`, `≠`
- `<=`, `≤`
- `>=`, `≥`
- Operator overloading
    - See:
        - https://www.geeksforgeeks.org/operator-overloading-in-julia/
        - https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm
    - Much more operators
        - https://stackoverflow.com/a/60321302
    - „Precedence and associativity: When defining new operators or overloading existing ones, you can also specify their precedence and associativity, which determines the order in which they are evaluated.“
        - That seems quite complicated to parse?!
- Many kinds of brackets?
    - https://stackoverflow.com/a/33357311
    - Problem: some of the brackets are also conceivable as operators.
