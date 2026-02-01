---
title: Basics.Declarations
permalink: /basics/declarations/
order: 1
---

## Variable Declaration
`Int i` as variable declaration, very much as in C/C++ (and Java, C#).
```
TypeName variableName
```
- Some simplifications and restrictions:
    - The type definition is completely on the left-hand side,  
      i.e. before the variable name, also for arrays and bit fields.
    - All variables in a multiple-variable declarations have to be of the exact same type.

- Examples:
    - `Int i`
    - `Int i = 0`
    - `Int x, y`
    - `Int x = 99, y = 199`
    - Arrays
        - `Int[10] highScoreTable`  // Array of ten integers (instead of ~~`Int highScoreTable[10]`~~)
    - Multiple-variable declarations
        - `Float* m, n`        // m _and_ n are pointers (contrary to C/C++)
        - `Int& m = x, n = y`  // m _and_ n are references (contrary to C/C++)
        - `Float[2] p1, p2`    // p1 _and_ p2 are arrays of two Float values each
    - Constructors
        - `Image image(width, height, 0.0)`
        - `Image image()`
            - is the same as `Image image`, i.e. it is a variable declaration,
            - a function declaration would be written as `func image() -> Image`.
    - References
        - `Complex<Float>& complexNumber = complexNumberWithOtherName`

- **`const`** always binds to the right (contrary to C/C++).  
    - Intuitively, one can read `const int` as “a constant integer”.
    - `const` binds more strongly than `*` and `&`, but less strongly than `[]`.
    - So the keyword `const` is always interpreted as a type qualifier that applies directly to the type specifier (e.g. `Float`), pointer declarator (`*`), or type specifier with array declarator (`Float[]`, `Float[3]`, or `Float[String]`) that appears immediately to its right.
    - `const` as a type qualifier for a reference (`&`) is not allowed, i.e. no ~~`Float const&`~~.
        - `const Float&` is allowed, of course.
    - Examples:
        - `const Float* pointerToConstantFloat`
        - `const Float const* constantPointerToConstantFloat`
        - `Float const* constantPointerToMutableFloat`
    - `const` as a type qualifier for an array declarator (`[]`):
        - `const Float[] constArrayOfFloat` is equivalent to `const Array<Float> constArrayOfFloat`.
            - `Float const[] constArrayOfFloat` is equivalent to `const Array<Float> constArrayOfFloat`, too.  
              Members of a const array are always effectively const anyway.
            - With the array declarator syntax (`[]`) it is _not_ possible to say `Array<const Float> arrayOfConstFloat`.  
              That does not compile in C++ anyway, because an array whose element type is non-assignable has no useful mutation model.
              (MSVC says 'The C++ Standard forbids containers of `const` elements because `allocator<const T>` is ill-formed.')
        - A `const` static array declarator `const Float[3]` is interpreted as a `const` static array of three `Float` (which effectively are `const`, too).
        - `const ContactInfo[String] constMapOfContactInfoByName` is equivalent to `const Map<String, ContactInfo> constMapOfContactInfoByName`.
- **Type inference** with `var` / `const`:
    - `var i = 3` instead of ~~`auto i = 3;`~~
    - `const i = 3` instead of ~~`const auto i = 3;`~~ (it is short, and `const var` / "constant variable" is a bit of a contradiction in terms.)

- Not allowed / a syntax error is:
    - ~~`Float* m, &n`~~
        - Type variations within multiple-variable declarations are _not_ allowed.
        - It has to be the exact same type.
    - ~~`Float*m`~~
        - Whitespace _between_ type specification and variable name is mandatory.
        - TODO Probably too difficult to realize, as the lexer already removes all whitespace.
    - ~~`Image image { width, height, 0.0 }`~~
        - No uniform / brace initialization _for plain constructors_, as there is no need anymore.
            - There are generally _no_ implicit narrowing conversions, e.g.
                - not ~~`Int64` -> `Int32`~~,
                - not  ~~`Float64` -> `Float32`~~,
            - and _no_ other _unsafe_ integral promotions allowed:
                - ~~`Int` -> `UInt`~~,
                - ~~`UInt` -> `Int`~~
            - Nowhere, _not_ in
                - assignments,
                - function or constructor calls,
                - list initialization (with `{ }`),
                - arithmetic expressions (integral promotions),
                - mixed types in expressions,
                - enums, nor
                - return values.
            - The most vexing parse is mitigated with the keyword `func`.
            - Brace initialization only for constructors with `InitializerList<T>` as parameter (i.e. for "list-initialization" and "copy-list-initialization").
        - See [Misc](/cilia/misc/#misc) / Mixed arithmetic and [https://stackoverflow.com/a/18222927](https://stackoverflow.com/a/18222927)

- Bit fields
    - `UInt32:1 sign` instead of ~~`UInt32 sign : 1`~~.
    - TODO Standardization of the bit field layout would be nice (LSB-first like on LittleEndian/Intel, or MSB-first like on BigEndian/Motorola),
        - but IMHO there is no clear/logical/right definition (especially with LittleEndian).
        - Dense packing of Int1, Int2, Int3, ..., Int64 could be more straightforward anyway.

---

## Classes
- Quite as in C++
  ```
  class MyArrayOfInt {
      Int* numbers = NullPtr
      Int size = 0
      func clear()
  }
  ```
- `public` as default
    - Default access specifier is `public`.
    - Default inheritance access specifier is also `public`:
      ```
      class MySubClass : MyBaseClass {
          ...
      }
      ```
- Not using ~~`struct`~~, as it is just too similar to `class` (especiallly in Cilia) with no real benefit.
    - Keep as a reserved keyword for future use.
    - Cilia's roots are more in C++ and OOP than in plain C. Not using ~~`record`~~ either (Pascal, Ada).

---

## Functions
```
func multiplyAdd(Float x, y, Int z) -> Float {
    return x * y  +  Float(z)
}
```
- Function declarations start with the keyword `func`,
    - as in Swift.
    - Easier parsing due to clear distinction between function declaration vs. variable declaration,  
      avoiding the [most vexing parse](https://en.wikipedia.org/wiki/Most_vexing_parse).
- Function parameters are given as `TypeName parameterName`, as with variable declarations.
- Multiple function parameters of the (exact) same type can be combined to e.g. `TypeName parameter1, parameter2`, as with variable declarations.
    - `func multiply(`**`Int x, y`**`) -> Int` // x _and_ y are Int
- Always and only in the trailing return type syntax (using `-> ReturnType`),
    - but void functions (AKA "procedures") are written _without_ trailing ~~`-> Void`~~
      (like `func print(String line) { ... }`).
- **Lambdas**
    - `[](Int i) -> Float { i * 3.14 }`  
      as in C++
- **Const** member functions:
  ```
  class MyArrayOfInt {
      const func size() -> Int {
          return size_;
      }
  protected:
      Int size_ = 0
  }
  ```
- **`constexpr`** and `consteval`
  ```
  constexpr multiply(Int x, y) -> Int {
      return x * y
  }
  consteval multiply(Int x, y) -> Int {
      return x * y
  }
  ```
- **Function pointers**
    - Trying to maintain consistency between declarations of functions, function pointers, functors and lambdas.
    - Examples:
        - **`func(Int, Int -> Int)* pointerToFunctionOfIntAndIntToInt`**
        - **`func(Int)* pointerToFunctionOfInt`**
        - `func(Int, Int -> Int)& referenceToFunctionOfIntAndIntToInt` // Can't be zero
        - `func(Int)& referenceToFunctionOfInt`

---

## Function Parameter Passing Modes
Each function parameter in Cilia has a "parameter passing mode" that defines how its argument is passed and used — whether it’s input-only, mutable, output, copied, or moved.  
The basic idea is to have the most efficient/appropriate parameter passing as the _default_, and to give more the intent than the technical realization.  
Taken from [Cpp2 / Herb Sutter](https://hsutter.github.io/cppfront/cpp2/functions/) (surely inspired by the `out` parameters of C#, and by Ada).
- **Default is passing as `in`**-parameter.
    - So if no parameter passing keyword is given, `in` parameter passing is used.
    - All other parameter passing methods need to be explicitly given.
- Function call parameters are passed as either **`in`**, **`inout`**, **`out`**, **`copy`**, **`move`**, or **`forward`**.
    - Wording fits nicely for function parameters: How does the parameter get into the function body (or out of it).
- The loop variable of `for ... in` is passed as either **`in`**, **`inout`**, **`copy`**, or **`move`**  
  (`out` and `forward` are not applicable here).
    - With `for` loops these keywords describe how the information (i.e. the variable) gets into the body of the loop (or out of it).
- The argument of `catch ... { ... }` is passed as **`in`**  
  (`copy`, `inout`, `move` are not recommended, `out` and `forward` are not applicable here).
- Parameter passing mode keywords:
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
        - ~~Keyword `inout` is also to be given at the caller: `swap(inout a, inout b)`~~
            - No, because
                - it is verbose,
                - it is not a reliable warning/guarantee, that the argumemt may be changed, as any reference-like type (e.g. `Span<T>`) allows change even without `inout`.
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
        - Maybe even with ad-hoc declaration of the out variable (as in C# 7.0):
            - ```
              if not open("...", out String errorDetails) {
                  cout << errorDetails
              }
              ```
            - ```
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
                - `i` is an `Int`
            - `for copy str in stringArray { ... }`
                - `str` is a `String`
            - `for copy str in ["an", "array", "of", "words"] { ... }`
                - `str` is a `String` (not a ~~`StringView`~~, due to the `X`/`XView`-copy-trick)
    - **`move`**
        - for move sematics.
        - Technically a right-value reference (`X&&`)
    - **`forward`**
        - for perfect forwarding in template functions.
        - TODO Technically a right-value reference (`X&&`), too?
- Type traits **`InParameterType`** to determine the concrete type to be used for `in`-passing.
    - The rule of thumb is:
        - Objects that are POD (Plain Old Data, i.e. with no pointers) with a size less than or equal to the size of two `Int` (i.e. up to 16 bytes on 64 bit platforms) are passed by value.
        - Larger objects (or non-POD) are passed by reference.
    - So, as general default, use _const reference_,
        - ```
          extension<type T> T {
              InParameterType = const T&
          }
          ```
    - and use a "list of exceptions" for the "const _value_ types".
        - ```
          extension     Bool { InParameterType = const Bool }
          extension     Int8 { InParameterType = const Int8 }
          extension    Int16 { InParameterType = const Int16 }
          extension    Int32 { InParameterType = const Int32 }
          extension    Int64 { InParameterType = const Int64 }
          extension    UInt8 { InParameterType = const UInt8 }
          extension   UInt16 { InParameterType = const UInt16 }
          extension   UInt32 { InParameterType = const UInt32 }
          extension   UInt64 { InParameterType = const UInt64 }
          extension  Float32 { InParameterType = const Float32 }
          extension  Float64 { InParameterType = const Float64 }
          extension  std::string_view { InParameterType = const std::string_view }
          extension std::span<type T> { InParameterType = const std::span<T> }
          ...
          ```
        - `extension<type T> Complex<T> { InParameterType = T::InParameterType }`
            - A generic rule: `Complex<T>` is passed the same way as `T`,
            - could be further refined/corrected with  
              `extension Complex<Float128> { InParameterType = const Complex<Float128>& }`  
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
        - `extension String { InParameterType = const StringView }`  
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
        - Though I don't see any advantage with respect to the `for ... in` loop, I would still apply the same rules just for consistency.
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
          extension String { InParameterType = const StringView }
          extension  Array { InParameterType = const ArrayView }
          extension Vector { InParameterType = const VectorView }
          ```
    - Bigger `...View`-classes with a size of _more_ than 16 bytes (such as `MatrixBasicView`, `ImageBasicView`, and `MDArrayBasicView`) will be passed by reference:
        - ```
          extension  Matrix { InParameterType = const MatrixBasicView& }
          extension   Image { InParameterType = const ImageBasicView& }
          extension MDArray { InParameterType = const MDArrayBasicView& }
          ```
        - (Which you don't have to write down explicitly, because `const&` simply is the standard for user defined types.)
- Type trait **`CopyParameterType`**
    - of a type `T` typically simply is `T`  
      `extension<type T> T { CopyParameterType = T }`  
    - but for `View`-types it is the corresponding "full" type:
      ```
      extension       StringView { CopyParameterType = String }
      extension        ArrayView { CopyParameterType = Array }
      extension       VectorView { CopyParameterType = Vector }
      extension       MatrixView { CopyParameterType = Matrix }
      extension  MatrixBasicView { CopyParameterType = Matrix }
      extension        ImageView { CopyParameterType = Image }
      extension   ImageBasicView { CopyParameterType = Image }
      extension      MDArrayView { CopyParameterType = MDArray }
      extension MDArrayBasicView { CopyParameterType = MDArray }
      ```
    - The idea is to get a _mutable copy_ of the object, even without understanding the concept of a `View`.
    - Example:
        - `for copy str in ["an", "array", "of", "words"] { ... }`
            - While the literal `["an", "array", "of", "words"]` is an `StringView[]`,  
              `str` is a `String` (not a ~~`StringView`~~).
            - This way people do not necessarily need to understand the concept of a `StringView` literal. They simply write `copy` to get a `String` with a copy of the content of the `StringView`.
            - (This is currently the only useful example I can think of.)

---

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

---

## Operator Declaration
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
        - Defined for _`Bool`_ (not for integers),
        - operators `!`, not ~~`~`~~,
            - `&&` and `||`, not ~~`&` and `|`~~.
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
        - operators `~`, not ~~`!`~~,
            - `&` and `|`, not ~~`&&` and `||`~~.
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

---

## Aliasing
Create an alias with `using`, for:
- Member **variable** alias  
  `using var x = data[0]`  
  `using Int y = data[1]`  
  `using T   z = data[2]`
    - Not quite possible in C++.
        - With `T& z = data[2]` unfortunately memory is created for the reference (the pointer).
        - And this indeed is necessary here, because the reference could be assigned differently in the constructor, so it is not possible to optimize it away.
- Member **function** alias
    - `using func f(String) = g(String)` to alias the function `g(String)`.
    - `using func f = g` to alias _all_ overloads of the function `g`.
- **Type** alias in a class
    - `using InParameterType = const StringView`  
      (no ~~`typedef`~~)

---

## Type Extension
To add "member like" types, functions/methods, constants (and maybe static variables) to "third party" classes/types.  
In case of conflicts, in-class definitions (inside the class) have priority (and a warning is issued).
Extensions are defined using the `extension` keyword followed by the type name and a block `{}`.
- **Extension methods**
    - Can be called like normal member functions (with standard dot-notation), but they but do not have access to private or protected members themselves.
    - Inside an extension, `this` refers to the instance itself.
    - Also possible for basic/arithmetic types, e.g.:  
      ```cpp
      extension Int {
          func toString() -> String { 
              // Logic to convert Int to String
          }
      }
     
      // Usage:
      Int i = 10
      i.toString()
      ```
- **Externally defined alias** (with `using`) for members:
    - Useful for adapting APIs or providing more descriptive names.
    - **Variables**  
      ```cpp
      extension Vector2 {
          using var x = data[0]
          using var y = data[1]
      }
      ```
    - **Functions**  
      ```cpp
      extension std::vector<type T> {
          // Alias for a specific signature
          using func pushBack(String) = push_back(String)
          
          // Alias for all overloads of 'push_back'
          using func append = push_back
        }
        ```
    - **Types**  
        - Define member types or traits externally.
        - ```cpp
          extension std::string_view {
              using InParameterType = const std::string_view // Pass by value
          }
          ```
- Static constants, typically for type traits
  ```cpp
  extension Float32 {
      static const Bool IsFloatingPoint = True
  }
  extension Float64 {
      static const Bool IsFloatingPoint = True
  }
  ```
- Static variablers
    - Why not?
    - ```cpp
      extension ContactInfo {
          // External mutable static variable
          static Int numOfCallsToExtensionFunctionX = 0
      }
      ```
- Generic Extensions (e.g., for Arrays)
    - Extensions can be parameterized to support generic types and native arrays.
    - ```cpp
      extension <type T, Int N> T[N] {
          using ValueType = T
          
          func length() -> Int {
              return N
          }
          
          func begin() -> T* { return &this[0] }
          func end()   -> T* { return &this[N] }
      }
      ```
