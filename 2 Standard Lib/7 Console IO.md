---
permalink: /standard-lib/console/
description: "Console I/O, cin, cout, cerr."
---

# Console I/O


## Global IO Functions

Convenience functions for simple console I/O.

- `print(String text)`
    - Writes `text` followed by a newline.
    - Equivalent to `cout.writeLine(text)`.
- `readLine() -> String`
    - Reads a line from standard input.
    - Equivalent to `cin.readLine()`.
- `input(String prompt = "") -> String`
    - Writes `prompt` without a newline and reads a line from standard input,
    - as in Python.
    - Equivalent to `cout.write(prompt)`, `cout.flush()`, and `cin.readLine()`.


## `cin`, `cout` & `cerr`

The I/O streams for current input and output `cin`, `cout`, and `cerr` are thread-safe
in C++, so they allow simultaneous access from multiple threads.

Cilia follows this approach with `ThreadSafeTextStream`s.


The "raw", not thread-safe in/out streams are three globals:
- `TextInStream  system::console::in`
- `TextOutStream system::console::out`
- `TextOutStream system::console::err`

With these plain `TextStream`s, simultaneous access from multiple threads would be undefined behaviour (UB) and sooner or later lead to _memory corruption_.

Then there are three _thread-safe_ globals:
- `ThreadSafeTextInStream  cin(system::console::in)`
- `ThreadSafeTextOutStream cout(system::console::out)`
- `ThreadSafeTextOutStream cerr(system::console::err)`


`ThreadSafeTextStream`s can be redirected, e.g. with `cerr.setBaseStream(system::console::out)`


## ThreadSafeTextStream

The thread-safe streams have the same interface as the plain `TextStream`s, but access to the "user-level" buffer is restricted via a lock, allowing simultaneous access from multiple threads.

> **Note**  
> While simultaneous access is "safe", the output of two threads might/will still be intertwined.


Due to the locking the performance is reduced, especially when reading/writing in small chunks (i.e. single bytes, integers, etc.). Use a local `TextBufferStream` to improve on that.

```
class ThreadSafeTextStream : ThreadSafeTextOutStream, ThreadSafeTextInStream
```


### ThreadSafeTextInStream

```
class ThreadSafeTextInStream {
    ThreadSafeTextInStream(TextInStream baseInStream)

    setBaseStream(TextInStream baseInStream)

    read() -> String
    // ...

protected:
    TextInStream* baseInStream
}
```


### ThreadSafeTextOutStream

```
class ThreadSafeTextOutStream {
    ThreadSafeTextOutStream(TextOutStream baseOutStream)

    setBaseStream(TextOutStream baseOutStream)

    write(String)
    // ...

protected:
    TextOutStream* baseOutStream
}
```


## TextBufferStream

A `TextBufferStream` buffers text locally. Small reads and writes are done efficiently without locking, the underlying stream is accessed in big chunks only (e.g. full lines or full buffers). The buffer of the base stream will mostly be circumvented.

It is used to buffer `ThreadSafeTextStream`s, as those are slow for small reads/writes.

```
class TextBufferStream : TextBufferOutStream, TextBufferInStream
```


### TextBufferInStream

A `TextBufferInStream` reads text from the underlying base stream (done efficiently in big chunks) and buffers it locally for small reads (done efficiently without locking).

```
class TextBufferInStream {
    TextBufferInStream(ThreadSafeTextInStream baseThreadSafeInStream)

    setBaseStream(ThreadSafeTextInStream baseThreadSafeInStream)

protected:
    ThreadSafeTextInStream* baseThreadSafeInStream
}
```


### TextBufferOutStream

A `TextBufferOutStream` buffers small writes locally (done efficiently without locking) and writes it to the underlying base stream (done efficiently in big chunks).

```
class TextBufferOutStream {
    TextBufferOutStream(ThreadSafeTextOutStream baseThreadSafeOutStream)

    setBaseStream(ThreadSafeTextOutStream baseThreadSafeOutStream)

protected:
    ThreadSafeTextOutStream* baseThreadSafeOutStream
}
```


## Platform-specific Raw Streams

`system::console::in`, `out`, and `err` are implemented by platform-specific streams. They wrap an operating-system handle or file descriptor and implement `TextOutStream::writeRaw()` / `TextInStream::readRaw()`.

They are **not** thread-safe. Use `cin` / `cout` / `cerr` for concurrent access.

The file descriptor / OS handle is _not owned_: `close()` flushes and marks the stream closed, but does not close the file descriptor / OS handle (as that would close stdin/stdout/stderr for the whole process).

They are meant to wrap the three standard streams. They could wrap any compatible handle or descriptor (console, pipe, file, socket), but that is rarely used.


### FileHandleStream

Windows only, wraps a Win32 `HANDLE` (typically from `GetStdHandle`, but also from `CreateFile`, `CreatePipe`, ...).

```
class FileHandleStream : FileHandleOutStream, FileHandleInStream
```

- `system::console::in`  uses `GetStdHandle(STD_INPUT_HANDLE)`
- `system::console::out` uses `GetStdHandle(STD_OUTPUT_HANDLE)`
- `system::console::err` uses `GetStdHandle(STD_ERROR_HANDLE)`

If the handle is a console (`GetFileType` → `FILE_TYPE_CHAR`):
- input uses `ReadConsole`,
- output uses `WriteConsole`.

If the handle is redirected to a file or pipe:
- input uses `ReadFile`,
- output uses `WriteFile`.

`isTerminal()` is `GetConsoleMode()`.


#### FileHandleInStream

```
class FileHandleInStream : TextInStream {
    FileHandleInStream(Handle handle)

protected:
    Handle inHandle
}
```


#### FileHandleOutStream

```
class FileHandleOutStream : TextOutStream {
    FileHandleOutStream(Handle handle)

protected:
    Handle outHandle
}
```


### FileDescriptorStream

Unix, Linux, macOS only, wraps a POSIX file descriptor (an `Int32`).

```
class FileDescriptorStream : FileDescriptorOutStream, FileDescriptorInStream
```

- `system::console::in`  uses file descriptor `0` (`STDIN_FILENO`)
- `system::console::out` uses file descriptor `1` (`STDOUT_FILENO`)
- `system::console::err` uses file descriptor `2` (`STDERR_FILENO`)

I/O uses `read()` / `write()`.

`isTerminal()` is `isatty()`.


#### FileDescriptorInStream

```
class FileDescriptorInStream : TextInStream {
    FileDescriptorInStream(Int inFD)

protected:
    Int32 inFD
}
```


#### FileDescriptorOutStream

```
class FileDescriptorOutStream : TextOutStream {
    FileDescriptorOutStream(Int outFD)

protected:
    Int32 outFD
}
```
