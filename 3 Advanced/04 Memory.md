---
permalink: /standard-lib/memory/
description: "Memory allocation with new or special/custom allocators."
---

# Memory Allocation

## Dynamic Allocation with `new`

Operator `new` is kept for dynamic/heap allocation, as a short and quite 'traditional' syntax (also used in C# and Java).
```
var imagePtr = new Image(1920, 1080, 0.0)
```

As an alternative, there is a function template syntax that can be more easily adapted for use with memory allocators.
```
var imagePtr = new<Image>(1920, 1080, 0.0)
var imagePtr = allocator.new<Image>(1920, 1080, 0.0)
```

> Note:  
> This assumes that `new`/`delete` can be both operator keyword and function 
> name. That should be possible with a context-sensitive parser.
> If that causes too many problems, we'll have to fall back on other keywords,
> such as `create`/`destroy`.


## Memory Allocators

For a plain `new` (operator as well as function template syntax) the default memory allocator is used. For special purposes, specialized allocators can be used instead:
- Arena allocator for very fast allocations (instead of the typical free-list-with-pools-allocator).
- Physical, or DMA memory in the OS kernel (instead of plain kernel/virtual memory).
- Fast but limited on-chip memory (instead of slow but plenty external memory).


Some allocators will be used via an instance object, e.g. the Arena allocator:
```
ArenaAllocator arena(20'000'000)
var imagePtr = arena.new<Image>(1920, 1080, 0.0)
...
arena.reset()
```


Some allocators might be used via static functions, as there is only one instance anyway, e.g. the PhysicalMemory allocator:
```
var imagePtr = PhysicalMemory::new<Image>(1920, 1080, 0.0)
```


### Memory Allocator

Abstract base class as interface for "all" memory allocators.

```
class MemoryAllocator {
    virtual func malloc(Int size, Int alignment = 16) -> Byte* = 0
    virtual func free(Byte*) = 0

    func new<type T>(TArgs args ...) -> T+ {
        Byte* address = malloc(sizeof(T))
        new (address) T(args ...)
        return address
    }
    func delete<type T>(T* address) {
        if address == NullPtr {
            return
        }

        address->~T()
        free(address)
    }
}
```

### User Space

Default memory allocator using heap memory.
Would use `malloc`/`free` to be compatible with C++.
```
class Memory : MemoryAllocator {
    override func malloc(Int size, Int alignment = 16, Int alignment) -> Byte* {
        return Byte*(::malloc(size))
    }
    override func free(Byte* address) {
        ::free(address)
    }
}
```


### Microcontroller

The on-chip memory of an Pi Pico is very fast but quite limited.
```
class FastMemory : MemoryAllocator {
    override func malloc(Int size, Int alignment = 16) -> Byte* { ... }
    override func free(Byte* address)  { ... }
}
```

PSRAM attached via QSPI.
Probably the default, simply as much more memory of this type is available.
```
class ExternalMemory : MemoryAllocator {
    override func malloc(Int size, Int alignment = 16) -> Byte* { ... }
    override func free(Byte* address)  { ... }
}
```


### Kernel Space

The default memory allocator in kernel space is based on `kvmalloc()`:
- `kmalloc()`/`kfree()` for small allocations,
- `vmalloc()`/`vfree()` for bigger allocations.

```
class Memory : MemoryAllocator {
    override func malloc(Int size, Int alignment = 16) -> Byte* {
        Byte* address = Byte*(kmalloc(size, __GFP_NOWARN))
        if address !=)NullPtr
            return address

        return vmalloc(size)
    }

    override func free(Byte* address) {
        if is_vmalloc_addr(address) {
            vfree(address)
        } else {
            kfree(address)
        }
    }
}
```


#### Physical Memory

Will allocate in page size.

```
class PhysicalMemory : MemoryAllocator {
    override func malloc(Int size, Int alignment = system::PageSize) -> Byte* { ... }
    override func free(Byte* address)  { ... }
}
```


#### DMA Memory

Some physical memory pages may be out of reach for DMA, so better use this (when you need DMA).
Will allocate in page size, too.

```
class DmaMemory : MemoryAllocator {
    override func malloc(Int size, Int alignment = system::PageSize) -> Byte* { ... }
    override func free(Byte* address)  { ... }
}
```


### Arena Allocator

Allocates memory sequentially from a contiguous memory region (the arena).
Individual objects are not freed; the entire arena is released or reset at once.
This makes allocation extremely fast.

```
class Arena : MemoryAllocator {
    Arena(Int size) {
        memory = ::alloc(size)
        next = memoy
    }
    ~Arena() {
        ::free(memory)
    }

    override func malloc(Int size, Int alignment = 16) -> Byte* {
        Byte* address = next
        next += size
        return address
    }
    override func free(Byte* address) {
        // Does nothing
    }

protected:
    Byte* memory
    Byte* next
}
```


### Temporary Memory Allocator

A full fledged memory allocator, meant to keep allocations for a special purpose cache-friendly "in one place".

Should be based on a free-list and several pools for e.g.  
16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256,
320, 384, 448, 512 bytes.

```
class TemporaryMemory : MemoryAllocator {
    TemporaryMemory(Int size) {
        // Allocate a single large block of memory, e.g. via HeapAlloc()
    }
    ~TemporaryMemory() {
        // Free the large block of memory, e.g. via HeapFree()
    }

    override func malloc(Int size, Int alignment = 16) -> Byte* { ... }
    override func free(Byte* address) { ... }

protected:
    Byte* memory
    // ...
}
```


## Pointers and Ownership

### `new` for `T+`

`new T` returns a `T+`, so that is the "default type" for pointers:
```
ContactInfo+ uniquePtrToContactInfo = new ContactInfo
var alsoAUniquePtrToContactInfo = new ContactInfo
```

### `new` for `T^`

In Cilia,
1. `new` acts like `makeUnique<T>() -> T+`, and
2. a _right value_ `T+` can also be moved to a `T^`,

so now you can use `new` for both pointer types:
```
T+ uniquePtr = new T
T^ sharedPtr = new T // Note: nice and short, but does two allocations
```
```
T+ uniquePtr = new T
T^ sharedPtr = move(uniquePtr)  // The uniquePtr is a NullPtr afterwards.
```

With `T+`/`T^` you do _not_ need to call `delete` yourself, that is done by the smart pointer.

### `new` for `T*`
In Cilia a _right value_ `T+` can even be assigned to `T*`,
so you still can use `new` for raw pointers.  
But it is inconvenient to use, as
- it is allowed in unsafe code only,
- you need to manage lifetime of the instance yourself (i.e. call `delete`), and
- you need to distinguish between a "pointer to a single element" and a "pointer to an array" (i.e. call `delete` or `delete[0]`).

```
unsafe {
    T* ptr = NullPtr

    ptr = new T
    delete ptr

    ptr = new T[10]
    delete[0] ptr
}
```
