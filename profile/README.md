<p align="center">
  <img
    src="https://i.postimg.cc/Pxp72hcT/aoughwl-white-transparent.png"
    alt="aoughwl"
    width="330"
  >
</p>

<h1 align="center">
  <i>aowl</i> - Nim 3 / Nimony from-scratch
</h1>





<p align="center">
  ✓ drop-in replacement
  &nbsp;&nbsp;·&nbsp;&nbsp;
  ∞ written in itself
  &nbsp;&nbsp;·&nbsp;&nbsp;
  ⇩ mostly private - requests welcome
</p>

<br>

<p align="center">
  <a href="https://aoughwl.github.io/docs/aowlparser">parser</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowlsem">semantic checker</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowlsem/lowering">lowering</a>
  ·
  <a href="https://aoughwl.github.io/aowli">interpreter</a>
  ·
  <a href="https://aoughwl.github.io/aowli/debugging">debugger</a>
  <br>
  <a href="https://aoughwl.github.io/docs/aowlc">C</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowljs">native JavaScript</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowlweb">faithful JavaScript / WASM</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowlts">TypeScript</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowlpy">Python</a>
  <br>
  <a href="https://aoughwl.github.io/docs/aowllib">runtime</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowlabi">ABI</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowllsp">LSP / VS Code</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowlmcp">MCP</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowlcode">Claude Code</a>
  <br>
  <a href="https://aoughwl.github.io/docs/aowlsuggest">suggestions</a>
  ·
  <a href="https://aoughwl.github.io/docs/aowlfmt">formatter</a>
  ·
  <a href="https://aoughwl.github.io/docs/obfuscate">obfuscator</a>
  ·
  <a href="https://aoughwl.github.io/">standard library</a>
  ·
  <a href="https://aoughwl.github.io/docs/net-stack">net stack</a>
  ·
  <a href="https://aoughwl.github.io/docs/web">typed HTML / CSS</a>
  <br>
  <a href="https://aoughwl.github.io/">... and much, much more!</a>
</p>

<br>



<h3 align="center">
  <a href="https://aoughwl.github.io/playground/">
    ◦&nbsp; Try it all in the web IDE &nbsp;◦
  </a>
  <br>
</h3>
<p align="center">
  ▸ <a href="https://discord.gg/nxa3W7w4rJ">Join the Discord</a>
  ▸ <a href="https://aoughwl.com/">Visit our website</a>
</p>

 
 
 
 
<br><br><br><br>

# Daily Blog

<br>

## 039 2026-08-14 - Friday, August 14th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 35 commits.** Template expansion, generic instantiation and converters, overload-set ordering, pointer coercion, symbol numbering, and lifetime hooks and instance reuse for types imported from another module. Divergence from the reference compiler fell **32% on the day, 3,877 → 2,641 tokens** over 54 modules; three more standard-library modules are byte-identical — **41 → 44 of 54** — and the differential corpus is **911/911** — with the module that compiles aowlsem itself measured against its own grown source, so its figure rose even though the day's fixes cut it too.

<br>

## 038 2026-08-13 - Thursday, August 13th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 24 commits.** Generic type aliases, tuple assignment, enum members visible under two names at once, and comparison lowering inside instantiated generics. Two more standard-library modules are byte-identical — **39 → 41 of 54** — divergence from the reference compiler stands at **3,877 tokens**, and the differential corpus is **909/909**.

