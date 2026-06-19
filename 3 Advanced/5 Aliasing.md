---
permalink: /advanced/aliasing/
description: "Cilia aliasing: using for member variables and functions. Type aliases, enables CamelCase wrapper design."
---

# Aliasing of Variables, Functions, and Types

Create an alias with `using`.


## Member **Variable** Alias

```
class Vector3<type T> : Vector<3, T> {
    using var x = data[0]
    using Int y = data[1]
    using T   z = data[2]
}
```

This is not quite possible in C++:
- With `T& z = data[2]`, unfortunately, memory is allocated for the reference (the pointer).
- And the compiler cannot optimize it away, because the reference could be rebound in the constructor.


## Member **Function** Alias

```
class A : B {
    using func f(String) = g(String)
    using func f = g
}
```
- `using func f(String) = g(String)` to alias the function `g(String)`.
- `using func f = g` to alias _all_ overloads of the function `g`.


## **Type** Alias in a Class

```
class String {
    using InParameterType = const StringView
}
```
(No ~~`typedef`~~.)
