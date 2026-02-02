---
title: Advanced.Type Extension
permalink: /advanced/type-extension/
order: 4
---

## Type Extension

To add "member like" functions/methods, constants, types (and maybe static variables) to "third party" classes/types.  
In case of conflicts, in-class definitions (inside the class) have priority (and a warning is issued).
Extensions are defined similar to classes, but with the `extension` keyword.

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
