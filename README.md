# Cilia
**C++ with Simplified Syntax**  
Many of C++'s shortcomings stem from the fact that it inherited from C or that backwards compatibility with existing code must be guaranteed.
Cilia can call into C++ (and vice versa), but is a separate language, so its _syntax_ does not need to be backwards compatible with C++.

**C++ with CamelCase Style**  
I'd like to have the standard library in the [style of Qt](https://wiki.qt.io/Qt_Coding_Style), and (a variant of) Qt with the standard library classes as base (but with exceptions, and with namespaces instead of the prefix "Q").


## By Example
Cilia is, in my opinion, a collection of quite obvious ideas (and mostly taken from other programming languages, of course):
- **Cilia**
    - `Int`, `Int32`, `Int64`, `Float`
    - `Int x = 42`
        - `var x = 42`
        - `const x = 42`
        - `String[] words`
        - `List<String> paragraphs`
        - `ContactInfo[String] contactInfoForID`
    - `func multiply(Int a, b) -> Int { return a * b }`
        - `func print(ContactInfo a) { ... }`
        - `func concat(String a, b) -> String { return a + b }`
    - `for i in 1..10 { ... }`
        - `for i in 0..<words.size() { ... }`
        - `for i in [5, 7, 11, 13] { ... }`
        - `for word in words { ... }`


## Comparison with C++, Cpp2, Carbon, and Rust
The follwing comparison aims to show the _exact_ equivalent in C++, Cpp2, Carbon, and Rust:
- **C++**
    - `int`, `int32_t`, `int64_t`, `float`
    - `int x = 42;`
        - `auto x = 42;`
        - `const auto x = 42;`
        - `vector<string> words;`
        - `list<string> paragraphs;`
        - `map<string, ContactInfo> contactInfoForID;`
    - `auto multiply(int a, int b) -> int { return a * b; }`
        - `auto print(const ContactInfo& a) { ...; }`
        - `auto concat(const string_view a, const string_view b) -> string { return a + b; }`
    - `for (int i = 1; i <= 10; ++i) { ...; }`
        - `for (int i = 0; i < words.ssize(); ++i) { ...; }`
        - `for (int i : {5, 7, 11, 13}) { ...; }`
        - `for (const auto& word : words) { ... }`
- **Cpp2**
    - `int`, `i32`, `i64`, `f32`
    - `x: int = 42;`
        - `x := 42;`
        - `x : const int = 42;`
        - `words: vector<string>;`
        - `paragraphs: list<string>;`
        - `contactInfoForID: map<string, ContactInfo>;`
    - `multiply: (a: int, b: int) -> int = a * b;`
        - `print: (a: ContactInfo) { ...; }`
        - `concat: (a: string_view, b: string_view) -> String = a + b;`
    - `i := 1;`  
      `while i <= 10 next i++ { ...; } `          
        - `i := 0;`  
          `while i < words.ssize() next i++ { ...; } `          
        - `for (5, 7, 11, 13) do (i) { ...; }`
        - `for words do (word) { ...; }`
