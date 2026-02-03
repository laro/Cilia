---
permalink: /comparison/swift/
order: 4
---

This is (should be) the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in Swift:

- Types
    - `Int`, `Int32`, `Int64`, `Float`
- Variables
    - `var x: Int = 42`
    - `var x = 42`
    - `let x = 42`
    - `var words: [String] = []`
    - `var names: Set<String> = Set()`
    - `var contactInfoForID: [String: ContactInfo] = [:]`
- Functions
    - `func multiply(_ a: Int, _ b: Int) -> Int { return a * b }`
    - `func print(_ a: ContactInfo) { ... }`
    - `func concat(_ a: String, _ b: String) -> String { return ... }`
- Loops
    - `for i in 1...10 { ... }`
    - `for i in 0..<words.count { ... }`
    - `for i in [5, 7, 11, 13] { ... }`
    - `for word in words { ... }`
