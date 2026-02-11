---
permalink: /standard-lib/image/
---

## Image

```
class Image<type T = Float32> : linalg::Matrix<T> {
    ...
}
```
Basically a two-dimensional array with dynamic size.

Pixel access with `operator[x, y]`:
- `var centerValue = image[width/2, height/2]`
- `image[10, 20] = 0.0`
- `var gradientX = image[x + 1, y] - image[x - 1, y]`

`ImageView` as "read-only reference" of sub-areas (with stride).  
`ImageBasicView` as "read-only reference" with continuous pixels (i.e. no stride, just cut off at top or bottom).

Common image-processing member functions:
- `extension Image<type T> {`
    - `func gaussianBlur(Float sigma) -> Image<T>&`
    - `func medianFilter(Int kernelSize) -> Image<T>&`
    - `func sobelEdges() -> Image<T>&`
    - `func resize(Int width, Int height, Interpolation interpolation) -> Image<T>&`
    - `func threshold(T lower, T upper) -> Image<T>&`
- `}`

Same operations as free functions:
- `func gaussianBlur<type T>(Image<T> image, Float sigma) -> Image<T>`
- `func medianFilter<type T>(Image<T> image, Int kernelSize) -> Image<T>`
- `func sobelEdges<type T>(Image<T> image) -> Image<T>`
- <span class="wide">`func resize<type T>(Image<T> image, Int width, Int height, Interpolation interpolation) -> Image<T>`</span>
- `func threshold<type T>(Image<T> image, T lower, T upper) -> Image<T>`


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
- `using RGB24Image = cilia::Image<RGB<UInt8>>`
- `using Gray8Image = cilia::Image<UInt8>`
