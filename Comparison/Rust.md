---
title: Comparison.Rust
permalink: /comparison/rust/
order: 3
---

This is (should be) the exact equivalent of the [Cilia example](/comparison/cilia/#by-example) in Rust:

- `isize`, `i32`, `i64`, `f32`
- 
- `let mut x: i64 = 42;`
- `let mut x = 42;`
- `let x = 42;`
- `let mut words: Vec<String> = Vec::new();`
- `let mut names: HashSet<String> = HashSet::new();`
- `let mut contactInfoForID: HashMap<String, ContactInfo> = HashMap::new();`
- 
- `fn multiply(a: i64, b: i64) -> i64 { return a * b; }`
- `fn print(a: &ContactInfo) { ...; }`
- `fn concat(a: &str, b: &str) -> String { return ...; }`
- 
- `for i in 1..=10 { ...; }`
- `for i in 0..words.len() { ...; }`
- `for i in [5, 7, 11, 13].iter() { ...; }`
- `for word in words.iter() { ...; }`

In Rust `42` is an `i32`, not an `i64`.  
That's Ok, this is a syntax comparison, not a performance benchmark.
