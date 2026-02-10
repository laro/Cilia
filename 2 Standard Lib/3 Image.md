---
permalink: /standard-lib/image/
---

## Image

```
Image<T = Float32>
```

Common image-processing examples:
```
gaussianBlur<type T>(const Image<T>& image, Float sigma) -> Image<T>
medianFilter<type T>(const Image<T>& image, Int kernelSize) -> Image<T>
sobelEdges<type T>(const Image<T>& image) -> Image<T>
resize<type T>(const Image<T>& image, Int width, Int height, Interpolation interpolation) -> Image<T>
threshold<type T>(const Image<T>& image, T lower, T upper) -> Image<T>
```

Same operations as in-place member functions:
```
image.gaussianBlur(sigma)
image.medianFilter(kernelSize)
image.sobelEdges()
image.resize(width, height, Interpolation::Bilinear)
image.threshold(lower, upper)
```

Examples for `operator[x, y]`:
```
var centerValue = image[width/2, height/2];
image[10, 20] = 0.0f;
var gradientX = image[x + 1, y] - image[x - 1, y];
```

- `ImageView`


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
