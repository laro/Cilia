---
title: Standard Library.Arrays
permalink: /standard-library/arrays/
order: 0
---

## Array & ArrayView

- `Int[] dynamicArrayOfIntegers`
    - „Dynamic array“ with **dynamic size**
      ```
      Int[] array = [0, 1, 2]
      array[0] = 0
      array[1] = 0
      array[2] = 0
      array[3] = 0  // Runtime error, no compile time bounds check
      ```
    - "Make simple things simple",  
      having a short and traditional syntax for dynamic arrays should encourage people to use it.
    - `T[] arr` is the short form of `cilia::Array<T> arr`
        - Also `[T] arr`, as in Swift or Rust, has some merits.  
          And `[3 T] arr` for fixed sized arrays would be fine for me (I don't like `[T;3] arr`), but I'll stick with the more traditional `T[] arr` (like C# and Java).
    - The long form is called `Array<T>`, not ~~`Vector<T>`~~, because
        - that's the more traditional wording,
        - by using the word "vector", the purpose of this class is not immediately clear (especially not for users of many languages other than C++, not even C),
        - `Vector` could too easily collide with the mathematical vector (as used in linear algebra or geometry).
    - "Raw" C/C++ arrays are handled with `T*` instead.
    - `std::array` is called `cilia::StaticArray` instead.
    - In C/C++ `T[]` means "array of certain (inferred) size",
        - but that can be replaced with `T*` and `T[N]`.
        - Also see [https://cplusplus.com/forum/beginner/267321/#msg1150228](https://cplusplus.com/forum/beginner/267321/#msg1150228)

- `Int[3] arrayOfThreeIntegers`  
  (instead of ~~`Int arrayOfThreeIntegers[3]`~~ in C/C++)
    - „Static array“ with **fixed size**
      ```
      Int[3] array = [0, 1, 2]
      array[0] = 0
      array[1] = 0
      array[2] = 0
      array[3] = 0  // Compilation error, due to compile time bounds check
      ```
    - `arrayOfThreeIntegers.size()` -> `3`
        - realized as extension function  
          `func<type T, Int N> T[N]::size() -> Int { return N }`

- Use `T+`/`UniquePtr<T>` for "raw" C/C++ arrays of arbitrary size.  
  But array subscript with `Int+` is unsafe.
    - ```
      Int+ array = new Int[3]  // Array-to-pointer decay possible
      unsafe {
          array[0] = 0
          array[1] = 0
          array[2] = 0
          array[3] = 0  // Undefined behaviour, no bounds check at all
      }
      ```
    - Using `Int*` for arrays is possible but generally unsafe.
        - ```
          Int+ uniquePtrToArray = new Int[3]  // Array-to-pointer decay possible
          unsafe {
              Int* array = uniquePtrToArray.release()
              array[0] = 0
              array[1] = 0
              array[2] = 0
              array[3] = 0  // Undefined behaviour, no bounds check at all
              delete[] array
          }
          ```
        - ```
          unsafe {
              Int* array = reinterpretCastTo<Int*>(malloc(3 * sizeof(Int)))
              array[0] = 0
              array[1] = 0
              array[2] = 0
              array[3] = 0  // Undefined behaviour, no bounds check at all
              free(array)
          }
          ```
    - Actually this is how to handle pointer to array of `Int` "properly":  
      ```
      Int[3]+ arrayPtr = new Int[3]
      (*arrayPtr)[0] = 0
      (*arrayPtr)[1] = 0
      (*arrayPtr)[2] = 0
      (*arrayPtr)[3] = 0  // Compilation error, due to compile time bounds check
      ```
        - But raw pointer access is still `unsafe`:  
          ```
          unsafe {
              Int[3]* arrayPtr = (new Int[3]).release()
              (*arrayPtr)[0] = 0
              (*arrayPtr)[1] = 0
              (*arrayPtr)[2] = 0
              (*arrayPtr)[3] = 0  // Compilation error, due to compile time bounds check
              delete[] arrayPtr
          }
          ```

- Examples:
    - `Int[] dynamicArrayOfInt`
    - `Int[3] arrayOfThreeInt`
    - `Int[3]& referenceToArrayOfThreeInt`
    - `Int[3]* pointerToArrayOfThreeInt`
    - `Int[3][]& referenceToDynamicArrayOfArrayOfThreeInt`
    - `String*[] dynamicArrayOfPointersToString`

- ArrayView AKA Slice AKA Subarray
    - `var subarray = array[1..2]`
    - `var subarray = array[1..<3]`
    - Incomplete ranges (need lower and/or upper bounds before use) are
      typcally implemented as inline functions that determine the concrete bounds and then call `array[start..end]` (or one of the exclusive counterparts).
        - `var subarray = array[..2]`
        - `var subarray = array[..]`
    - See Rust [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)

- Multidimensional array
    - dynamic size
        - `Int[,] dynamic2DArray`  
            - `T[,] array` is the short form of `cilia::MDArray<2, T> array`
        - `Int[,,] multidimensionalDynamicArray`  
            - `T[,,] array` is the short form of `cilia::MDArray<3, T> array`
        - and so on:  
            - `cilia::MDArray<N, T>`
    - static size
        - `Int[3, 2, 200]`
            - Multidimensional static array  
              ```
              Int[3, 2, 200] intArray3D
              intArray3D[2, 1, 199] = 1
              ```
            - `cilia::StaticMDArray<Int, 3, 2, 200> intArray3D`

- Mixed forms of static and dynamic array
    - `Int[3][,] dynamic2DArrayOfArrayOfThreeInt`
    - `Int[3,4][] dynamicArrayOfThreeByFourArrayOfInt`


## Associative Array

- AKA Map (or Dictionary)
- `TValue[TKey]` as short form of `Map<TKey, TValue>`
    - e.g. `ContactInfo[String] contactInfoForID` as short form  
      of `Map<String, ContactInfo> contactInfoForID`,
    - as [in D](https://dlang.org/spec/hash-map.html).
    - There is no difference between these two, but "OtherMap<String, ContactInfo> contactInfoForID" allows you to select other map variants (SortedMap, HashMap etc.) if necessary.
- "Make simple things simple",  
  having a short syntax for associative arrays so they are easy to use.
- Maybe partial template specialization:
    - `Map<Int, ...>` is a `HashMap`
    - `Map<String, ...>` is a `SortedMap`
