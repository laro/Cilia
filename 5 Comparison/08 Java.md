---
permalink: /comparison/java/
description: "Java equivalent of Cilia code. ArrayList, Matrix<double>, HashMap, var, static methods. JVM collections."
---

# Basic Lines of Code in Java

- Types
    - `int`, `long`, `double`
- Variables
    - `int n = 42;`
    - `var n = 42;`
    - `final var n = 42;`
    - `var words = new ArrayList<String>();`
    - `var mat = new Matrix<double>();`
    - `var contactInfoForID = new HashMap<String, ContactInfo>();`
- Functions
    - `static int multiply(int a, int b) { return a * b; }`
    - `static void print(ContactInfo a) { ... }`
    - `static String concat(String a, String b) { return ...; }`
- Loops
    - `for (int i = 1; i <= 10; ++i) { ... }`
    - `for (int i = 0; i < words.size(); ++i) { ... }`
    - `for (int i : List.of(5, 7, 11, 13)) { ... }`
    - `for (var word : words) { ... }`

> **Note**  
> In Java `int` and `42` are 32 bits wide, not 64 bits.  
