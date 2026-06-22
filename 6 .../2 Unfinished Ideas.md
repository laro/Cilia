---
permalink: /more/unfinished-ideas/
description: "Cilia unfinished ideas: T^ for GC languages, interoperability with C#, Java, Objective-C/Swift."
---

# Unfinished Ideas

Admittedly, many ideas for Cilia are not yet _fully_ developed, but these really do need some more work.


## `T^` to Objects of Other Languages

We can redefine `T^` for interoperability with other languages, e.g. garbage collected languages like C# and Java.

`T^` is defined via type traits `SharedPtrType`:
- For all C++/Cilia classes `T^` is `SharedPtr<T>`:  
  ```
  extension<type T> T {
      using SharedPtrType = SharedPtr<T>
  }
  ```
- Objective-C/Swift classes use their reference counting mechanism:
  ```
  class ObjectiveCObject {
      using SharedPtrType = ObjectiveCRefCountPtr
  }
  ```
- C#/.NET classes use garbage collected memory for instance/object allocation, add instance/object-pointers to the global list of C#/.NET instance pointers (with GCHandle and/or gcroot).  
  ```
  class DotNetObject {
      using SharedPtrType = DotNetGCPtr
  }
  ```
    - Access/dereferencing creates a temporary `DotNetGCPinnedPtr`, that pins the object (so the garbage collector cannot move it during access).
- Java classes use garbage collected memory, add pointers to the global list of Java instance pointers.  
  ```
  class JavaObject {
      using SharedPtrType = JavaGCPtr
  }
  ```
    - Probably very similar to C#/.NET.

`T+` is defined via type traits `UniquePtrType`:
- For C++/Cilia classes `T+` is `UniquePtr<T>`:
  ```
  extension<type T> T {
      using UniquePtrType = UniquePtr<T>
  }
  ```
- For Objective-C/Swift, C#/.NET, and Java the `UniquePtrType` will be very similar to the `SharedPtrType`, maybe even identical.


## Exotic Operators (e.g. Unicode)

### Synonyms for Existing Operators or Functions

The Unicode character is just an alternative spelling, so no new parsing mechanism is needed.
```
// Comparison
operator ≤(Int256 a, b) -> Bool { return a <= b }
operator ≥(Int256 a, b) -> Bool { return a >= b }
operator ≠(Int256 a, b) -> Bool { return a != b }

// Logical / boolean
operator ∧(Bool a, b) -> Bool { return a and b }
operator ∨(Bool a, b) -> Bool { return a or b }
operator ¬(Bool a) -> Bool { return not a }            // unary

// Set membership
operator ∈(T x, Set<T> s) -> Bool { return s.contains(x) }
operator ∉(T x, Set<T> s) -> Bool { return not s.contains(x) }
operator ∋(Set<T> s, T x) -> Bool { return s.contains(x) }
operator ∌(Set<T> s, T x) -> Bool { return not s.contains(x) }

// Subset / superset
operator ⊆(Set<T> a, b) -> Bool { return a.isSubsetOf(b) }
operator ⊇(Set<T> a, b) -> Bool { return a.isSupersetOf(b) }
operator ⊂(Set<T> a, b) -> Bool { return a.isProperSubsetOf(b) }
operator ⊃(Set<T> a, b) -> Bool { return a.isProperSupersetOf(b) }
```

Maybe also this:
```
// Approximate comparison
operator ≈(Float a, b) -> Bool { return isClose(a, b) }
operator ≉(Float a, b) -> Bool { return not isClose(a, b) }
operator ∼(Float a, b) -> Bool { return isSimilar(a, b) }
operator ∝(Float a, b) -> Bool { return isProportional(a, b) }
```

### Custom Operators with Declared Precedence

For some symbols (e.g. `⊕ ⊗ ⊘ ∘ ∪ ∩ ∖`) fixity and
precedence have to be given at declaration. 

The two main difficulties (see also the [Operators](/advanced/operators/) chapter) are:
- operator precedence,
- unary (prefix, postfix) vs. binary (infix) operators, and
- bracket variants.

