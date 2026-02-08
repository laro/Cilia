---
permalink: /standard-library/image/
---

## Image

- `cilia::Image<T = Float32>`
- Almost like `cilia::Matrix`,  
  but stored row-major, like:
  ```
  0 1 2
  3 4 5
  6 7 8
  ```
- `ImageView`

### Datatype & Precision
The default datatype is `Float32` (32-bit precision), better suited for image processing and machine vision.

For handling JPEG or PNG images you may use these derivations:
- `using ColorImage = cilia::Image<RGB<UInt8>>`
- `using ImageGrey8 = cilia::Image<UInt8>`
