---
permalink: /advanced/misc/
---

## Misc

### C++ Compatibility / Interoperability
Cilia is **compatible to C++** and maybe other languages of this "**language family**" / "**ecosystem**",  
as with:
- Java and Kotlin, Scala, Groovy, Clojure, Fantom, Ceylon, Jython, JRuby ...
- C# and C++/CLI, Visual Basic .NET, F#, A# (Ada), IronPython, IronRuby ...
- Objective-C and Swift

Bi-directional interoperability, so (with a hypothetical C++/Cilia compiler) it is possible to include
- C++ headers and modules from Cilia,
- Cilia headers and modules from C++.

Can call C functions, access C structs (as C++ can do).

The compiler recognizes the language (C, C++, or Cilia) by:
- Marked blocks
    - `lang "C++" { ... }`
    - `lang "Cilia" { ... }`
    - ~~`lang "C" { ... }`~~
    - TODO Limited to top level?
    - Technically limited to languages where the scope is marked with `{ }`.
- File extension
    - Cilia: `*.cil`, `*.hil`
    - C++: `*.cpp`, `*.hpp` or `*.cxx`, `*.hxx`
        - Even `*.h`, but that is a problem, as the header could be C or C++ code.  
          So use of `*.hpp` is recommended for C++ code.  
          This can probably best be solved using path based rules.
    - C: `*.c` `*.h`
- Path based rules,
    - to handle C or C++ standard headers in certain directories.
- File specific configuration,
    - can be set in the IDE or on the command line,  
      for each file individually.

When translating C++ code to Cilia then change conflicting names, e.g.
- `int var` -> `Int __variable_var`
- `class func` -> `class __class_func`
- `yield()` -> `func __function_yield()`


### Two-Pass Compiler

So no forward declarations necessary, as with C# and Java (but unlike C/C++, due to its single-pass compiler).


### Restricted Mixed Arithmetic

No mixing of signed with unsigned integer:
- `Signed + - * / Unsigned` is an error,
    - you have to cast explicitly,
    - i.e. no implicit cast (neither ~~`UInt` -> `Int`~~ nor ~~`Int` -> `UInt`~~).
    - `Int` (i.e. signed) is almost always used anyways.
- Error with `if aUInt < anInt`,
    - you have to cast: `if Int(aUInt) < anInt`.
- Error with `if aUInt < 0`,
    - if the literal on the right is `<= 0`
    - TODO Checking for `if aUInt <= -1` would be simple, as `-1` can _not_ implicitly be converted to an UInt. But `0` can, so how to check for that?

Mixing integer with float:
- `1 * aFloat` is possible
    - Warning, if the integer literal cannot be reproduced exactly as `Float32`/`64`
- `anInt * aFloat` is possible
    - Warning that the integer variable may not be reproduced exactly as `Float32`/`64`,  
      i.e. with
        - `aFloat32 * anInt8`  // OK
        - `aFloat32 * anInt16` // OK
        - `aFloat32 * anInt32` // Error
            - `aFloat32 * Float32(anInt32)` // OK
        - `aFloat32 * anInt64` // Error
            - `aFloat32 * Float32(anInt64)` // OK
        - `aFloat64 * anInt8`  // OK
        - `aFloat64 * anInt16` // OK
        - `aFloat64 * anInt32` // OK
        - `aFloat64 * anInt64` // Error
            - `aFloat64 * Float64(anInt64)` // OK


### Endianness

