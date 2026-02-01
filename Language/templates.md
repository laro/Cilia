---
title: Cilia.Templates
permalink: /cilia/templates/
order: 7
---

## Templates
The basic "new idea" is, to define templates (classes and functions) mostly the same as they are used.  
Similar as in Java, C#, Swift and Rust.
- **Class** templates  
  The template parameters (`<...>`) are given after the class name, so that the definition is similar to the usage (in a variable declaration).
  ```
  class MyArray<Number T> {
      T* numbers = NullPtr
      Int size = 0
  }
  ```
    - Template specialization
      ```
      class MyUniquePtr<type T> {
          ... destructor calls delete ...
      }
      class MyUniquePtr<type T[Int N]> {
          ... destructor calls delete[] ...
      }
      ```
    - Partial template specialization
      ```
      class KeyValuePair<type TKey, type TValue> {
          ...
      }
      class KeyValuePair<Int, type TValue> {
          ...
      }
      class KeyValuePair<type TKey, String> {
          ...
      }
      ```
    - Having to write `typename` (in C++) before dependent names in templates is quite annoying. It should possible to omit with two-pass compilation.
- **Function** templates
    - _Automatic_ function templates
        - If the type of (at least) one of the function parameters is a concept, then the function is (in fact) a function template. This is like abbreviated function templates in C++ 20, only ommitting the `auto` keyword.
            - Concept `Number`:
              ```
              func sq(Number x) -> Number {
                  return x * x
              }
              ```
                - However, the return type could be a _different_ type than `x` is (it just needs to satisfy the concept `Number`)
                - With `func add(Number a, b) -> Number` even `a` and `b` could be of a different type (but both need to satisfy the concept `Number`)
            - Concept `Real` (real numbers as `Float16`/`32`/`64`/`128`/`256` or `BigFloat`):
              ```
              func sqrt(Real x) -> Real {
                  // ... a series development ...
                  // (with number of iterations determined from the size of the mantissa)
              }
              ```
    - _Explicit_ function templates
        - When a common type is required:
          ```
          func add<Number T>(T x, y) -> T {
              return x + y
          }
          ```
        - When no deducing of the template type is possible (e.g. when there are no arguments).
            - The template parameters (`<...>`) are given after the function name,  
              as they are "type parameters" of the function.
            - This way the function definition is more similar to the function call.
              ```
              func getRandom<type T>() -> T { ... }
              Int random = getRandom<Int>();
              ```
    - For extension function templates it is necessary to know the _type_-specific template parameter(s) even before we write the function name, where the function-specific template parameters are given.  
      Therefore we write
        - `func<type T, Int N> T[N]::size() -> Int { return N }`
        - `func<type T, Int N> T[N]::convertTo<type TOut>() -> TOut[N] { ... }`  
            - Not ~~`func T[N]::convertTo<type T, Int N, type TOut>() { ... }`~~, as  
                - then T and N would be used even before they were declared, and
                - with `Float[3] arrayOfThreeFloat = [1.0, 2.0, 3.0]` we want to write  
                  `Int[3] arrayOfThreeInt = arrayOfThreeFloat.convertTo<Int>()` (not ~~`...convertTo<Float, 3, Int>()`~~)
            - The template parameters `T` and `N` belong to the type of the object `arrayOfThreeFloat` and are determined already. It would not be possible to change them in the call of `convertTo<>()`, so it is not desired to specify them here at all.

- Further restrict the type with `requires` (as in C++):
    - ```
      func sq<Number T>(T x) -> T
      requires (T x) { x * x }
      {
          return x * x
      }
      ```
    - ```
      class SlidingAverage<type T, type TSum = T>
      requires (T x, TSum sum) {
          sum = 0   // requires assignment of 0
          sum += x  // requires addition of type T to type TSum
          sum -= x  // requires subtraction of type T from type TSum
          sum / 1   // requires to divide sum by 1 (i.e. an Int)
      } {
          T+ numbers
          Int size = 0
          Int sizeMax = 0
          Int index = 0
          TSum sum = 0
      public:
          SlidingAverage(Int size) {
             sizeMax = size
             numbers = new T[sizeMax]
          }
          func append(T value) { ... }
          func average() -> TSum { ... }
          func reset() { ... }
          func reset(Int newSize) { ... }
      }
      ```
- Template **type alias** with `using` (not ~~`typedef`~~)
    - ```
      extension<type T> T {
          using InParameterType = const T&
      }
      ```
- Template static constants as type traits
    - ```
      extension<type T>          T { Bool IsFloatingPoint = False }
      extension            Float32 { Bool IsFloatingPoint = True }
      extension            Float64 { Bool IsFloatingPoint = True }
      extension<type T> Complex<T> { Bool IsFloatingPoint = T::IsFloatingPoint }
      ```
