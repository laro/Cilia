---
title: Cilia.Standard Library
permalink: /cilia/cilia-standard-library/
order: 18
---

## Cilia Standard Library
Standard library in namespace `cilia` (instead of `std` to avoid naming conflicts and to allow easy parallel use).
- With a Cilia version of each standard class/concept (i.e. CamelCase class names and camelCase function and variable names)
    - `cilia::String` instead of `std::string`
    - `Map` instead of `map`
        - `Dictionary` as alias with deprecation warning, as a hint for C# programmers.
    - `ForwardList` instead of `forward_list`
    - `UnorderedMap` instead of `unordered_map`
    - `ValueType` instead of `value_type`
    - Some exceptions/variations:
        - `Array` instead of `vector`
        - `StringStream` instead of `stringstream`
            - `TextStream`, `ByteStream`, ...
- Mostly a shallow wrapper,
    - e.g. `class cilia::String : public std::string { ... }`
    - with "**aliases**" for
        - member variables  
          `using var x = data[0]`  
          `using var y = data[1]`
        - member functions  
          `using func pushBack = push_back`
    - A wrapper is not strictly necessary, Cilia can access/call every C/C++ class/function without.  
      But only _with_ wrapper we have
        - a Cilia standard library in the "idiomatic" Cilia style (i.e. CamelCase),
        - whose types/classes are also used with existing C++ APIs (i.e. using Int, Int32, String and StringView instead of int, int32_t, string and string_view).
- Global IO functions
    - `print("...")` with Newline, calls `cout.writeLine()`.
    - `scan() -> String` reads up to Newline, calls `cin.readLine()`.
    - `ask("Name? ") -> String` calls `cout.write()`, then `cin.readLine()`.
