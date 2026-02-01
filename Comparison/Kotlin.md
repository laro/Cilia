---
title: Comparison.Kotlin
permalink: /comparison/kotlin/
order: 5
---

This is (should be) the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in Kotlin:

- `Int`, `Long`, `Float`
- 
- `var x: Int = 42`
- `var x = 42`
- `val x = 42`
- `var words: MutableList<String> = mutableListOf()` (an `Array` would have a fixed size)
- `var names: MutableSet<String> = mutableSetOf()`
- `var contactInfoForID: MutableMap<String, ContactInfo> = mutableMapOf()`
- 
- `fun multiply(a: Int, b: Int): Int { return a * b }`
- `fun print(a: ContactInfo) { ... }`
- `fun concat(a: String, b: String): String { return ... }`
- 
- `for (i in 1..10) { ... }`
- `for (i in 0 until words.size) { ... }`
- `for (i in listOf(5, 7, 11, 13)) { ... }`
- `for (word in words) { ... }`

In Kotlin `Int` and `42` are 32 bit wide, not 64 bits.  
That's Ok, this is a syntax comparison, not a performance benchmark.
