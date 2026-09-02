---
permalink: /standard-lib/textstream/
description: "Cilia text-based IO: print(), input(), ask(), TextStream, global cout/cin."
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


## TextStream

For input / output of _text_.

Writing
- `cout.write("...")` without newline.
- `cout.writeLine("...")` with newline.

Reading
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
    - TODO? `cin.readCodePoint() -> Char32` reads a single Unicode code point (as `Char32`).
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


## Class Hierarchy

- `TextStream`
    - `StringStream`
