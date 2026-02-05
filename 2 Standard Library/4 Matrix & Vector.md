---
permalink: /standard-library/matrix-and-vector/
---

## Matrix & Vector

### **Geometry**
For small, _fixed size_ vectors & matrices,  
as typically used in geometry (i.e. 2D, 3D, 4D).
- `cilia::Vector<Int size, T = Float>`
    - `cilia::Vector2<T = Float>`
    - `cilia::Vector3<T = Float>`
    - `cilia::Vector4<T = Float>`
- `cilia::Matrix<Int rows, Int columns, T = Float>`
    - `cilia::Matrix22<T = Float>`
    - `cilia::Matrix33<T = Float>`
    - `cilia::Matrix44<T = Float>`

### Linear Algebra
For large, dynamically sized vectors & matrices,  
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
- `VectorView`, `MatrixView`

### Datatype & Precision
The default datatype is `Float` (64-bit precision), which is better suited for scientific calculations.

Feel free to use your own derivations:
- `using Vec3 = cilia::Vector3<Float32>`
- `using RGB = cilia::Vector3<UInt8>`
