---
permalink: /comparison/
description: "Cilia syntax comparison with C++, Cpp2, Carbon, Rust, Swift, Kotlin, Java, C#, D. Side-by-side equivalents."
---

# Syntax Comparison with Other Languages

The syntax comparison on the following pages aims to show the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in various other languages.

In C++, Cpp2, Rust, Java, C#, and D the type `int`/`Int` and/or literals like `42` are 32 bits wide, not 64 bits.
That's OK, this is not a performance benchmark.

> **Note**  
> I may not be very familiar with all these languages, or not up to date.  
> I may not even be sufficiently up to date with C++14/17/20/23/26 either.


## Syntax of Carbon and Cpp2

[Bjarne Stroustrup said](https://www.stroustrup.com/devXinterview.html) (way back in 2000) in an interview about C++:
> Today, I'd look for a _much_ simpler syntax—and probably clash with people's confusion between the familiar and the simple.

While Carbon and Cpp2 ("C++ syntax 2") are based on the same basic idea, a new syntax with C++ interoperability, they both have a syntax more resembling Rust than C++.  

I like many aspects, especially of Cpp2 (Herb Sutter), but not the `name: Type` syntax. It indeed does not feel familiar to me, IMHO unnecessarily so. Cilia is a bit more conservative/traditional here. And I think its syntax is still "easy enough" to parse.

> **Note**  
> As far as I know, Bjarne Stroustrup has never said, which syntax he would choose today.


## Default vs. Explicit Initialization

Arrays, sets, and maps are **default-constructed**, so they can be used immediately after declaration (for example, to add values in a loop):
```
String[] words
for i in 0..9 {
    words.pushBack(i.toString());
}
```

In contrast, languages like Swift, Rust, Kotlin, Java, and C# require explicit initialization of collections before they can be used. After declaration, an instance must therefore be assigned explicitly:
```
var words: [String] = []
for i in 0...9 {
    words.append("\(i)")
}
```

In many examples this requirement is “hidden” by immediate assignment of a literal (such as `["one", "two", "three"]`) or of a function return value. It’s not a big deal, but in practice I still find the need for explicit initialization of empty collections somewhat annoying.
