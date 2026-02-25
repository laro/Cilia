---
permalink: /basics/classes/
description: "Cilia class declaration: C++-like syntax with this as reference. Member variables, functions, inheritance."
---

# Class Declaration

Quite as in C++
```
class MyArrayOfInt {
  Int* numbers = NullPtr
  Int size = 0
  func clear()
}
```

In member functions **`this` is a reference** to the instance/object (not a pointer).
```
class String {
  func toLower() -> String& {
    // ...
    return this
  }
}
```

**Default** member access specifier **is `public`**.

Default inheritance access specifier is also `public`:
```
class MySubClass : ThePublicBaseClass {
  ...
}
```
```
class MySubClass : protected ABaseClass {
  ...
}
```

## No ~~`struct`~~
Not using ~~`struct`~~, as it would be just too similar to `class` (especially in Cilia) with no real benefit. Keep as a reserved keyword for future use.  
Cilia's roots are more in C++ and OOP than in plain C. Not using ~~`record`~~ either (Pascal, Ada).
