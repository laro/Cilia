---
permalink: /comparison/carbon/
description: "Carbon equivalent of Cilia code. var/let, fn keyword, Array(String), HashMap. Google's C++ successor."
---

# Basic Lines of Code in Carbon

- Types
    - `i32`, `i64`, `f64`
- Variables
    - `var n: i64 = 42;`
    - `var n = 42;`
    - `let n = 42;`
    - `var words: Array(String);`
    - `var M: Matrix(f64) = Matrix(f64).Make(1000, 2000, 0.0);`
    - `var contactInfoForID: HashMap(String, ContactInfo);`
- Functions
    - `fn multiply(a: i64, b: i64) -> i64 { return a * b; }`
    - `fn print(a: ContactInfo) { ...; }`
    - <span class="wide">`fn concat(a: StringView, b: StringView) -> String { return ...; }`</span>
- Loops
    - `var i: i64 = 1;  while (i <= 10) { ...; ++i; }`
    - `var i: i64 = 0;  while (i < words.ssize()) { ...; ++i; }`
    - `for (i: i64 in (5, 7, 11, 13)) { ...; }`
    - `for (word: auto in words) { ...; }`

> **Note**  
> Is there really no range operator and no classical for-loop in Carbon?
