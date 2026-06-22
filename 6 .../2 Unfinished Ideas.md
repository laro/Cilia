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

### Vector / Matrix Operators

```
operator ×(Vec3 a, b) -> Vec3     { ... }   // cross product (beware of confusion with the letter 'x')
operator ⋅(Vec a, b) -> Float     { ... }   // dot / scalar / inner product

operator ⊙(Matrix a, b) -> Matrix { ... }   // Hadamard (element-wise) product
operator ⊘(Matrix a, b) -> Matrix { ... }   // Hadamard (element-wise) division
operator ⊞(Matrix a, b) -> Matrix { ... }   // element-wise addition ("boxplus")
operator ⊟(Matrix a, b) -> Matrix { ... }   // element-wise subtraction ("boxminus")

operator ⊕(Vec a, b) -> Vec       { ... }   // direct sum: {1 2} ⊕ {3 4} -> {1 2 3 4}
operator ⊖(Vec a) -> Vec          { ... }   // negation (unary)
operator ⊖(Vec a, b) -> Vec       { ... }   // subtraction (binary)
operator ⊛(Signal a, b) -> Signal { ... }   // convolution
operator ∗(Signal a, b) -> Signal { ... }   // convolution (alternative)

func ∠(Vec a, b) -> Float        { ... }  // angle between two vectors
func ∠(Point3D a, b, c) -> Float { ... }  // angle between three points (vectors ab and bc)

operator ⟂(Vec a, b) -> Bool { ... }   // perpendicular / orthogonal
operator ∥(Vec a, b) -> Bool  { ... }   // parallel to
operator ∦(Vec a, b) -> Bool  { ... }   // not parallel to
```

### Set Symbols

