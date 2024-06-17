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
- **Code points** could be represented by `UInt32` or by an distinct type `CodePoint` (== `UInt32`).
    - Would it be useful?
- `WideChar` could be useful for portable code (Linux `UInt32` <-> Windows `UInt16`)
    - But you may use `wchar_t` then.
- Alternative names/syntax to iterate over:
    - `for graphemeCluster in text.byGraphemeCluster()`
    - `for codePoint in text.byCodePoint()`
    - `for codeUnit in "abc 🥸👮🏻".asCodeUnits()`
    - `for codeUnit in text.byCodeUnit()`
    - `for codeUnit in text.byChar()`
    - `for word in text.byWord()`
    - `for line in text.byLine()`
    - `for sentence in text.bySentence()`
     

## `cilia` Standard Library
- "**Alias**" for 
    - member variables could be written as  
       `alias x = data[0]`
    - member functions could use perfect forwarding
        - But this would not work for virtual functions


## `is`, `as`, Casting
- Automatic casts
    - As multiple inheritance is problematic here:
        - In Cilia/C++, an object can be an instance of several base classes at once, whereby the pointer (sometimes) changes during casting.
        - What if you still want/need to access the functions for a `Type obj` after `if obj is ParentA`?
        - Therefore maybe better: `if obj is String str ...`
            - as in C#
