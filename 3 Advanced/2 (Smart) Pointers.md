---
permalink: /advanced/smart-pointers/
---

## Short Smart Pointer Syntax

“Make simple things simple” (or at least short to write), to encourage use of smart pointers. When you need them. The use of plain local/stack-allocated or member variables is still preferred, of course.

- `Type* ptr` is a "raw" pointer
- `Type+ ptr` is a `UniquePtr<Type> ptr`
- `Type^ ptr` is a `SharedPtr<Type> ptr`
- `Type- ptr` is a `WeakPtr<Type> ptr`


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

### `new` instead of `makeUnique<>` & `makeShared<>`
In Cilia `new` is redefined as `makeUnique<Type> -> Type+`, and a _right value_ `Type+` can also be assigned to `Type^` and `Type*`.

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

You still can use `makeUnique<Type>()` and `makeShared<Type>()`:
```
Type+ uniquePtr = makeUnique<Type>()
Type^ sharedPtr = makeShared<Type>()
```

`makeShared<Type>()` is more efficient for shared pointers `T^`.  
`new` is kept, as it is a short and quite 'traditional' syntax, also used in C# and Java.


### `Type+` vs. `Type[10]+`

`Type+` is short for `UniquePtr<Type>`, i.e. a unique pointer to a single object.  
`Type[0]+` is short for `UniquePtr<Type[0]>`, i.e. a unique pointer to a C/C++ array of fixed but unknown size, `0` is just a dummy here. In C++ `unique_ptr<Type[]>` the `Type[]` is an "incomplete type". But in Cilia `Type[]` is an `Array<Type>`, so we use `Type[0]` instead.

```
ContactInfo+    contactInfoUniquePtr      = new ContactInfo
ContactInfo[0]+ contactInfoUniqueArrayPtr = new ContactInfo[10]
```

Not ~~`ContactInfo+ contactInfoUniqueArrayPtr = new ContactInfo[10]`~~:  
There is no array-to-single-element-pointer decay possible with `UniquePtr`, as that is a necessary distinction in its type.

Also possible (but _not_ recommended) is `ContactInfo[0]^ contactInfoUniqueArrayPtr = makeUnique<ContactInfo[10]>()` (whether it is a single-element- or an array-pointer is stored in the SharedPtrInfo).


### Interoperability with Other Languages
We can redefine `T^` and `T+` for special cases, like interoperability with garbage collected languages like C# and Java.

`T^` is defined via type traits `SharedPtrType`:
- For all C++/Cilia classes `T^` is `SharedPtr<T>`:  
  ```
  extension<type T> T {
      using SharedPtrType = SharedPtr<T>
  }
  ```
- Objective-C/Swift classes use their reference counting mechanism:
  ```
  class ObjectiveCObject {
      using SharedPtrType = ObjectiveCRefCountPtr
  }
  ```
- C#/.NET classes use garbage collected memory for instance/object allocation, add instance/object-pointers to the global list of C#/.NET instance pointers (with GCHandle and/or gcroot).  
  ```
  class DotNetObject {
      using SharedPtrType = DotNetGCPtr
  }
  ```
    - Access/dereferencing creates a temporary `DotNetGCPinnedPtr`, that pins the object (so the garbage collector cannot move it during access).
- Java classes use garbage collected memory, add pointers to the global list of Java instance pointers.  
  ```
  class JavaObject {
      using SharedPtrType = JavaGCPtr
  }
  ```
    - Probably very similar to C#/.NET.

`T+` is defined via type traits `UniquePtrType`:
- For C++/Cilia classes `T+` is `UniquePtr<T>`:
  ```
  extension<type T> T {
      using UniquePtrType = UniquePtr<T>
  }
  ```
- For Objective-C/Swift, C#/.NET, and Java the `UniquePtrType` will be very similar to the `SharedPtrType`, maybe even identical.
