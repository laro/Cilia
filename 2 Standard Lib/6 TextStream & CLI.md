---
permalink: /standard-lib/textstream/
description: "print(), input(), cout/cin, TextStream, TextFile."
---

# TextStream & Command Line Interface


## Global IO Functions

Convenience functions for simple console I/O.

- `print(String text)`
    - Writes `text` followed by a newline.
    - Equivalent to `out.writeLine(text)`.
- `readLine() -> String`
    - Reads a line from standard input.
    - Equivalent to `in.readLine()`.
- `input(String prompt = "") -> String`
    - Writes `prompt` without a newline and reads a line from standard input,
    - as in Python.
    - Equivalent to `out.write(prompt)`, `out.flush()`, and `in.readLine()`.


## BasicStream

Interface as base for `Text*Stream` and `Byte*Stream`.

- `stream.isOpen() -> Bool`
- `stream.close()`


## TextStream

Interface for input / output of _text_, derived from `TextInStream` and `TextOutStream`.


### TextOutStream

Interface for writing text, derived from `BasicStream`.

- `out.write("...")` without newline.
- `out.writeLine("...")` with newline, default argument is `""` (i.e. an empty line).

<!-- -->
- `out.write(Char8`/`16`/`32 codePoint)` writes a single Unicode symbol
- `out.write(Int number)` writes a number
- `out.write(Float floatingPointNumber)`

<!-- -->
- `out.write(UInt8`/`16`/`32`/`64 hexNumber)` writes a number in hexadecimal format, without prefix, the width is derived from the type:
    - `UInt8`  -> `"2a"`
    - `UInt16` -> `"002a"`
    - `UInt32` -> `"0000002a"`
    - `UInt64` -> `"000000000000002a"`
- `out.write(String prefix, UInt8`/`16`/`32`/`64 hexNumber)` writes a number in hexadecimal format with the given prefix (e.g. `"0x"` or `"$"`)

<!-- -->
- `out.flush()` writes the data buffer to the operating system.
    - This protects against data loss in the event of a program crash.
- `out.flushAndSync()` calls `flush()`, then
    - calls `fsync()` to write the kernel buffers to the file system and then to the hard disk/SSD (the write cache should be written/cleared, too).
    - This protects against data loss in the event of a program or _system_ crash.

Cache:
- `Byte* outBuffer`  
  The output buffer is stored as pointer, to allow:
    - a single common buffer (for files) as well as two separate buffers for input and output (for network connections),
    - a dedicated buffer (for TextFile) as well as a String as backing store (for StringStream).
- `Int outPosition`
- `Int outCapacity`

<!-- -->
- `virtual writeRaw(Span<Byte> src)`
    - With TextFile: copies all bytes to the underlying File.
    - With StringStream:
        - on `flush()` : update the size of the buffer string,
        - on `writeRaw()`  with buffer capacity reached:
            - update the size of the buffer string,
            - allocate a new, bigger buffer string,
            - copy all bytes from the old buffer string to the new one,
            - adjust `outBuffer` = `newBufferString.data()`, `outPosition` = `newBufferString.size()` , and `outCapacity` = `newBufferString.capacity`.


#### Operator `<<`

Output stream operator `<<`, similar to C++ iostreams:
```
cout << "Text"

Int value = 1
cout << value
```

But TextStreams are stateless only, i.e. there are no "state manipulators".

`endl` does not flush, you need to `flush` explicitly:
- `cout << "Text" << endl` 
- `cout << "Text" << endl << flush` 

Using output descriptors to control the behaviour:
```
cout << Hex(address)
cout << Quoted(name)
cout << Escaped(text)
```


### TextInStream

Interface for reading text, derived from `BasicStream`.

- `in.read() -> String` reads
    - everything from the input buffer (if not empty),
    - or (otherwise) everything from the kernel buffer/cache:
        - With pipes/sockets this is everything currently in the kernel pipe/socket buffer (typically up to 64 KB).
        - With files this is everything currently in the kernel "read ahead" cache (typically 64 to 256 KB).
    - Blocks when this buffer/cache is empty.
    - Only when the pipe/socket is closed / end of file is reached, and no data is buffered anymore, then it returns `""`.
