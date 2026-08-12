---
permalink: /comparison/swift/
description: "Swift equivalent of Cilia code. var/let, [String], Set, [String: ContactInfo]. Closest syntax match."
---

# Basic Lines of Code in Swift

- Types
    - `Int`, `Int32`, `Int64`, `Double`
- Variables
    - `var n: Int = 42`
    - `var n = 42`
    - `let n = 42`
    - `var words: [String] = []`
    - `var M = Matrix<Double>(1000, 2000, repeating: 0.0)`
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
