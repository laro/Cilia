---
title: Cilia.Associative Arrays
permalink: /cilia/associative-arrays/
order: 14
---

## Associative Arrays
- AKA Maps (or Dictionaries)
- `TValue[TKey]` as short form of `Map<TKey, TValue>`
    - e.g. `ContactInfo[String] contactInfoForID` as short form  
      of `Map<String, ContactInfo> contactInfoForID`,
    - as [in D](https://dlang.org/spec/hash-map.html).
    - There is no difference between these two, but "OtherMap<String, ContactInfo> contactInfoForID" allows you to select other map variants (SortedMap, HashMap etc.) if necessary.
- "Make simple things simple",  
  having a short syntax for associative arrays so they are easy to use.
- Maybe partial template specialization:
    - `Map<Int, ...>` is a `HashMap`
    - `Map<String, ...>` is a `SortedMap`
