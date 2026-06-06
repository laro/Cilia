---
permalink: /standard-lib/
description: "Cilia standard library in namespace cilia: String, Array, Map, CamelCase names. Shallow wrappers over C++ std."
---

# Standard Library

The standard library is in the namespace `cilia` (instead of `std`, to avoid naming conflicts and to allow easy parallel use).

There is a Cilia variant of each standard class/concept (with CamelCase class names and camelCase function and variable names):
- `cilia::String` instead of `std::string`
- `SharedPtr` instead of `shared_ptr`
- `ValueType` instead of `value_type`
- `Map` instead of `map`
    - `FlatMap` instead of `flat_map`
- `Set` instead of `set`
    - `FlatSet` instead of `flat_set`

Some exceptions/variations:
- `Array` instead of `vector`
- `StringStream` instead of `stringstream`
    - `TextStream`, `ByteStream`, ...
- `LinkedList` instead of `list` (A doubly linked list; Doesn't need a short name, a plain `Array` most often is more apropriate anyway.)
    - `ForwardLinkedList` instead of `forward_list` (A singly linked list; Even more rare.)
- `HashMap` instead of `unordered_map`
    - `MultiMap` instead of `multimap`
    - `HashMultiMap` instead of `unordered_multimap`
- `HashSet` instead of `unordered_set`
    - `MultiSet` instead of `multiset`
    - `HashMultiSet` instead of `unordered_multiset`


## Shallow Wrappers

Mostly realized as shallow wrappers, like
```
class cilia::String : public std::string { ... }
```
with "**aliases**" for:
- Member variables  
  `using var x = data[0]`  
  `using var y = data[1]`
- Member functions  
  `using func pushBack = push_back`

A wrapper is not strictly necessary, Cilia can access/call every C/C++ class/function without it.  
We can even use the basic Cilia types when using the C++ APIs, e.g.
- `Int` for `long` (or `long long`),
- `Int32` for `int32_t`,
- `String` for `string`,
- `StringView` for `string_view`,
- `T[]` for `vector<T>`), etc.

But only _with_ a wrapper do we have a Cilia standard library in the "idiomatic" Cilia style, i.e.
- CamelCase class and camelCase function names,
- `Int` instead of `size_t`.