The set membership/subset symbols parse as relational operators, i.e. they inherit the (infix) fixity and precedence group of the comparison operators:
```
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

### Operator Precedence

The table sorts in **all currently known operators** from tightest to loosest binding:

| Precedence group | Operators | Fixity |
| --- | --- | --- |
| Postfix / call | `a()` `a[]` `a.b` `a++` `a--` | postfix |
| Prefix (unary, high) | `+a` `-a` `!` `not` `~` `++a` `--a` `√` `⊖` `¬` | prefix |
| `Power` | `^` | infix right |
| `Multiplication` | `*` `/` `%` `×` `⋅` `⊙` `⊘` `⊛` `∗` `&` | infix left |
| `Addition` | `+` `-` `⊞` `⊟` `⊕` `⊖` `\|` | infix left |
| `Shift` / `Rotation` | `<<` `>>` `<<<` `>>>` | infix left |
| `Range` | `..` `..<` | infix, non-associative |
| `Comparison` | `<` `>` `<=` `>=` `≤` `≥` `<=>` `∈` `∉` `∋` `∌` `⊆` `⊇` `⊂` `⊃` `⟂` `∥` `∦` | infix, non-associative |
| `Equality` | `==` `!=` `≠` | infix, non-associative |
| `LogicalAnd` | `&&` `and` `∧` | infix left |
| `LogicalXor` | `xor` `⊻` | infix left |
| `LogicalOr` | `\|\|` `or` `∨` | infix left |
| `Assignment` | `=` `+=` `-=` `*=` `/=` `%=` `<<=` `>>=` `<<<=` `>>>=` `&=` `\|=` `&&=` `\|\|=` | infix right |

- `⊖` is declared twice: once `prefix` (unary negation, Z. 98) and once `infix` (binary subtraction, Z. 99). Fixity is part of the signature, so the two forms are distinct (see next section).
- `×` and `⋅` share the `Multiplication` group and are left-associative, so `a × b ⋅ c` parses as `(a × b) ⋅ c` (the scalar triple product), which is the intended reading.
- The bitwise *symbols* `&` and `\|` follow Go's precedence: `&` binds like `*` (`Multiplication`), `\|` like `+` (`Addition`), so both bind **tighter** than `Comparison`/`Equality`. This avoids the well-known C/C++ pitfall where `x & mask == 0` parses as `x & (mask == 0)`; here it parses as the intended `(x & mask) == 0`.
- The word operators `and`/`or`/`xor` (and their Unicode synonyms `∧`/`∨`/`⊻`) keep their logical-level precedence whether applied to `Bool` or to integers; `nand`/`nor` (`⊼`/`⊽`) group with `and`/`or` respectively. Bitwise XOR therefore has no tight-binding ASCII symbol (`^` is `Power`) — use the word `xor` (at logical level) or parenthesize.
- The custom operators of the next section (`∘`, `⊗`, `∪`, `∩`, `∖`) introduce their own named groups (`Composition`, `Tensor`, `Union`, `Intersection`), whose position relative to the groups above is fixed at declaration.
- Cross-group ordering otherwise follows C++ (see the [Operators](/advanced/operators/) chapter), except the bitwise symbols `&`/`\|`, which follow Go (see above); per [Ideas from Others](/more/ideas-from-others/) this ordering may still be simplified.


### Custom Operators with Declared Precedence

For some symbols fixity and precedence have to be given at declaration. 

The two main difficulties (see also the [Operators](/advanced/operators/) chapter) are:
- operator precedence,
- unary (prefix, postfix) vs. binary (infix) operators.

Modelled after Swift/Haskell, preferably with _named_ precedence groups instead of magic numbers:
```
operator ∘(Fn f, g)     -> Fn     infix right precedence Composition   { ... }
operator ⊗(Matrix a, b) -> Matrix infix  left precedence Tensor        { ... }   // tensor / Kronecker product
operator ∪(Set a, b)    -> Set    infix  left precedence Union         { ... }   // union
operator ∩(Set a, b)    -> Set    infix  left precedence Intersection  { ... }   // intersection (binds tighter than ∪)
operator ∖(Set a, b)    -> Set    infix  left precedence Union         { ... }   // set difference: a without b
operator √(Float a)     -> Float  prefix                               { ... }   // unary
```
- Fixity (`prefix`/`infix`/`postfix`) is part of the signature, so unary and binary forms are distinct declarations (just like `-` in C++).
    - Only `infix` operators need an explicit precedence group; `prefix`/`postfix` operators have a fixed (high) precedence, which is why `√` above declares none.
- Allowed operator characters should be a curated whitelist (e.g. mathematical symbols U+2200–U+22FF plus some, e.g. `×` U+00D7, `⟂` U+27C2, `⟨ ⟩` U+27E8/9, `‖` U+2016), so the lexer can cleanly separate identifiers and operators.
- The whitelist should exclude (or the compiler should warn about) characters that are easily confused with ASCII operators or with each other, e.g. `∗` U+2217 vs. `*`, `∥` U+2225 vs. `||`, `⋅` U+22C5 vs. `.`, `∼` U+223C vs. `~` (see [Unicode TR39](https://www.unicode.org/reports/tr39/) confusables).


### Bracket / "Sandwich" Notation

`‖x‖`, `⟨a, b⟩` etc. are not infix operators but paired delimiters ("enclosing operator", "delimited form", "bracketed expression", informally "sandwich operator"). These should be a dedicated construct, _not_ `operator`:
```
bracket ‖Vec v‖ -> Float          { return v.length() }   // abs / norm
bracket ⟨T a, b⟩ -> Float         { ... }                // inner product
```
- `|x|` for `abs(x)` is problematic, as `|` is the bitwise `or` operator: an expression like `a | b | c` would be ambiguous (bitwise `or` vs. `a * |b| * c`).
    - So `‖x‖` (U+2016) might be the better choice for `abs(x)`, too.
- `‖x‖` (U+2016) for `norm(x)` instead of `||x||`, which would interfere with `||` as logical `or`.
- Symmetric delimiters that use the _same_ character for open and close (like `‖…‖`) cannot be nested unambiguously: `‖a + ‖b‖‖` has the same problem as `|a + |b||`. Only asymmetric pairs (e.g. `⟨…⟩`) nest cleanly, so `‖…‖` should be restricted to non-nested use (or nesting must be disallowed).
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
Remaining candidate symbols, not yet assigned to one of the cases above (with their usual mathematical meaning):

- Definition / assignment
    - `≔` "colon equals" (`:=`) – defined as / assignment.
    - `≕` "equals colon" (`=:`) – same, but reversed direction.
    - `≜` "delta equal to" – equal by definition.
    - `≝` "equal to by definition".
- Logic / proof notation
    - `∴` therefore.
    - `∵` because.
    - `∅` empty set.
    - `∞` infinity.
- Calculus
    - `∇` nabla / del – gradient, divergence, curl.
    - `∂` partial derivative.‚
- Geometry
    - `∟` right angle.
- Ratios / proportions
    - `∶` ratio (`a ∶ b`).
    - `∷` proportion (`a∶b ∷ c∶d`); beware: `::` is the scope operator in C++ & Cilia.
    - `∝` "proportional to" – `isProportional(a, b)`.
- Approximate comparison / similarity
    - `≈` "almost equal to" – `isClose(a, b)`.
    - `≉` "not almost equal to" – `not isClose(a, b)`.
    - `∼` "tilde operator" / "similar to" – `isSimilar(a, b)`.

- `∑`, `∏`, `∫`, `∮` are _not_ operators: they need an index/binder (e.g. `∑_{i=1}^{n}`), so for now they stay plain functions `sum(...)`, `product(...)`, `integrate(...)`.


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
