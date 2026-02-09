---
permalink: /basics/literals/
---

## Literals

### Bool
- `True`, `False` are `Bool`,
    - uppercase as they are constants (as in Python).

### Integer
- `123` is an integer literal of arbitrary precision
    - Typical integer literals like `123456` are interpreted as `Int`
        - in case of type inferring, parameter overloading and template matching.
    - Big integer literals are interpreted as `Int64`, `Int128`, `Int256`, `BigInt`, if required due to the size.
    - Positive integer literals up to a certain size can implicitly be used as `Int8`/`16`/`32`/`64`/`128`/`256` (i.e. signed), as there is no loss of information.
        - Up to `127` -> `Int8`
        - Up to `32'767` -> `Int16`
        - Up to `2'147'483'647` -> `Int32`
        - Up to `9'223'372'036'854'775'807` -> `Int64`/`Int`
        - Up to `170'141'183'460'469'231'731'687'303'715'884'105'727` -> `Int128`
        - Up to `57'896'044'618'658'097'711'785'492'504'343'953'926'634'992'332'820'282'019'728'792'003'956'564'819'967` -> `Int256`
    - Negative integer literals down to a certain size can implicitly be used as `Int8`/`16`/`32`/`64`/`128`/`256`, as there is no loss of information.
        - Down to `-128` -> `Int8`
        - Down to `-32'768` -> `Int16`
        - Down to `-2'147'483'648` -> `Int32`
        - Down to `-9'223'372'036'854'775'808` -> `Int64`/`Int`
        - Down to `-170'141'183'460'469'231'731'687'303'715'884'105'728` -> `Int128`
        - Down to `-57'896'044'618'658'097'711'785'492'504'343'953'926'634'992'332'820'282'019'728'792'003'956'564'819'968` -> `Int256`
    - Positive integer literals up to a certain size can implicitly be used as `UInt8`/`16`/`32`/`64`/`128`/`256`, as there is no loss of information.
        - Up to `255` -> `UInt8`
        - Up to `65'535` -> `UInt16`
        - Up to `4'294'967'295` -> `UInt32`
        - Up to `18'446'744'073'709'551'615` -> `UInt64`/`UInt`
        - Up to `340'282'366'920'938'463'463'374'607'431'768'211'455` -> `UInt128`
        - Up to `115'792'089'237'316'195'423'570'985'008'687'907'853'269'984'665'640'564'039'457'584'007'913'129'639'935` -> `UInt256`
    - Examples:
        - `Int8 a = 1`    // Works because `1` fits into `Int8`
        - `Int8 b = 127`  // Works because `127` fits into `Int8`
        - `Int8 c = 128`  // _Error_ because 128 does _not_ fit into `Int8`
        - `Int8 d = -128` // Works because `-128` fits into `Int8`
        - `Int8 e = -129` // _Error_ because `-129` does _not_ fit into `Int8`
        - `UInt8 f = 255` // Works because `255` fits into `UInt8`
        - `UInt8 g = 256` // _Error_ because `256` does _not_ fit into `UInt8`
        - `UInt8 h = -1`  // _Error_ because `-1` does _not_ fit into `UInt8`
        - `Int16 i = 32767` // Works
        - `Int32 j = 2'147'483'647` // Works
        - `Int64 k = 9'223'372'036'854'775'807` // Works
        - `Int l = a`     // Works because `Int8` fits into `Int32`
        - `UInt m = l`    // _Error_ because `Int` does _not always_ fit into `UInt`
            - `UInt m = UInt(l)` // Works
        - `Int n = m`     // Error because `UInt` does _not always_ fit into `Int`
            - `Int n = Int(m)`   // Works
    - Integer literals can automatically be converted to other sizes than `Int64`,
        - according to the C++ rules (admittedly without knowing the details),
        - but only if the converted-to-type can contain the value of the literal.
    - Difficult: Constexpr constructor that accepts an arbitrary precision integer literal and can store that in ROM
        - Store as array of `Int`/`UInt`
    - Suffixes/postfixes to write integer literals of a certain size:
        - `123u` is `UInt`
            - `-123u` is an error.
        - `123i8`, `123i16`, `123i32`, `123i64`,
        - `123u8`, `123u16`, `123u32`, `123u64` (as in Rust)
    - `-123` is always `Int` (signed)
