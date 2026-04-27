---
permalink: /comparison/swift/
description: "Swift equivalent of Cilia code. var/let, [String], Set, [String: ContactInfo]. Closest syntax match."
---

This is (should be) the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in Swift:

- Types
    - `Int`, `Int32`, `Int64`, `Float`
- Variables
    - `var n: Int = 42`
    - `var n = 42`
    - `let n = 42`
    - `var words: [String] = []`
    - `var names: Set<String> = Set()`
    - `var contactInfoForID: [String: ContactInfo] = [:]`
- Functions
    - `func multiply(_ a: Int, _ b: Int) -> Int { return a * b }`
    - `func print(_ a: ContactInfo) { ... }`
    - <span class="wide">`func concat(_ a: String, _ b: String) -> String { return ... }`</span>
- Loops
    - `for i in 1...10 { ... }`
    - `for i in 0..<words.count { ... }`
    - `for i in [5, 7, 11, 13] { ... }`
    - `for word in words { ... }`
