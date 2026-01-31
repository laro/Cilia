---
title: Comparison
permalink: /comparison/
order: 1
---

## Comparison with C++, Cpp2, Carbon, Rust, Swift, Kotlin, Java, and C#
The following comparison aims to show the _exact_ equivalent of the [Cilia example](/comparison/cilia/#by-example):

[Cilia](/comparison/cilia/), [C++](/comparison/cpp/), [Cpp2](/comparison/cpp2/), [Carbon](/comparison/carbon/), [Rust](/comparison/rust/), [Swift](/comparison/swift/), [Kotlin](/comparison/kotlin/), [Java](/comparison/java/), [C#](/comparison/csharp/)

> **Note**
> - I may not be very familiar with all these languages, or not up to date.
>     - Is there really no range operator and no classical for-loop in neither Cpp2 nor Carbon?
> - I may not even be sufficiently up to date with C++14/17/20/23/26 either.

### Syntax of Carbon and Cpp2
While Carbon and Cpp2 ("C++ syntax 2") are based on the same basic idea, a new syntax with C++ interoperability, they both have a syntax more resembling Rust than C++.  

[Someone said in an interview](https://www.stroustrup.com/devXinterview.html) (way back in 2000):
> Today, I'd look for a _much_ simpler syntax—and probably clash with people's confusion between the familiar and the simple.

I like many aspects, especially of Cpp2, but not the `name: Type` syntax. It indeed does not feel familiar to me, IMHO unnecessarily so. Cilia is a bit more conservative/traditional here. And I think its syntax is still "easy enough" to parse.


### Default vs. Explicit Initialization
Arrays, sets, and maps are **default-constructed**, so they can be used immediately after declaration (for example, to add values in a loop):
```
String[] words
for i in 0..9 {
    words.pushBack(toString(i));
}
```

In contrast, languages like Swift, Rust, Kotlin, Java, and C# require explicit initialization of collections before they can be used. After declaration, an instance must therefore be assigned explicitly:
```
var words: [String] = []
for i in 0...9 {
    words.append("\(i)")
}
```

In many examples this requirement is “hidden” by immediate assignment of a literal (such as ["one", "two", "three"]) or a function return value. It’s not a big deal, but in practice I still find the need for explicit initialization of empty collections somewhat annoying.
