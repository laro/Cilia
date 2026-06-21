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

- ⊕, ⊖, ⊗, ⊘, ⊙, ⊛, ⊞, ⊟, ∪, ∩, ∖, ∈, ∉, ∋, ∌, ∧, ∨, ¬, ∷, ∶, ∝, ∼, ≈, ≉, ≠, ≤, ≥, ≪, ≫, ⊂, ⊃, ⊆, ⊇, ∅, ∇, ∂, ∞, ∑, ∏, ∫, ∮, ∵, ∴, ∗, ∘, ∙, ∟, ∥, ∦, ∠, ⟂, ≜, ≝, ≔, ≕
- Reserved for future use, as it could get complicated and confusing.
    - Especially to differentiate
        - operator precedence and
        - unary (prefix, postfix) or binary (infix) operators.
    - Many seem more suitable for a computer algebra system (CAS), not for a general purpose programming language.
- `|x|` for `abs(x)`?
    - `||x||` for `norm(x)`?
        - This would interfere with `||` as logical `or`.
    - This form is called as "enclosing operator", "delimited form", "bracketed expression", or informally as a paired prefix/postfix or "sandwich operator".
    - More variants?
        - `≪...≫`
        - `‹...›` , `«...»`
        - `⦅...⦆` , `〚...〛` , `⦃...⦄`
        - `（...）`, `［...］`, `｛...｝`, `｟...｠`
        - `「...」`, `『...』`, `〈...〉`, `《...》`, `【...】`, `〖...〗`, `〔...〕`, `〘...〙`, `⦗...⦘`
    - Some may be used in reversed order: `≫...≪`
    - Also see [Unicode Math Brackets](http://xahlee.info/comp/unicode_math_brackets.html)


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
