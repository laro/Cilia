---
permalink: /basics/variables/
order: 1
---

## Variable Declaration

`Int i` as variable declaration,  
very much as in C/C++ (and Java, C#).
```
TypeName variableName
```

Some simplifications and restrictions:
- The type definition is completely on the left-hand side,  
  i.e. before the variable name, also for arrays and bit fields.
- All variables in a multiple-variable declarations have to be of the exact same type.

### Examples
- `Int i`
- `Int i = 0`
- `Int x, y`
- `Int x = 99, y = 199`
- Arrays
    - `Int[10] highScoreTable`  // Array of ten integers (instead of ~~`Int highScoreTable[10]`~~)
- Multiple-variable declarations
    - `Float* m, n`        // m _and_ n are pointers (contrary to C/C++)
    - `Int& m = x, n = y`  // m _and_ n are references (contrary to C/C++)
    - `Float[2] p1, p2`    // p1 _and_ p2 are arrays of two Float values each
- Constructors
    - `Image image(width, height, 0.0)`
    - `Image image()`
        - is the same as `Image image`, i.e. it is a variable declaration,
        - a function declaration would be written as `func image() -> Image`.
- References
    - `Complex<Float>& complexNumber = complexNumberWithOtherName`

### Const
**`const`** always binds to the right (contrary to C/C++).  
- One can read `const int` as “a constant integer”.
- `const` binds more strongly than `*` and `&`, but less strongly than `[]`.
    - So the keyword `const` is always interpreted as a type qualifier to what appears immediately to its right,  
      what may be:
        - a type specifier (e.g. `Float`),
        - a pointer declarator (`*`), or
        - a type specifier with array declarator (`Float[]`, `Float[3]`, or `Float[String]`).
- `const` as a type qualifier for a reference (`&`) is not allowed, i.e. no ~~`Float const&`~~.
    - `const Float&` is allowed, of course.
- Examples:
    - `const Float* pointerToConstantFloat`
    - `const Float const* constantPointerToConstantFloat`
    - `Float const* constantPointerToMutableFloat`
- `const` as a type qualifier for an array declarator (`[]`):
    - `const Float[] constArrayOfFloat` is equivalent to `const Array<Float> constArrayOfFloat`.
        - `Float const[] constArrayOfFloat` is equivalent to `const Array<Float> constArrayOfFloat`, too.  
          Members of a const array are always effectively const anyway.
        - With the array declarator syntax (`[]`) it is _not_ possible to say `Array<const Float> arrayOfConstFloat`.  
          That does not compile in C++ anyway, because an array whose element type is non-assignable has no useful mutation model.
          (MSVC says 'The C++ Standard forbids containers of `const` elements because `allocator<const T>` is ill-formed.')
    - A `const` static array declarator `const Float[3]` is interpreted as a `const` static array of three `Float` (which effectively are `const`, too).
    - `const ContactInfo[String] constMapOfContactInfoByName` is equivalent to `const Map<String, ContactInfo> constMapOfContactInfoByName`.

### **Type Inference**
with `var` / `const`:
- `var i = 3` instead of ~~`auto i = 3;`~~
- `const i = 3` instead of ~~`const auto i = 3;`~~ (it is short, and `const var` / "constant variable" is a bit of a contradiction in terms.)

### Not Allowed
It is a syntax error to write:
- ~~`Float* m, &n`~~
    - Type variations within multiple-variable declarations are _not_ allowed.
    - It has to be the exact same type.
- ~~`Float*m`~~
    - Whitespace _between_ type specification and variable name is mandatory.
    - TODO Probably too difficult to realize, as the lexer already removes all whitespace.
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

### Bit Fields
- `UInt32:1 sign` instead of ~~`UInt32 sign : 1`~~.
- TODO Standardization of the bit field layout would be nice (LSB-first like on LittleEndian/Intel, or MSB-first like on BigEndian/Motorola),
    - but IMHO there is no clear/logical/right definition (especially with LittleEndian).
    - Dense packing of Int1, Int2, Int3, ..., Int64 could be more straightforward anyway.
