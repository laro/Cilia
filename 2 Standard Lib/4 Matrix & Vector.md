---
permalink: /standard-lib/matrix-and-vector/
---

## Matrix & Vector

### **Geometry**

For small, _fixed size_ vectors & matrices,  
as typically used in geometry (i.e. 2D, 3D, 4D).
- `Vector<Int size, T = Float>`
    - `Vector2<T = Float>`
    - `Vector3<T = Float>`
    - `Vector4<T = Float>`
- `geometry::Matrix<Int rows, Int columns, T = Float>`
    - `Matrix22<T = Float>`
    - `Matrix33<T = Float>`
    - `Matrix44<T = Float>`
- `namespace geometry`


### Linear Algebra

For large, dynamically sized vectors & matrices,  
as typically used in linear algebra (i.e. BLAS – Basic Linear Algebra Subprograms).
- `Vector<T = Float>`
- `Matrix<T = Float>`
    - Stored column-major, like:
        ```
        0 3 6
        1 4 7
        2 5 8
        ```
- `MDArray<Int dimensions, T = Float>`
    - also see `MDSpan`
- `VectorView`, `MatrixView`
- `namespace linalg`
 
> **Note**  
> To avoid a naming conflict, we either need
> ```
> cilia::StaticVectorBase<Int size, T = Float>
> cilia::Vector<T = Float>
> ```
> or
> ```
> cilia::geometry::Vector<Int size, T = Float>
> cilia::linalg::Vector<T = Float>
> ```


### Datatype & Precision

The default datatype is `Float` (with 64-bit precision), which is well suited for scientific calculations.

Feel free to define your own type aliases:
- `using Vec3 = cilia::Vector3<Float32>`
- `using RGB = cilia::Vector3<UInt8>`
