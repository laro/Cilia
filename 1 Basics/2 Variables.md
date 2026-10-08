---
permalink: /basics/variables/
description: "Cilia variable declaration: TypeName variableName syntax. Arrays as Int[10] or Int[], multiple variables of same type. Top-level objects are file-local unless declared global."
---

# Variable Declaration

`Int i` as variable declaration,  
very much as in C/C++ (and Java, C#).
```
TypeName variableName
```

Some simplifications and restrictions:
- The type definition is completely on the left-hand side,  
  i.e. before the variable name, also for arrays and bit fields.
- In a multiple-variable declaration
    - all variables must be of the exact same type,
    - either all variables are initialized or none are.


## Examples

- `Int i`
- `Int i = 0`
- `Int x, y`
- `Int x = 99, y = 199`
- `Complex<Float>& complexNumber = complexNumberWithOtherName`
- `Int[10] highScoreTable`  // Array of ten integers (instead of ~~`Int highScoreTable[10]`~~)
- Multiple-variable declarations (unlike C/C++)
    - `Float* m, n`        // m _and_ n are pointers
    - `Int& m = x, n = y`  // m _and_ n are references
    - `Float[2] p1, p2`    // p1 _and_ p2 are arrays of two Float values each
- Constructors
    - `Image image(width, height, 0.0)`
    - `Image image()`
        - is the same as `Image image`, i.e. it is a variable declaration,
        - a function declaration would be written as `func image() -> Image`.


## Type Inference

with `var` / `const`:
- `var i = 3` instead of ~~`auto i = 3;`~~
- `const i = 3` instead of ~~`const auto i = 3;`~~ (it is short, and `const var` / "constant variable" is a bit of a contradiction in terms.)


## Structured Binding

C++17 structured bindings unpack one value into several names: a pair, a tuple, an array, or an aggregate.  
`var` instead of ~~`auto`~~, and `{ }` instead of ~~`[ ]`~~:

- `var {a, b} = ...` instead of ~~`auto [a, b] = ...;`~~
- `for {a, b} in ... { ... }` instead of ~~`for (auto [a, b] : ...) { ... }`~~

The names are declared here, and each name's type is inferred from its element, as with `var`.  
A constant binding is `const {a, b} = ...`, instead of ~~`const auto [a, b] = ...;`~~ — the same idea as `const i = 3` above.

This is not a multiple-variable declaration (`Int x, y`).  
The names need not share one type — a `String` and an `Int` from one pair is fine — and there is exactly one name per element.

`{ }` rather than `[ ]`, because `[ ]` is already the array and map declarator (`Int[10]`, `Float[String]`).


## Const

**`const`** always binds to the right (contrary to C/C++).  
- One can read `const Int` as “a constant integer”.
- `const` binds more strongly than `*`, `&`, and `?`, but less strongly than `[]`.
    - So the keyword `const` is always interpreted as a type qualifier to what appears to its right, which can be:
        - a type specifier (e.g. `Float`),
        - a pointer declarator (`*`),
        - an optional declarator (`?`), or
        - a type specifier with array declarator (e.g. `Float[]`, `Float[3]`, or `Float[String]`).
- `const` as a type qualifier for a reference (`&`) is not allowed, i.e. no ~~`Float const&`~~.
    - `const Float&` is allowed, of course.
- Examples:
    - `const Float* pointerToConstantFloat`
    - `const Float const* constantPointerToConstantFloat`
    - `Float const* constantPointerToMutableFloat`
    - `const Float[] constArrayOfFloat`  
       is equivalent to `const Array<Float> constArrayOfFloat`.
        - `Float const[]` is the same.
        - Members of a `const` array are always effectively `const` anyway.
        - With the array declarator syntax (`[]`) it is _not_ possible to say `Array<const Float>`. But that does not compile anyway, because you can't assign values to an array whose element type is non-assignable.
    - `const Float[3] constArrayOfThreeFloat`  
      is a `const` static array of three `Float` (which effectively are `const`, too).
    - `const ContactInfo[String] constMapOfContactInfoByName`  
      is equivalent to `const Map<String, ContactInfo>`,
        - keys and values of a `const Map` are always `const`, too.


## Global Objects

Unlike functions, which are available in every `.cil` file of a project, a normal object at the top level of a `.cil` file is visible _only in that file_.
```
Int a
```

It is not visible in the other `.cil` files of the project.
This corresponds to `static Int a` in C/C++.

A top-level object becomes visible in the other `.cil` files of the project only when marked `global`:

```
global Int a
```

Only such a `global` declaration is known throughout the project.

> **Note**  
> Global state should generally be avoided, so the default – the simple expression – is 'file-local'.


## Bit Fields

- `UInt32:1 sign` instead of ~~`UInt32 sign : 1`~~.
- TODO Standardization of the bit field layout would be nice (LSB-first like on LittleEndian/Intel, or MSB-first like on BigEndian/Motorola),
    - but IMHO there is no clear/logical/right definition (especially with LittleEndian).
    - Dense packing of Int1, Int2, Int3, ..., Int64 could be more straightforward anyway.


## Not Allowed

It is a syntax error to write:
- ~~`Float* m, &n`~~
    - Type variations within multiple-variable declarations are _not_ allowed.
    - It has to be the exact same type.
    - Separate it:
      ```
      Float* m
      Float& n
      ```
- ~~`Int x, y = 0`~~
    - You need to initialize both variables: `Int x = 0, y = 0`
- ~~`Float*m`~~
    - Whitespace _between_ type specification and variable name is mandatory:  
    `Float* m`
- ~~`Image image { width, height, 0.0 }`~~
    - No uniform / brace initialization _for plain constructors_, as there is no need anymore.
        - There are generally _no_ implicit narrowing conversions, e.g.
            - not ~~`Int64` -> `Int32`~~,
            - not  ~~`Float64` -> `Float32`~~,
        - and _no_ other _unsafe_ integral promotions allowed:
            - ~~`Int` -> `UInt`~~,
            - ~~`UInt` -> `Int`~~
        - Nowhere, _not_ in
            - assignments,
            - function or constructor calls,
            - list initialization (with `{ }`),
            - arithmetic expressions (integral promotions),
            - mixed types in expressions,
            - enums, nor
            - return values.
        - The most vexing parse is mitigated with the keyword `func`.
        - Brace initialization only for constructors with `InitializerList<T>` as parameter (i.e. for "list-initialization" and "copy-list-initialization").
    - See [Misc](/cilia/misc/#misc) / Mixed arithmetic and [https://stackoverflow.com/a/18222927](https://stackoverflow.com/a/18222927)
    