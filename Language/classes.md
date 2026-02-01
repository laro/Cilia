---
title: Cilia.Classes
permalink: /cilia/classes/
order: 1
---

## Classes
- Quite as in C++
  ```
  class MyArrayOfInt {
      Int* numbers = NullPtr
      Int size = 0
      func clear()
  }
  ```
- `public` as default
    - Default access specifier is `public`.
    - Default inheritance access specifier is also `public`:
      ```
      class MySubClass : MyBaseClass {
          ...
      }
      ```
- Not using ~~`struct`~~, as it is just too similar to `class` (especiallly in Cilia) with no real benefit.
    - Keep as a reserved keyword for future use.
    - Cilia's roots are more in C++ and OOP than in plain C. Not using ~~`record`~~ either (Pascal, Ada).
