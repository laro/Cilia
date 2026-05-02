---
permalink: /comparison/odin/
description: "Odin equivalent of Cilia code: types, variables, procedures, loops. Dynamic arrays and maps."
---

This is (should be) the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in Odin:

- Types
    - `int`, `i32`, `i64`, `f32`
- Variables
    - `n: int = 42`
    - `n := 42`
    - `n :: 42`
    - `words: [dynamic]string`
    - `names := make(map[string]bool)`
    - `contactInfoForID := make(map[string]ContactInfo)`
- Functions
    - `multiply :: proc(a, b: int) -> int { return a * b }`
    - `print :: proc(a: ContactInfo) { ... }`
    - <span class="wide">`concat :: proc(a, b: string) -> string { return fmt.aprintf("%s%s", a, b) }`</span>
- Loops
    - `for i in 1..=10 { ... }`
    - `for i in 0..<len(words) { ... }`
    - `for i in []int{5, 7, 11, 13} { ... }`
    - `for word in words { ... }`

> **Note**  
> In Odin `::` declares a compile-time constant.  
> Odin does not have a built-in set type for arbitrary strings; a `map[string]bool` is the usual simple equivalent.  
> String concatenation is commonly done with the standard library, for example `core:fmt` or `core:strings`.