**[aowli](https://aoughwl.github.io/docs/aowli) — 1 commit.** Floating-point classification moved into the JavaScript runtime, and all four browser bundles were rebuilt against it.

<br>

## 037 2026-08-12 - Wednesday, August 12th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 73 commits.** Borrowed parameters, template expansion, overload resolution and generic instantiation. Divergence from the reference compiler fell **24% on the day, 5,138 → 3,908 tokens** over 54 modules; two more modules went byte-identical, and the differential corpus grew **883 → 902** cases. Six of the day's fixes were programs the reference compiler accepts and aowlsem was rejecting outright, rather than formatting differences. The [playground](https://aoughwl.github.io/playground/) now checks with aowlsem by default.

**[aowli](https://aoughwl.github.io/docs/aowli) — 1 commit.** Floating-point classification in the JavaScript environment.

<br>

## 036 2026-08-11 - Tuesday, August 11th 2026

🎉 **[aowlsem](https://aoughwl.github.io/docs/aowlsem) passed its 2,000th commit today** — 27 days after the first, **173 of them today**. **45,679 lines** of Nimony, checking the language it is itself written in.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 173 commits.** Overload resolution, enum handling and generic instantiation. Divergence from the reference compiler fell **31% on the day, 11,244 → 7,736 tokens**, and two more standard-library modules are now byte-identical; three of the day's fixes were wrong-output bugs rather than formatting differences. Differential corpus **869/869** on a cold cache, diagnostics 176/176, no library module falling back to abort 54/54.

**[aowlparser](https://aoughwl.github.io/docs/aowlparser) — 16 commits.** YAML and ini/nim.cfg take the byte-exact set to ten languages, and a new JSON reader runs at **2,343 MB/s** where V8 manages 621 and CPython 225 on the same 9.9MB document. Every parser is now held to an outside implementation rather than to its own expectations — CPython's `json` over **10,029 files and 494,373 truncated prefixes**, CPython's `tokenize` over 3,492 Python files, the official yaml-test-suite over 402 cases — which surfaced 27 disagreements in the YAML dialect alone that reproducing the input byte for byte cannot see. CSS, HTML and `<style>` markup inside it now fail the build when they are invalid, through a Nimony plugin; unclosed HTML elements report at the opening tag, with 3 reports across 400 real pages and all three genuine.

<br>

## 035 2026-08-10 - Monday, August 10th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 74 commits.** Overload resolution and generic-body copying: **737 tokens** of divergence closed, one of them a call bound to the wrong module's function. Corpus **839/839** cold, no-abort 54/54, all 46 library rows at baseline.

**[aowlparser](https://aoughwl.github.io/docs/aowlparser) · [css](https://aoughwl.github.io/docs/css) — 11 commits.** A Nim-only parser became a library covering eight languages, each checked by reproducing its input byte for byte: **11,556** JavaScript files, 5,920 Markdown, 4,326 JSON, 2,885 Python, 1,224 CSS grammars and 150 HTML pages. Stylesheets now validate against the CSS specification's own value grammars — Bootstrap, **4,368 declarations, none invalid**.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 2 commits.** Conditional breakpoints in the debugger.

<br>

## 034 2026-08-09 - Sunday, August 9th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 171 commits.** Generic instantiation, `try` as an expression, and lifetime hooks. Library divergence 31,170 → **30,391 tokens**; corpus **799/799** cold, diagnostics 416/418, end-to-end 4/6.

**[aowli](https://aoughwl.github.io/docs/aowli) — 39 commits.** The foreign-function boundary, and the first measured cut to what interpretation costs: string hashing as a primitive took **18.7%** off interpreter work on a real compile, output byte-identical.

<br>

## 033 2026-08-08 - Saturday, August 8th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 89 commits.** Lifetime hooks for reference fields, overload arity, and overload-set ordering. **Four programs run end to end for the first time, 0/6 → 4/6**; corpus **797/797** cold, **31 of 54** library modules byte-identical.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 30 commits.** Running long-lived sessions unattended: supervision, restart limits, an on-disk mailbox, and attachable terminals. Gates **72/72** and **39/39**, negative cases first.

**[aowli](https://aoughwl.github.io/docs/aowli) — 10 commits.** Foreign-function crossings generated from signatures rather than hand-written bindings; TLS now runs interpreted.

<br>

## 032 2026-08-07 - Friday, August 7th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 41 commits.** End-to-end compilation, module rejection and cycle-collection hooks; five library modules the reference compiles were being rejected outright. **31 of 52** modules byte-identical, corpus **785/785**. A shared test cache took one gate from 49.4s to **1.8s**.

**[aowli](https://aoughwl.github.io/docs/aowli) — 4 commits.** Nested acquisition of the machine-wide compile lock; one gate went from over 400 seconds to **146**.

**[discord](https://aoughwl.github.io/docs/discord) · [colors](https://aoughwl.github.io/docs/colors) · [json](https://aoughwl.github.io/docs/aowljson) — 7 commits.** A Discord bot client on our own network stack — gateway WebSocket, REST, slash commands.

<br>

## 031 2026-08-06 - Thursday, August 6th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 93 commits.** Generic instances and field lookup — five wrong-output bugs of one shape. Corpus **772/772**, no-abort **46/46**.

**[aowlabi](https://aoughwl.github.io/docs/aowlabi) — 20 commits.** The ABI is now gated against everything that re-spells it: the JavaScript value representation, the C runtime's hand-copied offsets, and gcc at 32 bits. **122/122** layout, 208/208 heap, **1269/1269** marshalling.

**[aowlc](https://aoughwl.github.io/docs/aowlc) — 20 commits.** The C backend's two printers are compared against each other and against the reference — **73/73**, exemption list empty; every module compiles and links alone, **77/77**.

**[aowli](https://aoughwl.github.io/docs/aowli) — 25 commits.** A public wrong-answer fix, released as v0.3.5. Both engines **461/461** across 53 categories, zero divergences.

**[aowljs](https://aoughwl.github.io/docs/aowljs) — 9 commits.** `sizeof` of aggregates now comes from the ABI layout engine rather than a table of its own. Corpus **124/124**.

<br>

## 030 2026-08-05 - Wednesday, August 5th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 62 commits.** Type identity: eight details were missing from it, so genuinely different types could share one generic instance. Corpus 745 → **762/762**; library divergence 48,579 → **42,190 tokens**, **96.54%** of 1,220,605 matching byte for byte — about 5,000 of that drop a re-baseline rather than new ground.

**[aowli](https://aoughwl.github.io/docs/aowli) — 54 commits.** Hot-swapping, the foreign-function boundary and cache tooling. Hybrid **24/24**, corpus **460/460** across 53 categories, destructor mode 18/18 on both engines.

**[aowljs](https://aoughwl.github.io/docs/aowljs) — 45 commits.** Value semantics on a reference-semantics target — assignment, equality, `in`/`find`, byte strings, and five statement kinds that had been dropped whole. Corpus 18 → **102/102**.

**[aowlc](https://aoughwl.github.io/docs/aowlc) — 31 commits.** Three miscompiles that survived because the gate could not hear what gcc was reporting.

**[aowlabi](https://aoughwl.github.io/docs/aowlabi) — 6 commits.** The gates measured the checker's `sizeof` rather than the struct that reaches a binary.

<br>

## 029 2026-08-04 - Tuesday, August 4th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 150 commits.** Library divergence fell **73,809 → 48,579 tokens (−34%)**, and **30 modules are byte-exact**, up from 20.

**[aowli](https://aoughwl.github.io/docs/aowli) — 81 commits.** Capability grants, destructors on the error path, and the just-in-time compiler's in-process route.

**[aowlc](https://aoughwl.github.io/docs/aowlc) — 5 commits.** Translation-unit ordering.

<br>

## 028 2026-08-03 - Monday, August 3rd 2026

**[aowli](https://aoughwl.github.io/docs/aowli) — 124 commits.** Objects can live in flat allocated memory — the storage the compiler's own token buffers use — and the interpreter grew record/replay. Replay 19/19, cross-engine **189 agreeing, 0 diverging**; the interpreter now runs the real compiler end to end.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 48 commits.** Imported templates in overload resolution, and compile-time predicates. Corpus **718/718**, accept/reject 403/403, diagnostics 175/175.

**[aowlabi](https://aoughwl.github.io/docs/aowlabi) — 20 commits.** The canonical-layout claim checked against the compiler for the first time, which found every inherited field at the wrong offset. **96/96** layout, 153/153 heap, **857/857** marshalling.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 3 commits** · **[aowlmony](https://aoughwl.github.io/docs/aowlmony) — 3 commits** · **[aowltest](https://aoughwl.github.io/docs/aowltest) — 1 commit.** Token cost measured for the first time; `verify --memory` catching dangling pointers; the test gate turned into a corpus any implementation can run against.

<br>

## 027 2026-08-02 - Sunday, August 2nd 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 35 commits.** Compile-time evaluation moved beyond `const` initialisers, then got bounded by a capability policy. Corpus 685 → **701/701**, const evaluation **18/18**.

**[aowli](https://aoughwl.github.io/docs/aowli) — 21 commits.** Interpreted code is now replaceable *and* compilable while the process runs. Corpus **449/449**, hot-swap 9/9, just-in-time 6/6, policy 11/11.

**[aowltest](https://aoughwl.github.io/docs/aowltest) — new repo, 3 commits** · **[aowlrepl](https://github.com/aoughwl/aowlrepl) — new repo, 4 commits** · **[aowlhost](https://aoughwl.github.io/docs/aowlhost) — new repo, 4 commits.** Test results keyed by the hash of their transitive inputs, so an unchanged closure is never re-run (**41/41**); a REPL on the interpreter, cold 2.15s and warm 0.19s; and a module run as a plugin under a capability policy, with the interpreter embedded as a library.

**[web](https://aoughwl.github.io/docs/web) · [css](https://aoughwl.github.io/docs/css) · [web-state](https://github.com/aoughwl/web-state) · [aowlui](https://github.com/aoughwl/aowlui) — 20 commits.** The typed HTML and CSS surface.

<br>

## 026 2026-08-01 - Saturday, August 1st 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 71 commits.** Macros and `const` initialisers stopped being matched by shape and started being *run*. Corpus **677/677**, accept/reject 400/400, diagnostics 175/175.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 53 commits.** Every tool re-examined for what its verdict actually rests on: 197 curated plus 116 swept cases, 107 unit, 39 end-to-end, all 8 hooks smoke-tested.

**[aowli](https://aoughwl.github.io/docs/aowli-release) — 35 commits.** Silent wrong answers — plausible output, exit 0, empty stderr. **414/414**, later 434/434, three-way cross-check with zero divergences.

**[serve](https://aoughwl.github.io/docs/net-stack/serve) — 29 commits.** h2spec 95/146 → **146/146** over both h2c and TLS; 128 MiB streamed byte-exact at 6 MB peak memory.

<br>

## 025 2026-07-31 - Friday, July 31st 2026

🎉 **[aowlsem](https://aoughwl.github.io/docs/aowlsem) passed its 1,000th commit** — 16 days after the first, **98 of them today**, **~32,500 lines** of self-hosted Nimony.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 98 commits.** Generic instantiation: *when* an instance is created, and what a generic declaration may resolve while its arguments are still abstract. Byte-exact corpus 632 → **659**, no-false-positive gate 23 → **35**; `std/sets` 7,530 → **147** tokens, `std/bitabs` 5,863 → **1,236**, `std/widestrs` 5,009 → **415**.

**[aoughwl](https://aoughwl.github.io/docs/aoughwl) — 18 commits** · **[aowlmcp](https://aoughwl.github.io/docs/aowlmcp) — 2 commits.**

<br>

## 024 2026-07-30 - Thursday, July 30th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 89 commits.** Gained its second half: an [optimizer](https://github.com/aoughwl/aowlsem/blob/master/OPTIMIZER.md) over the checked IR — twenty-one passes to a fixpoint, kept structurally separate from the checker so the byte-parity claim and the meaning-preservation claim never share an exit path. A scale gate runs every real program three ways and demands identical output: **103 → 344** of 609 programs, and it caught nine miscompiles the small suite passed. Hot loops **5.3x**, **2.8x**, **1.8x**; whole library modules 1–3% smaller.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 8 commits.** 1.0: the tool gate is on by default, and [aowl mode](https://aoughwl.github.io/docs/aowlcode/aowl-mode) denies code searches and raw compiler invocations in favour of four bounded tools.

**[aoughwl](https://aoughwl.github.io/docs/aoughwl) — 19 commits.** Anonymous sum types, construction through `of`-pattern matching, across module boundaries.

<br>

## 023 2026-07-29 - Wednesday, July 29th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 120 commits.** The half of a checker that never shows up in its output: deciding which programs are *wrong*. About thirty new checks and four false positives removed, each confirmed to fire for the right reason rather than by coincidence. Corpus **618 modules**, accept/reject agreement 76 → **139**, error-message snapshots 64 → **97**, and all **71** diagnostic codes carry a long-form article.

**[aoughwl](https://aoughwl.github.io/docs/aoughwl) — 25 commits.** The [playground](https://aoughwl.github.io/playground/) became a real in-browser IDE — multi-file projects, clone-a-repo-from-a-link, split editors, and the debugger's flame timeline, all running in the tab.

<br>

## 022 2026-07-28 - Tuesday, July 28th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 123 commits.** Byte-level parity against the reference's typed output: generic `ref object` types, value objects carrying methods, and definite assignment — reading a variable before it is set is now an error. **~21.7k lines**, corpus **500/500**, accept/reject **10/10**, `std/system` clean.

**[aowli](https://aoughwl.github.io/docs/aowli) — 8 commits.** Debugging a large program stopped meaning recompiling it: first debug of a session ~47s, every one after **~1 second**. Released v0.3.3 — hybrid mode now crosses `ref` and `seq`-bearing data.

<br>

## 021 2026-07-27 - Monday, July 27th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 118 commits.** Generic type instantiation brought in line with the reference. **~18.6k lines**, corpus **498/498**, `std/system` checking clean.

**[aowli](https://aoughwl.github.io/docs/aowli) — 9 commits.** The debugger can pause a running program and step through it interactively rather than printing snapshots after the fact, with values rendered under a size budget and single fields addressable by name. Released v0.3.2 — two shipped-runtime correctness fixes found by running a real argument parser under the interpreter.

<br>

## 020 2026-07-26 - Sunday, July 26th 2026

**[aowlmcp](https://aoughwl.github.io/docs/aowlmcp) — 2 commits.** Speaks the [MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) spec — a stateless core, mid-call input elicitation, and a tasks extension — while still serving the previous version, negotiated per request. Proven over all three transports: stdio **27/27**, HTTP **15/15**, HTTP/3 **4/4**.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 25 commits** · **[aowli](https://aoughwl.github.io/docs/aowli) — 7 commits** · **[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 4 commits.** Released aowli v0.3.1: the interpreter runs the semantic checker itself, byte-identical to a native compile — **520/520 tokens**, after three root-cause fixes including an uninitialised-pointer class caught under valgrind.

<br>

## 019 2026-07-25 - Saturday, July 25th 2026

**[aowli](https://aoughwl.github.io/docs/aowli) — 27 commits.** Released v0.3.0, the correctness-complete build: both engines at **zero in-scope divergence across a 423-program corpus**, agreeing with each other and with native. Value semantics landed, the last OS-boundary gaps closed, and hybrid mode executed real foreign C for the first time.

**[aowlmony](https://aoughwl.github.io/docs/aowlmony) — 4 commits.**

<br>

## 018 2026-07-24 - Friday, July 24th 2026

**[aowlabi](https://aoughwl.github.io/docs/aowlabi) — 3 commits, new repo.** One source of truth for how values are laid out — sizes, field offsets, heap block layout, and which types cross a native boundary how. The interpreter and both backends had each kept their own copy, and they had drifted.

**[aowli](https://aoughwl.github.io/docs/aowli) — 34 commits.** A real runtime layer: the scattered crossings into faster or foreign executors became one provider registry, one codec, and a policy that is never silently wrong. The payoff is hybrid execution — interpret the file you care about, run every other module native, byte-identical either way.

<br>

## 017 2026-07-23 - Thursday, July 23rd 2026

**[aowli](https://aoughwl.github.io/docs/aowli) — 35 commits.** Became an actual runtime: flat memory, casts, allocation, unchecked arrays, file I/O, environment access, ownership hooks and refcounted `ref` objects, with fail-fast on unsupported calls. It runs about **92%** of compiler-buildable programs with no known silent wrong answers.

<br>

## 016 2026-07-22 - Wednesday, July 22nd 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 35 commits** · **[aowli](https://aoughwl.github.io/docs/aowli) — 12 commits.** Released aowli-release v0.1.0 — stripped binaries, a fail-closed licence gate, and no source paths or internal names.

**[aowlmcp](https://aoughwl.github.io/docs/aowlmcp) — 6 commits, new repo** · **[aowljson](https://aoughwl.github.io/docs/aowljson) — new repo.** Transport-independent MCP dispatch over stdio, HTTP and HTTP/3 (**13/13**, **6/6**, **4/4**), on reusable JSON values with error-as-value parsing.

**[serve](https://aoughwl.github.io/docs/net-stack/serve) — 11 commits** · **[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 5 commits.**

<br>

## 015 2026-07-21 - Tuesday, July 21st 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 55 commits** · **[aoughwl](https://aoughwl.github.io/docs/aoughwl) — 39 commits.** Generics and the toolchain around them.

<br>

## 014 2026-07-20 - Monday, July 20th 2026

**[aoughwl](https://aoughwl.github.io/docs/aoughwl) — 17 commits** · **[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 2 commits.** A light day.

<br>

## 013 2026-07-19 - Sunday, July 19th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 55 commits.** A generics push: typevar calls and signatures, generic object applications with substituted field types and attached hooks, generic array bounds, `var` forwarding through generic parameters, and late-bound hook calls. Around it, `out` parameters, `sink` normalisation, typed pointer comparisons, and `threadvar` globals.

<br>

## 012 2026-07-18 - Saturday, July 18th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 126 commits.** The clean-room checker's core: **397/397** corpus fixtures byte-exact, and a complete zero-diagnostic traversal of the whole of `std/system` — ~6,383 lines, 0 errors, 0 log lines. Parity against the reference's own output down to ~33k canonical diff lines from ~62k, a **46.5%** reduction. It also grows diagnostics the reference does not have.

**[obfuscate](https://github.com/aoughwl/obfuscate) · [aowlup](https://github.com/aoughwl/aowlup) — the distribution story.** Private components still ship to everyone: an IR-only obfuscator that cannot corrupt runtime data because it never touches source text, a hardening harness, and a toolchain version manager with interchangeable variants per pipeline slot.

**[aowlsuggest](https://aoughwl.github.io/docs/aowlsuggest) — 9 commits** · **[aowlparser](https://aoughwl.github.io/docs/aowlparser) — 9 commits.** Both now run client-side in the playground, so fix-its surface as you edit.

<br>

## 011 2026-07-17 - Friday, July 17th 2026

**[aowlparser](https://aoughwl.github.io/docs/aowlparser) — 44 commits.** Full **310/310** structural parity with the Nim standard library — the entire stdlib round-trips — plus a real `check` lint mode with fix-its, three parser hangs fixed, and a hardened lexer.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 78 commits.** A step toward a true drop-in: auto-import, real `include` splicing, definite assignment honouring `noinit`/`threadvar`/`importc`, `typedesc` modelled as a type, templates as an overload set, and the first value-object lifetime-hook synthesis.

**[aowlsuggest](https://aoughwl.github.io/docs/aowlsuggest) — 36 commits** · **[aowlts](https://aoughwl.github.io/docs/aowlts) — 22 commits** · **[aowljs](https://aoughwl.github.io/docs/aowljs) — 18 commits.** The interpreter and the JavaScript backend moved onto one shared high-level IR — one lowering, many emitters.

**The docs site was rebuilt from the ground up** — off Jekyll onto a single-page app with instant navigation, local search and self-hosted fonts, the playground preserved byte-identically.

<br>

## 010 2026-07-16 - Thursday, July 16th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 99 commits** · **[aowlparser](https://aoughwl.github.io/docs/aowlparser) — 85 commits** · **[aowli](https://aoughwl.github.io/docs/aowli) — 26 commits.** Repositioned as a ground-up Nimony toolchain, with the interop contract written down: our IR is byte-for-byte the reference's, so any Nim or Nimony program behaves identically. The compiler stages were renamed to `aowl*` and the docs split into reference and engineering notes.

<br>

## 009 2026-07-15 - Wednesday, July 15th 2026

**[aowlparser](https://aoughwl.github.io/docs/aowlparser) — 27 commits** · **[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 13 commits, first day** · **[aowli](https://aoughwl.github.io/docs/aowli) — 9 commits.** The hexer, the C and JavaScript backends and the checker all got their repos; the playground took 21 commits.

<br>

## 008 2026-07-14 - Tuesday, July 14th 2026

**[aowlparser](https://aoughwl.github.io/docs/aowlparser) — 9 commits** · **[aowli](https://aoughwl.github.io/docs/aowli) — 5 commits.** The interpreter went private, and took a **6–10×** performance gain.

<br>

## 007 2026-07-13 - Monday, July 13th 2026

**[aowlparser](https://aoughwl.github.io/docs/aowlparser) — 29 commits** · **[aowli](https://aoughwl.github.io/docs/aowli) — 6 commits.** The parser was finalised against the full reference suite, byte-identical to the reference parser, and gained curly-brace support.

<br>

## 006 2026-07-12 - Sunday, July 12th 2026

**[aowli](https://aoughwl.github.io/docs/aowli) — 24 commits** · **[aowlparser](https://aoughwl.github.io/docs/aowlparser) — 7 commits.** The parser and the in-browser playground were created.

<br>

## 005 2026-07-11 - Saturday, July 11th 2026

**[aowli](https://aoughwl.github.io/docs/aowli) — 16 commits, new repo.** A Nimony IR interpreter.

<br>

## 004 2026-07-10 - Friday, July 10th 2026

**6 commits.** A language server with a universal plugin system, and the editor extension that hosts it.

<br>

## 003 2026-07-09 - Thursday, July 9th 2026

**[aoughwl](https://aoughwl.github.io/docs/aoughwl) — 22 commits** · **[nimony-lsp](https://aoughwl.github.io/docs/nimony-lsp) — 14 commits.** The core spec finalised, incremental compilation fixed, and a NIF rewriting tool created. Live diagnostics as you type.

<br>

## 002 2026-07-08 - Wednesday, July 8th 2026

**[net stack](https://aoughwl.github.io/docs/net-stack) — 40 commits across eight repos.** TLS 1.3 client and server, HTTPS with a concurrent worker pool, HTTP/2 and HTTP/3, a native WebSocket, dual-stack IPv6, and one-shot gzip/brotli/zstd — each tested against real clients.

**[nimony-lsp](https://aoughwl.github.io/docs/nimony-lsp) — 13 commits.** Incremental compilation went **~1s → ~10ms**, and a NIF viewing tool made live diagnostics and suggestions work as you type.

<br>

## 001 2026-07-07 - Tuesday, July 7th 2026

**31 commits across four repos.** The official aoughwl/nimony fork starts here — features, bug fixes, and a more substantial standard library — alongside the language-server side and a Claude Code plugin focused on cutting token use with Nim and Nimony.

<br>
