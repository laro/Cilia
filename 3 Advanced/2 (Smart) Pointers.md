---
permalink: /advanced/smart-pointers/
---

## Short Smart Pointer Syntax

“Make simple things simple” (or at least short to write),  
encourage use of smart pointers (when you need to).

    - **`Type* pointer`** is a "raw" pointer,
        - the classical C/C++ pointer.
    - **`Type+ pointer`** is a "unique pointer",
        - short for **`UniquePtr<T>`.
    - **`Type^ pointer`** is a "shared pointer",
        - short for `SharedPtr<T>`.
    - **`Type- pointer`** is a "weak pointer",
        - short for `WeakPtr<T>`.

### `Type* pointer`
A "raw" pointer typically has no ownership.

A classical C/C++ "raw" pointer is still possible, but unsafe.
- `ContactInfo* contactInfoPtr = new ContactInfo`  
    `delete contactInfoPtr` (with classical/raw pointers you need to free the objects yourself)
- `ContactInfo* contactInfoPtr = new ContactInfo[10]`  
    `delete[0] contactInfoPtr` (you need to distinguish single-element- and array-pointers yourself)

### `Type+ pointer`
A "pointer plus ownership", a pointer with (exclusive) ownership: the object will be deleted when the pointer is deleted (e.g. goes out of scope).
- `T+` is short for **`UniquePtr<T>`** (i.e. a unique pointer to a single object)
- `T[0]+` is short for **`UniquePtr<T[0]>`** (i.e. a unique pointer to a C/C++ array of fixed but unknown size, `0` is just a dummy here)
- In C++ `unique_ptr<T[]>` the `T[]` is an "incomplete type". But in Cilia `T[]` is an `Array<T>`, so we use `T[0]` instead.

- **`makeUnique<T>(...) -> T+`**,
    - `ContactInfo+ contactInfoUniquePtr = makeUnique<ContactInfo>()`.
    - `ContactInfo[0]+ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()`  
        not ~~`ContactInfo+ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()`~~ (there is no array-to-    single-element-pointer decay possible with `UniquePtr`, as that is a necessary distinction in its type).
- Better just **`make<T>(...) -> T+`**, as "unique" is "hard to write".

### `Type^ pointer`
A pointer with shared ownership: the object will be deleted when all "its" pointers are deleted (e.g. go out of scope).  
Inspired by C++/CLI (so its a proven possiblilty).
        - **`makeShared<T>(...)`**,
            - `ContactInfo^ contactInfoSharedPtr = makeShared<ContactInfo>()`.
            - `ContactInfo^ contactInfoSharedArrayPtr = makeShared<ContactInfo[10]>()`  
              also possibler(but not recommended) is ~~`ContactInfo[0]^ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()`~~ (whether it is a single-element- or an array-pointer is stored in the SharedPtrInfo).
        - `T^`/`SharedPtr<T>` can take over the pointer from _rvalue_ `T+`/`UniquePtr<T>` and `T[0]+`/`UniquePtr<T[0]>` (as in C/C++):
            - `ContactInfo^ contactInfoSharedPtr = new ContactInfo`
            - `ContactInfo^ contactInfoSharedPtr = move(contactInfoUniquePtr)`
                - The `contactInfoUniquePtr` is a `NullPtr` afterwards.

### `Type- pointer`
A pointer to a shared pointer.  
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