- Hexadecimal, octal, and binary literals are UInt (i.e. unsigned)
    - Unsigned, as usually you want to describe flags, bit masks, hardware registers, hardware addresses, or color values, where signed integer doesn't fit.
        - As unsigned integer literals up to a certain size can implicitly be converted to Int (i.e. signed), _usually_ it is possible to give a hex literal as an Int argument
            - Up to `0x7f` -> `Int8`
            - Up to `0x7fff` -> `Int16`
            - Up to `0x7fffffff` -> `Int32`
            - Up to `0x7fffffffffffffff` -> `Int64`/`Int`
        - Otherwise you have to cast it like `Int mostNegativeInt = Int(0x8000000000000000)`.
    - `0xffffffff` is `UInt` in hexadecimal
    - `0b1011` is `UInt` in binary
    - `0o123` is `UInt` in octal
        - Using `0o` as in Python,
        - not `0123`, as that IMHO is confusing/unexpected, even though it is C++ standard.
- `Int` vs. `Bool`
    - ~~`Int a = True`~~      // Error,
        - because `Bool` is _not_ an `Int`
        - because a `Bool` should not be accidentally interpreted as an `Int`
        - cast if necessary: `Int a = Int(True)`
    - ~~`Bool a = 1`~~      // Error,
        - because `Int` is not a `Bool`
        - because an `Int` should not be accidentally interpreted as a `Bool`
        - cast if necessary: `Bool a = Bool(1)`

### Floating Point
- `1.0` is a floating point literal
    - Floating point literals are interpreted according to the size/precision requirements.
        - Counting the decimal places  
          (including the digits before the decimal point, the significant digits after the decimal point _and_ the trailing zeros!),  
          then the rules are:
            - up to 15 decimal places -> `Float64` (AKA `Float`)
            - up to 34 decimal places -> `Float128`
            - up to 71 decimal places -> `Float256`
            - more decimal places     -> `BigFloat`
                - Difficult: Constexpr constructor that accepts an arbitrary precision float literal and can store that in ROM
                    - Store the mantissa as arbitrary precision integer (i.e. array of `Int`), plus the exponent as arbitrary precision integer (i.e. array of `Int`, most always only a single `Int`)
        - So a plain float literal like `1.0` is a `Float` (AKA `Float64`). This way the precision is the same as in C++, but there `1.0` is called a `double` while `1.0f` is called a (single) `float`.
    - Can implicitly be converted to any smaller float type into which it still fits exactly,
        - otherwise explicit cast necessary: `Float16(3.1415926)`
        - Note: `0.1` as `Float64` has the significand `1001100110011001100110011001100110011001100110011010`, so _this can not_ implicitly be converted to `Float32` or `Float16`.
    - Postfixes to write float literals with a certain precision:  
      `0.1f16`, `0.1f32`, `0.1f64`, `0.1f128`, `0.1f256` (as in Rust)
        - That probably is clearer than ~~`0.1h`, `0.1s`, `0.1d`, `0.1q`, `0.1o`~~ for half, single, double, quadruple, octuple precision.
        - Use of ~~`0.1f`~~ for `Float` AKA `Float64` would be confusing, as in C++ `0.1f` means `single float` AKA `Float32`.
    - To ensure the literal has `Float128`/`Float256`/`BigFloat` precision you may add trailing zeros (`0.1000000000000000…`).
- `Infinity`/`-Infinity` is a `Float` literal for infinity values,
    - that can be converted to any float type.
- `NaN` is a `Float` literal for NaN ("not a number") values,
    - that can be converted to any float type.

### String
- `"Text"` is a `StringView` with UTF-8 encoding.
    - No null termination.
        - If necessary
            - use `"Text"sz`, `"Text\0"` or
            - convert using `StringZ("Text")`.
    - Data is typically stored in read-only data segments (".rodata") or ROM.
    - A Cilia-to-C++-transpiler would translate every string literal to a C++ string_view-literal:
        - `"Text"` -> `u8"Text"sv`
        - (`"Text"sv` as to avoid null termination, and `u8"Text"` as to have UTF-8 encoding.)
    - ~~A StringView starts like a String does: pointer to first character plus length,~~
        - ~~so slicing of String to StringView is possible.~~
        - TODO This would probably not work with small string optimization (SSO), so it is of limited use.

