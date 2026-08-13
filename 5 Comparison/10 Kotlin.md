---
permalink: /comparison/kotlin/
description: "Kotlin equivalent of Cilia code. var/val, MutableList, mutableSetOf, mutableMapOf. JVM syntax."
---

# Basic Lines of Code in Kotlin

- Types
    - `Int`, `Long`, `Double`
- Variables
    - `var n: Int = 42`
    - `var n = 42`
    - `val n = 42`
    - `var words = ArrayList<String>()`
    - `var M = DoubleMatrix(1000, 2000, 0.0)`
    - <span class="wide">`var contactInfoForID: MutableMap<String, ContactInfo> = mutableMapOf()`</span>
- Functions
    - `fun multiply(a: Int, b: Int): Int { return a * b }`
    - `fun print(a: ContactInfo) { ... }`
    - `fun concat(a: String, b: String): String { return ... }`
- Loops
    - `for (i in 1..10) { ... }`
    - `for (i in 0 until words.size) { ... }`
    - `for (i in listOf(5, 7, 11, 13)) { ... }`
    - `for (word in words) { ... }`

> **Note**  
> In Kotlin `Int` and `42` are 32 bits wide, not 64 bits.  
> An `Array` has a fixed size, so we use `ArrayList` instead.
