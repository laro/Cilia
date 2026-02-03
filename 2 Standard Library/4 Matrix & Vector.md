---
permalink: /standard-library/matrix-and-vector/
---

## Matrix & Vector

- **Geometry**
    - Static/fixed size
    - For small, fixed size vectors & matrices,  
      as typically used in geometry (i.e. 2D, 3D, 4D).
    - `cilia::Vector<Int size, T = Float>`
        - `cilia::Vector2<T = Float>`
        - `cilia::Vector3<T = Float>`
        - `cilia::Vector4<T = Float>`
    - `cilia::Matrix<Int rows, Int columns, T = Float>`
        - `cilia::Matrix22<T = Float>`
        - `cilia::Matrix33<T = Float>`
        - `cilia::Matrix44<T = Float>`

- **Linear Algebra**
    - Dynamic/variable size
    - For large, dynamically sized vectors & matrices,  
      as typically used in linear algebra (i.e. BLAS – Basic Linear Algebra Subprograms).
    - `cilia::Vector<T = Float>`
    - `cilia::Matrix<T = Float>`
        - Stored column-major, like:
            ```
            0 3 6
            1 4 7
            2 5 8
            ```
    - `cilia::MDArray<Int dimensions, T = Float>`
        - also see `MDSpan`

