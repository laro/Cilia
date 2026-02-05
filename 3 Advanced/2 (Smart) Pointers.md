---
permalink: /advanced/smart-pointers/
---

## Short Smart Pointer Syntax

“Make simple things simple” (or at least short to write), to encourage use of smart pointers. When you need them, the use of plain local, stack-allocated variables is still preferred, of course.

- `Type* pointer` is a "raw" pointer.
- `Type+ pointer` is short for `UniquePtr<Type>`.
- `Type^ pointer` is short for `SharedPtr<Type>`.
- `Type- pointer` is short for `WeakPtr<Type>`.


### `Type* pointer`
A "raw" pointer is a classical C/C++ pointer, in Cilia typically without ownership.  
In C/C++ the ownership depends, case by case.

A "raw" pointer is still possible in Cilia, but it is considered unsafe.
```
ContactInfo* contactInfoPtr = new ContactInfo
// With classical/raw pointers you need to free the objects yourself.
delete contactInfoPtr

ContactInfo* contactInfoPtr = new ContactInfo[10]
// You need to distinguish single-element- and array-pointers yourself.
delete[0] contactInfoPtr
```

### `Type+ pointer`
This is a "pointer plus ownership", a pointer with (exclusive) ownership: the object will be deleted when the pointer is deleted (e.g. goes out of scope).

- `T+` is short for `UniquePtr<T>`,
    - i.e. a unique pointer to a single object.
- `T[0]+` is short for `UniquePtr<T[0]>`,
    - i.e. a unique pointer to a C/C++ array of fixed but unknown size, `0` is just a dummy here.
    - In C++ `unique_ptr<T[]>` the `T[]` is an "incomplete type". But in Cilia `T[]` is an `Array<T>`, so we use `T[0]` instead.

```
ContactInfo+    contactInfoUniquePtr      = makeUnique<ContactInfo>()
ContactInfo[0]+ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()
```
Not ~~`ContactInfo+ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()`~~:  
There is no array-to-single-element-pointer decay possible with `UniquePtr`, as that is a necessary distinction in its type.

TODO: Better just `make<T>(...) -> T+`, as "unique" is "hard to write".


### `Type^ pointer`
A pointer with shared ownership: the object will be deleted when all "its" pointers are deleted (e.g. go out of scope).  
Inspired by C++/CLI (so it is a proven possiblilty).

```
ContactInfo^ contactInfoSharedPtr      = makeShared<ContactInfo>()`
ContactInfo^ contactInfoSharedArrayPtr = makeShared<ContactInfo[10]>()
```
Also possible (but _not_ recommended) is `ContactInfo[0]^ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()` (whether it is a single-element- or an array-pointer is stored in the SharedPtrInfo).

`T^`/`SharedPtr<T>` can take over the pointer from _rvalue_ `T+`/`UniquePtr<T>` and `T[0]+`/`UniquePtr<T[0]>` (as in C/C++):
```
ContactInfo^ contactInfoSharedPtr = new ContactInfo
ContactInfo^ contactInfoSharedPtr = move(contactInfoUniquePtr)
// The contactInfoUniquePtr is a NullPtr afterwards.
```

### `Type- pointer`
A weak pointer is a pointer to a shared pointer.  
So with  
`T- weakPointerToWindow = sharedPointerToWindow`  
you can write  
`weakPointerToWindow?.close()`  
instead of
```
if (Window^ window = weakPointerToWindow.lock()) {
    window->close()
}
```

### Interoperability with Other Languages
We may redefine `T^` and `T+` for special cases:
- `T^` is defined via type traits `SharedPtrType`,  
    - For C++/Cilia classes `T^` is `SharedPtr<T>`:
        - `using<type T> T::SharedPtrType = SharedPtr<T>`
    - Objective-C/Swift classes use their reference counting mechanism:
        - `using ObjectiveCObject::SharedPtrType = ObjectiveCRefCountPtr`
    - C#/.NET classes use garbage collected memory for instance/object allocation, add instance/object-pointers to the global list of C#/.NET instance pointers (with GCHandle and/or gcroot).
        - `using DotNetObject::SharedPtrType = DotNetGCPtr`
        - Access/dereferencing creates a temporary `DotNetGCPinnedPtr`, that pins the object (so the garbage collector cannot move it during access).
    - Java classes use garbage collected memory, add pointers to the global list of Java instance pointers.  
        - `using JavaObject::SharedPtrType = JavaGCPtr`
        - Probably very similar to C#/.NET.
- `T+` is defined via type traits `UniquePtrType`.
    - For C++/Cilia classes `T+` is `UniquePtr<T>`:
        - `using<type T> T::UniquePtrType = UniquePtr<T>`
