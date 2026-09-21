---
permalink: /standard-lib/textstream/
description: "print(), input(), cout/cin, TextStream, TextFile."
---

# TextStream & Command Line Interface


## Global IO Functions

- `print("...")` with Newline,
    - calls `cout.writeLine()`.
- `readLine() -> String` reads up to Newline,
    - calls `cin.readLine()`.
- `input("Name? ") -> String`
    - as in Python,
    - calls `cout.write()`, then `cin.readLine()`.
    - `input(String prompt = "") -> String`


## BasicStream

Interface as base for `Text*Stream` and `Byte*Stream`.

- `stream.isOpen() -> Bool`
- `stream.close()`


## TextStream

Interface for input / output of _text_, derived from `TextInStream` and `TextOutStream`.


### TextOutStream

Interface for writing text, derived from `BasicStream`.

- `cout.write("...")` without newline.
- `cout.writeLine("...")` with newline, default argument is `""` (i.e. an empty line).  
  &nbsp;
- `cout.write(Char32 codePoint)` writes a single Unicode symbol
- `cout.write(Int number)` writes a number
- `cout.write(Float floatingPointNumber)`  
  &nbsp;
- `cout.write(UInt8`/`16`/`32`/`64` `hexNumber)` writes a number in hexadecimal format, without prefix, the width is derived from the type:
    - UInt8  ->  "2a"
    - UInt16 ->  "002a"
    - UInt32 ->  "0000002a"
    - UInt64 ->  "000000000000002a"
- `cout.write(String prefix, UInt8`/`16`/`32`/`64` `hexNumber)` writes a number in hexadecimal format with the given prefix (e.g. "0x" or "$")


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
    - But as empty lines are also read as `""`, you need to check `atEnd()` here.
- `cin.readGraphemeCluster() -> String` reads a single grapheme cluster (mostly a character).
    - Returns a `String`, as UTF-8 "characters"/grapheme clusters may consist of multiple code points (therefore called a "grapheme _cluster_").
    - With pipes/sockets it blocks until a character is available (or the pipe/socket is closed).
    - When the end of file is reached, then it returns `""`.
    - Unicode variant of ~~`cin.readChar() -> Char`~~.
- `cin.readCodePoint() -> Char32` reads a single Unicode code point (as `Char32`).
    - But beware: some grapheme clusters, like emoji, consist of _multiple_ code points.
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
    - You need to check `atEnd()` separately!
        - As you cannot distinguish "no data available" from EOF or pipe/socket closed.
- `cin.atEnd()` (instead of ~~`cin.isEof()`~~)
    - returns `True` if
        - the end of the file is reached (or the pipe/socket is closed),
        - and no data is buffered anymore (neither in the `istream` user-level cache, nor in the kernel cache/buffer),
    - Typically necessary to call this function when `cin.read()` or `cin.readLine()` return `""`.  


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
  &nbsp;
- `textFile.path() -> String`
- `textFile.name() -> String`


### StringStream

Class derived from `TextStream`:
- `StringStream stringStream(String content)`
- `StringStream stringStream(Int capacity = 0)`
