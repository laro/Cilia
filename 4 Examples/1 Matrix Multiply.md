---
permalink: /examples/matrix-multiply/
description: "Matrix multiplication example in Cilia and C++. Side-by-side comparison of equivalent implementations."
---

# Matrix Multiply

Naive algorithm: triple nested loop, O(n³). For each element C[i,j], compute the dot product of row i of A and column j of B.

## Cilia

```text
{% include_relative MatrixMultiply.cil %}
```

## C++

```text
{% include_relative MatrixMultiply.cpp %}
```
