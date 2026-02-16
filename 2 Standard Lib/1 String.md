---
permalink: /standard-lib/string/
---

# String, Char & Unicode

## String
`cilia::String` (AKA `UTF8String`) with _basic/standard_ unicode support.  
Based on UTF-8, as that IMHO is (among all the Unicode formats)
- the most widespread nowadays,
- the most compatible (as it is ASCII based),
- the most efficient, at least for "western" use (and you are free to use UTF16- or UTF32String otherwise).
    
Iteration over a `String` or `StringView` by:
- **Graphemes**/Grapheme Clusters
    - each represented by a `StringView`.
    - This is the _default form of iteration_ over a `String` or `StringView`
    - A single grapheme will often consist of multiple code _units_  
      and may even consist of multiple code _points_ (then it is called a grapheme _cluster_).
    - `for grapheme in "abc 🥸👮🏻"`
        - "a", "b", "c", " ", "🥸", "👮🏻"
        - "\x61", "\x62", "\x63", "\x20", "\xf0\x9f\xa5\xb8", "\xf0\x9f\x91\xae\xf0\x9f\x8f\xbb"
    - A bit slow, as it has to find grapheme (and cluster) boundaries.
    - It is recommended to mostly use the standard functions for string manipulation anyway. But if you need to iterate manually over a Unicode-String, then grapheme-cluster-based iteration is the safe/right way.
    - Additional/alternative names?
        - `for graphemeCluster in text.asGraphemeClusters()`?
- **Code Points**
    - each represented by a `UInt32`,
        - independent of the encoding (i.e. the same for UTF-8, UTF-16, and UTF-32 strings).
            - Called "auto decoding" in D.
        - `for codePoint in "abc 🥸👮🏻".asCodePoints()`
        - 0x00000061, 0x00000062, 0x00000063, 0x00000020, &nbsp; 0x0001F978, &nbsp; 0x0001F46E, 0x0001F3FB
    - **Note:** _Not even with UTF-32_ do all grapheme clusters fit into a single code point,  
      so not:
        - Emoji ZWJ Sequences (Zero Width Joiner),
            - emoji with modifier characters like skin tone or variation selector,
        - diacritical characters (äöü..., depending on the normal form chosen),
        - surely some more ...
    - A bit faster than iteration over grapheme clusters, but still slow, as it has to find code point boundaries in UTF-8/16 strings.
    - Fast with UTF-32 strings, but UTF-32 strings in general are often slower than UTF-8, simply due to their size (cache, memory bandwidth).
- **Code Units**
    - each represented by a
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
- Lines
    - `for line in text.asLines()`
    - Break after:
      
        | Name | Codepoint         | Meaning                      |
        |------|-------------------|------------------------------|
        | LF   | `U+000A`          | `\n`, Unix/Linux/macOS       |
        | CR   | `U+000D`          | `\r`, Classic Mac            |
        | CRLF | `U+000D` `U+000A` | Windows                      |
        | LFCR | `U+000A` `U+000D` | AmigaOS                      |
        | NEL  | `U+0085`          | Next Line, EBCDIC/Mainframes |
        | LS   | `U+2028`          | Line Separator               |
        | PS   | `U+2029`          | Paragraph Separator          |
         

## Convert Upper/Lower Case

- `string.toUpper()`
- `string.toLower()`
- `toUpper(String) -> String`
- `toLower(String) -> String`


## Sorting

- `stringArray.sort()`
- `sort(Container<String>) -> Container<String>`
- `compare(stringA, stringB) -> Int`


## ByteString

`ByteString` to represent the strings with single byte encoding (i.e. the classical strings consisting of one-byte characters), like:
- ASCII,
- Latin-1,
- ANSI (mostly identical to Latin-1),
- almost every one of the "code pages".

The encoding is not defined, the user has to take care of this.  
Or a subclass with known encoding has to be used:
- **`ASCIIString`**, a string containing only ASCII characters.
    - Iteration over an `ASCIIString` or `ASCIIStringView` by `Char`==`Char8`
        - `for aChar in a"abc"`
            - 0x61, 0x62, 0x63
            - 'a', 'b', 'c'
            - Compilation error, if string literal contains non-ASCII characters.
            - same for `for aChar in ASCIIString("abc")`
                - but Exception thrown, if string contains non-ASCII characters.
    - Implicitly convertible to `String`==`UTF8String`.
        - Very fast conversion, as all characters have the same binary representation.
- **`Latin1String`**, a string containing only Latin-1 (ISO 8859-1) characters.
    - Iteration over an `Latin1String` or `Latin1StringView` by `Char`==`Char8`
        - `for aChar in l"äßç"`
            - 0xe4, 0xdf, 0xe7
            - 'ä', 'ß', 'ç'
            - Compilation error, if string literal contains non-Latin-1 characters.
            - same for `for aChar in Latin1String("abc")`
                - but Exception thrown, if string contains non-Latin1 characters.
    - Explicitly convertible to `String`==`UTF8String`.
        - Not as fast a conversion as ASCIIString to String, because typically some characters need to be translated into _two_ UTF-8 code units.


## Char
`Char8`, `Char16`, `Char32` are considered as _different_ types for parameter overloading,
but otherwise are like `UInt8`, `UInt16`, `UInt32`.


## ICU

[International Components for Unicode](https://unicode-org.github.io/icu/userguide/icu4c/) ("ICU") for advanced Unicode support.
> The ICU libraries provide support for:
> - The latest version of the Unicode standard
> - Character set conversions with support for over 220 codepages
> - Locale data for more than 300 locales
> - Language sensitive text collation (sorting) and searching based on the Unicode Collation Algorithm (=ISO 14651)
> - Regular expression matching and Unicode sets
> - Transformations for normalization, upper/lowercase, script transliterations (50+ pairs)
> - Resource bundles for storing and accessing localized information
> - Date/Number/Message formatting and parsing of culture-specific input/output formats
> - Calendar specific date and time manipulation
> - Text boundary analysis for finding characters, word and sentence boundaries

Even iterating through graphemes (or graphe clusters) is complicated for some/rare/historic scripts.
- Basic is Latin, combining marks, ZWJ, flags, variant selector, CJK (Han, Hiragana, Katakana, Hangul).
    - So most everything is covered.
- Give more complex cases to ICU (Arabic, Devanagari, Thai).
    - Maybe via weak linking.
    - Using the Unicode Text Segmentation Algorithm (UAX #29), the RuleBasedBreakIterator for characters, `BreakIterator::createCharacterInstance(...)`.

`import icu` adds extension methods for `cilia::String`
- Allow iteration over:
    - Words
        - `for word in text.asWords()`
        - Important/difficult for Chinese, Japanese, Thai or Khmer, needs list of words.
        - Using the RuleBasedBreakIterator for words, `BreakIterator::createWordInstance(...)`.
    - Sentences
        - `for sentence in text.asSentences()`
        - Needs list of abbreviations, like "e.g.", "i.e.", "o.ä.". Still just a heuristic, after all.
        - Using the RuleBasedBreakIterator for sentences, `BreakIterator::createSentenceInstance(...)`.
        
Depending on locale
- `string.toUpper(locale)`, `string.toLower(locale)`
    - `toUpper(String, locale) -> String`, `toLower(String, locale) -> String`
- `stringArray.sort(locale)`
    - `sort(Container<String>, locale) -> Container<String>`
- `compare(stringA, stringB, locale) -> Int`
