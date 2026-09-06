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


## Pure Functions

`punc` to declare pure functions:

```
punc compoundInterest(Float capital, Float interestRate, Int years) -> Float
{
    return capital * pow(1.0 + interestRate, years);
}
```


## Lambdas

Lambdas also similar to C++
```
[](Int i) -> Float { i * 3.1415926 }
```

### Capture without Variable

| Syntax      | Meaning                                             |
| ----------- | --------------------------------------------------- |
| `[]`        | Capture nothing                                     |
| `[default]` | Capture all used variables by const copy or const reference depending on its type |
| `[copy]`    | Capture all used variables by (mutable) copy        |
| `[ref]`     | Capture all used variables by reference             |
| `[move]`    | Move all used variables into the lambda             |

### Capture with Variable

| Syntax     | Meaning                                               |
| ---------- | ----------------------------------------------------- |
| `[x]`      | Const copy or const reference depending on `x`'s type |
| `[copy x]` | Capture `x` by (mutable) copy                         |
| `[ref x]`  | Capture `x` by reference                              |
| `[move x]` | Move `x` into the lambda                              |

### Capture `this`

| Syntax        | Meaning                                       |
| ------------- | --------------------------------------------- |
| `[this]`      | Capture the current object by const copy or const reference depending on its type |
| `[ref this]`  | Capture the current object by reference       |
| `[copy this]` | Capture the current object by (mutable) copy  |


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