- Streams
    - `TextStream`
        - `cout.write("...")` without newline.
        - `cout.writeLine("...")` with newline.
        - `cin.read() -> String` reads
            - everything from the `istream` user-level cache (if not empty),
            - or (otherwise) everything from the kernel buffer/cache:
                - With pipes/sockets this is everything currently in the kernel pipe/socket buffer (typically up to 64 KB). Blocks when this buffer is empty.
                  Only when the pipe/socket is closed (and no data is buffered anymore), then it returns `""`.
                - With files this is everything currently in the kernel "read ahead" cache (typically 64 to 256 KB). Blocks when this cache is empty.
                  Only when the end of file is reached (and no data is buffered anymore), then it returns `""`.
        - `cin.readAll() -> String` reads everything until the end of the file.
            - With pipes/sockets, it blocks until the pipe/socket is closed.
        - `cin.readLine() -> String` reads until newline (or end of file).
            - The newline character is removed from the line.
                - `\n`, `\r`, `\r\n` are recognized as (a single) newline.
                - (Maybe even `\n\r` from AmigaOS, and `NEL`/`U+0085` from EBCDIC/IBM.)
            - With pipes/sockets it blocks until a line is available (or pipe/socket is closed).
            - When the end of file is reached, then it returns `""`.
            - But as empty lines are also read as `""`, you need to check `isEOF()` here.
        - `cin.readGrapheme() -> String` reads a single grapheme (mostly a character).
            - Returns a String, as UTF-8 "characters"/graphemes may consist of multiple code points (called a "grapheme cluster").
            - With pipes/sockets it blocks until a character is available (or the pipe/socket is closed).
            - When the end of file is reached, then it returns `""`.
            - Unicode variant of ~~`cin.readChar() -> String`~~.
            - TODO? `cin.readCodePoint() -> Int32` reads a single Unicode code point (as Int32).
                - But beware: some graphemes, like emoji, consist of multiple code points.
                - When the end of file is reached, then it returns `-1`.
        - `cin.tryToRead() -> String` reads everything that is immediately available,
            - possibly/often returns `""`, it never blocks.
            - Reads everything from the `istream` user-level cache (if not empty),
            - or (otherwise) everything from the kernel buffer/cache:
                - With pipes/sockets this is everything currently in the kernel pipe/socket buffer (typically up to 64 KB).
                  Returns `""` when no data is buffered anymore (then maybe the pipe/socket is closed).
                - With files this is everything currently in the kernel "read ahead" cache (typically 64 to 256 KB).
                  Returns `""` when no data is buffered anymore (then maybe the end of file is reached).
            - Meant for polling / busy loops only, so _rarely_ appropriate.
            - You need to check isEOF() separately!
                - As you cannot distinguish "no data available" from EOF or pipe/socket closed.
        - `cin.isEOF()` returns `true` if no data is buffered anymore (neither in the `istream` user-level cache, nor in the kernel cache/buffer),
            - and the end of the file is reached or the pipe/socket is closed.
            - Only really necessary to call this function when using `cin.readImmediately()` or `cin.readLine()`.
    - `ByteStream`
        - `out.close()`
        - `out.write(Byte[])`
        - `out.flush()` writes the data buffer (the `istream` user-level cache) to the operating system.
            - This protects against data loss in the event of a program crash.
        - `out.flushAndSync()` calls `flush()`, then
            - calls `fsync()` to write the kernel buffers to the file system and then to the harddisk/SSD (the write cache should be written/cleared, too).
            - This protects against data loss in the event of a program or _system_ crash.
        - `in.read() -> Byte[]` reads
            - everything from the `istream` user-level cache, if not `0`,  
              otherwise everything from the kernel buffer/cache:
                - With pipes/sockets this is everything currently in the kernel pipe/socket buffer (typically 64 KB).
                  Blocks when this buffer is empty.
                  When the pipe/socket is closed (and no data is buffered anymore), then it returns an empty array.
                - With files this is everything currently in the kernel "read ahead" cache (typically 64 to 256 KB).
                  Blocks when this cache is empty.
                  When the end of file is reached (and no data is cached anymore), then it returns an empty array.
        - `in.read(Int n) -> Byte[]` reads exactly n bytes.
            - Blocks until (at least) the given number of bytes are read.
            - Throws an exception if end of file is reached (or pipe/socket closed) before n bytes are read.
        - `in.read(Int minimum, maximum) -> Byte[]` reads everything that is currently available, up to the given `maximum` number of bytes.
            - Blocks until (at least) the `minimum` number of bytes are read (may return immediately with an empty array when `minimum` is `0`).
            - `in.read(minimum..maximum) -> Byte[]`
        - `in.readAll() -> Byte[]` reads everything until the end of the stream.
        - `in.readInto(Span<Byte> buffer, Int minimum = 1)` reads into the given buffer.
            - Blocks until (at least) the `minimum` number of bytes are read (may return immediately with an empty array when `minimum` is `0`).
            - Throws an exception if end of file reached (or pipe/socket closed) before `minimum` bytes are read.
            - The effective `maximum` if defined by `buffer.size()`.
                - You may limit the maximum number of bytes to read by using `buffer.subspan(0, 4096)`,
                  or configure the starting point (in the buffer) by using `buffer.subspan(100)`.
            - Usually more efficient, as the buffer is reused and less allocations are necessary.
        - `in.available() -> Int` says how many bytes are _immediately_ available for reading.
            - Returns the size of the `istream` cache, if not 0,  
              otherwise reports the size of the kernel cache/buffer.
            - As that is the number of bytes you would get with the next `in.read()`.
        - `in.peek(Int n) -> Byte[]`
            - Blocks until (at least) the `minimum` number of bytes are read.
            - May throw an `ArgumentException("Unable to peek() more than ... bytes.")`.
            - TODO Limited to 16 bytes or to the buffer size?
        - `in.ignore(Int n)` ignores/discards n bytes from the input stream.
        - `in.ignoreAll()` ignores/discards everything that is currently in the input stream.
        - `in.isEOF()` returns true if no data is buffered anymore (neither in the `istream` user-level cache, nor in the kernel cache/buffer),
            - and the end of the file is reached or the pipe/socket is closed.
    - `File`, derived from `ByteStream`
        - `file.size() -> Int`
        - `file.position() -> Int`
            - `file.setPosition(Int n)` (AKA `file.seekFromStart()`)
            - A common position for read and write.
        - `file.seek(Int offsetToCurrentPos)`
            - `offsetToCurrentPos` can be positive (moving towards the end) or negative (moving towards the beginning).
        - `file.seekFromEnd(Int distanceToEnd)`
            - `distanceToEnd` is `0` or positive (here moving from the end towards the beginning).
        - `file.truncate()` truncates the file at the current position.
            - `file.truncate(Int n)` truncates the file at the given position.
        - `file.path() -> String`
    - `NetworkConnection`, derived from `ByteStream`,
        - a base class for TCP/IP, Bluetooth, infrared, ...
        - `connection.connect(...)`
        - `connection.disconnect()`
        - `connection.isConnected() -> Bool`
        - `connection.remoteAddress() -> String`
        - `connection.localAddress() -> String` for finding out which interface (WLAN, LAN, VPN) the connection is actually running on.
        - `connection.readTimeout() -> Duration`
            - `connection.setReadTimeout(Duration)`
    - `TcpConnection`, derived from `NetworkConnection`
        - `connection.shutdownWrite()` sends FIN (half-close), allows further reading.
        - `connection.connectionTimeout() -> Duration`
            - `connection.setConnectionTimeout(Duration)`
        - `connection.remotePort() -> UInt16`
        - `connection.localPort() -> UInt16`
        - `connection.noDelay() -> Bool`
            - `connection.setNoDelay(Bool disableNagle)` to disable the Nagle algorithm.
        - `connection.keepAlive() -> Bool`
            - `connection.setKeepAlive(Bool)` prevents connection termination due to inactivity.
        - `connection.protocolVersion() -> Int` returns `4` or `6`.
        - `connection.receiveBufferSize() -> Int`
            - `connection.setReceiveBufferSize(Int bytes)`
        - `connection.sendBufferSize() -> Int`
            - `connection.setSendBufferSize(Int bytes)`
    - `LocalConnection`, drived from `ByteStream`
        - `connection.path() -> String` returns the file system path (for Unix sockets) or the name (for pipes).
        - `connection.peerCredentials() -> String` returns the process ID (PID) or user ID of the other party.
            - TODO Move to `UnixDomainSocket`? But on Windows this info is available for pipes, too.
    - `SerialConnection` (RS-232/UART)
        - `setBaudRate(Int)`
        - `setParity(Bool)`
        - `setDataBits(Int)`
    - Hierarchy
        - `ByteStream`
            - `File`
            - `MemoryStream` as RAM buffer.
            - `NetworkStream`
                - `TCPConnection`
                    - `TLSConnection` / `SSLConnection`
                - `SSHStream`
            - `LocalStream` for interprocess communication.
                - `Pipe`
                - `UnixDomainStream` in stream configuration.
            - `DeviceStream`
                - `SerialConnection` for RS-232/UART.
                - `USBConnection` for USB bulk transfers.
        - `MessageChannel` for message/packet/frame/datagram-based protocols (i.e. _not_ only a stream of bytes).
            - `UDPSocket` for UDP over IP.
            - `UnixDomainSocket` in datagram configuration.
            - Communication with sensors on microcontrollers
                - `I2CDevice` (register read/write cycles)
                - `SPIDevice` (chip-select-controlled frames)
                - `CANBusNode`
            - `BluetoothConnection` Bluetooth RFCOMM / L2CAP
            - `ZigbeeEndpoint`
            - `WebSocketConnection` (message frames over TCP)

