---
permalink: /comparison/carbon/
---

This is (should be) the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in Carbon:

- Types
    - `i32`, `i64`, `f32`
- Variables
    - `var x: i64 = 42;`
    - `var x: auto = 42;`
    - `let x: auto = 42;`
    - `var words: Array(String);`
    - `var names: Set(String);`
    - `var contactInfoForID: HashMap(String, ContactInfo);`
- Functions
    - `fn multiply(a: i64, b: i64) -> i64 { return a * b; }`
    - `fn print(a: ContactInfo) { ...; }`
    - `fn concat(a: StringView, b: StringView) -> String { return ...; }`
- Loops
    - `var i: i64 = 1;  while (i <= 10) { ...; ++i; }`
    - `var i: i64 = 0;  while (i < words.ssize()) { ...; ++i; }`
    - `for (i: i64 in (5, 7, 11, 13)) { ...; }`
    - `for (word: auto in words) { ...; }`

Is there really no range operator and no classical for-loop in Carbon?
