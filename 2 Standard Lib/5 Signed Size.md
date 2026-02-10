---
permalink: /basics/signed-size/
---

## Signed Size

`Int` (i.e. signed) as type for `*.size()`, because mixing signed and unsigned integer (e.g. "signed - unsigned") and even calculating "unsigned - unsigned" is difficult to handle.

Problem in C/C++:
- `aUInt - 1 >= 0` is _always_ true (even if `aUInt` is `0`)
    
When working with sizes, calculating the difference is common; then you are limited to `Int`/~~`SSize`~~/~~`PtrDiff`~~ (i.e. signed integer) anyway.

Anyone who needs more than 2GB of data in a single "byte array", should please use a 64 bit platform.

For bounds checking, the two comparisons `x >= 0` and `x < width` may very well be reduced to a single `UInt(x) < width` _by the compiler_ in an optimization step.

Then types ~~`Size`~~ and ~~`SSize`~~/~~`PtrDiff`~~ are not necessary anymore, so two/three types less.
- We simply use `Int` instead.
- `UInt` is used in rare cases (i.e. hardware registers, masks, flags), surely _not_ for sizes.

See also Going Native 2012, Day 2, Interactive Panel: Ask Us Anything
- [42:41 - 45:28](https://youtu.be/Puio5dly9N8?feature=shared&t=2561)
    - Bjarne Stroustrup and Herb Sutter recommend using _signed_ integer.
- [1:02:51 - 1:03:14](https://youtu.be/Puio5dly9N8?feature=shared&t=3771)
    - Herb Sutter and Chandler Carruth about _unsigned_ `size_t` in the C++ STL containers: "They are wrong", "We are sorry"
