---
permalink: /examples/quicksort/
description: "QuickSort implementation in Cilia and C++. Recursive sorting algorithm side-by-side comparison."
---

# QuickSort

Divide-and-conquer sorting by [Tony Hoare](https://en.wikipedia.org/wiki/Tony_Hoare): pick middle element as pivot, partition via two pointers, recurse on both halves. O(n log n) average, in-place via `Span`.


## Cilia

```text
{% include_relative QuickSort.cil %}
```


## C++

```text
{% include_relative QuickSort.cpp %}
```
