---
title: Cilia.Operator Declaration
permalink: /cilia/operator-declaration/
order: 16
---

## Operator Declaration
- Keyword **`operator`** instead of `func`.
- As with normal functions: Parameters are passed as `in` by default (i.e. `const T&` or `const T`).
- Assignment operator
  ```
  class Int256 {
      operator =(Int256 other) { ... }
  }
  ```
    - No return of this-reference,
        - [as in Swift](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/),
        - so `if a = b { ... }` is _not_ accidentally allowed.
    - Move assignment
      ```
      class Int256 {
          operator =(move Int256 other) { ... }
      }
      ```
- Arithmetic operators
  ```
  operator +(Int256 a, b) -> Int256 { ... }
  operator -(Int256 a, b) -> Int256 { ... }
  operator *(Int256 a, b) -> Int256 { ... }
  operator /(Int256 a, b) -> Int256 { ... }
  operator %(Int256 a, b) -> Int256 { ... }
  ```
- Shift and rotate operators
  ```
  operator <<(Int256 a, Int shiftCount) -> Int256 { ... }
  operator >>(Int256 a, Int shiftCount) -> Int256 { ... }
  operator <<<(UInt256 a, Int shiftCount) -> UInt256 { ... }
  operator >>>(UInt256 a, Int shiftCount) -> UInt256 { ... }
  ```
- Compound assignment operators
  ```
  class Int256 {
      operator +=(Int256 other) { ... }
      operator -=(Int256 other) { ... }
      operator *=(Int256 other) { ... }
      operator /=(Int256 other) { ... }
      operator %=(Int256 other) { ... }
      operator <<=(Int shiftCount) { ... }
      operator >>=(Int shiftCount) { ... }
      operator &=(Int256 other) { ... }
      operator |=(Int256 other) { ... }
  }
  class UInt256 {
      operator <<<=(Int shiftCount) { ... }
      operator >>>=(Int shiftCount) { ... }
  }
  ```
    - Not ~~`operator ^=(Int256 other) { ... }`~~
- Increment and decrement operators
  ```
  class Int256 {
      operator ++() -> Int256& { ... }
      operator ++(Int dummy) -> Int256 { ... } // post-increment
      operator --() -> Int256& { ... }
      operator --(Int dummy) -> Int256 { ... } // post-decrement
  }
  ```
- Relational and comparison operators
  ```
  operator ==(Int256 a, b) -> Bool { ... }
  operator !=(Int256 a, b) -> Bool { ... }
  operator <(Int256 a, b) -> Bool { ... }
  operator >(Int256 a, b) -> Bool { ... }
  operator <=(Int256 a, b) -> Bool { ... }
  operator >=(Int256 a, b) -> Bool { ... }
  operator <=>(Int256 a, b) -> Int { ... }
  ```
- Logical operators
    - Boolean operators
      ```
      operator and(Bool a, b) -> Bool { ... }
      operator or(Bool a, b) -> Bool { ... }
      operator nand(Bool a, b) -> Bool { ... }
      operator nor(Bool a, b) -> Bool { ... }
      operator xor(Bool a, b) -> Bool { ... }
      operator not(Bool a) -> Bool { ... }
      operator &&(Bool a, b) -> Bool { return a and b }
      operator ||(Bool a, b) -> Bool { return a or b }
      operator !(Bool a) -> Bool { return not a }
      operator ∧(Bool a, b) -> Bool { return a and b }
      operator ∨(Bool a, b) -> Bool { return a or b }
      operator ⊼(Bool a, b) -> Bool { return a nand b }
      operator ⊽(Bool a, b) -> Bool { return a nor b }
      operator ⊻(Bool a, b) -> Bool { return a xor b }
      ```
        - Defined for _`Bool`_ (not for integers),
        - operators `!`, not ~~`~`~~,
            - `&&` and `||`, not ~~`&` and `|`~~.
    - Bitwise operators
      ```
      operator and(Int256 a, b) -> Int256 { ... }
      operator or(Int256 a, b) -> Int256 { ... }
      operator nand(Int256 a, b) -> Int256 { ... }
      operator nor(Int256 a, b) -> Int256 { ... }
      operator xor(Int256 a, b) -> Int256 { ... }
      operator not(Int256 a) -> Int256 { ... }
      operator &(Int256 a, b) -> Int256 { return a and b }
      operator |(Int256 a, b) -> Int256 { return a or b }
      operator ~(Int256 a) -> Int256 { return not a }
      operator ∧(Int256 a, b) -> Int256 { return a and b }
      operator ∨(Int256 a, b) -> Int256 { return a or b }
      operator ⊼(Int256 a, b) -> Int256 { return a nand b }
      operator ⊽(Int256 a, b) -> Int256 { return a nor b }
      operator ⊻(Int256 a, b) -> Int256 { return a xor b }
      ```
        - Defined for _integers_ (not for `Bool`),
        - operators `~`, not ~~`!`~~,
            - `&` and `|`, not ~~`&&` and `||`~~.
- Subscript/bracket/parenthesis/functor operators:
  ```
  class MyImage<type T> {
      // Array subscript
      operator [Int i] -> T& {
          return data[i]
      }

      // 2D array (i.e. image like) subscript
      operator [Int x, y] -> T& {
          return data[x + y*stride]
      }
      
      // Functor call
      operator (Int a, Float b, String c) {
          ...
      }
  }
  ```
- Exotic operators (e.g. Unicode)
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
