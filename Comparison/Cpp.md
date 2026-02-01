---
title: Comparison.C++
permalink: /comparison/cpp/
order: 0
---

This is (should be) the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in C++:

- `int`, `int32_t`, `int64_t`, `float`
- 
- `int x = 42;`
- `auto x = 42;`
- `const auto x = 42;`
- `vector<string> words;`
- `set<string> names;`
- `map<string, ContactInfo> contactInfoForID;`
- 
- `auto multiply(int a, int b) -> int { return a * b; }`
- `auto print(const ContactInfo& a) { ...; }`
- `auto concat(const string_view a, const string_view b) -> string { return ...; }`
- 
- `for (int i = 1; i <= 10; ++i) { ...; }`
- `for (int i = 0; i < words.ssize(); ++i) { ...; }`
- `for (int i : {5, 7, 11, 13}) { ...; }`
- `for (const auto& word : words) { ... }`

In C++ `int` and `42` are 32 bit wide, not 64 bit.  
That's Ok, this is a syntax comparison, not a performance benchmark.
