---
permalink: /comparison/cilia/
description: "Cilia syntax by example: types, variables, functions, loops. Reference for comparison with other languages."
---

These are some basic lines of code in Cilia:

- Types
    - `Int`, `Int32`, `Int64`, `Float`
- Variables
    - `Int x = 42`
    - `var x = 42`
    - `const x = 42`
    - `String[] words`
    - `Set<String> names`
    - `ContactInfo[String] contactInfoForID`
- Functions
    - `func multiply(Int a, b) -> Int { return a * b }`
    - `func print(ContactInfo a) { ... }`
    - `func concat(String a, b) -> String { return ... }`
- Loops
    - `for i in 1..10 { ... }`
    - `for i in 0..<words.size() { ... }`
    - `for i in [5, 7, 11, 13] { ... }`
    - `for word in words { ... }`
