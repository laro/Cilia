---
permalink: /advanced/operators/
---

## Operators

### Power function
- **`a^x`** for `pow(a, x)` (as in Julia),
- "raise a to the power of x".

### Boolean operators
- **`and`**, **`or`**, **`nand`**, **`nor`**, **`xor`** in addition to `&&`/`&`, `||`/`|`, ...
    - similar to [Python](https://www.w3schools.com/python/python_operators.asp),
        [Carbon](https://www.naukri.com/code360/library/operators-and-precedence-in-carbon)
    - Used for both
        - boolean operation (when used on Bool)
            - `aBool`**`and`**`anotherBool` -> `Bool`
        - bitwise operation (when used on integers)
            - `anInt`**`and`**`anotherInt` -> `Int`
        - No mixed types allowed (you need to explicitly cast one side instead).
    - Words like `and` and `or` IMHO are a bit clearer than `&&`/`&` and `||`/`|`, so they are recommended.
    - Still _also_ use `&` and `|` for bitwise operation,
        - as C/C++/Java/C# programmers are used to it,
        - as we keep `&=` and `|=` anyway.
    - Still _also_ use `&&` and `||` for boolean operation,
        - as C/C++/Java/C# programmers are used to it,
            - even [Swift](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/#Logical-Operators)
                and [Kotlin](https://www.w3schools.com/kotlin/kotlin_operators.php) keep `&&` and `||`,
        - as we want `&&=` and `||=` anyway.
        - Defined on `Bool` only (_not_ on integers).
- **`not`** in addition to `!` (for boolean negation)
    - `not` is a bit clearer than `!` (especially as many modern languages like Rust and Swift use `!` also for error handling).
    - Still _also_ `!` for negation (in addition to `not`), as we keep `!=` for "not equal" anyways.  
        (We could use `<>` instead of `!=`, but that's really not familiar to C/C++ programmers.)
    - Still use `~` for bitwise negation,
        - as C/C++/Java/C# programmers are used to it,
        - as we keep `~T` for the destructor anyway.
- **`xor`** _instead_ of `^`  
    because we want `^` for the power function.

### Equality
- Default `operator==`
    - If not defined, then
        - use negated `operator!=` (if defined), or
        - use `operator<=>` (if defined), or
        - use elementwise comparison with `==`
            - Only possible if all elements themselves offer the `operator==`.
            - Optimization for simple types: Byte-by-byte comparison.
- Default `operator!=`
    - If not defined, then
        - use negated `operator==` (if defined), or
        - use `operator<=>` (if defined), or
        - use negated generated `operator==`.

### **Range operator** `..` and `..<`
- `1..10` and `0..<10` are ranges
    - as in [Kotlin](https://kotlinlang.org/docs/ranges.html)
    - Similar, but diffentent:
        - Swift would be ~~`1...10`~~ and ~~`0..<10`~~
        - Rust would be ~~`1..=10`~~ and ~~`0..10`~~
        - Cpp2 would be ~~`1..=10`~~ and ~~`0..<10`~~ (as of recently)
- Different kinds of ranges:
    - `1..3` – 1, 2, 3
        - `Range(1, 3)`
    - `0..<3` – 0, 1, 2
        - `RangeExclusiveEnd(0, 3)`
    - Range with step (especially to **iterate with the given step size in the `for` loop**)
        - `1..6:2` – 1, 3, 5
            - `RangeByStep(1, 6, 2)`
        - `0..<6:2` – 0, 2, 4
            - `RangeExclusiveEndByStep(0, 6, 2)`
    - Downwards iterating range (especially to **iterate downwards in the `for` loop**).  
        Step size is mandatory here (to make it clear that we are counting down, to avoid wrong conclusions).
        - `8..0:-1` – 8, 7, 6, 5, 4, 3, 2, 1, 0
            - `RangeByStep(8, 0, -1)`
            - Not ~~`8..0`~~, as `Range(8, 0)` is always empty (it is counting up, not down!)
            - Not `8..<0:-1`
                - With staticAssert in `RangeExclusiveEndByStep` that `step > 0`:  
                    "The range operator with exclusive end (`..<`) is not compatible with negative increments, because when counting downwards it would be necessary/logical to write `..>` and that is not available."
                - It simply would be too much, IMHO.
                - Use `8..1:-1` instead.
    - If both start and end of the range are compile time constants, then it may be warned when the range contains no elements at all (e.g. when `start >= end` with `step > 0`).
    - Incomplete ranges (need lower and/or upper bounds to be set before use)  
        - `..2` – ..., 1, 2
            - `RangeTo(2)`
        - `..<3` – ..., 1, 2
            - `RangeToExclusiveEnd(3)`
        - `0..` – 0, 1, 2, ...
            - `RangeFrom(0)`
        - `..`
            - `RangeFull()`
        - Incomplete range with step
            - `..2:2` – `RangeToByStep(2, 2)`
            - `..<3:2` – `RangeToExclusiveEndByStep(3, 2)`
            - `0..:2` – `RangeFromByStep(0, 2)`
            - `..:2` – `RangeFullByStep(2)`
    - See Rust [Ranges](https://doc.rust-lang.org/std/ops/index.html#structs) and [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)

### Bit-Shift & Rotation
- `>>` Shift right (logical shift with unsigned integers, arithmetic shift with signed integers)
- `<<` Shift left (here a logical shift left with unsigned integers is the same as an arithmetic shift left with signed integers)
- `>>>` Rotate right (circular shift right, only defined for unsigned integers)
- `<<<` Rotate left (circular shift left, only defined for unsigned integers)



## Operator Declaration

- Keyword **`operator`** instead of `func`.
- As with normal functions: Parameters are passed as `in` by default (i.e. `const T&` or `const T`).

### Assignment operator
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

### Arithmetic operators
```
operator +(Int256 a, b) -> Int256 { ... }
operator -(Int256 a, b) -> Int256 { ... }
operator *(Int256 a, b) -> Int256 { ... }
operator /(Int256 a, b) -> Int256 { ... }
operator %(Int256 a, b) -> Int256 { ... }
```

### Shift and rotate operators
```
operator <<(Int256 a, Int shiftCount) -> Int256 { ... }
operator >>(Int256 a, Int shiftCount) -> Int256 { ... }
operator <<<(UInt256 a, Int shiftCount) -> UInt256 { ... }
operator >>>(UInt256 a, Int shiftCount) -> UInt256 { ... }
```

### Compound assignment operators
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

### Increment and decrement operators
```
class Int256 {
    operator ++() -> Int256& { ... }
    operator ++(Int dummy) -> Int256 { ... } // post-increment
    operator --() -> Int256& { ... }
    operator --(Int dummy) -> Int256 { ... } // post-decrement
}
```

### Relational and comparison operators
```
operator ==(Int256 a, b) -> Bool { ... }
operator !=(Int256 a, b) -> Bool { ... }
operator <(Int256 a, b) -> Bool { ... }
operator >(Int256 a, b) -> Bool { ... }
operator <=(Int256 a, b) -> Bool { ... }
operator >=(Int256 a, b) -> Bool { ... }
operator <=>(Int256 a, b) -> Int { ... }
```

### Logical operators
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

### Subscript/Bracket Operator
```
class MyArray<type T> {
    // Array subscript
    operator [Int i] -> T& {
        return data[i]
    }
}
```
```
class MyImage<type T> {
    // 2D array (i.e. image like) subscript
    operator [Int x, y] -> T& {
        return data[x + y*stride]
    }
}
```

### Parenthesis/Functor Operator
```
class MyFunctor {
    // Functor call
    operator (Int a, Float b, String c) {
        ...
    }
}
```

### Exotic operators (e.g. Unicode)
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

