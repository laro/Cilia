---
permalink: /basics/functions/
description: "Cilia functions: func keyword, trailing return type, combined parameters. Avoids most vexing parse, supports lambdas."
---

# Function Declaration

```
func multiplyAdd(Float x, y, Int z) -> Float {
    return x * y  +  Float(z)
}
```

Function declarations start with the keyword `func`, as in Swift.  
Easier parsing due to clear distinction between function declaration vs. variable declaration, avoiding the [most vexing parse](https://en.wikipedia.org/wiki/Most_vexing_parse).

Always and only in the trailing return type syntax (using `-> ReturnType`).  
Void functions (AKA "procedures") are written _without_ trailing ~~`-> Void`~~:  
`func print(String line) { ... }`

Function parameters are given as `TypeName parameterName`, multiple function parameters of the (exact) same type can be combined:  
`func multiply(`**`Int x, y`**`) -> Int` // x _and_ y are Int


## Misc

- Lambdas as in C++
  ```
  [](Int i) -> Float { i * 3.1415926 }
  ```

- `const` Member Functions
  ```
  class MyArrayOfInt {
      const func size() -> Int { ... }
  }
  ```

- `constexpr`, `consteval`
  ```
  constexpr multiply(Int x, y) -> Int {
      return x * y
  }
  consteval multiply(Int x, y) -> Int {
      return x * y
  }
  ```


## Function pointers

Trying to maintain consistency between declarations of functions, function pointers, functors and lambdas.

Examples:
- **`func(Int, Int -> Int)* pointerToFunctionOfIntAndIntToInt`**
- **`func(Int)* pointerToFunctionOfInt`**
- `func(Int, Int -> Int)& referenceToFunctionOfIntAndIntToInt` // Can't be zero
- `func(Int)& referenceToFunctionOfInt`


## Function Parameters

By default, function arguments are passed as const reference. Only small types (with a size of up to 16 bytes) are passed as const value.

For details, see [Function Parameters](/advanced/function-parameters/).
