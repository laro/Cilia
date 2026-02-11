---
permalink: /advanced/smart-pointers/
---

## Short Smart Pointer Syntax

"Make simple things simple" (or at least short to write),  
to encourage the use of smart pointers.

- `T* ptr` is a "raw" pointer
- `T+ ptr` is a `UniquePtr<T>`
- `T^ ptr` is a `SharedPtr<T>`
- `T- ptr` is a `WeakPtr<T>`

> The use of plain local/stack-allocated or of member variables is still preferred, of course.  
> Use (smart) pointers only when you need them.


### `T+` pointer

This is a "pointer plus ownership", a pointer with (exclusive) ownership: the object will be deleted when the pointer is destroyed (e.g. when it goes out of scope). Unique pointers have _zero_ overhead over plain, raw C/C++ pointers. 

```
ContactInfo+ uniquePtrTocontactInfo = new ContactInfo
```


### `T^` pointer

A pointer with shared ownership: the object will be deleted when all of "its" pointers are destroyed (e.g. when all of them go out of scope).  
Inspired by C++/CLI.

```
ContactInfo^ sharedPtrToCcontactInfo = new ContactInfo
```

For shared pointers this is more efficient (due to a single-allocation optimization):
```
ContactInfo^ sharedPtrToCcontactInfo = makeShared<ContactInfo>()
```


### `T-` pointer

A weak pointer observes an object managed by a shared pointer without extending its lifetime (it does not increase the reference count).  
You can `lock()` it to obtain a `T^` if the object is still alive.  

Initialized as  
`T- weakPointerToWindow = sharedPointerToWindow`  
you can write  
```
Window^ shreadPtrToWindow = weakPointerToWindow.lock()
if shreadPtrToWindow {
    shreadPtrToWindow->show()
    // ...
    shreadPtrToWindow->close()
}
```
or
```
weakPointerToWindow?.close()
```


### `T*` pointer

A "raw" pointer is a classical C/C++ pointer. Ownership depends, case by case. In Cilia a `T*` typically is without ownership, as for pointers _with_ ownership you would use a `T+` pointer instead.

A "raw" pointer is considered **unsafe** in Cilia:
```
unsafe {
    ContactInfo* contactInfoPtr = new ContactInfo
    delete contactInfoPtr  // With classical/raw pointers you need to free the objects yourself.

    ContactInfo[0]* contactInfoArrayPtr = new ContactInfo[10]
    delete[0] contactInfoArrayPtr  // You need to distinguish between single-element and array pointers yourself.
}
```


### Dynamic Allocation with `new`

`new` is kept as a short and quite 'traditional' syntax (also used in C# and Java) for dynamic/heap allocation. `new T` returns a `T+`/`UniquePtr<T>`, so that is the "default type" for pointers:
```
ContactInfo+ uniquePtrToContactInfo = new ContactInfo
var alsoAUniquePtrToContactInfo = new ContactInfo
```

In Cilia,
1. `new` acts like `makeUnique<T> -> T+`, and
2. a _right value_ `T+` can also be moved to a `T^`,

so now you can use `new` for both pointer types:
```
T+ uniquePtr = new T
T^ sharedPtr = new T
```
```
T+ uniquePtr = new T
T^ sharedPtr = move(uniquePtr)  // The uniquePtr is a NullPtr afterwards.
```

With `T+`/`T^` you do _not_ need to call `delete` yourself, that is done by the smart pointer.

In Cilia a _right value_ `T+` can even be assigned to `T*`,
so you still can use `new` for raw pointers.  
But it is inconvenient to use as
- it is allowed in unsafe code only,
- you need to manage lifetime of the instance yourself (i.e. call `delete`), and
- you need to distinguish between a pointer to a single element and a pointer to an array (i.e. call `delete` or `delete[0]`).

```
unsafe {
    T* ptr = new T
    delete ptr

    T* ptr = new T[10]
    delete[10] ptr
}
```


### `T+`/`T^` vs. `T[0]+`/`T[0]^`

`T+`/`T^` is a unique/shared pointer to a _single_ object.  
`T[0]+`/`T[0]^` is a unique/shared pointer to a C/C++ _array_ of fixed but unknown size, `0` is just a dummy here.

In C++ `unique_ptr<T[]>`/`shared_ptr<T[]>`, the `T[]` is an "incomplete type". But in Cilia `T[]` is an `Array<T>`, so we use `T[0]` instead.

```
T+    uniquePtr        = new T
T[0]+ uniquePtrToArray = new T[10]

T^    sharedPtr        = new T
T[0]^ sharedPtrToArray = new T[10]
```

Not ~~`T+ uniquePtrToArray = new T[10]`~~. There is no array-to-single-element-pointer decay possible with `T+`/`UniquePtr<T>` or `T^`/`SharedPtr<T>`, as that is a necessary distinction in the type.