- **Carbon**
    - [`Int`](https://bayramblog.medium.com/overview-of-the-carbon-language-part-1-1963e5640ff5), `i32`, `i64`, `f32`
    - `var x: i64 = 42;`
        - `var x: auto = 42;`
        - `let x: auto = 42;`
        - `var words: Array(String);`
        - `var paragraphs: List<String>;`
        - `var contactInfoForID: HashMap(String, ContactInfo);`
    - `fn multiply(a: i64, b: i64) -> i64 { return a * b; }`
        - `fn print(a: ContactInfo) { ...; }`
        - `fn concat(a: StringView, b: StringView) -> String { return a + b; }`
    - `var i: i64 = 1;`  
      `while (i <= 10) { ...; ++i; }`
        - `var i: i64 = 0;`  
          `while (i < words.ssize()) { ...; ++i; } `          
        - `for (i: i64 in (5, 7, 11, 13)) { ...; }`
        - `for (word: auto in words) { ...; }`
- **Rust**
    - `isize`, `i32`, `i64`, `f32`
    - `let mut x: i64 = 42;`
        - `let mut x = 42;` (actually, this is `i32`, but that's fine with me)
        - `let x = 42;`
        - `let mut words: Vec<String> = Vec::new();`
        - `let mut paragraphs: LinkedList<String> = LinkedList::new();`
        - `let mut contactInfoForID: HashMap<String, ContactInfo> = HasMap::new();`
    - `fn multiply(a: i64, b: i64) -> i64 { return a * b; }`
        - `fn print(a: &ContactInfo) { ...; }`
        - `fn concat(a: &str, b: &str) -> String { return a + b; }`
    - `for i in 1..=10 { ...; }`
        - `for i in 1..words.len() { ...; } `          
        - `for i in [5, 7, 11, 13].iter() { ...; }`
        - `for word in words.iter() { ...; }`

> [!NOTE]
> - I may not be very familiar with Cpp2, Carbon, or Rust or not up to date.
>     - Is there really no range operator and no classical for-loop in neither Cpp2 nor Carbon?
> - I may not be sufficiently up to date with C++14/17/20/23/26 either.

While Carbon and Cpp2 ("C++ syntax 2") are based on the same basic idea, a new syntax with C++ interoperability, they both have a syntax more resembling Rust than C++.  

[Someone said in an interview (back in 2000):](https://www.stroustrup.com/devXinterview.html)
> Today, I'd look for a much simpler syntax—and probably clash with people's confusion between the familiar and the simple.

I like many aspects, especially of Cpp2, but not the `name: Type` syntax. It indeed does not feel familiar to me, IMHO unnecessarily so. Cilia is a bit more conservative/traditional here. And I think its syntax is still "easy enough" to parse.


## Introduction
- Ideas / a wish list for an "improved" C++
    - with a **simplified** syntax,
    - in the **[style of Qt](https://wiki.qt.io/Qt_Coding_Style)** (roughly like Java, JavaScript, Kotlin, Swift)
    - Isomorphic mapping of all C++ functionality to Cilia possible
        - only with other/better/shorter "expression".
- C++ "Successor Language / Syntax"
     - similar to [CppFront/Cpp2](https://github.com/hsutter/cppfront#cppfront), [Carbon](https://github.com/carbon-language/carbon-lang), or [Circle](https://github.com/seanbaxter/circle).
     - Like the transitions from C to C++, Java to Kotlin, Objective-C to Swift, JavaScript to TypeScript
- Uses the same compiler backend as C++ (clang comes to mind)  
  with an own / a new compiler frontend.
    - Or a precompiler, like Cpp2, if that is significantly easier to do.
- So _no_ garbage collection,  
  instead in Cilia you use, as in C++:
    - automatic/stack variables,
    - **RAII** (Resource Acquisition is Initialization)
        - I'd like to call it "RROD" (Resource Release on Object Destruction)
    - shared pointers (`T^`).
- Why a new language, not extending C++?
    - The [CamelCase style](#style) could basically be archieved in C++, too
    - C++ could be extended by some features:
        - Aliasing of member names (functions and variables) seems necessary for having a CamelCase standard library, that is realized as a shallow wrapper for the C++ standard library (i.e. a translation layer).
    - Some parts are impossible or at least extremely unlikely, to include in a future C++ standard:
       - [Const reference as default type](#const-reference-as-default-type) for function arguments
       - [Fixing C++ "wrong defaults"](#interesting-ideas-from-other-languages)
           - Restricted integral promotions and implicit narrowing conversions, etc.
       - New array declaration (`Int[] array` instead of `Int array[]`)
       - [New/simplified keywords](#better-readable-keywords)
       - [No trailing semicolons](#No-trailing-semicolons)
- The names [D](https://dlang.org/), [C2](http://c2lang.org/), [C3](https://c3-lang.org), and [Cpp2](https://github.com/hsutter/cppfront#cppfront) were already taken,  
  as well as [Cone](https://cone.jondgoodwin.com/) and many others `¯\_(ツ)_/¯`.


## C++ Compatibility / Interoperability
- **Compatible to C++** and maybe other languages of this "**language family**" / "**ecosystem**",
    - as with
        - Java: Kotlin, Scala, Groovy, Clojure, Fantom, Ceylon, Jython, JRuby ...
        - C#: C++/CLI, Visual Basic .NET, F#, A# (Ada), IronPython, IronRuby ...
        - Objective-C: Swift
    - Bi-directional interoperability, so it is possible to include
        - C++ headers and modules from Cilia,
        - Cilia headers and modules from C++.
    - Can call C functions, access C structs (as C++ can do).
    - The compiler recognizes the language (C, C++, or Cilia) by
        - the file extension
            - Cilia: `*.cilia` `*.hilia`  &nbsp;  `*.cil` `*.hil`
            - C++: `*.cpp` `*.hpp` &nbsp; `*.cxx` `*.hxx` &nbsp; `*.h`
                - `*.h` is of course a problem, as the header could be C or C++ code.  
                  So use of `*.hpp` is recommended for C++ code.  
                  This can probably best be solved using path based rules.
            - C: `*.c` `*.h`
        - path based rules
            - to handle C or C++ standard headers in certain directories 
        - can be set in the IDE or on the command line
            - for each file individually 


## CamelCase Style
Roughly in the style of Qt, Java, JavaScript, TypeScript, Kotlin, Swift.

- All types and **classes in upper CamelCase**.
    - Basic/arithmetic types
        - `Bool`, `Int`, `Int64`, `UInt`, `BigInt`, `Float`, `Float64`, `BFloat16`, `BigFloat`
    - Cilia standard library
        - `String`, `Array`, `Map`, `ForwardList`, `UnorderedMap`, `ValueType`

- **Functions in lower camelCase**
    - `str.findFirstOf(...)`
    - `vec.pushBack(...)`
    - `Thread::hardwareConcurrency()`

- Variables/instances/objects in lower camelCase
    - `Int i`
    - `String word`
    - `String[] words`
    - `ContactInfo[String] contactInfoForID`
    - Feel free to bend/break this rule, e.g. name matrices as `Matrix M, R, L`
      
- Global constants in upper CamelCase
    - `Pi`, `Euler` (feel free to bend/break this rule, e.g. define a constant `const e = Euler`)
    - Constant-like keywords
        - `NullPtr`
        - `True`, `False`
        - `NaN`, `Infinity`
    - But keep _local_ constants in lower camelCase:  
        - `const Int lastIndex = 100` instead of ~~`const Int LastIndex = 100`~~

- Namespaces fully lowercase 
    - `cilia`
    - `cilia::lapack`
    - `cilia::geometry`
    - I don't think this is that important, but it helps to differentiate between classes and namespaces.


## No Trailing Semicolons
For better readability.  
When we are at it, after a quick look at Python, Kotlin, Swift, JavaScript, Julia.
- Typically a statement or expression ends with the end of a line.
- Multiline expressions:
    - Explicitly via `\` at end of line, or
    - up to closing of `(...)` or `[...]` (as in Python).
- Multiple expressions in a single line _are_ separated by semicolon.  
  `x += offset; y += offset`
- Disadvantages:
    - Errors are less easily recognized (Walter Bright / D: „Redundancy helps“)
    - Probably a completely new parser must be written, as the one from clang (for C++) no longer fits at all.
- Only in REPL:
    - Trailing semicolon used to suppress evaluation output,  
      as in Matlab, Python, Julia.
    - See [cling](https://root.cern/cling/)


## Basic / Arithmetic Types
- `Bool`
    - not ~~`bool`~~ nor ~~`Boolean`~~
- `Int`, `UInt`
    - `Int` == `Int64`
        - `Int` == `Int32` on 32 bit systems only (i.e. old/small platforms).
        - _No_ ~~`Size`~~ or ~~`SSize`~~, use `Int` instead.
    - `Int8`, `Int16`, `Int32`, `Int64`
    - `UInt8`, `UInt16`, `UInt32`, `UInt64`
- `Byte` == `UInt8` (Alias, i.e. the same type for parameter overloading)
- `Float`
    - `Float` == `Float32`
        - Among other things because this is how it works in C/C++.
        - Is faster than Float64 and good enough most of the time.
    - `Float16`, `Float32`, `Float64` (half, single, double precision floating point)


## Variable Declaration
`Int i` as variable declaration, very much as in C/C++, plus some simplifications/restrictions.
- Examples:
    - `Int i`
    - `Int i = 0`
    - `Int x, y`
    - `Int x = 99, y = 199`
    - **`Float* m, n`   // m _and_ n are pointers** (contrary to C/C++)
    - `const Complex<Float>& complexNumber = complexNumberWithOtherName`
    - `const Float* pointerToConstantFloat`
    - `const Float const* constPointerToConstantFloat`
- Not allowed / a syntax error is:
    - ~~`Float* m, &n`~~
        - Type variations within multiple-variable declarations are _not_ allowed.
        - It has to be the exact same type.
    - ~~`Float*m`~~
        - Whitespace _between_ type specification and variable name is mandatory.
- **Type inference** with `var` / `const`:
    - `var i = 3` instead of ~~`auto i = 3;`~~
    - `const i = 3` instead of ~~`const auto i = 3;`~~ (`const var` would be a contradiction in terms, as there is no such thing as a "constant variable".)


## Classes
- Quite as in C++
  ```
  class MyVectorOfInt {
  public:
      Int* numbers = NullPtr
      Int size = 0
  }
  ```
- Not ~~`struct`~~, as it is just too similar to `class` with no real benefit.
   - Keep as a reserved keyword for future use.


## Functions
```
func multiplyAdd(Int x, y, Float z) -> Float {
    return x * y  +  z
}
```
- Function declarations start with the keyword `func`,
    - as in Swift.
    - Easier parsing due to clear distinction between function vs. variable declaration.
- Always and only in the trailing return type syntax.
- `func multiply(`**`Int x, y`**`) -> Int` // x _and_ y are Int
- **Lambdas**
    - `[](Int i) -> Float { i * 3.14 }`  
      as in C++
- **Extension methods**
    - To add "member like" functions to "third party" classes/types.
    - Can be called like normal member functions, but they but do not have access to private or protected members themselves.
    - Also possible for basic/arithmetic types, e.g.:  
      `Int i`  
      `i.toString()`  
      based on  
      `func Int::toString() -> String { ... }`  // as in Kotlin
- **`constexpr`** and `consteval`
  ```
  constexpr multiply(Int x, y) -> Int {
      return x * y
  }
  consteval multiply(Int x, y) -> Int {
      return x * y
  }
  ```
- **Function pointers**
    - Difficult to maintain consistency between declarations of functions, function pointers, functors and lambdas.
    - Examples:
        - **`func(Int, Int -> Int)* pointerToFunctionOfIntAndIntToInt`**
        - **`func(Int)* pointerToFunctionOfInt`**
        - `func(Int, Int -> Int)& referenceToFunctionOfIntAndIntToInt` // Can't be zero; is that useful?
        - `func(Int)& referenceToFunctionOfInt`

          
## Operators
- Power function
    - **`a^x`** for `pow(a, x)` (as in Julia)
- Boolean operators
    - **`and`**, **`or`**, **`xor`** instead of `&&`/`&`, `||`/`|`, `!=`/`^`
        - as in Python, Carbon
        - Used for both
            - boolean operation
                - `aBool`**`and`**`anotherBool` -> `Bool`
            - bitwise operation
                - `anInt`**`and`**`anotherInt` -> `Int`
    - **`not`** in addition to `!`
        - `not` is a bit clearer than `!` (especially as many modern languages like Rust and Swift use `!` also for error handling).
        - Both `!` and `not` for negation, as we keep `!=` for "not equal" anyways.  
          (We could use `<>` instead of `!=`, but that's really not familiar to C/C++ programmers.)
- Equality
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
- **Range operator** `..` and `..<`
    - `1..10` and `0..<10` are ranges
        - as in Kotlin
        - Similar, but diffentent:
            - Swift would be ~~`1...10`~~ and ~~`0..<10`~~
            - Rust would be ~~`1..=10`~~ and ~~`0..10`~~
    - Different kinds of ranges:
        - `1..3` – 1, 2, 3
            - Range(1, 3)
        - `0..<3` – 0, 1, 2
            - RangeExclusiveEnd(0, 3)
        - Range with step (especially to **iterate with the given step size in the `for` loop**)
            - `1..6:2` – 1, 3, 5
                - RangeByStep(1, 3, 2)
            - `0..<6:2` – 0, 2, 4
                - RangeExclusiveEndByStep(0, 3, 2)
        - Downwards iterating range (especially to **iterate downwards in the `for` loop**).  
          Step size is mandatory (to make it clear that we are counting down, to avoid wrong conclusions).
            - `8..0:-1` – 8, 7, 6, 5, 4, 3, 2, 1, 0
                - RangeByStep(8, 0, -1)
                - Not ~~`8..0`~~, as Range(8, 0) is always empty!
            - `8>..0:-1` – 7, 6, 5, 4, 3, 2, 1, 0
                - RangeExclusiveStartByStep(8, 0, -1)
            - `8..>0:-1` – 8, 7, 6, 5, 4, 3, 2, 1
                - RangeExclusiveEndByStep(8, 0, -1)
            - `8>..0:-3` – 5, 2
                - RangeExclusiveStartByStep(8, 0, -3)
        - If both start and end of the range are compile time constants, then it may be warned when the range contains no elements at all (e.g. when `start >= end` with `step > 0`).
        - Incomplete ranges (need lower and/or upper bounds to be set before use)  
            - `..2` – ..., 1, 2
                - RangeTo(2)
            - `..<3` – ..., 1, 2
                - RangeToExclusiveEnd(3)
            - `0..` – 0, 1, 2, ...
                - RangeFrom(0)
            - `..`
                - RangeFull()
            - Incomplete range with step
                - `..2:2` – RangeToByStep(2, 2)
                - `..<3:2` – RangeToExclusiveEndByStep(3, 2)
                - `0..:2` – RangeFromByStep(0, 2)
                - `8>..:-1` – RangeFromExclusiveStartByStep(8, -1)
                - `8>..:-2` – RangeFromExclusiveStartByStep(8, -2)
                - `..:2` – RangeFullByStep(2)
        - See Rust [Ranges](https://doc.rust-lang.org/std/ops/index.html#structs) and [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- Bit-Shift & Rotation
    - `>>` Shift right (logical shift with UInt, arithmetic shift with Int)
    - `<<` Shift left (here a logical shift with UInt is the same as arithmetic shift with Int)
    - `>>>` Rotate right (circular shift right)
    - `<<<` Rotate left (circular shift left)


## Branches & Loops
No braces around the condition clause.
- **if**
    - ```
      if a > b {
          // ...
      }
      ```
    - ```
      if a > b {
          // ...
      } else {
          // ...
      }
      ```
    - ```
      if a > b {
          // ...
      } else if a > c {
          // ...
      } else {
          // ...
      }
      ```
    - `if 1 <= x <= 10 { ... }`
        - chained comparison as in Cpp2 (Herb Sutter), Python, Julia
- **while**
  ```
  while a > b {
      // ...
  }
  ```
- **do-while**
  ```
  do {
      // ...
  } while a > b
  ```
- **for-in**
    - as in Swift, Rust
    - Write
      ```
      for str in ["a", "b", "c"] {
          // ...
      }
      ```
      instead of `for (... : ...)` (AKA range-for in C++, `for each` in C++/CLI, `foreach` in C#)
    - Use the **range operator** to write          
        - `for i in 1..10 { ... }`  
          instead of ~~`for (Int i = 1; i <= 10; ++i) { ... }`~~,  
          translates to `for i in Range(1, 10) { ... }`.
        - `for i in 0..<10 { ... }`  
          instead of ~~`for (Int i = 0; i < 10; ++i) { ... }`~~,  
          translates to `for i in RangeExclusiveEnd(0, 10) { ... }`.
        - `for i in 10..1:-1 { ... }`  
          instead of ~~`for (Int i = 10; i >= 1; --i) { ... }`~~,  
          translates to `for i in RangeByStep(10, 1, -1) { ... }`.
        - I find this for-loop-syntax so tempting that I accept the somewhat complex details of the range operator (with all its variants).
    - The loop variable is declared "with the loop", with its type inferred from the range, array, etc. used (similar to `var` but with `in` (the default), `inout`, `copy`, `move`),  
      so `for i in 0..<10 { ... }` is equivalent to:
      ```
      {
          var i = 0
          while i < 10 {
              ...
              ++i
          }
      }
      ```
    - In general you can replace the (overly) powerful C/C++ for-loop like
      ```
      for (<Initialization>; <Condition>; <Increment>) {
          <Body>
      }  
      ```
      with a while-loop:
      ```
      {
          <Initialization>
          while <Condition> {
              <Body>
              <Increment>
          }
      }
      ```
- **switch/case** with `fallthrough` instead of ~~`break`~~
    - ```
      switch i {
      case 0:
          print("0")
          // implicit break
      
      case 1:
          print("1")
      
      case 2:      
          fallthrough
      case 3:
          print("2 or 3")
      
      default:
          print("default")
      }
      ```


## (Smart) Pointers
- **Short Smart Pointer Syntax**
    - “Make simple things simple”,  
      encourage use of smart pointers.
    - **`Type+ pointer`**
        - `T+` is short for **`UniquePtr<T>`**
    - **`Type^ pointer`**
        - `T^` is short for **`SharedPtr<T>`**
        - Inspired by C++/CLI (so its a proven possiblilty),  
          Sean Baxter is also using `T^` for Rust-style references in Circle (so there may be a conflict in the future).
        - _But_ there is an inconsistency in its usage:
            - A normal pointer `T* pointer` is dereferenced with `*pointer`.
            - A smart pointer `T^ pointer` is dereferenced also with `*pointer` (not `^pointer`).
- **`new T` returns a `T+`/`UniquePtr<T>`**,
    - so `T+`/`UniquePtr<T>` is the "default type" for pointers,
    - e.g. `ContactInfo+ contactInfoUniquePtr = new ContactInfo`.
    - `T^`/`SharedPtr<T>` can take over the pointer from rvalue `T+`/`UniquePtr<T>` (as in C/C++).
        - `ContactInfo^ contactInfoSharedPtr = new ContactInfo`
        - `ContactInfo^ contactInfoSharedPtr = move(contactInfoUniquePtr)`
            - The `contactInfoUniquePtr` is a `NullPtr` afterwards.
    - TODO Is array-to-pointer decay possible with `UniquePtr`?
        - `Int+ array = new Int[3]`
- A classical C/C++ "raw" pointer is still possible, but inconvenient to use.
    - `ContactInfo* contactInfoPtr = (new ContactInfo).release()`  
      `delete contactInfoPtr`
- Redefine `T^` and `T+` for special cases / **interoperability with other languages**:
    - `T^` is defined via type traits `SharedPtrType`,  
        - For C++/Cilia classes `T^` is `SharedPtr<T>`:
            - `using<type T> T::SharedPtrType = SharedPtr<T>`
        - Objective-C/Swift classes use their reference counting mechanism:
            - `using ObjectiveCObject::SmartPtrType = ObjectiveCRefCountPtr`
        - C#/.NET classes use garbage collected memory for instance/object allocation, add instance/object-pointers to the global list of C#/.NET instance pointers (with GCHandle and/or gcroot).   
            - `using DotNetObject::SmartPtrType = DotNetGCPtr`
            - Access/dereferencing creates a temporary `DotNetGCPinnedPtr`, that pins the object (so the garbage collector cannot move it during access).
        - Java classes use garbage collected memory, add pointers to the global list of Java instance pointers.  
            - `using JavaObject::SmartPtrType = JavaGCPtr`
            - Probably very similar to C#/.NET.
    - `T+` is defined via type traits `UniquePtrType`.
        - For C++/Cilia classes `T+` is `UniquePtr<T>`:
            - `using<type T> T::UniquePtrType = UniquePtr<T>`


## Templates
The basic new idea is, to define templates (classes and functions) mostly the same as they are used.
- **Class** templates  
  The template parameters (`<...>`) are given after the class name, so that the definition is similar to the usage (in a variable declaration).
  ```
  class MyVector<Number T> {
      T* numbers = NullPtr
      Int size = 0
  }
  ```
    - Template specialization
      ```
      class MyUniquePtr<type T> {
          ... destructor calls delete ...
      }
      class MyUniquePtr<type T[Int N]> {
          ... destructor calls delete[] ...
      }
      ```
    - Partial template specialization
      ```
      class KeyValuePair<type TKey, type TValue> {
          ...
      }
      class KeyValuePair<int, type TValue> {
          ...
      }
      class KeyValuePair<type TKey, String> {
          ...
      }
      ```
- **Function** templates
    - _Automatic_ function templates
        - If (at least) one of the function arguments is a concept, then the function is (in fact) a function template.
            - Concept `Number`:
              ```
              func sq(Number x) -> Number {
                   return x * x
              }
              ```
                - However, the return type could be a _different_ type than `x` is (but it needs to satisfy the concept `Number`)
                - With `func add(Number a, b) -> Number` even `a` and `b` could be of a different type (but both need to satisfy the concept `Number`)
            - Concept `Real` (real numbers as `Float16`/`32`/`64`/`128` or `BigFloat`):
              ```
              func sqrt(Real x) -> Real {
                  // ... a series development ...
                  // (with number of iterations determined from the size of the mantissa)
              }
              ```
        - Like abbreviated function templates in C++ 20, only without `auto`.
    - _Explicit_ function templates for cases where a common type is required.  
        - The template parameters (`<...>`) are given after the function name, so that the function definition is similar to the function call.
          ```
          func add<Number T>(T x, y) -> T {
               return x + y
          }
          ```
    - For extension function templates it is necessary to know the _type_-specific template parameter(s) even before we write the function name, where the function-specific template parameters are given.  
      Therefore we write
        - `func<type T, Int N> T[N]::size() -> Int { return N }`
        - `func<type T, Int N> T[N]::convertTo<type TOut>() -> TOut[N] { ... }`  
            - Not ~~`func T[N]::convertTo<type T, Int N, type TOut>() { ... }`~~, as  
                - then T and N would be used even before they were declared, and
                - with `Float[3] arrayOfThreeFloat = [1.0, 2.0, 3.0]` we want to write  
                  `Int[3] arrayOfThreeInt = arrayOfThreeFloat.convertTo<Int>()` (not ~~`...convertTo<Float, 3, Int>()`~~)
            - The template parameters `T` and `N` belong to the type of the object `arrayOfThreeFloat` and are determined already. It would not be possible to change them in the call of `convertTo<>()`, so it is not desired to specify them here at all.

- Further restrict the type with `requires`:
    - ```
      func sq<Number T>(T x) -> T
      requires (T x) { x * x }
      {
           return x * x
      }
      ```
    - ```
      class SlidingAverage<type T>
      requires {
          T + T    // required addition
          T / Int  // required to divide sum by Int
      }
      {
          T* numbers = new T[TSize]
          Int size = 0
          Int index = 0
          T sum = T(0)
      
      public:
          SlidingAverage(Int size) { ... }
          average() { ... }
          append(T value) { ... }
          reset() { ... }
      }
      ```
    - TODO Really this syntax: `{ ... } { ... }`?
- Template **type alias** with `using` (not ~~`typedef`~~)
    - `using<type T> T::InArgumentType = const T&`
- Template static variables/constants as type traits
    - ```
      static<type T> const Bool          T::IsFloatingPoint = False
      static         const Bool    Float32::IsFloatingPoint = True
      static         const Bool    Float64::IsFloatingPoint = True
      static<type T> const Bool Complex<T>::IsFloatingPoint = T::IsFloatingPoint
      ```


## Arrays & ArrayViews
- `Int[] dynamicArrayOfIntegers`
    - „Dynamic array“ with **dynamic size**
      ```
      Int[] array = [0, 1, 2]
      array[2] = 0
      array[3] = 0  // Runtime error, no compile time bounds check
      ```
    - `T[] array` is the short form of `cilia::Array<T> array`
    - "Make simple things simple",  
      having a short and traditional syntax for dynamic arrays should encourage people to use it.
    - The long form is called `Array<T>`, not ~~`Vector<T>`~~, because
        - that's the more traditional wording,
        - by using the word "vector", the purpose of this class is not immediately clear (especially not for users of many languages other than C++, not even C),
        - `Vector` could too easily collide with the mathematical vector (as used in linear algebra or geometry).
- `Int[3] arrayOfThreeIntegers`  
  (instead of ~~`Int arrayOfThreeIntegers[3]`~~ in C/C++)
    - „Static array“ with **fixed size**
      ```
      Int[3] array = [0, 1, 2]
      array[2] = 0
      array[3] = 0  // Compilation error, due to compile time bounds check
      ```
    - `arrayOfThreeIntegers.size()` -> `3`
        - realized as extension function  
          `func<type T, Int N> T[N]::size() -> Int { return N }`
- Use `T+`/`UniquePtr<T>` for "raw" C/C++ arrays of arbitrary size.  
  But array subscript with `Int+` is unsafe.
    - ```
      Int+ array = new Int[3]  // Array-to-pointer decay possible
      unsafe {
          array[2] = 0
          array[3] = 0  // Undefined behaviour, no bounds check at all
      }
      ```
    - Using `Int*` is possible but unsafe.
        - ```
          unsafe {
              Int* array = (new Int[3]).release()  // Array-to-pointer decay possible
              array[2] = 0
              array[3] = 0  // Undefined behaviour, no bounds check at all
              delete[] array
          }
          ```
        - ```
          unsafe {
              Int* array = reinterpretCastTo<Int*>(malloc(3 * sizeof(Int)))
              array[2] = 0
              array[3] = 0  // Undefined behaviour, no bounds check at all
              free(array)
          }
          ```
    - Actually this is how to handle pointer to array of `Int` "properly":  
      ```
      Int[3]+ arrayPtr = new Int[3]
      *arrayPtr[2] = 0
      *arrayPtr[3] = 0  // Compilation error, due to compile time bounds check
      ```
        - But raw pointer access is still `unsafe`:  
          ```
          unsafe {
              Int[3]* arrayPtr = (new Int[3]).release()
              *arrayPtr[2] = 0
              *arrayPtr[3] = 0  // Compilation error, due to compile time bounds check
              delete[] arrayPtr
          }
          ```
- Examples:
    - `Int[] dynamicArrayOfInt`
    - `Int[3] arrayOfThreeInt`
    - `Int[3]* pointerToArrayOfThreeInt`
    - `Int[3][]* pointerToDynamicArrayOfArrayOfThreeInt`
    - `String*[] dynamicArrayOfPointersToString`
- ArrayViews AKA Slices AKA Subarrays
    - `var subarray = array[1..2]`
    - `var subarray = array[1..<3]`
    - Incomplete ranges (need lower and/or upper bounds before use) are
      typcally implemented as inline functions that determine the concrete bounds and then call `array[start..end]` (or one of the exclusive counterparts).
        - `var subarray = array[..2]`
        - `var subarray = array[..]`
    - See Rust [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- Multidimensional arrays
    - dynamic size
        - `Int[,] dynamic2DArray`  
            - `T[,] array` is the short form of `cilia::MDArray<T, 2> array`
        - `Int[,,] multidimensionalDynamicArray`  
            - `T[,,] array` is the short form of `cilia::MDArray<T, 3> array`
        - and so on:  
            - `cilia::MDArray<T, N>`
    - static size
        - `Int[3, 2, 200]`
            - Multidimensional static array  
              ```
              Int[3, 2, 200] intArray3D
              intArray3D[2, 1, 199] = 1
              ```
- Mixed forms of static and dynamic array
    - `Int[3][,] dynamic2DArrayOfArrayOfThreeInt`
    - `Int[3,4][] dynamicArrayOfThreeByFourArrayOfInt`


## Signed Size
`Int` (i.e. signed) as type for `*.size()`
- Because mixed integer arithmetic ("signed - unsigned") and "unsigned - unsigned" is difficult to handle.
    - In C/C++ `aUInt - 1 >= 0` is _always_ true (even if `aUInt` is `0`)
- When working with sizes, calculating the difference is common; Then you are limited to `Int`/`SSize`/`PtrDiff` (i.e. signed integer) anyway.
- Who needs more than 2GB of data in a single "array", should please use a 64 bit platform.
- For bounds checking, the two comparisons `x >= 0` and  `x < width` may very well be reduced to a single `UInt(x) < width` _by the compiler_ in an optimization step. 
- Then types ~~`Size`~~ and ~~`SSize`~~/~~`PtrDiff`~~ are not necessary anymore, so two types less.
    - We simply use `Int` instead. Or `UInt` in rare cases.
- See also Going Native 2012, Day 2, Interactive Panel: Ask Us Anything
    - [42:41 - 45:28](https://youtu.be/Puio5dly9N8?feature=shared&t=2561)
    - [1:02:51 - 1:03:14](https://youtu.be/Puio5dly9N8?feature=shared&t=3771)


## Associative Arrays
- AKA Maps (or Dictionaries)
- `TValue[TKey]` as short form of `Map<TKey, TValue>`
    - e.g. `ContactInfo[String] contactInfoForID` as short form  
      of `Map<String, ContactInfo> contactInfoForID`
- "Make simple things simple",
  having a short syntax for associative arrays should encourage people to use it.
- Maybe template specialization:
    - `Map<Int, ...>` is a `HashMap`
    - `Map<String, ...>` is a `SortedMap`


## Function/Loop Parameter Passing
- Function call arguments are passed as either **`in`**, **`inout`**, **`out`**, **`copy`**, **`move`**, or **`forward`**.
    - **Default is passing as `in`**, explicitly to override with one of the other keywords.
    - Wording fits nicely for function arguments: How does the argument get into the function body (or out of it).
- The loop variable of `for ... in` is passed as either **`in`**, **`inout`**, **`copy`**, or **`move`**  
  (**`out`** and **`forward`** are not applicable here).
    - **Default is passing as `in`**, explicitly to override with one of the other keywords.
    - With `for` loops these keywords describe how the information (i.e. the variable) gets into the body of the loop (or out of it).
- Parameter passing keywords:
    - **`in`**
        - Is the default if no parameter passing keyword is given.
        - Technically either `const X&` or `const X` (sometimes `const XView`)
            - `const X&` as default:
                - `add(BigInt a, BigInt b)`
                    - is effectively translated to `add(const BigInt& a, const BigInt& b)`  
                - `BigInt[] bigIntArray = ...`  
                  `for i in bigIntArray { ... }`
                    - `i` is `const BigInt&`  
            - `const X` for "small types":
                - `for i in [1, 2, 3] { ... }`
                    - `i` is `const Int`
                - `for str in ["a", "b", "c"] { ... }`
                    - `str` is `const StringView` (a string-literal like `"a"` forms a `const StringView`, therefore `["a", "b", "c"]` is a `StringView[]`)
            - `const XView` for types that have a corresponding view type:
                - `concat(String first, String second)`
                    - is effectively translated to `concat(const StringView first, const StringView second)`
                - `String[] stringArray = ["a", "b", "c"]`  
                  `for str in stringArray { ... }`
                    - `str` is `const StringView`
    - **`inout`**
        - to mark as mutable/non-const reference.
        - Technically a non-const/mutable reference (`X&`)
        - Also at the caller `swap(inout a, inout b)`
        - Examples:
            - `for inout str in stringArray { ... }`
                - `str` is `String&`
            - `for inout i in intArray { ... }`
                - `i` is `Int&`
    - **`out`**
        - to mark as (non-const) reference.
        - Technically, like `inout`, a non-const/mutable reference (`X&`), but without prior initialization.
        - Also at the caller:
          ```
          String errorDetails
          if not open("...", out errorDetails) {
              cout << errorDetails
          }
          ```
        - Maybe even with ad-hoc declaration of the out variable:
          ```
          if not open("...", out String errorDetails) {
              cout << errorDetails
          }
          ```
        - Maybe even with broader scope:
          ```
          if open("...", out String errorDetails) {
              // ...
          } else {
              cout << errorDetails
          }
          ```
    - **`copy`**
        - to create a (mutable) copy (i.e. pass "by value"). 
        - Technically a non-const/mutable value (`X`), sometimes the "full class" `X` of a view class `XView`.
        - Examples:
            - `for copy i in [1, 2, 3] { ... }`
                - `i` is `Int`
            - `for copy str in stringArray { ... }`
                - `str` is `String`
            - `for copy str in ["an", "array", "of", "words"] { ... }`
                - `str` is `String` (not ~~`StringView`~~, due to the `X`/`XView`-copy-trick)
    - **`move`**
        - for move sematics.
        - Technically a right-value reference (`X&&`)
    - **`forward`**
        - for perfect forwarding.
        - Technically a right-value reference (`X&&`)?
- Type traits **`InArgumentType`** to determine the concrete type to be used for `in`-passing.
    - The rule of thumb is:
        - Objects that are POD (Plain Old Data) with a size less than or equal to the size of two pointers (i.e. of up to 16 bytes) are passed by value.
        - Larger objects (or non-POD) are passed by reference.
    - So use const _reference_ as general default.
        - `using<type T> T::InArgumentType = const T&`  
    - A "list of exceptions" for the "const _value_ types".
        - ```
          using       Bool::InArgumentType = const Bool
          using       Int8::InArgumentType = const Int8
          using      Int16::InArgumentType = const Int16
          using      Int32::InArgumentType = const Int32
          using      Int64::InArgumentType = const Int64
          ...
          using     UInt64::InArgumentType = const UInt64
          using    Float32::InArgumentType = const Float32
          using    Float64::InArgumentType = const Float64
          using StringView::InArgumentType = const StringView
          using  ArrayView::InArgumentType = const ArrayView
          ...
          ```
        - `using<type T> Complex<T>::InArgumentType = T::InArgumentType`
            - A generic rule: `Complex<T>` is passed the same way as `T`.
            - Could be further refined/corrected with  
              `using Complex<Float128>::InArgumentType = const Complex<Float128>&`  
              as `sizeof(Complex<Float128>)` is 32 bytes (so pass by reference), despite `sizeof(Float128)` is 16 (so pass by value would be the default).
        - This way developers only need to extend this list if they create _small_ classes (and if they want/need maximum performance). And I expect most custom class to be larger than 16 bytes (so nothing to do for those).
- Special **trick for types with views**
    - Applicable only for types `X` that have an `XView` counterpart where
        - `X` can implicitly be converted to `XView`,
        - `XView` can (explicitly) be converted to `X`, and
        - `XView` has the same "interface" as `const X` (i.e. contiguous memory access).
    - like:  
        - `String` - `StringView`
        - `Array` - `ArrayView`
        - `Vector` - `VectorView`
    - As example, with `String`/`StringView`:
        - `using String::InArgumentType = const StringView`  
          i.e. **for a `in String` _in fact_ a `const StringView`** is used as parameter type.
        - So all functions with a `String` (AKA `in String`) parameter would _implicitly_ accept
            - a `String` (as that can implicitly be converted to `StringView`) 
            - a `StringView` (that somehow is the more versatile variant of `const String&`),
            - and therefore also _every third-party string_ class (as long as it is implicitly convertable to `StringView`).
        - This way people do not necessarily need to understand the concept of a `StringView`. They simply write `String` and still cover all these cases.
        - Example:
            - `concat(String first, String second)`
                - is short for `concat(in String first, in String second)`
                - and extends to `concat(const StringView first, const StringView second)`
        - For cases where you need to _change_ the string argument, an **`in`**`String` (whether it is a `const String&` or a `const StringView`) is not suitable anyway. And all other parameter passing modes (`inout`, `out`, `copy`, `move`, `forward`) are based on real `String`s.
        - Though I don't see any advantage with respect to the `for ... in` loop, I would still apply the same rules just to ensure consistency.
        - Example:
            - `String[] stringArray = ["a", "b", "c"]`  
              `for str in stringArray { ... }`
                - `str` is `const StringView`
    - This is not possible with every view type, as some views do not guarantee contiguous memory access (typically when they do support stride):
        - ~~`Matrix` - `MatrixView`~~
        - ~~`Image` - `ImageView`~~
        - ~~`MDArray` - `MDArrayView` (AKA MDSpan?)~~
        - Maybe having some `XBasicView` instead, explicitly _without_ stride support,  
          that can cut off at start and end, but no slicing:
            - `Matrix` - `MatrixBasicView`
            - `Image` - `ImageBasicView`
            - `MDArray` - `MDArrayBasicView`
    - Small `...View`-classes with a size of up to 16 bytes (such as `StringView`, `ArrayView`, and `VectorView`) will be passed by value:
        - ```
          using String::InArgumentType = const StringView
          using  Array::InArgumentType = const ArrayView
          using Vector::InArgumentType = const VectorView
          ```
    - Bigger `...View`-classes with a size of _more_ than 16 bytes (such as `MatrixBasicView`, `ImageBasicView`, and `MDArrayBasicView`) will be passed by reference:
        - ```
          using  Matrix::InArgumentType = const MatrixBasicView&
          using   Image::InArgumentType = const ImageBasicView&
          using MDArray::InArgumentType = const MDArrayBasicView&
          ```
- Type trait **`CopyArgumentType`**
    - of a type `T` typically simply is `T`  
      `using<type T> T::CopyArgumentType = T`  
    - but for `View`-types it is the corresponding "full" type:
      ```
      using       StringView::CopyArgumentType = String
      using        ArrayView::CopyArgumentType = Array
      using       VectorView::CopyArgumentType = Vector
      using       MatrixView::CopyArgumentType = Matrix
      using  MatrixBasicView::CopyArgumentType = Matrix
      using        ImageView::CopyArgumentType = Image
      using   ImageBasicView::CopyArgumentType = Image
      using      MDArrayView::CopyArgumentType = MDArray
      using MDArrayBasicView::CopyArgumentType = MDArray
      ```
    - The idea is to get a _mutable copy_ of the object, even without understanding the concept of a `View`.
    - Example:
        - `for copy str in ["an", "array", "of", "words"] { ... }`
            - `str` is `String` (not ~~`StringView`~~)
            - This way people do not necessarily need to understand the concept of a `StringView` literal. They simply write `copy` to get a `String` with a copy of the content of the `StringView`.
            - (This is currently the only useful example I can think of.)


## Literals
- `True`, `False` are Bool,
    - as in Python,
    - as they are constants.  
- `NullPtr` is the null pointer,
    - it is of the type `NullPtrType`,
    - explicit cast necessary to convert any pointer to `Int`.
- `123` is an integer literal of arbitrary precision
    - Can be converted to any integer type it fits into (signed and unsigned)
        - `Int8 a = 1`    // Works because `1` fits into `Int8`
        - `Int8 b = 127`  // Works because `127` fits into `Int8`
        - `Int8 c = 128`  // _Error_ because 128 does _not_ fit into `Int8`
        - `Int8 d = -128` // Works because `-128` fits into `Int8`
        - `Int8 e = -129` // _Error_ because `-129` does _not_ fit into `Int8`
        - `UInt8 f = 255` // Works because `255` fits into `UInt8`
        - `UInt8 g = 256` // _Error_ because `256` does _not_ fit into `Int8`
        - `UInt8 h = -1`  // _Error_ because `-1` does _not_ fit into `UInt8`
        - `Int16 i = 32767` // Works
        - `Int32 j = 2'147'483'647` // Works
        - `Int64 k = 9'223'372'036'854'775'807` // Works
        - `Int l = a`     // Works because `Int8` fits into `Int32`
        - `UInt m = l`    // _Error_ because `Int` does _not always_ fit into `UInt`
            - `UInt m = UInt(l)` // Works
        - `Int n = m`     // Error because `UInt` does _not always_ fit into `Int`
            - `Int n = Int(m)`   // Works
    - `123` is interpreted as `Int` (or `Int64`, `Int128`, `Int256`, `BigInt`, if required due to the size)
        - in case of type inferring, parameter overloading and template matching.
    - Difficult: Constexpr constructor that accepts an arbitrary precision integer literal and can store that in ROM
        - Store as array of `Int`
    - `123u` is `UInt`
    - `-123` is always `Int` (signed)
- `0xffffffff` is `UInt` in hexadecimal
- `0b1011` is `UInt` in binary
- `0o123` is `UInt` in octal
    - as in Python
    - not `0123`, as that is confusing/unexpected, even if it is C++ standard
- `Int` vs. `Bool`
    - ~~`Int a = True`~~      // Error,
        - because `Bool` is _not_ an `Int`
        - because a `Bool` should not be accidentally interpreted as an `Int`
        - cast if necessary: `Int a = Int(True)`
    - ~~`Bool a = 1`~~      // Error,
        - because `Int` is not a `Bool`
        - because an `Int` should not be accidentally interpreted as a `Bool`
        - cast if necessary: `Bool a = Bool(1)` 
- `1.0` is a floating point literal of arbitrary precision
    - Can be converted to any float type into which it fits exactly
        - otherwise explicit cast necessary: `Float16(3.1415926)`
    - Difficult: Constexpr constructor that accepts an arbitrary precision float literal  and can store that in ROM
        - Store the mantissa as arbitrary precision integer (i.e. array of `Int`), plus the exponent as as arbitrary precision integer (i.e. array of `Int`, most always only a single `Int`)
    - `1.0` is interpreted as `Float` (or `Float64`, `Float128`, `Float256`, `BigFloat`, if required due to the size/precision)
        - in case of type inferring, parameter overloading and template matching.
    - `1.0f` is always `Float32`
    - `1.0d` is always `Float64`
- `Infinity`/`-Infinity` is a floating point literal of arbitrary precision for infinity values
    - Can be converted to any float type
    - Is interpreted as `Float`
        - in case of type inferring, parameter overloading and template matching.
- `NaN` is a floating point literal of arbitrary precision for NaN ("not a number") values
    - Can be converted to any float type
    - Is interpreted as `Float`
        - in case of type inferring, parameter overloading and template matching.
- `"Text"` is a `StringView`
    - Like String starts: pointer to first character and length,
        - so slicing of String to StringView is possible.
        - TODO What about small string optimization?
    - No null termination
        - If necessary
            - use `"Text\0“`  or
            - convert using `StringZ(...)`.
    - Data is typically stored in read-only data segments or ROM.
- Multiline String Literal
    - ```
      """
      First line
      Second line
      """
      ```
    - Removes indentation as in the last line
    - Removes first newline (if the opening """ is on a separate line)
    - Removes last newline (if the closing """ is on a separate line)
    - Similar to Swift, Julia, late Java, ...
    - Also as single line string literal with very few restrictions, good for RegEx
        - `"""(.* )whatever(.*)"""`
- Interpolated Strings
    - `$"M[{i},{j}] = {M[i, j]}"`
        - as in C#
        - Any reason to use/prefer any other syntax?
- Alternative string literals
    - `"Text"utf8` (but UTF-8 is the default anyway)
    - `"Text"utf16`
    - `"Text"utf32`
    - `"Text"ascii`
        - Syntax error, if one of the characters is not ASCII
    - `"Text"latin1`
        - Syntax error, if one of the characters is not Latin-1
    - ~~`"Text"sz` is a zero terminated string (as used in C)~~
        - ~~Problem: How to combine e.g. `"..."ascii` and `"..."sz`?~~
            - Workaround: Use `"Text\0"ascii` instead
    - All these available for multiline string literals and interpolated strings, too.
        - Any reason, not to? 
- `[1, 2, 3]` is an array (here an `Int[]`),
    - all elements have the same type.
- `{1, "Text", 3.0}` is an initialization list
    - e.g. for `Tuple`
- `Map<String,String>` is initialized with
  ```
  {
      "Key1": "Value1"
      "Key2": "Value2"
      "Key3": "Value3"
      "Key4": "Value4"
  }
  ```
- Rules for user defined literals
    - as in C++.


## Comments
- Single-line comments
    - ```
      // if a < b {
      //   TODO
      // }
      ```
- Block comments can be _nested_
    - ```
      /* This
      /* (and this) */
         is a comment */ 
      ```


## Better Readable Keywords
C++ has a "tradition" of complicated names, keywords or reuse of keywords, simply as to avoid compatibility problems with old code, which may have used one of the new keywords as name (of a variable, function, class, or namespace). Cilia can call into C++ (and vice versa), but is a separate language, so its syntax does not need to be backwards compatible.

- Cilia has
    - `var` instead of ~~`auto`~~
    - `func` instead of ~~`auto`~~
    - `type` instead of ~~`typename`~~
    - `await` instead of ~~`co_await`~~
    - `yield` instead of ~~`co_yield`~~
    - `return` instead of ~~`co_return`~~
    - `and`, `or`, `xor` instead of ~~`&&`/`&`~~, ~~`||`/`|`~~, ~~`!=`/`^`~~
    - `not` in addition to `!`
- `Int32` instead of `int32_t` or `qint32`,
    - so no prefix "q" nor postfix "_t", and in CamelCase.
- When translating C++ code to Cilia then change conflicting names, e.g.
    - `int var` -> `Int __variable_var`
    - `class func` -> `class __class_func`
    - `yield()` -> `func __function_yield()`


## Safety and Security
- **Range Checks**
    - The low hanging fruit would be to enable range checks _by default_, also in release builds (not only in debug), to detect **buffer overflows** or similar. This should fix the majority of C/C++ security issues.  
      To achieve maximum performance in all cases, there could be a third build configuration for even faster, but potentially unsafe builds.  
      So we would have:
        - **Debug**
            - for debugging,
            - with range checks,
            - with line by line debug info, and
            - often with a modified memory layout (to find more types of errors).
        - **Release**
            - for deployment,
            - _with_ range checks,
            - suitable for most situations,
            - with memory layout compatible to ~~EvenFasterBut~~UnsafeRelease.
        - ~~EvenFasterBut~~**UnsafeRelease**
            - for deployment,
            - _without_ range checks.
            - when maximum performance is desired.
- **Initialization**
    - No initialization means random values. In this case they are in fact often zero, but _not always_.
    - Initializing large arrays (e.g. `Array`, `Image`, `Vector`, or `Matrix` with many elements) takes a noticeable amount of time, so we don't always want to initialize everything.
        - With virtual memory it is actually (almost) "free" to initialize _large_ arrays with zero. (When using heap memory directly.)
    - We could warn (or maybe even consider it an error) if not initialized,  
      and use a keyword `noinit` to avoid that warning/error.  
      ```
      Int i         // Warning
      Int j noinit  // No warning
      Int j = 1     // No warning
      ```
    - Classes / custom types
        - Mark constructors with `noinit` when they do not initialize their values, so `noinit` should be used when calling them consciously.
        - ```
          class Array<type T> {
              Array(Int size) noinit { ... }
              Array(Int size, T value) { ... }
          }
          Array<Float> anArray(10)         // Warning
          Array<Float> anArray(10) noinit  // No warning
          Array<Float> anArray(10, 1.0)    // No warning
          ```
    - Also for free memory/heap
        - ```
          var arrayPtr = new Array<Float>(10)         // Warning
          var arrayPtr = new Array<Float>(10) noinit  // No warning
          var arrayPtr = new Array<Float>(10, 1.0)    // No warning
          ```
- **`safe`** as default, **`unsafe`** code blocks as escape.
    - Mainly to guide developers:
        - to signal what to do and what not to do,
        - `unsafe` is not regularly used, normally you just use the already _existing_, carefully developed and tested abstractions (like `Array`, `Vector`, `Matrix`, ...).
    - Not allowed in safe code:
        - Subscript access to pointers,
        - `reinterpretCastTo<T>(...)`,
        - calling functions marked as `unsafe`,
    - Still allowed/undetected in unsafe code:
        - Integer overflow (checking that all the time seems too costly)
    - But `unsafe` code is necessary to implement certain abstractions (as container classes):
        - ```
          func Array<T>::operator[](Int i) -> T& {
              if i < 0 or i >= size {
                  terminate()
              }
              unsafe {
                  return data[i]
              }
          }
          ```
    - Not every function with unsafe code needs to be marked as `unsafe`.
        - `unsafe` is a marker for those parts that need to be checked carefully.
        - Functions containing unsafe code not enclosed in an `unsafe` block need to be marked themselves with `unsafe`.
        - Unsafe is transitive (from an `unsafe` inner function to the outer function), but limited by `unsafe` blocks.
- `cilia::safe::Int`
    - Like `cilia::Int`, but with **overflow check** for all operations,
        - may throw OverflowException (or abort the program).
    - Generally considered to be too costly, even in language that are otherwise considered as "safe".
    - `safe::Int8`/`Int16`/`Int32`/`Int64`
    - `safe::Uint`
        - `safe::UInt8`/`UInt16`/`UInt32`/`UInt64`
- No further security features planned beyond C++
    - not as in [Rust](https://www.rust-lang.org/) or [Hylo](https://www.hylo-lang.org/),
        - that is just out of scope,
    - no _additional_ thread safety measures
        - A thread safety issue can easily lead to a deadlock or crash, but that is a reliabilty problem, usually IMHO not a security problem.
        - While thread safety can be a hard problem, there are currently no plans to extend the possibilities beyond plain C++ here (just because I am not aware of / familiar with better solutions than already available/recommended in C++).


## `is`, `as`, Casting
- `is` (type query)
    - See Cpp2 [is](https://hsutter.github.io/cppfront/cpp2/expressions/#is-safe-typevalue-queries):
        - `obj is Int` (i.e. a type)
        - `objPtr is T*` instead of `dynamic_cast<T*>(objPtr) != NullPtr`
        - `obj is cilia::Array` (i.e. a template)
        - `obj is cilia::Integer` (i.e. a concept)
    - Also support value query?
- `as`
    - See Cpp2 [as](https://hsutter.github.io/cppfront/cpp2/expressions/#as-safe-casts-and-conversions)
        - `obj as T` instead of `T(obj)`
        - `objPtr as T*` instead of `dynamic_cast<T*>(objPtr)`
        - With `Variant v` where T is one alternative:  
          `v as T` instead of`std::get<T>(v)`
        - With `Any a`:  
          `a as T` instead of `std::any_cast<T>(a)`
        - With `Optional<T> o`:  
          `o as T` instead of `o.value()`
- Constructor casting
    - `Float(3)`
    - Casting via constructor is `explicit` by default, `implicit` as option.
    - No classic C-style casting: ~~`(Float) 3`~~
    - but also
        - `castToMutable<T>(...)` or `mutableCastTo<T>(...)`
            - instead of ~~`constCastTo<>(...)`~~
        - `reinterpretCastTo<T>(...)`
        - `staticCastTo<T>(...)`?
- Automatic casts
    - as in Kotlin,
    - for template types, references and pointers.
    - ```
      func getStringLength(Type obj) -> Int {
           if obj is String {
               // "obj" is automatically cast to "String" in this branch
               return obj.length
           }
           // "obj" is still a "Type" outside of the type-checked branch
           return 0
      }
      ```
    - ```
      func getStringLength(Type obj) -> Int {
          if not obj is String
              return 0
          // "obj" is automatically cast to "String" in this branch
          return obj.length
       }
      ```
    - ```
      func getStringLength(Type obj) -> Int {
          // "obj" is automatically cast to "String" on the right-hand side of "and"
          if obj is String  and  obj.length > 0 {
              return obj.length
          }
          return 0
      }
      ```
    - Multiple inheritance is problematic here:
        - In Cilia/C++, an object can be an instance of several base classes at once, whereby the pointer (sometimes) changes during casting.
        - What if you still want/need to access the functions for a `Type obj` after `if obj is ParentA`?
            - Workaround: Cast back with `Type(obj).functionOfA()`


## `cilia` Standard Library
Standard library in namespace `cilia` (instead of `std` to avoid naming conflicts and to allow easy parallel use).
- With a Cilia version of each standard class/concept (i.e. CamelCase class names and camelCase function and variable names)
    - `cilia::String` instead of `std::string`
    - `Map` instead of `map`
        - `Dictionary` as alias with deprecation warning, as a hint for C# programmers.
    - `ForwardList` instead of `forward_list`
    - `UnorderedMap` instead of `unordered_map`
    - `ValueType` instead of `value_type`
    - Some exceptions/variations:
        - `Array` instead of `vector`
        - `StringStream` instead of `stringstream`
            - `TextStream`, `ByteStream`, ...
- Shallow wrapper,
    - e.g. `cilia::String : public std::string`
- "**Alias**" for 
    - member variables  
      `using var x = data[0]`  
      `using var y = data[1]`  
        - Not quite possible in C++.
            - With ...  
              `Float& imaginary = im`  
              or  
              `T& x = data[0]`  
              ... unfortunately memory is created for the reference (the pointer).
            - And this indeed is necessary here, because the reference could be assigned differently in the constructor, so it is not possible to optimize it away.
    - member functions
        - `using func f() = g()`

- Matrix & Vector
    - Geometry
        - Static/fixed size
        - For small, fixed size vectors & matrices ,
            - as typically used in geometry (i.e. 2D, 3D, 4D).
        - `cilia::Vector<T = Float, Int size>`
            - `cilia::Vector2<T = Float>`
            - `cilia::Vector3<T = Float>`
            - `cilia::Vector4<T = Float>`
        - `cilia::Matrix<T = Float, Int rows, Int columns>`
            - `cilia::Matrix22<T = Float>`
            - `cilia::Matrix33<T = Float>`
            - `cilia::Matrix44<T = Float>`
    - Linear Algebra
        - Dynamic/variable size
        - For large, dynamically sized vectors & matrices,
            - as typically used in linear algebra: BLAS (Basic Linear Algebra Subprograms)
        - `cilia::Vector<T = Float>`
        - `cilia::Matrix<T = Float>`
            - Stored column-major, like:
              ```
              0 3 6
              1 4 7
              2 5 8
              ```
        - `cilia::MDArray<T = Float, Int dimensions>`
            - also see `MDSpan`
          
- Image
    - `cilia::Image<T = Float>`
    - Almost like `cilia::Matrix`, but stored row-major, like:
      ```
      0 1 2
      3 4 5
      6 7 8
      ```
      
- Views, Slices
    - `ArrayView`
    - `VectorView`
    - `MatrixView`
    - `ImageView`
    - `MDArrayView`


## String, Char & CodePoint
- `cilia::String` with _basic/standard_ unicode support.
    - Iteration over a `String` or `StringView` by:
        - **grapheme clusters**
            - represented by `StringView`.
            - This is the _default form of iteration_ over a `String` or `StringView`
            - A single grapheme cluster will typically consist of multiple code units   
              and may even consist of multiple code points.
            - `for graphemeCluster in "abc 🥸👮🏻"`
                - "a", "b", "c", " ", "🥸", "👮🏻"
                - "\x61", "\x62", "\x63", "\x20", "\xf0\x9f\xa5\xb8", "\xf0\x9f\x91\xae\xf0\x9f\x8f\xbb"
            - A bit slow, as it has to find grapheme cluster boundaries.
            - It is recommended to mostly use the standard functions for string manipulation anyway. But if you need to iterate manually over a Unicode-String, then grapheme-cluster-based iteration is the safe/right way. 
            - Additional/alternative names?
                - `for graphemeCluster in text.asGraphemeClusters()`?
        - **code points**
            - represented by `UInt32`,
                - independent of the encoding (i.e. the same for UTF-8, UTF-16, and UTF-32 strings).
                - Called "auto decoding" in D.
            - `for codePoint in "abc 🥸👮🏻".asCodePoints()`
                - 0x00000061, 0x00000062, 0x00000063, 0x00000020, &nbsp; 0x0001F978, &nbsp; 0x0001F46E, 0x0001F3FB 
            - A bit faster than iteration over grapheme clusters, but still slow, as it has to find code point boundaries in UTF-8/16 strings.
            - Fast with UTF-32, **but** even with UTF-32 not all grapheme clusters fit into a single code point,
                - so not:
                    - emoji with modifier characters like skin tone or variation selector,
                    - diacritical characters (äöü..., depending on the normal form chosen),
                    - surely some more ...
                - Often slower than UTF-8, simply due to its size (cache, memory bandwidth).
        - **code units**
            - represented by
                - `Char` for `String`
                    - it is `Char`==`Char8`==`Byte`==`UInt8` and `String`==`UTF8String`
                - `Char16` for `UTF16String`
                - `Char32` for `UTF32String`
            - `for aChar8 in "abc 🥸👮🏻".asArray()`
                - 0x61, 0x62, 0x63, 0x20,  &nbsp;  0xf0, 0x9f, 0xa5, 0xb8,  &nbsp;  0xf0, 0x9f, 0x91, 0xae, 0xf0, 0x9f, 0x8f, 0xbb
                - same for
                    - `for codeUnit in "abc 🥸👮🏻"utf8.asArray()`
                    - `for codeUnit in UTF8String("abc 🥸👮🏻").asArray()`
            - `for aChar16 in "abc 🥸👮🏻"`**`utf16`**`.asArray()`
                - 0x0061, 0x0062, 0x0063, 0x0020,  &nbsp;  0xD83E, 0xDD78,  &nbsp;  0xD83D, 0xDC6E, 0xD83C, 0xDFFB
                - same for `for aChar16 in UTF16String("abc 🥸👮🏻").asArray()`
            - `for aChar32 in "abc 🥸👮🏻"`**`utf32`**`.asArray()`
                - 0x00000061, 0x00000062, 0x00000063, 0x00000020,  &nbsp;  0x0001F978,  &nbsp;  0x0001F46E , 0x0001F3FB
                - same for `for aChar32 in UTF32String("abc 🥸👮🏻").asArray()`
    - `string.toUpper()`, `string.toLower()`
        - `toUpper(String) -> String`, `toLower(String) -> String`
    - `stringArray.sort()`
        - `sort(Container<String>) -> Container<String>`
    - `compare(stringA, stringB) -> Int`
- `ByteString` to represent the strings with single byte encoding (i.e. the classical strings consisting of one-byte characters),
    - like
        - ASCII
        - Latin-1
        - ANSI (mostly identical to Latin-1)
        - almost every one of the "code pages"
    - Encoding is not defined.
        - The user has to take care of this,
        - or a subclass with known encoding has to be used (`ASCIIString`, `Latin1String`). 
    - `ASCIIString`, a string containing only ASCII characters.
        - Iteration over an `ASCIIString` or `ASCIIStringView` by `Char`==`Char8`==`Byte`
            - `for aChar in "abc"ascii`
                - 0x61, 0x62, 0x63
                - 'a', 'b', 'c'
                - Compilation error, if string literal contains non-ASCII characters.
                - same for `for aChar in ASCIIString("abc")`
                    - but Exception thrown, if string contains non-ASCII characters.
        - Implicitly convertable to `String`==`UTF8String`.
            - Very fast conversion, as all characters have the same binary representation.
    - `Latin1String`, a string containing only Latin-1 (ISO 8859-1) characters.
        - Iteration over an `Latin1String` or `Latin1StringView` by `Char`==`Char8`==`Byte`
            - `for aChar in "äbc"latin1`
                - 0xe4, 0x62, 0x63
                - 'ä', 'b', 'c'
                - Compilation error, if string literal contains non-Latin-1 characters.
                - same for `for aChar in ASCIIString("abc")`
                    - but Exception thrown, if string contains non-Latin1 characters.
        - Explicitly convertable to `String`==`UTF8String`.
            - Not as fast conversion as with ASCIIString, as typically some characters need to be translated into two UTF-8 code units.
- `Char8`, `Char16`, `Char32`
    - are considered as _different_ types for parameter overloading,
    - but otherwise are like `UInt8`, `UInt16`, `UInt32`,

- [**ICU**](https://unicode-org.github.io/icu/userguide/icu4c/) ("International Components for Unicode") for advanced Unicode support.
    - "The ICU libraries provide support for:
        - The latest version of the Unicode standard
        - Character set conversions with support for over 220 codepages
        - Locale data for more than 300 locales
        - Language sensitive text collation (sorting) and searching based on the Unicode Collation Algorithm (=ISO 14651)
        - Regular expression matching and Unicode sets
        - Transformations for normalization, upper/lowercase, script transliterations (50+ pairs)
        - Resource bundles for storing and accessing localized information
        - Date/Number/Message formatting and parsing of culture specific input/output formats
        - Calendar specific date and time manipulation
        - Text boundary analysis for finding characters, word and sentence boundaries"
    - `import icu` adds extension methods for `cilia::String`
        - Allows iteration over:
            - words (important/difficult for Chinese, Japanese, Thai or Khmer, needs list of words)
                - `for word in text.asWords()`
            - lines
                - `for line in text.asLines()`
            - sentences (needs list of abbreviations, like "e.g.", "i.e.", "o.ä.")
                - `for sentence in text.asSentences()`
        - Depending on locale
            - `string.toUpper(locale)`, `string.toLower(locale)`
                - `toUpper(String, locale) -> String`, `toLower(String, locale) -> String`
            - `stringArray.sort(locale)`
                - `sort(Container<String>, locale) -> Container<String>`
            - `compare(stringA, stringB, locale) -> Int`
     

## Misc 
- Two-Pass Compiler
    - as with C#, Java,
    - no forward declarations necessary (as it is in C/C++, due to the single-pass compiler).

- **Mixed arithmetic**
    - Mixing signed with unsigned integer
        - `Signed + - * / Unsigned` is an error
            - you have to cast explicitly,
            - i.e. no implicit cast (neither ~~`UInt` -> `Int`~~ nor ~~`Int` -> `UInt`~~).
            - `Int` (i.e. signed) is almost always used anyways.
        - Error with `if aUInt < anInt`
            - you have to cast
        - Error with `if aUInt < 0`
            - if the literal on the right is `<= 0`
    - Mixing integer with float
        - `1 * aFloat` is possible
            - Warning, if the integer literal cannot be reproduced exactly as `Float32`/`64`
        - `anInt * aFloat` is possible
            - Warning that the integer variable may not be reproduced exactly as `Float32`/`64`, i.e. with
                - `aFloat32 * anInt8`  // OK
                - `aFloat32 * anInt16` // OK
                - `aFloat32 * anInt32` // Warning
                - `aFloat32 * anInt64` // Warning
                - `aFloat64 * anInt8`  // OK
                - `aFloat64 * anInt16` // OK
                - `aFloat64 * anInt32` // OK
                - `aFloat64 * anInt64` // Warning

- Extended & Arbitrary Precision Integer & Float
    - `Int128`, `Int256`
    - `UInt128`, `UInt256` e.g. for SHA256
    - `BigInt` – Arbitrary Precision Integer
        - for cryptography, maybe computer algebra, numerics
        - see [Boost.Multiprecision](https://www.boost.org/doc/libs/1_79_0/libs/multiprecision/doc/html/index.html), [GMP](https://gmplib.org)
    - `Float128`, `Float256`
        - typically probably realized as double-double respectively double-double-double-double
        - [https://stackoverflow.com/a/6770329](https://stackoverflow.com/a/6770329)
        - Problem: Should be saved in IEEE 754 compatible format.
    - `BigFloat<>` for arbitrary precision float,
        - see [GMP](https://gmplib.org), [MPFR](https://www.mpfr.org)
        - The precision is arbitrary but fixed, either
          - statically, i.e. at compile time, as part of the BigFloat type, or
          - dynamically, i.e. at runtime, as property of a BigFloat variable.
    - `BFloat16` (Brain Floating Point)

- Integer operations **with carry** (flag or UInt)  
  (to implement `Int128`, `Int256` etc.)
    - Add with carry (flag, i.e. one bit only)
        - `UInt c = add(UInt a, UInt b, inout Bool carryFlag)`
            - `c = bits63..0(a + b + carryFlag)`  
              `carryFlag = bit64(a + b + carryFlag)`
        - `a.add(UInt b, inout Bool carryFlag)`
            - `a = bits63..0(a + b + carryFlag)`  
              `carryFlag = bit64(a + b + carryFlag)`
    - Mutiply with carry (high data, i.e. one UInt)
        - `UInt c = multiply(UInt a, UInt b, out UInt cHigh)`
            - `c = bits63..0(a * b)`  
              `cHigh = bit127..64(a * b)`
        - `a.multiply(UInt b, out UInt aHigh)`
            - `a = bits63..0(a * b)`  
              `aHigh = bit127..64(a * b)`
        - Mutiply-Add with carry (high data, i.e. one UInt)
            - `UInt d = multiplyAdd(UInt a, UInt b, UInt c, out UInt dHigh)`
                - `d = bits63..0(a * b + c)`  
                  `dHigh = bit127..64(a * b)`
            - `a.multiplyAdd(UInt b, UInt c, out UInt aHigh)`
                - `a = bits63..0(a * b + c)`  
                  `aHigh = bit127..64(a * b + c)`
    - Shift
        - `b = shiftLeftAdd(UInt a, Int steps, inout UInt addAndHigh)`
        - `a.shiftLeftAdd(Int steps, inout UInt addAndHigh)`
        - `b = shiftOneLeft(UInt a, inout Bool carryFlag)`
        - `a.shiftOneLeft(inout carryFlag)`
      
- `cilia::saturating::Int`
    - Like `cilia::Int`, but with **saturation** for all operations.
        - Limit to maximum, no wrap around.
        - Typically using SIMD (as those „media/DSP instructions“ do support saturation natively).
    - see https://en.wikipedia.org/wiki/Saturation_arithmetic 
    - `saturating::Int8`/`Int16`/`Int32`/`Int64`
    - `saturating::Uint`
        - `saturating::UInt8`/`UInt16`/`UInt32`/`UInt64`

- Reserved keywords for _future_ use (maybe, maybe not).
    - `Null`
    - `parallel`
    - `struct` for some variant of C++ strcuts/classes
    - `interface` for pure abstract base classes or similar constructs
    - `template`

- Versioning of the Cilia source code
    - Via file ".ciliaVersion" in a (project) directory,
        - similar to ".clang_format",
        - also possible file by file: Matrix.ciliaVersion (for Matrix.cilia).
    - Via file extension: 
        - "*.cilia" – always the latest language version (if not overridden via ".ciliaVersion")
        - "*.2024.cilia" – version from the year 2024
        - "*.2024b.cilia" – second version from the year 2024

- No [function-like macros](https://www.geeksforgeeks.org/cpp-macros/), just object-like `#define` and:
    - `#if`
    - `#else`
    - `#endif`


## Interesting Ideas from Other Languages
- **Circle**
    - **Fix C++ "wrong defaults"**  
        [Sean Baxter](https://x.com/seanbax), creator of [Circle](https://github.com/seanbaxter/circle), [writes about C++'s wrong defaults](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#to-err-is-human-to-fix-divine):
        > C++ has a number of "wrong defaults," design decisions either inherited from C or specific to C++ which many programmers consider mistakes.
        > They may be counter-intuitive, go against expected practice in other languages, leave data in undefined states, or generally be prone to misuse.
        
        I am not familiar with all these issues, but in a new language we certainly coud fix a lot of it.
        
        1. [Uninitialized automatic variables.](http://eel.is/c++draft/dcl.init#general-7.3)
            - See [Safety and Security](#safety-and-security)/Initialization
        2. [Integral promotions.](http://eel.is/c++draft/conv.prom)
            - Only allow safe ones,  
              otherwise an explicit cast is necessary.
        3. [Implicit narrowing conversions.](http://eel.is/c++draft/conv.integral#3)
            - Not allowed,  
              only implicit widening is allowed.
            - Assigment of integer and float literals to variables of certain precision only possible if "it fits".
        4. [Switches should break rather than fallthrough.](http://eel.is/c++draft/stmt.switch#6)
            - Use the keyword `fallthrough` instead, as in Swift.
        5. [Operator precedence is complicated and wrong.](http://eel.is/c++draft/expr.compound#expr.bit.and)
            - If the [suggestion](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#simpler_precedence) of Circle (Sean Baxter) works well, then that would be fine.
            - Cpp2 (Herb Sutter) has [this precedence](https://hsutter.github.io/cppfront/cpp2/common/?h=operator#binary-operators).
        6. [Hard-to-parse declarations and the most vexing parse.](http://eel.is/c++draft/dcl.pre#nt:simple-declaration)
            - Use `func` (but not typically `var`)
        7. [Template brackets `< >` are a nightmare to parse.](http://eel.is/c++draft/temp.names#nt:template-argument-list)
            - I would not like to change this, only if it _really_ has to be.
            - Cpp2 / Herb Sutter kept `< >` after all.
        8. [Forwarding parameters and `std::forward` are error prone.](http://eel.is/c++draft/temp.deduct#call-3)
           - I am not familiar with the problem(s), but Cpp2 / Herb Sutter offers the `forward` keyword.
        10. [Braced initializers can choose the wrong constructor.](http://eel.is/c++draft/dcl.init.list#2)
            - Do without braced initializers altogether.
            - With `func` there is now a clear distinction between function declaration and variable declaration with initialization.
            - The classic initialization via `(...)`, ultimately a function call of the constructor, fits better.
            - Curly brackets only for initializer lists, i.e. for tuples, lists etc.
            - Square brackets for arrays.
        11. [`0` shouldn't be a null pointer constant.](http://eel.is/c++draft/expr#conv.ptr-1)
            - Not allowed, use `NullPtr`.
        12. [`this` shouldn't be a pointer.](http://eel.is/c++draft/expr.prim.this#1)
            - Better it is a reference.
    - [Versioning with feature directives](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#versioning-with-feature-directives)
        - Standardization is better than having multiple different language "dialects"  
          **but**
            - for transitioning of existings source code  and
            - for the evolution of a language
        - it is a very interesting idea to selectively enable new language features or defaults.
    - [Circle C++ with Memory Safety](https://www.circle-lang.org/site/index.html)
        - Extending C++ for Rust-level safety.

- **Cpp2** (Herb Sutter)
    - [is](https://hsutter.github.io/cppfront/cpp2/expressions/#is-safe-typevalue-queries)
    - [as](https://hsutter.github.io/cppfront/cpp2/expressions/#as-safe-casts-and-conversions)
    -  [Function](https://hsutter.github.io/cppfront/cpp2/functions/) [Parameter Passing](https://hsutter.github.io/cppfront/cpp2/functions/#parameters)
        - `in`, `inout`, `out`, `move`, `copy`, `forward`
    - [Labelled `break` and `continue`](https://github.com/ntrel/cpp2?tab=readme-ov-file#labelled-break-and-continue) (i.e. multi-level)
      ```
      outer: while true {
          j := 0;
          while j < 3 next j++ {
              if done() {
                  break outer;
              }
          }
      }
      ```
    - `for words next i++ do (word) { ... word & i ... }` iterates over all words and with an index, at the same time.
    - [Uniform Call Syntax](https://github.com/ntrel/cpp2?tab=readme-ov-file#uniform-call-syntax)
      for member functions and free functions.
    - [Function Bodies](https://github.com/ntrel/cpp2?tab=readme-ov-file#function-bodies)
        - `multiply: (x: int, y: int) -> int = x * y;`
        - `multiply: (x: int, y: int) x * y;` (not even an `=` anymore?)
        - `multiply: (x: int, y: int) -> int = return x * y;`
        - Nice and short, as in math, but in the end it is one more kind of notation for functions.
    - [Unified `operator=` for assignment, constructor, and destructor)](https://github.com/ntrel/cpp2?tab=readme-ov-file#operator).
        - Takes a bit of getting used to.
    - [Implicit Move on Last Use](https://github.com/ntrel/cpp2?tab=readme-ov-file#implicit-move-on-last-use)
        - So resources are freed even earlier than in C++.
    - [Named Return Values](https://github.com/ntrel/cpp2?tab=readme-ov-file#named-return-values)
    - [Inspect](https://github.com/ntrel/cpp2?tab=readme-ov-file#inspect),
      a kind of pattern matching.

- **Rust**
    - Security, of course: borrow checker etc.
    - Ranges

- [**Julia**](https://julialang.org/)
    - "Cilia" sounds like something in between [C](https://en.wikipedia.org/wiki/C_(programming_language))/[C++](https://en.wikipedia.org/wiki/C%2B%2B) and [Julia](https://julialang.org), so maybe I could/should add some more of Julias interesting features to the Cilia wish list.
    - Julia has very strong math support. Some of its features should be easy to copy.
        - `b = 2a` as short form of `b = 2*a`
        - `x ÷ y`, integer divide, like `x / y`, truncated to an integer
        - `sqrt(x)`, `√x`
        - `cbrt(x)`, `∛x`
        - `!=`, `≠`
        - `<=`, `≤`
        - `>=`, `≥`
        - Operator overloading
            - See:
                - [https://www.geeksforgeeks.org/operator-overloading-in-julia/](https://www.geeksforgeeks.org/operator-overloading-in-julia/)
                    - „Precedence and associativity:  When defining new operators or overloading existing ones, you can also specify their precedence and associativity, which determines the order in which they are evaluated.“
                        - That seems quite complicated to parse?!
                        - I cannot find any other reference to this feature, I assume it is a misunderstanding.
                - [https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm](https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm)
            - Much more operators
                - [https://stackoverflow.com/a/60321302](https://stackoverflow.com/a/60321302)
        - Many kinds of brackets?
            - [https://stackoverflow.com/a/33357311](https://stackoverflow.com/a/33357311)
            - TODO: Are these "unusual" brackets meant to be used as operators?
