---
permalink: /standard-lib/matrix-and-vector/
---

## Matrix & Vector

### **Geometry**

For small, _fixed size_ vectors & matrices, as typically used in geometry (i.e. 2D, 3D, 4D).
```
Vector<Int size, T = Float>  // as base class
Vector2<T = Float>
Vector3<T = Float>
Vector4<T = Float>
```
```
Matrix<Int rows, Int columns, T = Float>  // as base class
Matrix22<T = Float>
Matrix33<T = Float>
Matrix44<T = Float>
```
Using `namespace geometry` to avoid naming conflicts, but `Vector2/3/4` could still be (also) in namespace `cilia`.


### Linear Algebra

For large, dynamically sized vectors & matrices, as typically used in linear algebra (i.e. BLAS – Basic Linear Algebra Subprograms), in the `namespace linalg`.
```
Vector<T = Float>
Matrix<T = Float>
```

- `MDArray<Int dimensions, T = Float>`
    - also see `MDSpan`
- `VectorView`, `MatrixView`


### Column-Major
Matrices (unlike images) are stored column-major, like:
```
0 3 6
1 4 7
2 5 8
```


### Datatype & Precision

The default datatype is `Float` (with 64-bit precision), which is well suited for scientific calculations.

Feel free to define your own type aliases:
- `using Vec3 = cilia::Vector3<Float32>`
- `using RGB = cilia::Vector3<UInt8>`
