---
title: C++
permalink: /comparison/cpp/
order: 0
parent: Comparison
---

This is the exact equivalent of the [Cilia example](/#by-example) in C++:

- `int`, `int32_t`, `int64_t`, `float`
- `int x = 42;`
    - `auto x = 42;`
    - `const auto x = 42;`
    - `vector<string> words;`
    - `set<string> names;`
    - `map<string, ContactInfo> contactInfoForID;`
- `auto multiply(int a, int b) -> int { return a * b; }`
    - `auto print(const ContactInfo& a) { ...; }`
    - `auto concat(const string_view a, const string_view b) -> string { return a + b; }`
- `for (int i = 1; i <= 10; ++i) { ...; }`
    - `for (int i = 0; i < words.ssize(); ++i) { ...; }`
    - `for (int i : {5, 7, 11, 13}) { ...; }`
    - `for (const auto& word : words) { ... }`
