---
permalink: /advanced/operators/
description: "Cilia operators: a**b for pow, and/or/nand/nor/xor. Operator overloading, precedence, custom operators."
---

# Operators

## Power Function

**`a**x`** for `pow(a, x)` (as in Python), "raise a to the power of x".

`infix right` precedence (group `Power`), so `a**b**c` parses as `a**(b**c)`.


## Boolean and Bitwise Operators

No mixed types allowed (you need to explicitly cast one side instead).


### Logical (Bool) Operators

The word operators **`and`**, **`or`**, **`nand`**, **`nor`**, **`not`** are used on `Bool` (only), e.g.  `aBool`**`and`**`anotherBool` -> `Bool`.  

Words like `and` and `or` IMHO are a bit clearer than `&&` and `||`, so they are recommended.
And actually **`and`** / **`or`** are valid C++ keywords, too.

**`nand`** and **`nor`** (as in VHDL).

**`xor`** is a Bool operator, too (unlike C++, where it is a bitwise operator).

Still _also_ use **`&&`** and **`||`** for boolean operation,
- as C/C++/Java/C# programmers are used to it,
    - even [Swift](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/#Logical-Operators)
        and [Kotlin](https://www.w3schools.com/kotlin/kotlin_operators.php) keep `&&` and `||`,
- as we want `&&=` and `||=` anyway.

**`not`** in addition to `!` (for boolean negation), as `not` is a bit clearer than `!` (especially as many modern languages like Rust and Swift use `!` also for error handling).

Still _also_ `!` for negation, as we keep `!=` for "not equal" anyway. (We could use `<>` instead of `!=`, but that's really not familiar to C/C++ programmers.)

`and`/`or`/`nand`/`nor`/`not` are _not_ also used for bitwise operations, because bitwise operators bind more strongly than logical operators.

The keyword ~~`not_eq`~~ is not supported.


### Bitwise (Int) Operators

Use **`&`** / **`|`** for bitwise and / or, **`~`** for bitwise negation, and **`^`** for bitwise xor, all with tight binding.

Example:  
`anInt`**`&`**`anotherInt` -> `Int`. 

Also `&=`, `|=`, and `^=`.


The keywords ~~`bitand`~~, ~~`bitor`~~, ~~`compl`~~, ~~`and_eq`~~, ~~`or_eq`~~, ~~`xor_eq`~~ are not supported.


## Equality

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


## **Range Operator** `..` and `..<`

- `1..10` and `0..<10` are ranges
    - as in [Kotlin](https://kotlinlang.org/docs/ranges.html)
    - Similar, but different:
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


## Bit-Shift & Rotation

- `>>` Shift right
    - Logical shift with unsigned integers,
    - arithmetic shift with signed integers.
- `<<` Shift left
    - Here a logical shift left with unsigned integers is the same as an arithmetic shift left with signed integers.
- `>>>` Rotate right
    - Circular shift right,
    - only defined for unsigned integers,
    - and only for fixed size integers (i.e. not for `BigUInt`).
- `<<<` Rotate left
    - Circular shift left,
    - only defined for unsigned integers,
    - and only for fixed size integers (i.e. not for `BigUInt`).



## Operator Declaration

- Keyword **`operator`** instead of `func`.
- As with normal functions: Parameters are passed as `in` by default (i.e. `const T&` or `const T`).

### Assignment Operator
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

### Arithmetic Operators
```
operator (Int256 a) + (Int256 b) -> Int256 { ... }
operator (Int256 a) - (Int256 b) -> Int256 { ... }
operator (Int256 a) * (Int256 b) -> Int256 { ... }
operator (Int256 a) / (Int256 b) -> Int256 { ... }
operator (Int256 a) % (Int256 b) -> Int256 { ... }
```

### Shift and Rotate Operators
```
operator (Int256 a) << (Int shiftCount) -> Int256 { ... }
operator (Int256 a) >> (Int shiftCount) -> Int256 { ... }
operator (UInt256 a) <<< (Int shiftCount) -> UInt256 { ... }
operator (UInt256 a) >>> (Int shiftCount) -> UInt256 { ... }
```

### Compound Assignment Operators
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
    operator ^=(Int256 other) { ... }
}
class UInt256 {
    operator <<<=(Int shiftCount) { ... }
    operator >>>=(Int shiftCount) { ... }
}
```

### Increment and Decrement Operators
```
operator ++(Int256 x) -> Int256& { ... }   // pre-increment
operator (Int256 x)++ -> Int256  { ... }   // post-increment
operator --(Int256 x) -> Int256& { ... }   // pre-decrement
operator (Int256 x)-- -> Int256  { ... }   // post-decrement
```

### Relational and Comparison Operators
```
operator (Int256 a) == (Int256 b) -> Bool { ... }
operator (Int256 a) != (Int256 b) -> Bool { ... }
operator (Int256 a) < (Int256 b) -> Bool { ... }
operator (Int256 a) > (Int256 b) -> Bool { ... }
operator (Int256 a) <= (Int256 b) -> Bool { ... }
operator (Int256 a) >= (Int256 b) -> Bool { ... }
operator (Int256 a) <=> (Int256 b) -> Int { ... }

operator (Int256 a) ≠ (Int256 b) -> Bool { return a != b }
operator (Int256 a) ≤ (Int256 b) -> Bool { return a <= b }
operator (Int256 a) ≥ (Int256 b) -> Bool { return a >= b }
```

### Logical Operators
- Boolean operators
  ```
  operator (Bool a) and (Bool b) -> Bool { ... }
  operator (Bool a) or (Bool b) -> Bool { ... }
  operator (Bool a) nand (Bool b) -> Bool { ... }
  operator (Bool a) nor (Bool b) -> Bool { ... }
  operator (Bool a) xor (Bool b) -> Bool { ... }
  operator not(Bool a) -> Bool { ... }

  operator (Bool a) && (Bool b) -> Bool { return a and b }
  operator (Bool a) || (Bool b) -> Bool { return a or b }
  operator !(Bool a) -> Bool { return not a }
  
  operator (Bool a) ∧ (Bool b) -> Bool { return a and b }
  operator (Bool a) ∨ (Bool b) -> Bool { return a or b }
  operator (Bool a) ⊼ (Bool b) -> Bool { return a nand b }
  operator (Bool a) ⊽ (Bool b) -> Bool { return a nor b }
  operator (Bool a) ⊻ (Bool b) -> Bool { return a xor b }
  operator ¬(Bool a) -> Bool { return not a }
  ```
    - Defined for _`Bool`_ (not for integers),
    - operators `!`, not ~~`~`~~,
        - `&&` and `||`, not ~~`&` and `|`~~.
- Bitwise operators
  ```
  operator (Int256 a) & (Int256 b) -> Int256 { return a and b }
  operator (Int256 a) | (Int256 b) -> Int256 { return a or b }
  operator (Int256 a) ^ (Int256 b) -> Int256 { return a xor b }
  operator ~(Int256 a) -> Int256 { return not a }
  ```
    - Defined for _integers_ (not for `Bool`),
    - operators `~`, not ~~`!`~~,
        - `&`, `|` and `^`, not ~~`&&` and `||`~~.

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