- Multiline String Literal
    - Use triple double-quotes `"""` to start and end the literal.
    - ```
      """
      First line
      Second line
      """
      ```
    - Similar to Swift, Julia, Java 15, C# 11, ...
    - Also as single line string literal with very few restrictions, good for RegEx
        - `"""(.* )whatever(.*)"""`
    - Opening Delimiter Rules
        - If the opening `"""` is followed by a newline, that newline is _not_ part of the string content.
        - This allows the content to start cleanly on the next line.
    - Closing Delimiter & Indentation (Strip-Logic)
        - The position of the closing `"""` defines the indentation guide.
        - If the closing `"""` is on its own line:  
            - The newline preceding it is removed from the content.
            - The exact sequence of whitespace (spaces/tabs) before the closing `"""` is treated as a "prefix" and is stripped from every line of the string.
        - Indentation Safety: It is a compile-time error if any non-empty line begins with less indentation than the closing delimiter.
    - Whitespace & Line Handling
        - Trailing Whitespace: Whitespace at the end of lines is preserved.
        - Blank Lines: Lines containing only whitespace that is shorter than the indentation guide are treated as empty lines (\n).
    - To include `"""` within the string content, the literal can be opened and closed with more than three double-quotes (e.g., `""""`).
        - The closing delimiter must match the number of quotes used for the opening delimiter.
        - This eliminates the need for escape backslashes within the literal, ensuring truly "raw" content.

- Interpolated Strings
    - `f"M[{i},{j}] = {M[i, j]}"`
        - like f-strings in Python.
    - Curly braces (`{}`) are used in std::format already.
    - `f"..."` as in `format`.
    - TODO Any reason to use/prefer any other syntax?
        - Maybe `$"M[{i},{j}] = {M[i, j]}"` like in C#?

- Alternative string literals
    - Prefixes
        - as in C++:
            - `u"..."` and `u'...'` for UTF-16
            - `U"..."` and `U'...'` for UTF-32
        - No ~~`u8"..."`~~ and no ~~`u8'...'`~~ for UTF-8, as that is the default in Cilia.
        - Maybe `a"..."` for ASCII and `l"..."` for Latin-1.
    - User defined string suffixes
        - as in C++:
            - `"..."s` for `std::string`.
        - No ~~`"..."sv`~~ for `std::string_view`, as that is the default in Cilia.
        - `"..."sz` for null terminated strings.
            - Type of `"..."sz` is `Char*`.
            - `"...\0"` is a StringView of a zero terminated string.
    - All these available for multiline string literals and interpolated strings, too.
        - TODO Any reason, not to?

### Char
- `' '` is a character literal.
    - `'A'` is an ASCII character literal, a `Char8` (can implicitly be converted to `Char16` and `Char32`).
    - `'Ä'` is a non-ASCII Latin-1 character literal, a `Char8` (can implicitly be converted to `Char16` and `Char32`).
    - `'Ω'` is a `Char16` character literal (can implicitly be converted to `Char32`).
    - `'𝄞'` is a `Char32` character literal.
    - `'👮🏻'` is an _invalid_ character literal, as grapheme clusters consist of multiple code points. Use the string literal `"👮🏻"` instead.

### Array
- `[1, 2, 3]` is an array (here an `Int[3]`),
    - all elements have the same type.
- `{1, "Text", 3.0}` is an initialization list,
    - e.g. for `Tuple` or `Pair`.
- `[ 1: "one", 2: "two", 3: "three", 4: "four" ]` is a `String[Int]` (AKA `Map<Int, String>`).
- ```
  String[Int] keywords = [
      1: "one"
      2: "two"
      3: "three"
      4: "four"
  ]
  ```
- ```
  ContactInfo[String] contactInfoForID = [
      "John Doe": {"John", "Doe", "03465 452634"}
      "Jane Doe": {"Jane", "Doe", "03245 687534"}
  ]
  ```

### Misc
- `NullPtr` is the null pointer,
    - it is of the type `NullPtrType`,
    - explicit cast necessary to convert any pointer to `Int`.
- User Defined Literals
    - The same rules as in C++.
