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

Using the trailing return type syntax `-> ReturnType`, but void functions (AKA "procedures") are written _without_ trailing ~~`-> Void`~~:
```
func print(String line) { ... }
```


Function parameters are given as `TypeName parameterName`, multiple function parameters of the (exact) same type can be combined:  
`func multiply(`**`Int x, y`**`) -> Int` // x _and_ y are Int


## Lambdas

Lambdas also similr to C++
```
[](Int i) -> Float { i * 3.1415926 }
```

### Capture with Variable

| Capture       | Syntax     | Meaning                                               |
| ------------- | ---------- | ----------------------------------------------------- |
| **Default**   | `[x]`      | Const copy or const reference depending on `x`'s type |
| **Copy**      | `[copy x]` | Capture `x` by copy                                   |
| **Reference** | `[ref x]`  | Capture `x` by reference                              |
| **Move**      | `[move x]` | Move `x` into the lambda                              |

### Capture `this`

| Capture            | Syntax        | Meaning                                       |
| ------------------ | ------------- | --------------------------------------------- |
| **Const this**     | `[this]`      | Capture the current object by const reference |
| **Reference this** | `[ref this]`  | Capture the current object by reference       |
| **Copy this**      | `[copy this]` | Capture the current object by copy            |

### Capture without Variable

| Capture       | Syntax      | Meaning                                             |
| ------------- | ----------- | --------------------------------------------------- |
| **Nothing**   | `[]`        | Capture nothing                                     |
| **Default**   | `[default]` | Capture all used variables by const copy or const reference depending on its type |
| **Copy**      | `[copy]`    | Capture all used variables by copy                  |
| **Reference** | `[ref]`     | Capture all used variables by reference             |
| **Move**      | `[move]`    | Move all used variables into the lambda             |


## Misc

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


## Function Pointers

Trying to maintain consistency between declarations of functions, function pointers, functors and lambdas.

Examples:
- **`func(Int, Int -> Int)* pointerToFunctionOfIntAndIntToInt`**
- **`func(Int)* pointerToFunctionOfInt`**
- `func(Int, Int -> Int)& referenceToFunctionOfIntAndIntToInt` // Can't be zero
- `func(Int)& referenceToFunctionOfInt`


## Function Parameters

By default, function arguments are passed as const reference. Only small types (with a size of up to 16 bytes) are passed as const value.

For details, see [Parameter Passing](/advanced/parameter-passing/).
