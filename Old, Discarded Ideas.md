# Old, Discarded Ideas for Cilia
For several topics there are alternative ideas, that were discarded but are still worth mentioning.


## No Trailing Semicolons
- As this is difficult & unclear/disputed: Keep C++ semicolons for now?
- Implicitly/clever multiline expressions as in Swift, Kotlin and JavaScript?  
  (Actually I don't know / remember the rules anymore.)


## Better Readable Keywords
- Instead of `class ... : ...` Cilia could have
    - `class ... extends ...` 
       - good for extending base classes
    - `class ... implements ...`
       - good fit for implementing pure abstract base classes (like interfaces)
- But then we would have two different keywords. And what about mixed cases, i.e. abstract classes with partly function implementation? (Probably best to use `implements` then, but still not nice.)

## Basic / Arithmetic Types
- `Float` could be 64-bit float: `Float` == `Float64`
    - Among other things because already in C/C++ `1.0` == `Float64` (while `1.0f` == `Float32`)
    - `Float32` only on certain platforms


## Variable Declaration
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
    - When having `func` for function declaration, but not `var` for variable declaration, is still not clear enough.
    - Swift, Kotlin and Circle always start variable declarations with `var`.
    - Not starting with `var` could be especially problematic in connection with omitting the trailing semicolons.
  

## Arrays & ArrayViews
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
  `a**x` (as Python did)
- Range operator
    - `8>..0:-1` – 7, 6, 5, 4, 3, 2, 1, 0
        - RangeExclusiveStartByStep(8, 0, -1)
    - `8>..0:-3` – 7, 4, 1
        - RangeExclusiveStartByStep(8, 0, -3)
    - `8..>0:-1` – 8, 7, 6, 5, 4, 3, 2, 1
        - RangeExclusiveEndByStep(8, 0, -1)
    - `8..>0:-1` – 8, 7, 6, 5, 4, 3, 2, 1
        - RangeDownwardsExclusiveEndByStep(8, 0, -1)
    - Incomplete range with step
        - `8>..:-1` – RangeFromExclusiveStartByStep(8, -1)
        - `8>..:-2` – RangeFromExclusiveStartByStep(8, -2)
- Maybe remove `++i`, `--i`, `i++`, `i--`?
    - as Python
    - only offer/allow `i += 1`, `i -= 1`  
      or even only `i = i + 1`, `i = i - 1`


## Templates
- **Class** templates  
    - Partial template specialization coulb be written
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


## Function/Loop Parameter Passing
- If you want even the basic type to be different, we could write:
    - `for Double d in [1, 2, 3] { ... }`
        - `d` is `const Double`
    - `for String str in ["a", "b", "c"] { ... }`
        - ~~`str` is `const String&` (not `const StringView&`)~~
            - TODO This dosnn't actually make sense here, you can not get a (const) reference to a string, when the underlying array is in fact a `StringView[]`.
        - `str` is `const String` (not `const StringView&`)
    - `for inout String str in ["a", "b", "c"] { ... }`
        - `str` is `String&`
        - TODO This dosnn't actually make sense here, you can not get a (mutable/non-const) reference to a string, when the underlying array is in fact a `StringView[]`.
    - `for copy String str in ["a", "b", "c"] { ... }`
        - `str` is `String`


## Literals
- `true`, `false` are Bool
- `Null` could be the null pointer, and `NullType` its type.
    - Shorter and more similar to C `NULL`.
- Some more kinds of range literals could be useful:
    - `0<..2` – RangeExclusiveStart(0, 2)
    - Incomplete ranges
        - `0<..` – RangeFromExclusiveStart(0)
    - Range with negative step used for downwards iterating ranges: 
        - `2..0:-1` – RangeWithStep(2, 0, -1)
        - `3>..0:-1` – RangeExclusiveStartWithStep(3, 0, -1)
        - Incomplete ranges with negative step: 
            - `..1:-1` – RangeToWithStep(1, -1)
            - `2..:-1` – RangeFromWithStep(2, -1)
            - `3>..:-1` – RangeFromExclusiveStartWithStep(3, -1)
            - `..:-1` – RangeFullWithStep(-1)


## String, Char & CodePoint
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
     

## `cilia` Standard Library
- "**Alias**" for 
    - member variables could be written as  
       `alias x = data[0]`,
    - member functions could use perfect forwarding,
        - see https://stackoverflow.com/a/9864472
        - but that would not work for virtual functions.


## (Smart) Pointers
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


## `is`, `as`, Casting
- Automatic casts
    - As multiple inheritance is problematic here:
        - In Cilia/C++, an object can be an instance of several base classes at once, whereby the pointer (sometimes) changes during casting.
        - What if you still want/need to access the functions for a `Type obj` after `if obj is ParentA`?
        - Therefore maybe better: `if obj is String str ...`
            - as in C#


## Misc
- Versioning of the Cilia source code could alternatively be done
    - via file ".cilia_version" in a (project) directory,
    - via file extension: 
        - "*.cilia2024" – Version from the year 2024
        - "*.cilia2024b" – Second version from the year 2024
        - "*.cilia_2024" – Version from the year 2024
        - "*.cilia_2024b" – Second version from the year 2024
        - "*.ciliaA"
        - "*.ciliaB"
