---
permalink: /standard-lib/image/
---

## Image

```
class Image<type T = Float32> : linalg::Matrix<T> {
    ...
}
```
Basically a two dimensional array, with dynamic size.

`ImageView` as "read-only reference" of sub-areas.  
`ImageBasicView` as "read-only reference" with continuous pixels.

Common image-processing examples:
- `func gaussianBlur<type T>(Image<T> image, Float sigma) -> Image<T>`
- `func medianFilter<type T>(Image<T> image, Int kernelSize) -> Image<T>`
- `func sobelEdges<type T>(Image<T> image) -> Image<T>`
- `func resize<type T>(Image<T> image, Int width, Int height, Interpolation interpolation) -> Image<T>`
- `func threshold<type T>(Image<T> image, T lower, T upper) -> Image<T>`

Same operations as member functions:
- `class Image<type T = Float32> {`
    - `func gaussianBlur(Float sigma) -> Image<T>`
    - `func medianFilter(Int kernelSize) -> Image<T>`
    - `func sobelEdges() -> Image<T>`
    - `func resize(Int width, Int height, Interpolation interpolation) -> Image<T>`
    - `func threshold(T lower, T upper) -> Image<T>`
- `}`

Examples for `operator[x, y]`:
- `var centerValue = image[width/2, height/2]`
- `image[10, 20] = 0.0`
- `var gradientX = image[x + 1, y] - image[x - 1, y]`


### Row-Major

Images (unlike matrices) are stored row-major, like:
```
0 1 2
3 4 5
6 7 8
```


### Datatype & Precision

The default datatype is `Float32` (32-bit precision), well suited for image processing and machine vision.

For handling JPEG or PNG images you may use these derivations:
- `using ColorImage = cilia::Image<RGB<UInt8>>`
- `using Grey8Image = cilia::Image<UInt8>`