Modelled after Swift/Haskell, preferably with _named_ precedence groups instead of magic numbers:
```
operator ⊕(Vec a, b) -> Vec   infix left  precedence Additive     { ... }
operator ∘(Fn f, g) -> Fn     infix right precedence Composition  { ... }
operator ⊖(Vec a)    -> Vec   prefix                              { ... }   // unary
operator ⊖(Vec a, b) -> Vec   infix left  precedence Additive     { ... }   // binary
```
- Fixity (`prefix`/`infix`/`postfix`) is part of the signature, so unary and binary forms are distinct declarations (just like `-` in C++).
- Allowed operator characters should be a curated whitelist (e.g. mathematical symbols U+2200–U+22FF), so the lexer can cleanly separate identifiers and operators.


### Bracket / "Sandwich" Notation

`|x|`, `‖x‖`, `⟨a, b⟩` etc. are not infix operators but paired delimiters ("enclosing operator", "delimited form", "bracketed expression", informally "sandwich operator"). These should be a dedicated construct, _not_ `operator`:
```
bracket |…|    (Vec v) -> Float          { return v.length() }   // abs / norm
bracket ⟨…, …⟩ (T a, b) -> InnerProduct   { ... }
```
- `|x|` for `abs(x)` then collides with nothing, as it is a dedicated bracket type.
- `‖x‖` (U+2016) for `norm(x)` instead of `||x||`, which would interfere with `||` as logical `or`.
- More bracket variants:
    - `≪...≫`
    - `‹...›` , `«...»`
    - `⦅...⦆` , `〚...〛` , `⦃...⦄`
    - `（...）`, `［...］`, `｛...｝`, `｟...｠`
    - `「...」`, `『...』`, `〈...〉`, `《...》`, `【...】`, `〖...〗`, `〔...〕`, `〘...〙`, `⦗...⦘`
    - Some may be used in reversed order: `≫...≪`
    - Also see [Unicode Math Brackets](http://xahlee.info/comp/unicode_math_brackets.html)

### Later

Many of the symbols seem more suitable for a computer algebra system (CAS) than for a general purpose programming language, so they stay unassigned for now.

Reserved for future use, as it could get complicated and confusing.
Full list of candidate symbols, not yet assigned to one of the cases above:

- ⊕, ⊖, ⊗, ⊘, ⊙, ⊛, ⊞, ⊟, ∪, ∩, ∖, ∈, ∉, ∋, ∌, ∧, ∨, ¬, ∷, ∶, ∝, ∼, ≈, ≉, ≠, ≤, ≥, ≪, ≫, ⊂, ⊃, ⊆, ⊇, ∅, ∇, ∂, ∞, ∑, ∏, ∫, ∮, ∵, ∴, ∗, ∘, ∙, ∟, ∥, ∦, ∠, ⟂, ≜, ≝, ≔, ≕

- `∑`, `∏`, `∫`, `∮` are _not_ operators: they need an index/binder (e.g. `∑_{i=1}^{n}`),
  which is macro/CAS territory, so they stay plain functions `sum(...)`, `product(...)`, `integrate(...)`.


## OpenMP-like Parallel Programming

- Serial code
  ```
  Float[] arr = ...
  for i in 0..<arr.size() {
      arr[i] = 2 * arr[i]
  }
  ```
- Parallel code
  ```
  for i in 0..<arr.size() parallel { ... }
  ```
  ```
  for i in 0..<arr.size()
  parallel batch(1024) { ... }
  ```
  ```
  for i in 0..<arr.size()
  parallel if arr.size() > 65535 { ... }
  ```
  ```
  for i in 0..<arr.size() parallel reduce(sum: +) { ... }
  ```
  ```
  for i in 0..<arr.size()
  parallel
  if arr.size() > 65535
  reduce(sum: +)
  schedule(dynamic, 65536) { ... }
  ```

> TODO  
> Syntactically this is not a good solution.
> - We avoid brackets in `if` and `while`, but then use it for `reduce` and `schedule`...
> - Syntax should be better, clearer, or more powerful than plain OpenMP, otherwise better use just that.
