‎‎‎‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎‎‎ ‎![aoughwl](https://i.postimg.cc/Pxp72hcT/aoughwl-white-transparent.png)<br>
‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎*‎next-gen self-hosted platform for  things n stuff*

<br><br>
# Daily Blog


<br>


## 001 ‎2026-07-07 -  Thursday, July 7th, 2026
Today starts the official **aoughwl/nimony fork**.<br>
This is now the main place my Nimony work will go:
* features
* bug fixes
* more opinionated, dynamic, and substantial stdlib

We also shipped **aoughwl/nimony-lsp** and **aoughwl/nim-code**:
* `nimony-lsp` is the language-server side
* `nim-code` is a Claude Code plugin and MCP server focused on reducing token usage with Nim and Nimony

**Effective indefinitely,  the Nimony JavaScript/TypeScript/WASM/Python backend work is private.**<br>
For interested parties: the JavaScript and WebAssembly backends are ~complete and remain true to the original vision.<br>
I will gladly and promptly add anyone who wants access, but you will need to reach out to me directly over Discord (timbuktu_guy)


<br>

# Projects & Docs

Full documentation now lives at **[aoughwl.github.io](https://aoughwl.github.io/)**.

## ⭐ aoughwl/nimony — the main work

Our opinionated fork of [Nimony](https://github.com/nim-lang/nimony) (the NIF-based
Nim compiler): tracks upstream **daily**, ships our own compiler fixes and features
on top, and carries a fuller, opinionated stdlib. Everything else below is tooling,
stdlib, and backends built around it.

**→ [Full record: Issues Fixed & Features Added](https://aoughwl.github.io/nimony)**

### Features Added

| Feature | What it enables |
|---|---|
| Cross-module `.passive` | `await`/`sleepAsync`/coroutine helpers resolve & compose across modules |
| `delay <call>` in generics | spawn a coroutine from inside a generic proc (generic `race[T]`) |
| `suspend()` in generic `.passive` | generic passive procs that park now instantiate |
| Proc-pragma macros (`{.async.}`) | a macro can receive & return a `proc`, imported & cross-bit |
| Async runtime (`nimony-web`) | `Future[T]`/`await`, dispatcher, `sleepAsync`, generic `gather` & `race[T]`, `{.async.}` sugar — **46/46** |

### Issues Fixed

| # | Issue | Fix | Verified |
|---|---|---|---|
| 1 | `.passive` helpers didn't resolve across modules | `coroSuffix` from defining module + publish foreign wrapper | `tsleep3`, `tgather2` |
| 2 | `delay <call>` in a generic proc → `[Bug] expected ')'` | make `semDelay` re-entrant | cps suite |
| 3 | macro plugins failed for files outside the repo | add `nimonyDir()/src/lib` unconditionally (`semos.nim`) | macros suite |
| 4 | `.passive` capturing a `.raises` result crashed hexer | copy non-Symbol operand verbatim (`constparams.nim`) | cps suite |
| 5 | proc-pragma macros silently dropped the routine | add `"proc"` case to the NimNode NIF codec | macros suite |
| 6 | `suspend()` in a generic `.passive` proc mis-typed | type `(suspend)` as `void` (`sem.nim`) | cps suite |
| 7 | generic `race[T]` via `delay` failed to link (native + JS) | reconstruct+re-sem the call, re-flatten to `(delay …)` | `tgenrace` |
| 8 | imported `{.async.}` macro: unrecognized / cross-bit build / segfault | on-disk plugin fallback + host-bits build in isolated nifcache | `tasyncsugar` |

*Known limit: raise-across-await is deferred (errors propagate via `Future.err`).*
Every future fix/feature gets a row — here and on the site.

## The rest

| Project | Docs |
|---|---|
| **nimony-web** — JS + WASM backends & async runtime | [docs](https://aoughwl.github.io/docs/nimony-web) |
| **nim-code** — Claude Code plugin + MCP server | [docs](https://aoughwl.github.io/docs/nim-code) |
| **niflens** — NIF lens CLI for tooling | [docs](https://aoughwl.github.io/docs/niflens) |
| **nimony-lsp** — Language Server + VSCode extension | [docs](https://aoughwl.github.io/docs/nimony-lsp) |
| **net stack** — `tcp`/`net`/`serve`/`http`/`requests` | [docs](https://aoughwl.github.io/docs/net-stack) |
| **web / html / css** — typed HTML5 + MDN CSS engine + DSL | [docs](https://aoughwl.github.io/docs/web) |
| **nimony-ts / nimony-py / nimony-hl** — idiomatic TS/Py backends + shared HL-IR | [ts](https://aoughwl.github.io/docs/nimony-ts) · [py](https://aoughwl.github.io/docs/nimony-py) · [hl](https://aoughwl.github.io/docs/nimony-hl) |