- Matrix & Vector
    - Geometry
        - Static/fixed size
        - For small, fixed size vectors & matrices ,
            - as typically used in geometry (i.e. 2D, 3D, 4D).
        - `cilia::Vector<Int size, T = Float>`
            - `cilia::Vector2<T = Float>`
            - `cilia::Vector3<T = Float>`
            - `cilia::Vector4<T = Float>`
        - `cilia::Matrix<Int rows, Int columns, T = Float>`
            - `cilia::Matrix22<T = Float>`
            - `cilia::Matrix33<T = Float>`
            - `cilia::Matrix44<T = Float>`
    - Linear Algebra
        - Dynamic/variable size
        - For large, dynamically sized vectors & matrices,
            - as typically used in linear algebra: BLAS (Basic Linear Algebra Subprograms)
        - `cilia::Vector<T = Float>`
        - `cilia::Matrix<T = Float>`
            - Stored column-major, like:
              ```
              0 3 6
              1 4 7
              2 5 8
              ```
        - `cilia::MDArray<Int dimensions, T = Float>`
            - also see `MDSpan`

- Image
    - `cilia::Image<T = Float>`
    - Almost like `cilia::Matrix`, but stored row-major, like:
      ```
      0 1 2
      3 4 5
      6 7 8
      ```

- Views, Slices
    - `ArrayView`
    - `VectorView`
    - `MatrixView`
    - `ImageView`
    - `MDArrayView`