Having integers with a defined [endianness](https://en.wikipedia.org/wiki/Endianness) is mainly useful for binary file and network message formats, which typically follow specific (often traditional) conventions.

When integers are read and written in the processor’s native endianness, there is no overhead at all. Handling the non-native endianness merely involves shuffling bytes at read and write time, with no impact on the actual calculations.

Big Endian (Motorola)
- `cilia::be::Int`, `Int8`, `Int16`, `Int32`, `Int64`
- MSB first (most significant byte first), starting with the "big end"
- MSb first (most significant bit first)
- classical "[network byte order](https://en.wikipedia.org/wiki/Endianness#Networking)"

Little Endian (Intel)
- `cilia::le::Int`, `Int8`, `Int16`, `Int32`, `Int64`
- LSB first (least significant byte first), starting with the "little end"
- LSb first (least significant bit first)
- "[USB byte order](http://cholla.mmto.org/computers/usb/endian.html)"


### Extended & Arbitrary Precision Integer & Float

- `Int128`, `Int256`
- `UInt128`, `UInt256` e.g. for SHA256
- `BigInt` – Arbitrary Precision Integer
    - for cryptography, maybe computer algebra, numerics
    - see [Boost.Multiprecision](https://www.boost.org/doc/libs/1_79_0/libs/multiprecision/doc/html/index.html), [GMP](https://gmplib.org)
- `BFloat16` (Brain Floating Point) with 1 bit sign, 8 bit exponent, 7 bit significand,
    - i.e. the 16 low bits of the Float32 significand are cut off.
- `Float128` with 1 bit sign, 15 bit exponent, 112 bit significand
- `Float256` with 1 bit sign, 19 bit exponent, 237 bit significand
- Non-standardized floating point types
    - `BigFloat` for arbitrary precision float,
        - see [GMP](https://gmplib.org), [MPFR](https://www.mpfr.org)
        - The precision (i.e. the number of bits of significand and exponent) is a property of a BigFloat variable,
            - is set at construction (e.g. `BigFloat bigFloat(1024, 64)`)
            - and can dynamically be changed with assignment.
    - `HighPrecisionFloat<Int SignificandBits, Int ExponentBits>` as template for custom float types with statically fixed precision, like `Float1024`, `Float2048`, ...
        - NumberOfBits must be multiples of `sizeof(Int)` (i.e. multiples of 64).
    - `DDFloat`, `TDFloat`, `QDFloat`
        - double-double/triple-double/quad-double arithmetic
        - [wiki.org/Double-Double Arithmetic](https://en.wikipedia.org/w/index.php?title=Quadruple-precision_floating-point_format)
        - [https://stackoverflow.com/a/6770329](https://stackoverflow.com/a/6770329)
    - General problem: All these types, when saved in binary form, are incompatible to the IEEE 754 format for 128/256/... bit float. So better to save them as string.


### Integer Operations with Carry

I want integer operations **with carry** (flag or UInt) to implement `Int128`, `Int256` etc. without the need for processor specific assembler or compiler intrinsics.
- Add with carry (flag, i.e. one bit only)
    - `UInt c = add(UInt a, UInt b, inout Bool carryFlag)`
        - `c = bits63..0(a + b + carryFlag)`  
          `carryFlag = bit64(a + b + carryFlag)`
    - `a.add(UInt b, inout Bool carryFlag)`
        - `a = bits63..0(a + b + carryFlag)`  
          `carryFlag = bit64(a + b + carryFlag)`
- Multiply with carry (high data, i.e. one UInt)
    - `UInt c = multiply(UInt a, UInt b, out UInt cHigh)`
        - `c = bits63..0(a * b)`  
          `cHigh = bit127..64(a * b)`
    - `a.multiply(UInt b, out UInt aHigh)`
        - `a = bits63..0(a * b)`  
          `aHigh = bit127..64(a * b)`
- Multiply-add with carry (high data, i.e. one UInt)
    - `UInt d = multiplyAdd(UInt a, UInt b, UInt c, out UInt dHigh)`
        - `d = bits63..0(a * b + c)`  
          `dHigh = bit127..64(a * b + c)`
    - `a.multiplyAdd(UInt b, UInt c, out UInt aHigh)`
        - `a = bits63..0(a * b + c)`  
          `aHigh = bit127..64(a * b + c)`         
- Shift
    - `b = shiftLeftAdd(UInt a, Int steps, inout UInt addAndHigh)`
    - `a.shiftLeftAdd(Int steps, inout UInt addAndHigh)`
    - `b = shiftOneLeft(UInt a, inout Bool carryFlag)`
    - `a.shiftOneLeft(inout carryFlag)`


### Saturation Arithmetic

`cilia::saturating::Int` behaves like `cilia::Int`, but applies saturation to all operations. Values are clamped to their minimum and maximum limits instead of wrapping around. This is typically implemented using SIMD, as many media/DSP instruction sets provide native support for saturation.  
See [https://en.wikipedia.org/wiki/Saturation_arithmetic](https://en.wikipedia.org/wiki/Saturation_arithmetic)
- `saturating::Int`
    - `saturating::Int8`/`Int16`/`Int32`/`Int64`
- `saturating::UInt`
    - `saturating::UInt8`/`UInt16`/`UInt32`/`UInt64`


### Reserved Keywords

Reserved keywords for _future_ use (maybe, maybe not).
- `parallel` for `parallel for ...`
- `interface` for pure abstract base classes or similar constructs?
- `struct` for some variant of C++ strcuts/classes?
- `Null` instead of `NullPtr`? (But actually it always is a pointer in our context.)
- `template`, as it still is unclear, if the "new", shorter template expressions are really better.
- `let` for `const` variable declarations?
- `constfunc` instead of `constexpr` or `consteval`?
- `module`
- `import`
- `export`
- `package`
- `match`
- `defer`
- `let`
- `mut`
- `override`
- `final`
- `sealed`
- `alias`


### Cilia Versioning

Versioning of the Cilia source code
- Via file ".cilVersion" in a (project) directory,
    - similar to ".clang_format",
    - also possible file by file: "Matrix.cilVersion" (for "Matrix.cil").
- Via file extension: 
    - "*.cil" – always the latest language version (if not overridden via ".cilVersion")
    - "*.25.cil" – version from the year 2025
    - "*.25b.cil" – second version from the year 2025


### Macros

No [function-like macros](https://www.geeksforgeeks.org/cpp-macros/), just basics like:
- `#define`
- `#if`
- `#else`
- `#endif`


### Optionals

```String? name = ...```  
translates to  
```Optional<String> name = ...```

#### Optional Member Access
- ```String? name = contactInfo?.name```  
  translates to  
  ```Optional<String> name = (contactInfo ? Optional((*contactInfo).name) : NullOpt)```
- ```String name = contactInfo?.name ?? ""```  
  translates to  
  ```String name = (contactInfo ? Optional((*contactInfo).name) : NullOpt).valueOr("")```

#### Optional Chaining
- ```Int? len = name?.length()```  
  translates to  
  ```Optional<Int> len = (name ? Optional((*name).length()) : NullOpt```
- ```Int len = name?.length() ?? 0```  
  translates to  
  ```Int len = (name ? Optional((*name).length()) : NullOpt).valueOr(0)```
    - ~~```Int len = name?.length()```~~ is not allowed, i.e. no implicit `.value()`, that could throw an exception.
- ```Bool? isJpeg = name?.endsWith(".jpeg")```  
  translates to  
  ```Optional<Bool> isJpeg = name ? Optional((*name).endsWith(".jpeg")) : NullOpt```
- ```Bool isJpeg = name?.endsWith(".jpeg") ?? false```  
  translates to  
  ```Bool isJpeg = (name ? Optional((*name).endsWith(".jpeg")) : NullOpt).valueOr(false)```
  
#### Optional Pointers
Plain `T*` as well as `T^`, `T+`, `T-` pointers can be used like an optional.

```Int? len = pointerToWindow?.title()?.length()```  
translates to  
```
Optional<String> __tmpTitle = pointerToWindow ?
  Optional((*pointerToWindow).title())
  :
  NullOpt

Optional<Int> len = __tmpTitle ?
  Optional((*__tmpTitle).length())
  :
  NullOpt
```

And while technically an `Optional<T>` is an object `T` plus a `Bool hasValue`, _for pointers_ `T*` the `Optional<T*>` is _just a pointer_, as a pointer can be null in itself:
- `Optional<T*>` internally is just a `T*`,
- `Optional<T^>` internally is just a `T^`,
- `Optional<T+>` internally is just a `T+`,
- `Optional<T->` internally is just a `T-`.

Therefore a `T*?`/`Optional<T*>` can be assigned to a plain `T*`, and you better use just that:
```
// Not this:
//T*? optionalPtrToContactInfo = user?.ptrToContactInfo
// But this:
T* ptrToContactInfo = user?.ptrToContactInfo

String realName = ptrToContactInfo?.name ?? ""
```

So in Cilia for a `T*?`/`Optional<T*>` that has a value, that value is never `NullPtr`. And when you assign `NullPtr` to a `T*?`/`Optional<T*> optionalPtr`, then `optionalPtr.hasValue()` returns `false`.  
This is different than in C++, so for interop with C++ you may need to use `std::optional<T*>` or `Optional<Optional<T*>>`.


### Anonymous Members
- You write
  ```
  class OkDialog : Window {
      Label("Message to user")
      Button("Ok")
  }
  ```
  instead of
  ```
  class OkDialog : Window {
      Label __anonymousLabel1("Message to user")
      Button __anonymousButton1("Ok")
  }
  ```
- Accessible only through static _reflection_ (C++26).
- Internally the compiler generates proxy names, e.g. `Label __anonymousLabel1` and `Button __anonymousButton1`.
- These widgets are member variables of the container, so they don't need to be deleted explicitly.
    - They are added with `container.addChild(Widget* child)`, signaling non-ownership.
    - Other children are added with `container.addChild(Widget+ child)`, using `Widget+`/`UniquePtr<Widget>` to signal ownership, i.e. the child is deleted when the container is deleted.
    - The container has two arrays:
        - `Array<Widget*> children` to manage all children (e.g. their order),
        - `Array<Widget+> ownedChildren` to manage those children that need to be deleted (in the destructor of the container).
- Maybe even
  ```
  class OkDialog : Window {
      Label("Message to user").horizontalAlignment(Alignment::Center)
      Button("Ok").onClick(&OkDialog::onOk)
  }
  ```
  instead of
  ```
  class OkDialog : Window {
      Label __anonymousLabel1("Message to user")
      Button __anonymousButton1("Ok")
      
      OkDialog() {
          __anonymousLabel1.horizontalAlignment(Alignment::Center)
          __anonymousButton1.onClick(&OkDialog::onOk)
      }
  }
  ```


### Anonymous Class Declarations

- You write
  ```
  VStack {
      Label("Message to user")
      Button("Ok")
  }
  ```
  instead of
  ```
  class __AnonymousVStack1 : VStack {
      Label("Message to user")
      Button("Ok")
  } __anonymousVStack1
  ```
- You write
  ```
  VStack {
      Label label("Message to user")
      Button okButton("Ok")
  } vertical
  ```
  instead of
  ```
  class __AnonymousVStack1 : VStack {
      Label label("Message to user")
      Button okButton("Ok")
  } vertical
  ```


### Late / Deferred Compiled Member Functions

For Compile Time Polymorphism, instead of CRTP (Curiously Recurring Template Pattern).
- You write
  ```
  class OkDialog : Window {
      Label("Message to user")
      Button("Ok")
  }
  ```
  based on
  ```
  class Window {
      Window() {
          registerWidgetMembers()
      }
      late virtual func registerWidgetMembers() {
          // Via static reflection:
          // Register all members of the derived class, that are derived from type Widget.
      }
  }
  ```
    - instead of
      ```
      class OkDialog : Window<OkDialog> {
          Label("Message to user")
          Button("Ok")
      }
      ```
      based on
      ```
      class Window<type T> {
          Window() {
              registerWidgetMembers<T>()
          }
          func registerWidgetMembers<type T>() {
              // Via static reflection:
              // Register all members of T, that are derived from type Widget.
          }
      }
      ```
