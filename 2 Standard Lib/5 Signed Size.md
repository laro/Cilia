---
permalink: /basics/signed-size/
---

## Signed Size

Use `Int` (i.e. signed) as the return type for `*.size()`.

Mixing signed and unsigned integers is error-prone, and even pure unsigned arithmetic is often unintuitive and dangerous.

Classic C/C++ pitfall:  
`aUInt - 1 >= 0` is _always_ true (even if `aUInt` is `0`)
    
When working with sizes, subtraction is common. The moment you compute differences, you need a signed type anyway. Therefore ~~`Size`~~ and ~~`SSize`~~/~~`PtrDiff`~~ are unnecessary — just use `Int`. `UInt` should be reserved for rare cases like hardware registers, bit masks, and flags — _not_ for sizes.

See also Going Native 2012, Day 2, Interactive Panel: Ask Us Anything
- [42:41 - 45:28](https://youtu.be/Puio5dly9N8?feature=shared&t=2561)
    - Bjarne Stroustrup and Herb Sutter recommend using _signed_ integer.
- [1:02:51 - 1:03:14](https://youtu.be/Puio5dly9N8?feature=shared&t=3771)
    - Herb Sutter and Chandler Carruth about _unsigned_ `size_t` in the C++ STL containers: "They are wrong", "We are sorry"

Anyone who needs more than 2GB of data in a single "byte array", should please use a 64 bit platform.

For bounds checking, the two comparisons `x >= 0` and `x < width` may very well be reduced to a single `UInt(x) < width` _by the compiler_ in an optimization step.
