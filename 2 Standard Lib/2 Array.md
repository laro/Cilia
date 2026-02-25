---
permalink: /standard-lib/array/
description: "Cilia Array and ArrayView: Int[] dynamic arrays, Int[10] static, associative arrays. Simple syntax for common cases."
---

# Array & ArrayView

"Make simple things simple",  
having a short and traditional syntax not only for static, but also for dynamic and associative arrays should encourage people to use it.


## Dynamic Array

**`Int[] dynamicArrayOfIntegers`** is an array with **dynamic size**.
```
Int[] array = [0, 1, 2]
array[0] = 0
array[1] = 0
array[2] = 0
array[3] = 0  // Runtime error, no compile time bounds check
```

`T[] arr` is the short form of `cilia::Array<T> arr`.

The long form is called `Array<T>`, not ~~`Vector<T>`~~, because
- that's the more traditional wording,
- by using the word "vector", the purpose of this class is not immediately clear (especially not for users of many languages other than C++, not even C),
- `Vector` could too easily collide with the mathematical vector (as used in linear algebra and geometry).

"Raw" C/C++ arrays are handled with `T*` instead.  
`std::array` is called `cilia::StaticArray` instead.

In C/C++ `T[]` means "array of certain (inferred) size",
- but that can be replaced with `T*` and `T[N]`.
- Also see [https://cplusplus.com/forum/beginner/267321/#msg1150228](https://cplusplus.com/forum/beginner/267321/#msg1150228)


## Static Array
**`Int[3] arrayOfThreeIntegers`** is an array with **fixed size** (instead of ~~`Int arrayOfThreeIntegers[3]`~~ in C/C++).
```
Int[3] array = [0, 1, 2]
array[0] = 0
array[1] = 0
array[2] = 0
array[3] = 0  // Compilation error, due to compile time bounds check
```

`arrayOfThreeIntegers.size()` -> `3`  
is realized as extension function
```
extension<type T, Int N> T[N] {
    func size() -> Int { return N }
}
```

Use `T+`/`UniquePtr<T>` for "raw" C/C++ arrays of arbitrary size.  
But array subscript with `Int+` is unsafe.
```
Int[0]+ array = new Int[3]
unsafe {
    array[0] = 0
    array[1] = 0
    array[2] = 0
    array[3] = 0  // Undefined behaviour, no bounds check at all
}
```

Using `Int*` for arrays is possible but generally unsafe.
```
Int[0]+ uniquePtrToArray = new Int[3]
unsafe {
    Int* array = move(uniquePtrToArray)
    array[0] = 0
    array[1] = 0
    array[2] = 0
    array[3] = 0    // Undefined behaviour, no bounds check at all
    delete[] array  // Array-delete!
}
```
```
unsafe {
    Int* array = reinterpretCastTo<Int*>(malloc(3 * sizeof(Int)))
    array[0] = 0
    array[1] = 0
    array[2] = 0
    array[3] = 0  // Undefined behaviour, no bounds check at all
    free(array)
}
```

Actually this is how to handle pointer to array of `Int` "properly":  
```
Int[3]+ arrayPtr = new Int[3]
(*arrayPtr)[0] = 0
(*arrayPtr)[1] = 0
(*arrayPtr)[2] = 0
(*arrayPtr)[3] = 0  // Compilation error, due to compile time bounds check
```

But raw pointer access is still `unsafe`:  
```
unsafe {
    Int[3]* arrayPtr = new Int[3]
    (*arrayPtr)[0] = 0
    (*arrayPtr)[1] = 0
    (*arrayPtr)[2] = 0
    (*arrayPtr)[3] = 0  // Compilation error, due to compile time bounds check
    delete[] arrayPtr   // Array-delete!
}
```


## Examples

- `Int[] dynamicArrayOfInt`
- `Int[3] arrayOfThreeInt`
- `Int[3]& referenceToArrayOfThreeInt`
- `Int[3]* pointerToArrayOfThreeInt`
- `Int[3][]& referenceToDynamicArrayOfArrayOfThreeInt`
- `String*[] dynamicArrayOfPointersToString`


## ArrayView

AKA Slice AKA Subarray.
- `var subarray = array[1..2]`
- `var subarray = array[1..<3]`

Incomplete ranges (need lower and/or upper bounds before use) are typically implemented as inline functions that determine the concrete bounds and then call `array[start..end]` (or one of the exclusive counterparts).
- `var subarray = array[..2]`
- `var subarray = array[..]`

See Rust [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)


## Multidimensional Array

- dynamic size
    - **`Int[,] dynamic2DArray`**  
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
    - `Int[3,4][] dynamicArrayOfArrayOfThreeByFourInt`
- `MDArrayView`


## Associative Array

AKA Map (or Dictionary).  
**`TValue[TKey]`** as short form of `Map<TKey, TValue>` (as [in D](https://dlang.org/spec/hash-map.html)).

There is no difference between these two forms, but the long form is necessary for other map variants (SortedMap, HashMap, etc.).

Example:
```
ContactInfo[String] contactInfoForID
// as short form of  
Map<String, ContactInfo> contactInfoForID
```

Maybe partial template specialization:
- `Map<Int, ...>` is a `HashMap`
- `Map<String, ...>` is a `SortedMap`
