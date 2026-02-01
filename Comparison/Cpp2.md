---
title: Comparison.Cpp2
permalink: /comparison/cpp2/
order: 1
---

This is (should be) the exact equivalent of the [Cilia example](/comparison/cilia/#by-example) in Cpp2:

- `int`, `i32`, `i64`, `f32`
- `x: int = 42;`
- 
- `x := 42;`
- `x : const int = 42;`
- `words: vector<string>;`
- `names: set<string>;`
- `contactInfoForID: map<string, ContactInfo>;`
- `multiply: (a: int, b: int) -> int = a * b;`
- 
- `print: (a: ContactInfo) { ...; }`
- `concat: (a: string_view, b: string_view) -> String = ...;`
- `i := 1;  while i <= 10 next i++ { ...; }`
- 
- `i := 0;  while i < words.ssize() next i++ { ...; }`
- `for (5, 7, 11, 13) do (i) { ...; }`
- `for words do (word) { ...; }`
