---
title: Comparison.Java
permalink: /comparison/java/
order: 6
---

This is (should be) the exact equivalent of the [Cilia example](/comparison/cilia/#by-example) in Java:

- `int`, `long`, `float`
- 
- `int x = 42;`
- `var x = 42;`
- `final var x = 42;`
- `var words = new ArrayList<String>();`
- `var names = new HashSet<String>();`
- `var contactInfoForID = new HashMap<String, ContactInfo>();`
- 
- `static int multiply(int a, int b) { return a * b; }`
- `static void print(ContactInfo a) { ... }`
- `static String concat(String a, String b) { return ...; }`
- 
- `for (int i = 1; i <= 10; ++i) { ... }`
- `for (int i = 0; i < words.size(); ++i) { ... }`
- `for (int i : List.of(5, 7, 11, 13)) { ... }`
- `for (var word : words) { ... }`

In Java `int` and `42` are 32 bit wide, not 64 bit.  
That's Ok, this is a syntax comparison, not a performance benchmark.