- `in.read(minimum..) -> String` reads everything that is immediately available,
    - blocks until at least `minimum` characters are read.
    - Reads everything from the input buffer (if not empty),
    - or (otherwise) everything from the kernel buffer/cache:
        - With pipes/sockets this is everything currently in the kernel pipe/socket buffer (typically up to 64 KB).
        - With files this is everything currently in the kernel "read ahead" cache (typically 64 to 256 KB).
    - Returns `""` when no data is buffered anymore (then maybe the pipe/socket is closed / the end of file is reached).
    - With `minimum` = `0`:
        - Never blocks.
        - Meant for polling / busy loops only, so _rarely_ appropriate.
        - You need to check `atEnd()` separately!
            - As you cannot distinguish "no data available" from EOF or pipe/socket closed.
- `in.readAll() -> String` reads everything until the end of the file.
    - With pipes/sockets, it blocks until the pipe/socket is closed.
- `in.readLine() -> String` reads until newline (or end of file).
    - The newline character is removed from the line.
        - `\n`, `\r`, `\r\n` are recognized as (a single) newline.
        - (Maybe even `\n\r` from Acorn RISC OS "spooled text", and `NEL`/`U+0085` from EBCDIC/IBM.)
    - With pipes/sockets it blocks until a line is available (or pipe/socket is closed).
    - When the end of file is reached, then it returns `""`.
    - But as empty lines are also read as `""`, you need to check `atEnd()` here.
- `in.readGraphemeCluster() -> String` reads a single grapheme cluster (mostly a character).
    - Returns a `String`, as UTF-8 "characters"/grapheme clusters may consist of multiple code points (therefore called a "grapheme _cluster_").
    - With pipes/sockets it blocks until a character is available (or the pipe/socket is closed).
    - When the end of file is reached, then it returns `""`.
    - Unicode variant of ~~`in.readChar() -> Char`~~.
- `in.readCodePoint() -> Char32` reads a single Unicode code point (as `Char32`).
    - But beware: some grapheme clusters, like emoji, consist of _multiple_ code points.
    - When the end of file is reached, then it returns `-1`.

<!-- -->
- `in.atEnd()` (instead of ~~`in.isEof()`~~)
    - returns `True` if
        - the end of the file is reached (or the pipe/socket is closed),
        - and no data is buffered anymore (neither in the `istream` user-level cache, nor in the kernel cache/buffer),
    - Typically necessary to call this function when `in.read()` or `in.readLine()` return `""`.  


#### Operator `>>`

Input stream operators `>>`, similar to C++ iostreams:
```
Int i
cin >> i

Float f
cin >> f

Char32 codePoint
cin >> codePoint

String word
cin >> word
```

But TextStreams are stateless only, i.e. there are no "state manipulators".

Using input descriptors to control the behaviour:
```
UInt address
cin >> Hex(address)

String grapheme
cin >> GraphemeCluster(grapheme)

String line
cin >> Line(line)
```

Technically realized as:
```
class GraphemeCluster {
    String& storage
}
operator (TextInStream stream) >> (GraphemeCluster graphemeCluster) {
    graphemeCluster.storage = stream.readGraphemeCluster()
}
```
```
class Line {
    String& storage
}
operator (TextInStream stream) >> (Line line) {
    line.storage = stream.readLine()
}
```


### TextFile

Class derived from `TextStream`:
- `TextFile::open("Test.txt") -> File`
- `TextFile::create("Test.txt") -> File`
- `TextFile::openOrCreate("Test.txt") -> File`

<!-- -->
- `textFile.path() -> String`
- `textFile.name() -> String`


### StringStream

Class derived from `TextStream`:
- `StringStream stringStream(String content)`
- `StringStream stringStream(Int capacity = 0)`
