---
permalink: /comparison/cpp/
---

This is (should be) the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in C++:

- Types
    - `int`, `int32_t`, `int64_t`, `float`
- Variables
    - `int x = 42;`
    - `auto x = 42;`
    - `const auto x = 42;`
    - `vector<string> words;`
    - `set<string> names;`
    - `map<string, ContactInfo> contactInfoForID;`
- Functions
    - `auto multiply(int a, int b) -> int { return a * b; }`
    - `auto print(const ContactInfo& a) { ...; }`
    - `auto concat(const string_view a, const string_view b) -> string { return ...; }`
- Loops
    - `for (int i = 1; i <= 10; ++i) { ...; }`
    - `for (size_t i = 0; i < words.size(); ++i) { ...; }`
    - `for (int i : {5, 7, 11, 13}) { ...; }`
    - `for (const auto& word : words) { ... }`

> **Note**  
> In C++ `int` and `42` are typically 32 bits wide, not 64 bits.  
