---
title: Cilia.Functions
permalink: /cilia/functions/
order: 2
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