---

## Arrays & ArrayViews
- `Int[] dynamicArrayOfIntegers`
    - „Dynamic array“ with **dynamic size**
      ```
      Int[] array = [0, 1, 2]
      array[0] = 0
      array[1] = 0
      array[2] = 0
      array[3] = 0  // Runtime error, no compile time bounds check
      ```
    - "Make simple things simple",  
      having a short and traditional syntax for dynamic arrays should encourage people to use it.
    - `T[] arr` is the short form of `cilia::Array<T> arr`
        - Also `[T] arr`, as in Swift or Rust, has some merits.  
          And `[3 T] arr` for fixed sized arrays would be fine for me (I don't like `[T;3] arr`), but I'll stick with the more traditional `T[] arr` (like C# and Java).
    - The long form is called `Array<T>`, not ~~`Vector<T>`~~, because
        - that's the more traditional wording,
        - by using the word "vector", the purpose of this class is not immediately clear (especially not for users of many languages other than C++, not even C),
        - `Vector` could too easily collide with the mathematical vector (as used in linear algebra or geometry).
    - "Raw" C/C++ arrays are handled with `T*` instead.
    - `std::array` is called `cilia::StaticArray` instead.
    - In C/C++ `T[]` means "array of certain (inferred) size",
        - but that can be replaced with `T*` and `T[N]`.
        - Also see [https://cplusplus.com/forum/beginner/267321/#msg1150228](https://cplusplus.com/forum/beginner/267321/#msg1150228)
- `Int[3] arrayOfThreeIntegers`  
  (instead of ~~`Int arrayOfThreeIntegers[3]`~~ in C/C++)
    - „Static array“ with **fixed size**
      ```
      Int[3] array = [0, 1, 2]
      array[0] = 0
      array[1] = 0
      array[2] = 0
      array[3] = 0  // Compilation error, due to compile time bounds check
      ```
    - `arrayOfThreeIntegers.size()` -> `3`
        - realized as extension function  
          `func<type T, Int N> T[N]::size() -> Int { return N }`
- Use `T+`/`UniquePtr<T>` for "raw" C/C++ arrays of arbitrary size.  
  But array subscript with `Int+` is unsafe.
    - ```
      Int+ array = new Int[3]  // Array-to-pointer decay possible
      unsafe {
          array[0] = 0
          array[1] = 0
          array[2] = 0
          array[3] = 0  // Undefined behaviour, no bounds check at all
      }
      ```
    - Using `Int*` for arrays is possible but generally unsafe.
        - ```
          Int+ uniquePtrToArray = new Int[3]  // Array-to-pointer decay possible
          unsafe {
              Int* array = uniquePtrToArray.release()
              array[0] = 0
              array[1] = 0
              array[2] = 0
              array[3] = 0  // Undefined behaviour, no bounds check at all
              delete[] array
          }
          ```
        - ```
          unsafe {
              Int* array = reinterpretCastTo<Int*>(malloc(3 * sizeof(Int)))
              array[0] = 0
              array[1] = 0
              array[2] = 0
              array[3] = 0  // Undefined behaviour, no bounds check at all
              free(array)
          }
          ```
    - Actually this is how to handle pointer to array of `Int` "properly":  
      ```
      Int[3]+ arrayPtr = new Int[3]
      (*arrayPtr)[0] = 0
      (*arrayPtr)[1] = 0
      (*arrayPtr)[2] = 0
      (*arrayPtr)[3] = 0  // Compilation error, due to compile time bounds check
      ```
        - But raw pointer access is still `unsafe`:  
          ```
          unsafe {
              Int[3]* arrayPtr = (new Int[3]).release()
              (*arrayPtr)[0] = 0
              (*arrayPtr)[1] = 0
              (*arrayPtr)[2] = 0
              (*arrayPtr)[3] = 0  // Compilation error, due to compile time bounds check
              delete[] arrayPtr
          }
          ```
- Examples:
    - `Int[] dynamicArrayOfInt`
    - `Int[3] arrayOfThreeInt`
    - `Int[3]& referenceToArrayOfThreeInt`
    - `Int[3]* pointerToArrayOfThreeInt`
    - `Int[3][]& referenceToDynamicArrayOfArrayOfThreeInt`
    - `String*[] dynamicArrayOfPointersToString`
- ArrayViews AKA Slices AKA Subarrays
    - `var subarray = array[1..2]`
    - `var subarray = array[1..<3]`
    - Incomplete ranges (need lower and/or upper bounds before use) are
      typcally implemented as inline functions that determine the concrete bounds and then call `array[start..end]` (or one of the exclusive counterparts).
        - `var subarray = array[..2]`
        - `var subarray = array[..]`
    - See Rust [Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- Multidimensional arrays
    - dynamic size
        - `Int[,] dynamic2DArray`  
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
    - `Int[3,4][] dynamicArrayOfThreeByFourArrayOfInt`

---

## Associative Arrays
- AKA Maps (or Dictionaries)
- `TValue[TKey]` as short form of `Map<TKey, TValue>`
    - e.g. `ContactInfo[String] contactInfoForID` as short form  
      of `Map<String, ContactInfo> contactInfoForID`,
    - as [in D](https://dlang.org/spec/hash-map.html).
    - There is no difference between these two, but "OtherMap<String, ContactInfo> contactInfoForID" allows you to select other map variants (SortedMap, HashMap etc.) if necessary.
- "Make simple things simple",  
  having a short syntax for associative arrays so they are easy to use.
- Maybe partial template specialization:
    - `Map<Int, ...>` is a `HashMap`
    - `Map<String, ...>` is a `SortedMap`

---

## String, Char & CodePoint
- `cilia::String` with _basic/standard_ unicode support.
    - Based on UTF-8, as that IMHO is (among all the Unicode formats)
        - the most widespread nowadays,
        - the most compatible (as it is ASCII based),
        - the most efficient, at least for "western" use (and you are free to use UTF16- or UTF32String otherwise).
    - Iteration over a `String` or `StringView` by:
        - **grapheme clusters**
            - represented by `StringView`.
            - This is the _default form of iteration_ over a `String` or `StringView`
            - A single grapheme cluster will often consist of multiple code units
              and may even consist of multiple code points.
            - `for graphemeCluster in "abc 🥸👮🏻"`
                - "a", "b", "c", " ", "🥸", "👮🏻"
                - "\x61", "\x62", "\x63", "\x20", "\xf0\x9f\xa5\xb8", "\xf0\x9f\x91\xae\xf0\x9f\x8f\xbb"
            - A bit slow, as it has to find grapheme cluster boundaries.
            - It is recommended to mostly use the standard functions for string manipulation anyway. But if you need to iterate manually over a Unicode-String, then grapheme-cluster-based iteration is the safe/right way.
            - Additional/alternative names?
                - `for graphemeCluster in text.asGraphemeClusters()`?
        - **code points**
            - represented by `UInt32`,
                - independent of the encoding (i.e. the same for UTF-8, UTF-16, and UTF-32 strings).
                - Called "auto decoding" in D.
            - `for codePoint in "abc 🥸👮🏻".asCodePoints()`
                - 0x00000061, 0x00000062, 0x00000063, 0x00000020, &nbsp; 0x0001F978, &nbsp; 0x0001F46E, 0x0001F3FB
            - **Note:** _Not_ even with UTF-32 do all grapheme clusters fit into a single code point,  
              so not:
                - emoji with modifier characters like skin tone or variation selector,
                - diacritical characters (äöü..., depending on the normal form chosen),
                - surely some more ...
            - A bit faster than iteration over grapheme clusters, but still slow, as it has to find code point boundaries in UTF-8/16 strings.
            - Fast with UTF-32 strings, but UTF-32 strings in general are often slower than UTF-8, simply due to their size (cache, memory bandwidth).
        - **code units**
            - represented by
                - `Char` for `String`
                    - it is `Char`==`Char8`==`UInt8` and `String`==`UTF8String`
                - `Char16` for `UTF16String`
                - `Char32` for `UTF32String`
            - `for aChar8 in "abc 🥸👮🏻".asArray()`
                - 0x61, 0x62, 0x63, 0x20,  &nbsp;  0xf0, 0x9f, 0xa5, 0xb8,  &nbsp;  0xf0, 0x9f, 0x91, 0xae, 0xf0, 0x9f, 0x8f, 0xbb
                - same for
                    - `for aChar8 in u8"abc 🥸👮🏻".asArray()`
                    - `for aChar8 in UTF8String("abc 🥸👮🏻").asArray()`
            - `for aChar16 in u"abc 🥸👮🏻".asArray()`
                - 0x0061, 0x0062, 0x0063, 0x0020,  &nbsp;  0xD83E, 0xDD78,  &nbsp;  0xD83D, 0xDC6E, 0xD83C, 0xDFFB
                - same for `for aChar16 in UTF16String("abc 🥸👮🏻").asArray()`
            - `for aChar32 in U"abc 🥸👮🏻".asArray()`
                - 0x00000061, 0x00000062, 0x00000063, 0x00000020,  &nbsp;  0x0001F978,  &nbsp;  0x0001F46E , 0x0001F3FB
                - same for `for aChar32 in UTF32String("abc 🥸👮🏻").asArray()`
    - `string.toUpper()`, `string.toLower()`
        - `toUpper(String) -> String`, `toLower(String) -> String`
    - `stringArray.sort()`
        - `sort(Container<String>) -> Container<String>`
    - `compare(stringA, stringB) -> Int`
- `ByteString` to represent the strings with single byte encoding (i.e. the classical strings consisting of one-byte characters),
    - like
        - ASCII
        - Latin-1
        - ANSI (mostly identical to Latin-1)
        - almost every one of the "code pages"
    - Encoding is not defined.
        - The user has to take care of this,
        - or a subclass with known encoding has to be used (`ASCIIString`, `Latin1String`).
    - `ASCIIString`, a string containing only ASCII characters.
        - Iteration over an `ASCIIString` or `ASCIIStringView` by `Char`==`Char8`
            - `for aChar in a"abc"`
                - 0x61, 0x62, 0x63
                - 'a', 'b', 'c'
                - Compilation error, if string literal contains non-ASCII characters.
                - same for `for aChar in ASCIIString("abc")`
                    - but Exception thrown, if string contains non-ASCII characters.
        - Implicitly convertable to `String`==`UTF8String`.
            - Very fast conversion, as all characters have the same binary representation.
    - `Latin1String`, a string containing only Latin-1 (ISO 8859-1) characters.
        - Iteration over an `Latin1String` or `Latin1StringView` by `Char`==`Char8`
            - `for aChar in l"äßç"`
                - 0xe4, 0xdf, 0xe7
                - 'ä', 'ß', 'ç'
                - Compilation error, if string literal contains non-Latin-1 characters.
                - same for `for aChar in Latin1String("abc")`
                    - but Exception thrown, if string contains non-Latin1 characters.
        - Explicitly convertable to `String`==`UTF8String`.
            - Not as fast a conversion as ASCIIString to String, because typically some characters need to be translated into _two_ UTF-8 code units.
- `Char8`, `Char16`, `Char32`
    - are considered as _different_ types for parameter overloading,
    - but otherwise are like `UInt8`, `UInt16`, `UInt32`,

- [**ICU**](https://unicode-org.github.io/icu/userguide/icu4c/) ("International Components for Unicode") for advanced Unicode support.
    - "The ICU libraries provide support for:
        - The latest version of the Unicode standard
        - Character set conversions with support for over 220 codepages
        - Locale data for more than 300 locales
        - Language sensitive text collation (sorting) and searching based on the Unicode Collation Algorithm (=ISO 14651)
        - Regular expression matching and Unicode sets
        - Transformations for normalization, upper/lowercase, script transliterations (50+ pairs)
        - Resource bundles for storing and accessing localized information
        - Date/Number/Message formatting and parsing of culture specific input/output formats
        - Calendar specific date and time manipulation
        - Text boundary analysis for finding characters, word and sentence boundaries"
    - `import icu` adds extension methods for `cilia::String`
        - Allows iteration over:
            - words (important/difficult for Chinese, Japanese, Thai or Khmer, needs list of words)
                - `for word in text.asWords()`
            - lines
                - `for line in text.asLines()`
            - sentences (needs list of abbreviations, like "e.g.", "i.e.", "o.ä.")
                - `for sentence in text.asSentences()`
        - Depending on locale
            - `string.toUpper(locale)`, `string.toLower(locale)`
                - `toUpper(String, locale) -> String`, `toLower(String, locale) -> String`
            - `stringArray.sort(locale)`
                - `sort(Container<String>, locale) -> Container<String>`
            - `compare(stringA, stringB, locale) -> Int`