---
title: Cilia.Templates
permalink: /cilia/templates/
order: 7
---

## Templates
The basic "new idea" is, to define templates (classes and functions) mostly the same as they are used.  
Similar as in Java, C#, Swift and Rust.
- **Class** templates  
  The template parameters (`<...>`) are given after the class name, so that the definition is similar to the usage (in a variable declaration).
  ```
  class MyArray<Number T> {
      T* numbers = NullPtr
      Int size = 0
  }
  ```
    - Template specialization
      ```
      class MyUniquePtr<type T> {
          ... destructor calls delete ...
      }
      class MyUniquePtr<type T[Int N]> {
          ... destructor calls delete[] ...
      }
      ```
    - Partial template specialization
      ```
      class KeyValuePair<type TKey, type TValue> {
          ...
      }
      class KeyValuePair<Int, type TValue> {
          ...
      }
      class KeyValuePair<type TKey, String> {
          ...
      }
      ```
    - Having to write `typename` (in C++) before dependent names in templates is quite annoying. It should possible to omit with two-pass compilation.
- **Function** templates
    - _Automatic_ function templates
        - If the type of (at least) one of the function parameters is a concept, then the function is (in fact) a function template. This is like abbreviated function templates in C++ 20, only ommitting the `auto` keyword.
            - Concept `Number`:
              ```
              func sq(Number x) -> Number {
                  return x * x
              }
              ```
                - However, the return type could be a _different_ type than `x` is (it just needs to satisfy the concept `Number`)
                - With `func add(Number a, b) -> Number` even `a` and `b` could be of a different type (but both need to satisfy the concept `Number`)
            - Concept `Real` (real numbers as `Float16`/`32`/`64`/`128`/`256` or `BigFloat`):
              ```
              func sqrt(Real x) -> Real {
                  // ... a series development ...
                  // (with number of iterations determined from the size of the mantissa)
              }
              ```
    - _Explicit_ function templates
        - When a common type is required:
          ```
          func add<Number T>(T x, y) -> T {
              return x + y
          }
          ```
        - When no deducing of the template type is possible (e.g. when there are no arguments).
            - The template parameters (`<...>`) are given after the function name,  
              as they are "type parameters" of the function.
            - This way the function definition is more similar to the function call.
              ```
              func getRandom<type T>() -> T { ... }
              Int random = getRandom<Int>();
              ```
    - For extension function templates it is necessary to know the _type_-specific template parameter(s) even before we write the function name, where the function-specific template parameters are given.  
      Therefore we write
        - `func<type T, Int N> T[N]::size() -> Int { return N }`
        - `func<type T, Int N> T[N]::convertTo<type TOut>() -> TOut[N] { ... }`  
            - Not ~~`func T[N]::convertTo<type T, Int N, type TOut>() { ... }`~~, as  
                - then T and N would be used even before they were declared, and
                - with `Float[3] arrayOfThreeFloat = [1.0, 2.0, 3.0]` we want to write  
                  `Int[3] arrayOfThreeInt = arrayOfThreeFloat.convertTo<Int>()` (not ~~`...convertTo<Float, 3, Int>()`~~)
            - The template parameters `T` and `N` belong to the type of the object `arrayOfThreeFloat` and are determined already. It would not be possible to change them in the call of `convertTo<>()`, so it is not desired to specify them here at all.

- Further restrict the type with `requires` (as in C++):
    - ```
      func sq<Number T>(T x) -> T
      requires (T x) { x * x }
      {
          return x * x
      }
      ```
    - ```
      class SlidingAverage<type T, type TSum = T>
      requires (T x, TSum sum) {
          sum = 0   // requires assignment of 0
          sum += x  // requires addition of type T to type TSum
          sum -= x  // requires subtraction of type T from type TSum
          sum / 1   // requires to divide sum by 1 (i.e. an Int)
      } {
          T+ numbers
          Int size = 0
          Int sizeMax = 0
          Int index = 0
          TSum sum = 0
      public:
          SlidingAverage(Int size) {
             sizeMax = size
             numbers = new T[sizeMax]
          }
          func append(T value) { ... }
          func average() -> TSum { ... }
          func reset() { ... }
          func reset(Int newSize) { ... }
      }
      ```
- Template **type alias** with `using` (not ~~`typedef`~~)
    - ```
      extension<type T> T {
          using InParameterType = const T&
      }
      ```
- Template static constants as type traits
    - ```
      extension<type T>          T { Bool IsFloatingPoint = False }
      extension            Float32 { Bool IsFloatingPoint = True }
      extension            Float64 { Bool IsFloatingPoint = True }
      extension<type T> Complex<T> { Bool IsFloatingPoint = T::IsFloatingPoint }
      ```
