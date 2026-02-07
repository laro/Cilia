---
permalink: /advanced/smart-pointers/
---

## Short Smart Pointer Syntax

“Make simple things simple” (or at least short to write), to encourage use of smart pointers.

- `Type* ptr` is a "raw" pointer
- `Type+ ptr` is a `UniquePtr<Type> ptr`
- `Type^ ptr` is a `SharedPtr<Type> ptr`
- `Type- ptr` is a `WeakPtr<Type> ptr`

> The use of plain local/stack-allocated or member variables is still preferred, of course.  
> Use (smart) pointers only when you need them. 


### Type+ pointer

This is a "pointer plus ownership", a pointer with (exclusive) ownership: the object will be deleted when the pointer is deleted (e.g. goes out of scope).

```
ContactInfo+ contactInfoUniquePtr = new ContactInfo
```


### Type^ pointer

A pointer with shared ownership: the object will be deleted when all "its" pointers are deleted (e.g. go out of scope).  
Inspired by C++/CLI.

```
ContactInfo^ contactInfoSharedPtr = new ContactInfo
```


### Type- pointer

A weak pointer is a pointer to a shared pointer.  

With  
`T- weakPointerToWindow = sharedPointerToWindow`  
you can write  
`weakPointerToWindow?.close()`  
and
```
if (Window^ window = weakPointerToWindow.lock()) {
    window->show()
    // ...
    window->close()
}
```

### Type* pointer
A "raw" pointer is a classical C/C++ pointer. Ownership depends, case by case, but in Cilia it typically is without ownership.  

A "raw" pointer is considered **unsafe** in Cilia:
```
unsafe {
    ContactInfo* contactInfoPtr = new ContactInfo
    delete contactInfoPtr  // With classical/raw pointers you need to free the objects yourself.

    ContactInfo[0]* contactInfoPtr = new ContactInfo[10]
    delete[0] contactInfoPtr  // You need to distinguish single-element- and array-pointers yourself.
}
```

### Dynamic Allocation with `new`
`new` is kept as a short and quite 'traditional' syntax (also used in C# and Java) for dynamic allocation (heap allocation). In Cilia `new` is redefined as `makeUnique<Type> -> Type+`, and as a _right value_ `Type+` can also be assigned to `Type^` and `Type*`, you can use `new` for all three pointer types:
```
Type+ uniquePtr = new Type
Type^ sharedPtr = new Type

unsafe {
    Type* ptr = new Type
    delete ptr
}
```
```
Type+ uniquePtr = new Type
Type^ sharedPtr = move(uniquePtr)  // The uniquePtr is a NullPtr afterwards.
```

You still can use `makeShared<Type>()` (that is more efficient for shared pointers `T^`) and `makeUnique<Type>()`, of course:
```
Type+ uniquePtr = makeUnique<Type>()
Type^ sharedPtr = makeShared<Type>()
```


### `Type+`/`Type^` vs. `Type[0]+`/`Type[0]^`

`Type+`/`Type^` is short for `UniquePtr<Type>`/`SharedPtr<Type>`, i.e. a unique/shared pointer to a _single_ object.  
`Type[0]+`/`Type[0]^` is short for `UniquePtr<Type[0]>`/`SharedPtr<Type[0]>`, i.e. a unique pointer to a C/C++ _array_ of fixed but unknown size, `0` is just a dummy here.

In C++ `unique_ptr<Type[]>`/`shared_ptr<Type[]>`, the `Type[]` is an "incomplete type". But in Cilia `Type[]` is an `Array<Type>`, so we use `Type[0]` instead.

```
Type+    uniquePtr        = new Type
Type[0]+ uniquePtrToArray = new Type[10]

Type^    sharedPtr        = new Type
Type[0]^ sharedPtrToArray = new Type[10]
```

Not ~~`Type+ uniquePtrToArray = new Type[10]`~~. There is no array-to-single-element-pointer decay possible with `T+`/`UniquePtr<T>` or `T^`/`SharedPtr<T>`, as that is a necessary distinction in the type.
