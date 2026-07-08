‎‎‎‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎‎‎ ‎![aoughwl](https://i.postimg.cc/Pxp72hcT/aoughwl-white-transparent.png)<br>
‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎*‎next-gen self-hosted platform for  things n stuff*<br>
 ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎ ‎‎ **[aoughwl.github.io](https://aoughwl.github.io/)**
<br><br><br>
# ⭐ aoughwl/nimony
Our opinionated fork of [Nimony](https://github.com/nim-lang/nimony) (the NIF-based
Nim compiler)
* tracks upstream **daily**
* ships our own compiler fixes and features on top
* carries a fuller, opinionated stdlib.
**→ [Full record: Issues Fixed & Features Added](https://aoughwl.github.io/nimony)**

| Project | Docs |
|---|---|
| **nimony-web** — JS + WASM backends & async runtime | [docs](https://aoughwl.github.io/docs/nimony-web) |
| **nim-code** — Claude Code plugin + MCP server | [docs](https://aoughwl.github.io/docs/nim-code) |
| **niflens** — NIF lens CLI for tooling | [docs](https://aoughwl.github.io/docs/niflens) |
| **nimony-lsp** — Language Server + VSCode extension | [docs](https://aoughwl.github.io/docs/nimony-lsp) |
| **net stack** — `tcp`/`net`/`serve`/`http`/`requests` | [docs](https://aoughwl.github.io/docs/net-stack) |
| **web / html / css** — typed HTML5 + MDN CSS engine + DSL | [docs](https://aoughwl.github.io/docs/web) |
| **nimony-ts / nimony-py / nimony-hl** — idiomatic TS/Py backends + shared HL-IR | [ts](https://aoughwl.github.io/docs/nimony-ts) · [py](https://aoughwl.github.io/docs/nimony-py) · [hl](https://aoughwl.github.io/docs/nimony-hl) |


<br><br><br>

# Daily Blog


<br>

## 002 ‎2026-07-08 -  Wednesday, July 8th, 2026

**Pushed IC to aoughwl/Nimony:**  *~1s -> ~10ms*<br>
see: [ic-parallel-deps](https://aoughwl.github.io/changes/ic-parallel-deps.html), [ic-cursor-traversal](https://aoughwl.github.io/changes/ic-cursor-traversal.html), [ic-warm-daemon](https://aoughwl.github.io/changes/ic-warm-daemon.html), [ic-batch-intern](https://aoughwl.github.io/changes/ic-batch-intern.html)

Created [niflens](https://aoughwl.github.io/docs/niflens), a CLI tool for parsing and viewing NIF<br>
Updated [nimony-lsp](https://aoughwl.github.io/docs/nimony-lsp) and [nim-code](https://aoughwl.github.com/io/docs/nim-code) to benefit from [niflens](https://aoughwl.github.io/docs/niflens)

Live diagnostic and suggestions now work as you type!

## 001 ‎2026-07-07 -  Tuesday, July 7th, 2026
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
