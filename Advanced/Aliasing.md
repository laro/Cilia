---
title: Advanced.Aliasing
permalink: /advanced/aliasing/
order: 3
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
