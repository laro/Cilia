## Comparison with C++, Cpp2, Carbon, and Rust
The follwing comparison aims to show the _exact_ equivalent of the [Cilia example](README.md#by-example) in C++, Cpp2, Carbon, and Rust:
- **C++**
    - `int`, `int32_t`, `int64_t`, `float`
    - `int x = 42;`
        - `auto x = 42;`
        - `const auto x = 42;`
        - `vector<string> words;`
        - `set<string> names;`
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
        - `names: set<string>;`
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
        - `var names: Set(String);`
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
        - `let mut names: HashSet<String> = HashSet::new();`
        - `let mut contactInfoForID: HashMap<String, ContactInfo> = HasMap::new();`
    - `fn multiply(a: i64, b: i64) -> i64 { return a * b; }`
        - `fn print(a: &ContactInfo) { ...; }`
        - `fn concat(a: &str, b: &str) -> String { return a + b; }`
    - `for i in 1..=10 { ...; }`
        - `for i in 0..words.len() { ...; } `          
        - `for i in [5, 7, 11, 13].iter() { ...; }`
        - `for word in words.iter() { ...; }`
- **Swift**
    - `Int`, `Int32`, `Int64`, `Float`
    - `var x: Int = 42`
        - `var x = 42`
        - `let x = 42`
        - `var words: [String]`
        - `var names: Set<String> = Set()`
        - `var contactInfoForID: [String: ContactInfo]`
    - `func multiply(_ a: Int, _ b: Int) -> Int { return a * b }`
        - `func print(_ a: ContactInfo) { ... }`
        - `func concat(_ a: String, _ b: String) -> String { return a + b }`
    - `for i in 1...10 { ... }`
        - `for i in 0..<words.count { ... } `          
        - `for i in [5, 7, 11, 13] { ... }`
        - `for word in words { ... }`
- **Kotlin**
    - `Int`, `Long`, `Float`
    - `var x: Int = 42`
        - `var x = 42`
        - `val x = 42`
        - `var words: MutableList<String>` (an `Array` would have a fixed size)
        - `var names: MutableSet<String>`
        - `var contactInfoForID: MutableMap<String, ContactInfo>`
    - `fun multiply(a: Int, b: Int): Int { return a * b }`
        - `fun print(a: ContactInfo) { ... }`
        - `fun concat(a: String, b: String): String { return a + b }`
    - `for (i in 1..10) { ... }`
        - `for (i in 0 until words.size) { ... } `          
        - `for (i in listOf(5, 7, 11, 13)) { ... }`
        - `for (word in words) { ... }`

> [!NOTE]
> - I may not be very familiar with Cpp2, Carbon, Rust, Swift, and Kotlin or not up to date.
>     - Is there really no range operator and no classical for-loop in neither Cpp2 nor Carbon?
> - I may not be sufficiently up to date with C++14/17/20/23/26 either.

While Carbon and Cpp2 ("C++ syntax 2") are based on the same basic idea, a new syntax with C++ interoperability, they both have a syntax more resembling Rust than C++.  

[Someone said in an interview](https://www.stroustrup.com/devXinterview.html) (way back in 2000):
> Today, I'd look for a much simpler syntax—and probably clash with people's confusion between the familiar and the simple.

I like many aspects, especially of Cpp2, but not the `name: Type` syntax. It indeed does not feel familiar to me, IMHO unnecessarily so. Cilia is a bit more conservative/traditional here. And I think its syntax is still "easy enough" to parse.


