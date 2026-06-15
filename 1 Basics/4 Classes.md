---
permalink: /basics/classes/
description: "Cilia class declaration: C++-like syntax with this as reference. Member variables, functions, inheritance."
---

# Class Declaration

Quite as in C++
```
// Manual container; normally you'd just use Int[].
class MyArrayOfInt {
    Int[0]+ numbers = NullPtr
    Int size = 0
    Int capacity = 0
    func clear()
}
```


## `this`-Reference

In member functions `this` is a reference to the instance/object (not a pointer).
```
class String {
    func toLower() -> String& {
        // ...
        return this
    }
}
```
Getting the pointer via `&this`.


## `public` as Default

Default member access specifier is `public`.

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


## Interfaces
```
interface Seekable {
    func seek(Int offset)
    func getPosition() -> Int
}
```
instead of (but still possible)
```
class Seekable {
    virtual ~Seekable() = default
    virtual func seek(Int offset) = 0
    virtual func getPosition() -> Int = 0
}
```
Interfaces have
- no member variables ("data members", "fields"),
    - maybe allow`const static`,
- no constructors, and
- all methods are automatically `public` and `virtual`,
    - optionally with default implementation.


### Multiple Interfaces

A class can implement several interfaces:
```
class File : Stream, Seekable, Closeable {
    ...
}
```


### No Diamond Problem for State

Because interfaces have **no member variables**, a class can never inherit the same data member twice. The classic C++ "diamond problem" — duplicated base-class state — therefore cannot occur, and no `virtual` inheritance is needed to merge base subobjects:
```
interface A {
    func name() -> String
}
interface B : A {
    ...
}
interface C : A {
    ...
}
// `A` is reached via both `B` and `C`, but there is only ever one
// object, with no duplicated state.
class D : B, C {
    func name() -> String { return "C" }
}
```


### Ambiguous Default Implementations

The only ambiguity that can remain is a **method** for which _two_ interfaces provide a (different) default implementation. The compiler then requires the class to resolve it explicitly by overriding the method. A specific interface's default can still be called via `Interface::method()`:
```
interface Greeter {
    func greet() -> String { return "Hello from Greeter" }
}
interface Logger {
    func greet() -> String { return "Hello from Logger" }
}
class Service : Greeter, Logger {
    // Required, as it would otherwise be ambiguous.
    override func greet() -> String {
        return Greeter::greet()   // explicitly pick one
    }
}
```


## No ~~`struct`~~

Not using ~~`struct`~~, as it would be just too similar to `class` (especially in Cilia) with no real benefit. Keep as a reserved keyword for future use.  
Cilia's roots are more in C++ and OOP than in plain C. Not using ~~`record`~~ either (Pascal, Ada).