---
title: Cilia.Templates
permalink: /cilia/templates/
order: 7
---

## Templates
The basic "new idea" is, to define templates (classes and functions) mostly the same as they are used.  
Similar as in Java, C#, Swift and Rust.
- **Class** templates  
  The template parameters (`<...>`) are given after the class name, so that the definition is similar to the usage (in a variable declaration).
  ```
  class MyArray<Number T> {
      T* numbers = NullPtr
      Int size = 0
  }
  ```
    - Template specialization
      ```
      class MyUniquePtr<type T> {
          ... destructor calls delete ...
      }
      class MyUniquePtr<type T[Int N]> {
          ... destructor calls delete[] ...
      }
      ```
    - Partial template specialization
      ```
      class KeyValuePair<type TKey, type TValue> {
          ...
      }
      class KeyValuePair<Int, type TValue> {
          ...
      }
      class KeyValuePair<type TKey, String> {
          ...
      }
      ```
    - Having to write `typename` (in C++) before dependent names in templates is quite annoying. It should possible to omit with two-pass compilation.
- **Function** templates
    - _Automatic_ function templates
        - If the type of (at least) one of the function parameters is a concept, then the function is (in fact) a function template. This is like abbreviated function templates in C++ 20, only ommitting the `auto` keyword.
            - Concept `Number`:
              ```
              func sq(Number x) -> Number {
                  return x * x
              }
              ```
                - However, the return type could be a _different_ type than `x` is (it just needs to satisfy the concept `Number`)
                - With `func add(Number a, b) -> Number` even `a` and `b` could be of a different type (but both need to satisfy the concept `Number`)
            - Concept `Real` (real numbers as `Float16`/`32`/`64`/`128`/`256` or `BigFloat`):
              ```
              func sqrt(Real x) -> Real {
                  // ... a series development ...
                  // (with number of iterations determined from the size of the mantissa)
              }
              ```
    - _Explicit_ function templates
        - When a common type is required:
          ```
          func add<Number T>(T x, y) -> T {
              return x + y
          }
          ```
        - When no deducing of the template type is possible (e.g. when there are no arguments).
            - The template parameters (`<...>`) are given after the function name,  
              as they are "type parameters" of the function.
            - This way the function definition is more similar to the function call.
              ```
              func getRandom<type T>() -> T { ... }
              Int random = getRandom<Int>();
              ```
    - For extension function templates it is necessary to know the _type_-specific template parameter(s) even before we write the function name, where the function-specific template parameters are given.  
      Therefore we write
        - `func<type T, Int N> T[N]::size() -> Int { return N }`
        - `func<type T, Int N> T[N]::convertTo<type TOut>() -> TOut[N] { ... }`  
            - Not ~~`func T[N]::convertTo<type T, Int N, type TOut>() { ... }`~~, as  
                - then T and N would be used even before they were declared, and
                - with `Float[3] arrayOfThreeFloat = [1.0, 2.0, 3.0]` we want to write  
                  `Int[3] arrayOfThreeInt = arrayOfThreeFloat.convertTo<Int>()` (not ~~`...convertTo<Float, 3, Int>()`~~)
            - The template parameters `T` and `N` belong to the type of the object `arrayOfThreeFloat` and are determined already. It would not be possible to change them in the call of `convertTo<>()`, so it is not desired to specify them here at all.

- Further restrict the type with `requires` (as in C++):
    - ```
      func sq<Number T>(T x) -> T
      requires (T x) { x * x }
      {
          return x * x
      }
      ```
    - ```
      class SlidingAverage<type T, type TSum = T>
      requires (T x, TSum sum) {
          sum = 0   // requires assignment of 0
          sum += x  // requires addition of type T to type TSum
          sum -= x  // requires subtraction of type T from type TSum
          sum / 1   // requires to divide sum by 1 (i.e. an Int)
      } {
          T+ numbers
          Int size = 0
          Int sizeMax = 0
          Int index = 0
          TSum sum = 0
      public:
          SlidingAverage(Int size) {
             sizeMax = size
             numbers = new T[sizeMax]
          }
          func append(T value) { ... }
          func average() -> TSum { ... }
          func reset() { ... }
          func reset(Int newSize) { ... }
      }
      ```
- Template **type alias** with `using` (not ~~`typedef`~~)
    - ```
      extension<type T> T {
          using InParameterType = const T&
      }
      ```
- Template static constants as type traits
    - ```
      extension<type T>          T { Bool IsFloatingPoint = False }
      extension            Float32 { Bool IsFloatingPoint = True }
      extension            Float64 { Bool IsFloatingPoint = True }
      extension<type T> Complex<T> { Bool IsFloatingPoint = T::IsFloatingPoint }
      ```
