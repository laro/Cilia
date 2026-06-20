---
permalink: /advanced/type-extension/
description: "Cilia type extension: add methods to third-party types. Extension methods, static members, extension keyword."
---

# Type Extension

"Third party" classes or built-in types that we cannot change otherwise can be extended with "member-like"
- functions/methods (non-virtual and static),
- dependent types (`T::InParameterType`) or type aliases,
- static constants and variables.

In case of conflicts, in-class definitions (inside the class) have priority (and a warning is issued).

Extensions are defined similar to classes, but with the `extension` keyword.


## Extension Methods

- Can be called like normal member functions (with standard dot-notation), but they do not have access to private or protected members.
- Inside an extension, `this` refers to the instance itself.
- Also possible for basic/arithmetic types, e.g.:
  ```
  extension Int {
      func toString() -> String { 
          // Logic to convert Int to String
      }
  }
  
  // Usage:
  Int i = 10
  i.toString()
  ```


## Externally Defined Alias

`using` for members, useful for adapting APIs or providing more descriptive names.
- **Variables**
  ```
  extension Vector2 {
      using var x = data[0]
      using var y = data[1]
  }
  ```
- **Functions**
  ```
  extension std::vector<type T> {
      // Alias for a specific signature
      using func pushBack(String) = push_back(String)
      
      // Alias for all overloads of 'push_back'
      using func append = push_back
  }
  ```
- **Types**  
    - Define member types or traits externally.
    - ```
      extension std::string_view {
          using InParameterType = const std::string_view // Pass by value
      }
      ```


## Static Constants & Variables

- Static constants, typically for type traits
  ```
  extension Float32 {
      static const Bool IsFloatingPoint = True
  }
  extension Float64 {
      static const Bool IsFloatingPoint = True
  }
  ```
- Static variables
  ```
  extension ContactInfo {
      // External mutable static variable
      static Int numOfCallsToExtensionFunctionX = 0
  }
  ```
    - Rarely used, but why not.
    - It is not possible to add _non-static_ member variables, as that would change the size of the class.


## Generic Extensions
Extensions can be parameterized to support 
- generic types and
- basic types, e.g. native static arrays.

```
extension<type T, Int N> T[N] {
    using ValueType = T
    
    func length() -> Int {
        return N
    }
    
    func begin() -> T* { return &this[0] }
    func end()   -> T* { return &this[N] }
}
```

## Extension Classes
Allow to create drop-in replacements for existing classes. With no-op conversion similar to `operator String&`, but in both directions.  
Extension classes do _not_ have any additional member variables.

```
extension class String : std::string {
    using func startsWith = starts_with
}
```
