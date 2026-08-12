---
permalink: /comparison/rust/
description: "Rust equivalent of Cilia code. let mut, Vec, Matrix, HashMap, fn. Ownership and borrowing syntax."
---

# Basic Lines of Code in Rust

- Types
    - `isize`, `i32`, `i64`, `f64`
- Variables
    - `let mut n: i64 = 42;`
    - `let mut n = 42;`
    - `let n = 42;`
    - `let mut words = Vec::<String>::new();`
    - `let mut mat = Matrix::<f64>::new(1000, 2000, 0.0);`
    - <span class="wide">`let mut contactInfoForID = HashMap::<String, ContactInfo>::new();`</span>
- Functions
    - `fn multiply(a: i64, b: i64) -> i64 { a * b }`
    - `fn print(a: &ContactInfo) { ...; }`
    - `fn concat(a: &str, b: &str) -> String { return ...; }`
- Loops
    - `for i in 1..=10 { ...; }`
    - `for i in 0..words.len() { ...; }`
    - `for i in [5, 7, 11, 13].iter() { ...; }`
    - `for word in words.iter() { ...; }`

> **Note**  
> In Rust `42` is an `i32`, not an `i64`.  
