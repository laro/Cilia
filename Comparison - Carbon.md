---
title: Carbon
permalink: /comparison/carbon/
order: 2
parent: Comparison
---

This is the exact equivalent of the [Cilia example](/#by-example) in Carbon:

- [`Int`](https://bayramblog.medium.com/overview-of-the-carbon-language-part-1-1963e5640ff5), `i32`, `i64`, `f32`
- `var x: i64 = 42;`
    - `var x: auto = 42;`
    - `let x: auto = 42;`
    - `var words: Array(String);`
    - `var names: Set(String);`
    - `var contactInfoForID: HashMap(String, ContactInfo);`
- `fn multiply(a: i64, b: i64) -> i64 { return a * b; }`
    - `fn print(a: ContactInfo) { ...; }`
    - `fn concat(a: StringView, b: StringView) -> String { return a + b; }`
- `var i: i64 = 1;`  
  `while (i <= 10) { ...; ++i; }`
    - `var i: i64 = 0;`  
      `while (i < words.ssize()) { ...; ++i; } `          
    - `for (i: i64 in (5, 7, 11, 13)) { ...; }`
    - `for (word: auto in words) { ...; }`
