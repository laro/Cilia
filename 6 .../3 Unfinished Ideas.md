---
permalink: /more/unfinished-ideas/
---

## Unfinished Ideas

Admittedly, many ideas for Cilia are not yet _fully_ developed, but these are not at all.

### OpenMP-like Parallel Programming
- Serial code
  ```
  Floar[] arr = ...
  for i in 0..<arr.size() {
      arr[i] = 2 * arr[i]
  }
  ```
- Parallel code
    - ```
      for i in 0..<arr.size() parallel { .. }
      ```
      ```
      for i in 0..<arr.size()
      parallel batch(1024) { .. }
      ```
      ```
      for i in 0..<arr.size()
      parallel if arr.size() > 65535 { .. }
      ```
      ```
      for i in 0..<arr.size()
      parallel if arr.size() > 65535 { .. }
      ```
      ```
      for i in 0..<arr.size() parallel reduce(sum: +) { .. }
      ```
      ```
      for i in 0..<arr.size()
      parallel
      if arr.size() > 65535
      reduce(sum: +)
      schedule(dynamic, 65536) { .. }
      ```
> TODO
> Syntactically this is not a good solution.
> - We avoid brackets in `if` and `while`, but then use it for `reduce` and `schedule`...
> - Syntax should be better, clearer, or more powerful than plain OpenMP, otherwise better use just that.
