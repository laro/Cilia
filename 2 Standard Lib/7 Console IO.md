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


## `cin`, `cout` & 'cerr`

The I/O streams for current input and output `cin`, `cout`, and `cerr` are thread-safe
in C++, so they allow simultaneous access from multiple threads.

Cilia follows this approach with `ThreadSafeTextStream`s.


The "raw", not thread-safe in/out streams are three globals:
- `TextInStream  system::console::in`
- `TextOutStream system::console::out`
- `TextOutStream system::console::err`
With these plain `TextStream`s, simultaneous access from multiple threads would be undefined behaviour (UB) and sooner or later lead to _memory corruption_.

Then there are three thread-safe globals:
- `ThreadSafeTextInStream  cin(system::console::in)`
- `ThreadSafeTextOutStream cout(system::console::out)`
- `ThreadSafeTextOutStream cerr(system::console::err)`


`ThreadSafeTextStream`s can be redirected, e.g. with `cerr.setBaseStream(system::console::out)`


## ThreadSafeTextStream

The thread-safe streams have the same interface as the plain `TextStream`s, but access to the "User-level" buffer is restricted via a lock, allowing simultaneous access from multiple threads.

> **Note**  
> While simultaneous access is "safe", the output of two threads might/will still be intertwined.


Due to the locking the performance is reduced, especially when reading/writing in small chunks (i.e. single bytes, integers, etc.). You may use a local `TextBufferStream` to read/write small chunks fast locally, and write bigger chunks (i.e. full lines or full buffers) to the underlying thread-safe stream.

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

A `TextBufferStream` buffers text locally. Small reads and writes are done efficiently without locking. The buffer of the base stream will mostly be circumvented.

A `TextBufferStream` can be used to buffer a `ThreadSafeTextStream` (as those are a bit slow for small reads/writes) and also a plain `TextStream`.

```
class TextBufferStream : TextBufferOutStream, TextBufferInStream
```


### TextBufferInStream

A `TextBufferInStream` reads text from the underlying base stream (done efficiently in big chunks) and buffers it locally for small reads (done efficiently without locking).

```
class TextBufferInStream {
    TextBufferInStream(TextInStream baseInStream)
    TextBufferInStream(ThreadSafeTextInStream baseThreadSafeInStream)

    setBaseStream(TextInStream baseInStream)
    setBaseStream(ThreadSafeTextInStream baseThreadSafeInStream)

protected:
    // Only one of these two streams can be set.
    TextInStream* baseInStream
    ThreadSafeTextInStream* baseThreadSafeInStream
}
```


### TextBufferOutStream

A `TextBufferOutStream` buffers small writes locally (done efficiently without locking) and writes it to the underlying base stream (done efficiently in big chunks).

```
class TextBufferOutStream {
    TextBufferOutStream(TextOutStream baseOutStream)
    TextBufferOutStream(ThreadSafeTextOutStream baseThreadSafeOutStream)

    setBaseStream(TextOutStream baseOutStream)
    setBaseStream(ThreadSafeTextOutStream baseThreadSafeOutStream)

protected:
    // Only one of these two streams can be set.
    TextOutStream* baseOutStream
    ThreadSafeTextOutStream* baseThreadSafeOutStream
}
```
