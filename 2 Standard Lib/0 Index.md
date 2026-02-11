---
permalink: /standard-lib/
---

## Standard Library

Standard library in namespace `cilia` (instead of `std` to avoid naming conflicts and to allow easy parallel use).

With a Cilia variant of each standard class/concept (with CamelCase class names and camelCase function and variable names):
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


### Shallow Wrappers

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
But only _with_ a wrapper do we have
- a Cilia standard library in the "idiomatic" Cilia style (i.e. CamelCase),
- whose types/classes can also be used with existing C++ APIs (i.e. using `Int`, `Int32`, `String`, `StringView`, `T[]`, etc. instead of `long` / `long long`, `int32_t`, `string`, `string_view`, `vector<T>`).
