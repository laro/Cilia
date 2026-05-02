---
permalink: /comparison/zig/
description: "Zig equivalent of Cilia code: types, variables, functions, loops. Allocator-aware containers and strings."
---

This is (should be) the exact equivalent of the [Cilia code](/comparison/cilia/#by-example) in Zig:

- Types
    - `i64`, `i32`, `i64`, `f32`
- Variables
    - `var n: i64 = 42;`
    - `var n = @as(i64, 42);`
    - `const n = 42;`
    - `var words = std.ArrayList([]const u8).init(allocator);`
    - `var names = std.StringHashMap(void).init(allocator);`
    - <span class="wide">`var contactInfoForID = std.StringHashMap(ContactInfo).init(allocator);`</span>
- Functions
    - `fn multiply(a: i64, b: i64) i64 { return a * b; }`
    - `fn print(a: ContactInfo) void { ... }`
    - <span class="wide">`fn concat(allocator: std.mem.Allocator, a: []const u8, b: []const u8) ![]u8 { return try std.mem.concat(allocator, u8, &.{ a, b }); }`</span>
- Loops
    - `for (1..11) |i| { ... }`
    - `for (0..words.items.len) |i| { ... }`
    - `for ([_]i64{ 5, 7, 11, 13 }) |i| { ... }`
    - `for (words.items) |word| { ... }`

> **Note**  
> In Zig integer literals like `42` have the type `comptime_int`. Mutable variables therefore need an explicit runtime type or cast.  
> Standard-library containers and runtime string concatenation generally require an allocator.
