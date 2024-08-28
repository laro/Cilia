# Interesting Ideas from Other Languages
- **Circle**
    - **Fix C++ "wrong defaults"**  
        [Sean Baxter](https://x.com/seanbax), creator of [Circle](https://github.com/seanbaxter/circle), [writes about C++'s wrong defaults](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#to-err-is-human-to-fix-divine):
        > C++ has a number of "wrong defaults," design decisions either inherited from C or specific to C++ which many programmers consider mistakes.
        > They may be counter-intuitive, go against expected practice in other languages, leave data in undefined states, or generally be prone to misuse.
        
        I am not familiar with all these issues, but in a new language we certainly coud fix a lot of it.
        
        1. [Uninitialized automatic variables.](http://eel.is/c++draft/dcl.init#general-7.3)
            - See [Safety and Security](#safety-and-security)/Initialization
        2. [Integral promotions.](http://eel.is/c++draft/conv.prom)
            - Only allow safe ones,  
              otherwise an explicit cast is necessary.
        3. [Implicit narrowing conversions.](http://eel.is/c++draft/conv.integral#3)
            - Not allowed,  
              only implicit widening is allowed.
            - Assigment of integer and float literals to variables of certain precision only possible if "it fits".
        4. [Switches should break rather than fallthrough.](http://eel.is/c++draft/stmt.switch#6)
            - Use the keyword `fallthrough` instead, as in Swift.
        5. [Operator precedence is complicated and wrong.](http://eel.is/c++draft/expr.compound#expr.bit.and)
            - If the [suggestion](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#simpler_precedence) of Circle (Sean Baxter) works well, then that would be fine.
            - Cpp2 (Herb Sutter) has [this precedence](https://hsutter.github.io/cppfront/cpp2/common/?h=operator#binary-operators).
        6. [Hard-to-parse declarations and the most vexing parse.](http://eel.is/c++draft/dcl.pre#nt:simple-declaration)
            - Use the keyword `func` (but not typically `var`, unless you want type inferring)
        7. [Template brackets `< >` are a nightmare to parse.](http://eel.is/c++draft/temp.names#nt:template-argument-list)
            - I would not like to change this, only if it _really_ has to be.
            - Cpp2 / Herb Sutter kept `< >` after all.
        8. [Forwarding parameters and `std::forward` are error prone.](http://eel.is/c++draft/temp.deduct#call-3)
           - I am not familiar with the problem(s), but Cpp2 / Herb Sutter offers the `forward` keyword.
        10. [Braced initializers can choose the wrong constructor.](http://eel.is/c++draft/dcl.init.list#2)
            - Do without braced initialization altogether.
                - With the keyword `func` there is now a clear distinction between function declaration and variable declaration with initialization.
                - The classic initialization via `(...)`, ultimately a function call of the constructor, is a better fit anyway.
            - Braces / curly brackets only for initializer lists,
                - only when a constructor or assignment operator is defined, with `InitializerList` as input parameter,
                - i.e. for tuples, lists etc.
        11. [`0` shouldn't be a null pointer constant.](http://eel.is/c++draft/expr#conv.ptr-1)
            - Not allowed, use `NullPtr` or explicit casting.
        12. [`this` shouldn't be a pointer.](http://eel.is/c++draft/expr.prim.this#1)
            - Better `this` is a reference.
    - [Versioning with feature directives](https://github.com/seanbaxter/circle/blob/master/new-circle/README.md#versioning-with-feature-directives)
        - Standardization is better than having multiple different language "dialects"  
          **but**
            - for transitioning of existings source code  and
            - for the evolution of a language
        - it is a very interesting idea to selectively enable new language features or defaults.
    - [Circle C++ with Memory Safety](https://www.circle-lang.org/site/index.html)
        - Extending C++ for Rust-level safety.

- **Cpp2** (Herb Sutter)
    - [is](https://hsutter.github.io/cppfront/cpp2/expressions/#is-safe-typevalue-queries)
    - [as](https://hsutter.github.io/cppfront/cpp2/expressions/#as-safe-casts-and-conversions)
    -  [Function](https://hsutter.github.io/cppfront/cpp2/functions/) [Parameter Passing](https://hsutter.github.io/cppfront/cpp2/functions/#parameters)
        - `in`, `inout`, `out`, `move`, `copy`, `forward`
        - I like this and therefore "copied" it. Admittedly without fully understanding the difference between move and forward.
    - [Labelled `break` and `continue`](https://github.com/ntrel/cpp2?tab=readme-ov-file#labelled-break-and-continue) (i.e. multi-level)
      ```
      outer: while true {
          j := 0;
          while j < 3 next j++ {
              if done() {
                  break outer;
              }
          }
      }
      ```
    - `for words next i++ do (word) { ... word & i ... }` iterates over all words and with an index, at the same time.
    - [Uniform Call Syntax](https://github.com/ntrel/cpp2?tab=readme-ov-file#uniform-call-syntax)
      for member functions and free functions.
    - [Function Bodies](https://github.com/ntrel/cpp2?tab=readme-ov-file#function-bodies)
        - `multiply: (x: int, y: int) -> int = x * y;`
        - `multiply: (x: int, y: int) x * y;` (not even an `=` anymore?)
        - `multiply: (x: int, y: int) -> int = return x * y;`
        - Nice and short, as in math, but
            - actually not quite as in math, as math usually does not denote the type,
            - in the end it is _one more kind_ of notation for functions.
    - [Unified `operator=` for assignment, constructor, and destructor)](https://github.com/ntrel/cpp2?tab=readme-ov-file#operator).
        - Takes a bit of getting used to.
    - [Implicit Move on Last Use](https://github.com/ntrel/cpp2?tab=readme-ov-file#implicit-move-on-last-use)
        - So resources are freed even earlier than in C++.
    - [Named Return Values](https://github.com/ntrel/cpp2?tab=readme-ov-file#named-return-values)
    - [Inspect](https://github.com/ntrel/cpp2?tab=readme-ov-file#inspect),
      a kind of pattern matching.

- **Rust**
    - Security, of course: borrow checker etc.
    - Ranges

- [**Julia**](https://julialang.org/)
    - "Cilia" sounds like something in between [C](https://en.wikipedia.org/wiki/C_(programming_language))/[C++](https://en.wikipedia.org/wiki/C%2B%2B) and [Julia](https://julialang.org), so maybe I could/should add some more of Julias interesting features to the Cilia wish list.
    - Julia has very strong math support. Some of its features should be easy to copy.
        - `b = 2a` as short form of `b = 2*a`
        - `x ÷ y`, integer divide, like `x / y`, truncated to an integer
        - `sqrt(x)`, `√x`
        - `cbrt(x)`, `∛x`
        - `!=`, `≠`
        - `<=`, `≤`
        - `>=`, `≥`
        - Operator overloading
            - See:
                - [https://www.geeksforgeeks.org/operator-overloading-in-julia/](https://www.geeksforgeeks.org/operator-overloading-in-julia/)
                    - „Precedence and associativity:  When defining new operators or overloading existing ones, you can also specify their precedence and associativity, which determines the order in which they are evaluated.“
                        - That seems quite complicated to parse?!
                        - I cannot find any other reference to this feature, I assume it is a misunderstanding.
                - [https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm](https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm)
            - Much more operators
                - [https://stackoverflow.com/a/60321302](https://stackoverflow.com/a/60321302)
        - Many kinds of brackets?
            - [https://stackoverflow.com/a/33357311](https://stackoverflow.com/a/33357311)
            - TODO: Are these "unusual" brackets meant to be used as operators?
