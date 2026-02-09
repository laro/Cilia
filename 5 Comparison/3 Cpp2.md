---
permalink: /comparison/cpp2/
---

This is (should be) the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in Cpp2:

- Types
    - `int`, `i32`, `i64`, `f32`
- Variables
    - `x: int = 42;`
    - `x := 42;`
    - `x : const int = 42;`
    - `words: vector<string> = ();`
    - `names: set<string> = ();`
    - `contactInfoForID: map<string, ContactInfo> = ();`
- Functions
    - `multiply: (a: int, b: int) -> int = a * b;`
    - `print: (a: ContactInfo) = { ...; }`
    - `concat: (a: string_view, b: string_view) -> string = ...;`
- Loops
    - `i := 1;  while i <= 10 next i++ { ...; }`
    - `i := 0;  while i < words.ssize() next i++ { ...; }`
    - `for (5, 7, 11, 13) do (i) { ...; }`
    - `for words do (word) { ...; }`

In Cpp2 `int` and `42` are typically 32 bit wide, not 64 bit.  
Is there really no range operator and no classical for-loop in Cpp2?
