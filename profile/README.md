‎‎‎‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎‎‎ ‎![aoughwl](https://i.postimg.cc/Pxp72hcT/aoughwl-white-transparent.png)<br>
‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎*‎next-gen self-hosted platform for  things n stuff*<br>
 ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎  ‎‎ ‎ ‎‎ ‎‎ ‎‎ **[aoughwl.github.io](https://aoughwl.github.io/)**
<br><br><br>
# ⭐ aowlmony — a ground-up Nimony toolchain
A from-scratch reimplementation of the [Nimony](https://github.com/nim-lang/nimony)
toolchain (the NIF-based Nim compiler) — parser, semchecker, lowering, backends —
written *in* Nimony and self-hosting, built from the ground up.

Our intermediate format is **[AIF ≡ NIF](https://aoughwl.github.io/docs/aif)**,
byte-for-byte, so every stage is a drop-in and **any Nim/Nimony program behaves
identically** — and it also runs in the browser and ships native C / JavaScript
backends.

> We didn't set out to replace Nimony. The aoughwl substrate was going to run *on*
> it; we patched where it fell short, then rebuilt the pieces from scratch, and ours
> ended up better. We're here now, so we're finishing it.

**→ [AIF ≡ NIF: how it interops](https://aoughwl.github.io/docs/aif)** · **[the full stack](https://aoughwl.github.io/documentation)**

### The pipeline
`.nim / .aowl → aowlparse → aowlsem* → aowlhexer* → { aowlc → C · aowljs → JS · aowli → interpret }`

<sub>*`aowlsem` and `aowlhexer` are intentionally private for now — docs are public, access on request (Discord: **timbuktu_guy**). The playground moves onto the new sem + hexing shortly.*</sub>

| Project | Docs |
|---|---|
| **aowl toolchain** — `aowlparse` · `aowlsem` · `aowlhexer` · `aowlc` · `aowljs` · `aowli` | [AIF ≡ NIF](https://aoughwl.github.io/docs/aif) |
| **aowlup** — `rustup` for the stack: installs / versions / selects the toolchain (variants · profiles) | [repo ↗](https://github.com/aoughwl/aowlup) |
| **nim-code** — Claude Code plugin + MCP server | [docs](https://aoughwl.github.io/docs/nim-code) |
| **nimony-lsp** — Language Server + VSCode extension | [docs](https://aoughwl.github.io/docs/nimony-lsp) |
| **net stack** — `tcp`·`net`·`tls`·`http`·`compress`·`serve`·`ws`·`requests` — TLS 1.3, HTTP/1.1+2, WebSocket, HTTP/3 | [docs](https://aoughwl.github.io/docs/net-stack) |
| **web / html / css** — typed HTML5 + MDN CSS engine + DSL | [docs](https://aoughwl.github.io/docs/web) |
| **nimony-ts / nimony-py / nimony-hl** — idiomatic TS/Py backends + shared HL-IR | [ts](https://aoughwl.github.io/docs/nimony-ts) · [py](https://aoughwl.github.io/docs/nimony-py) · [hl](https://aoughwl.github.io/docs/nimony-hl) |


<br><br><br>

# Daily Blog

<br>

## 013 2026-07-19 - Sunday, July 19th 2026

More **aowlsem** — the whole day is a generics push. The semchecker now instantiates and preserves generic constructs end to end: typevar calls and signatures, generic object applications with substituted field types and attached hooks, generic array bounds and range iterators, generic seq index reads, `var` forwarding through generic params, late-bound generic hook calls, and quoted generic operators. Around it: `out` parameter type resolution, `sink`/`source` normalization, typed pointer comparisons lowered to magics, unchecked-pointer index assignments wrapped, `requires` pragma expression checking, and `threadvar` globals emitted. Steady, surgical commits — aowlsem is now **past 340 total commits** since Tuesday.

## 012 2026-07-18 - Saturday, July 18th 2026

**The biggest day yet for [aowlsem](https://aoughwl.github.io/docs/aowlsem)** — 126 commits landing the clean-room semchecker's core. It now passes **397/397 corpus fixtures byte-exact** against the nimony oracle, and — the milestone — it does a **complete zero-diagnostic traversal of the full `std/system`**: the whole `system.nim` plus its included `std/system/*.nim` set, ~6,383 lines, semcheck with **0 errors and 0 log lines**. Full-system parity against nimony's own output is down to ~33k canonical diff lines from an earliest baseline of ~62k — a **46.5% reduction**, with the first mismatch now a third of the way into the semantic output.

Under that headline: the magic table (arithmetic / comparison / set / pointer magics), `varargs[T]` params with call-site collection, membership (`x in coll`) generalized across seq/array/string, seq slicing and `s[a..b]`, `for (a, b) in …` tuple destructuring, `^k` backwards indexing, `countdown` typevar inference, concept declarations, lifetime-hook attachment, and `ptr UncheckedArray[T]` indexing. aowlsem also grows **diagnostics that go beyond nimony** — E0205 self-comparison, E0206 unsigned-compared-to-zero, E0207 empty-loop-range, E0208 tuple-index-out-of-bounds, E0209 shift-amount-out-of-range. *(source private for now; docs public, access on request)*

**We also stood up the whole distribution story — private components, public binaries.** The plan is simple: anything that stays source-private, we still ship to *everyone* — obfuscated, inside a stripped binary.

- **[obfuscate](https://github.com/aoughwl/obfuscate)** was reworked to be **IR-only**. It operates entirely on the compiler's own NIF/AIF token tree, never on source text, so it *inherently* can't corrupt runtime data — strings, chars and comments are their own token kinds and are never touched. Its `obfnif` pass renames every declared symbol to an opaque token (by spelling on parsed NIF, symbol-precise on typed NIF) and weaves in behaviour-preserving control flow, then the result re-feeds the pipeline and behaves identically.
- **[aowl-release](https://github.com/aoughwl/aowl-release)** is the hardening harness — a `build-release.sh` that wraps each component's *own* build and layers source obfuscation → a fail-closed licence/version gate → NIF control-flow injection → `--strip-all` (drops the symbol table decompilers love). The gate refuses to run an expired build; there's no risky client-side kill-switch.
- **Five `-release` repos** now exist as the public homes for the currently-private stages — **aowlsem-release**, **aowli-release**, **aowlts-release**, **aowlpy-release**, **aowlweb-release**. Source stays private; the obfuscated, gated, stripped binaries land here shortly so anyone can *run* the full stack.

**And [aowlup](https://github.com/aoughwl/aowlup) — `rustup` for the aowl/nimony stack.** It installs, versions, and *selects* the pipeline: every slot has interchangeable **variants** (parser `aowlparser`|`nifler`, sem `aowlsem`|`nimsem`, hexer `aowlhexer`|`hexer`, plus backends and tooling), grouped into one-command **profiles** (`aowl` = all ours, `nimony` = all theirs, `hybrid` = the driver default), each pinned to a git **version** with a GitHub update check (it doubles as a nimony version manager). [aowlmony](https://github.com/aoughwl/aowlmony) then compiles against whatever aowlup has selected — exactly the **rustup : cargo** split. The `-release` binaries plug straight into this: aowlup is how you'll pull, pin, and select them, and `aowlup +nimony` gives one-shot toolchain overrides.

And the playground grew a semantics choice. **aowlsem now runs in the browser** — you can pick **aowl semantics** instead of the default nim semantics when type-checking, right in the playground. It's marked **experimental**: real and checking a substantial slice today, but not the full stdlib or generics yet, so it grows from here. **aowlsuggest moved into the playground too** — its quick-fix / lint layer now runs client-side over the parser's diagnostics, so fix-its surface as you edit — and **aowlparser got another update**, with the latest parser bundle now shipping in the playground.

## 011 2026-07-17 - Friday, July 17th 2026

A heavy day on the front and middle of the pipeline.

**[aowlparser](https://aoughwl.github.io/docs/aowlparser)** — reached **full 310/310 structural parity** with the upstream Nim standard library: the entire stdlib round-trips. Shipped a real **`check` lint mode** — grammar-level error detection with fix-its and source-ordered diagnostics: assignment `=` where `==` was meant, a `for` missing its `in`, identifier-expected on `let`/`const`, and more. Fixed three parser **hangs** (infinite recursion) and hardened the lexer — UTF-8 identifiers, BOM stripping, custom numeric literals (`N'big`), parenthesized proc literals, term-rewriting template patterns.

**aowlsem** — a big step toward a true drop-in: an **auto-import system** that pulls in `system` and the module's own imports with no manual flags, real **`include`** splicing, `when not defined(...)` folding, definite-assignment that honours `noinit`/`threadvar`/`importc`, `typedesc` modelled as a type, templates as an overload set, accent-quoted/operator routine names, and the first **value-object ARC hook synthesis** — the foundation for `Table`. *(source private for now; docs public, access on request)*

**[aowli](https://aoughwl.github.io/aowli)** — the interpreter/VM now reads the shared **[aowlhl](https://aoughwl.github.io/docs/aowlhl)** HL-IR layer (`hlload` / `hlclassify` / `hlwalk`) instead of its own tree-walk, and gained **dynamic method dispatch** with field write-through for `ptr`/`var` receivers, closures with nested capture, and UTF-8 `add(string, Rune)`. With this, **aowli is feature-complete: it reproduces 100% of the runnable test corpus byte-for-byte** against nimony's own compile-and-run, on both engines (tree-walker and bytecode VM).

**aowlhl is now the shared high-level IR** — one Nim→HL-IR reader that both `aowli` and `aowljs` consume, so the interpreter and the JavaScript backend classify and walk the same skeleton. One lowering, many emitters.

**The docs site got a ground-up rebuild.** Migrated **[aoughwl.github.io](https://aoughwl.github.io)** off Jekyll / just-the-docs onto **VitePress** — it's now a single-page app with instant client-side navigation (no full reloads), a collapsible nested sidebar, a near-black dark theme, local search, and self-hosted fonts (no font or page flash). It deploys through a GitHub Actions workflow instead of Jekyll, and the in-browser [playground](https://aoughwl.github.io/playground/) is preserved byte-identically.

The nav is region-grouped — Overview / Pipeline / Emitters / Tools / Libraries — and every pipeline, emitter, and tool row carries a small right-aligned "↗" straight to that project's GitHub repo. A floating theme toggle sits in the corner, and GitHub · Discord · Support links live in the top bar.

## 010 2026-07-16 - Thursday, July 16th 2026

Repositioned: **aoughwl is a ground-up Nimony toolchain.** Wrote the interop contract — **[AIF ≡ NIF](https://aoughwl.github.io/docs/aif)**, byte-for-byte, so any Nim/Nimony program behaves identically. Renamed the compiler stages **`aif* → aowl*`** (aowlparse / aowlsem / aowlhexer / aowlc / aowljs / aowli / aowlmony) — `aif` now names the **format** only — and **`nim-code → aowl-code`**. Reworked the docs into two homes — **Documentation** (terse reference) and **Engineering Notes** (opinionated writeups) — collapsed the changelog into a single **Changes** record, and normalized every repo description + topics across the org. `aowlsem` and `aowlhexer` stay private for now (docs public, access on request); the playground moves onto the new sem + hexing shortly.

## 009 2026-07-015 - Wednesday, July 15th 2026

Created [aifhexer](https://github.com/aoughwl/aifhexer)<br>
Created [aif](https://aoughwl.github.io/docs/aif)<br>
Created [aifmony](https://github.com/aoughwl/aifmony)<br>
Created [aifc](https://aoughwl.github.io/docs/nifjs)<br>
Created [aifjs](https://aoughwl.github.io/docs/nifjs)<br>
Created [aifjs-js](https://github.com/aoughwl/nifjs-js)<br>
Created [aifsem](https://github.com/aoughwl/nifsem)<br>

Updated [aifi](https://github.com/aoughwl/nifi)<br>
Updated [aifparser](https://github.com/aoughwl/nifi)<br>
Updated [nimony-playground](https://aoughwl.github.io/playground/)<br>

## 008 2026-07-014 - Tuesday, July 14th 2026
Took [nifi](https://github.com/aoughwl/nifi) private,  oh- the fish weren't bittin today<br> 
Updated [nifi](https://github.com/aoughwl/nifi), 6-10x performance gain

## 007 2026-07-013 - Monday, July 13th 2026
Updated [nimony-playground](https://aoughwl.github.io/playground/)<br>
Updated [nifparser](https://github.com/aoughwl/nifparser)<br>
Updated [nifi](https://github.com/aoughwl/nifi)
* Added curly bracket support to the nifparser
* Finalized nifparser, passing against the full nimony suite- byte identical to niffler
* Nearly finished [nimony-playground](https://aoughwl.github.io/playground/), missing small QOL  and a final port to the aoughwl ecosystem (I cannot wait)

## 006 2026-07-012 - Sunday, July 12th 2026
Created [nimony-playground](https://aoughwl.github.io/playground/)<br>
Created [nifparser](https://github.com/aoughwl/nifparser)

## 005 2026-07-11 - Saturday, July 11th 2026
Created [nifi](https://github.com/aoughwl/nifi), a Nimony NIF Interpreter

## 004 2026-07-10 -  Friday, July 10th 2026

Created [aowl-lsp](https://aoughwl.github.io/docs/private), it's [nimony-lsp](https://aoughwl.github.io/docs/nimony-lsp.html), but with a universal plugin system. Obtain novel features!<br>
Created [vscode-aowl](https://aoughwl.github.io/docs/aowl), aoughwl hosted on-machine within VSCode

## 003 2026-07-09 -  Thursday, July 9th, 2026
Finalized the aoughwl core spec.<br>

Noticed a memory bug exists-  likely roots as a true Nimony bug  which interacts with niflens and my nim-code instances<br>
Created [nifrewrite](https://aoughwl.github.io/docs/nifrewrite) makes NIF rewrites simple<br>

Fixed [IC](https://aoughwl.github.io/docs/tooling-stack.html)<br>
Updated [niflens](https://aoughwl.github.io/docs/niflens.html)<br>
Updated [nimony-lsp](https://aoughwl.github.io/docs/nimony-lsp.html)<br>
Our VSCode extension + Nimony LSP is nearly as performant and featurefull as it can be, live diagnostics work phenomenally as you type... more to come here.

## 002 ‎2026-07-08 -  Wednesday, July 8th, 2026

**Pushed IC to aoughwl/Nimony:**  *~1s -> ~10ms*<br>
see: [ic-parallel-deps](https://aoughwl.github.io/changes/ic-parallel-deps.html), [ic-cursor-traversal](https://aoughwl.github.io/changes/ic-cursor-traversal.html), [ic-warm-daemon](https://aoughwl.github.io/changes/ic-warm-daemon.html), [ic-batch-intern](https://aoughwl.github.io/changes/ic-batch-intern.html)

Created [niflens](https://aoughwl.github.io/docs/niflens), a CLI tool for parsing and viewing NIF<br>
Updated [nimony-lsp](https://aoughwl.github.io/docs/nimony-lsp) and [nim-code](https://aoughwl.github.io/docs/nim-code) to benefit from [niflens](https://aoughwl.github.io/docs/niflens) — live diagnostics and suggestions now work as you type!

**Massively expanded the [net stack](https://aoughwl.github.io/docs/net-stack)** — now **8 one-concern repos**:<br>
&nbsp;&nbsp;• [tls](https://aoughwl.github.io/docs/net-stack/tls) — **TLS 1.3** over OpenSSL 3, client + server (SNI, ALPN, verification); pulled into its own repo<br>
&nbsp;&nbsp;• [serve](https://aoughwl.github.io/docs/net-stack/serve) — **HTTPS**, a **concurrent** worker pool, **HTTP/2** (nghttp2: h2c + ALPN `h2`), chunked request bodies + `Expect: 100-continue`, opt-in gzip/br compression<br>
&nbsp;&nbsp;• dual-stack **IPv6** across [tcp](https://aoughwl.github.io/docs/net-stack/tcp) / [net](https://aoughwl.github.io/docs/net-stack/net) — one listener serves v4 + v6<br>
&nbsp;&nbsp;• new [compress](https://aoughwl.github.io/docs/net-stack/compress) repo — one-shot **gzip / brotli / zstd** codecs<br>
&nbsp;&nbsp;• [ws](https://aoughwl.github.io/docs/net-stack/ws) — a nimony-native **WebSocket** (RFC 6455), server + client, `ws://` and `wss://`<br>
&nbsp;&nbsp;• **HTTP/3** in [requests](https://aoughwl.github.io/docs/net-stack/requests) (`useHttp3`) via curl-impersonate's bundled ngtcp2<br>
Every layer is tested against real clients — `curl --http2`, live `wss://`, TLS 1.3 handshakes.

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
