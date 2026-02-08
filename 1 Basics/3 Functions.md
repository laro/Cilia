---
permalink: /basics/functions/
---

## Function Declaration

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
                - it is not a reliable warning/guarantee that the argument may be changed, as any reference-like type (e.g. `Span<T>`) allows change even without `inout`.
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
            - and therefore also _every third-party string_ class (as long as it is implicitly convertible to `StringView`).
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
