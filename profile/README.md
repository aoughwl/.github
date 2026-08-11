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

## 036 2026-08-11 - Tuesday, August 11th 2026

🎉 **[aowlsem](https://aoughwl.github.io/docs/aowlsem) passed its 2,000th commit today** — 27 days after the first, **146 of them today**. **45,679 lines** of Nimony, checking the language it is itself written in.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 146 commits.** Overload resolution, enum handling and generic instantiation. Divergence from the reference compiler fell **31% on the day, 11,244 → 7,742 tokens**, and two more standard-library modules are now byte-identical; three of the day's fixes were wrong-output bugs rather than formatting differences. Differential corpus **869/869** on a cold cache, diagnostics 176/176, no library module falling back to abort 54/54.

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

**[discord](https://aoughwl.github.io/docs/discord) · [colors](https://aoughwl.github.io/docs/colors) · [json](https://aoughwl.github.io/docs/aowljson) · [mcp](https://aoughwl.github.io/docs/aowlmcp) — 8 commits.** A Discord bot client on our own network stack — gateway WebSocket, REST, slash commands.

<br>

## 032 2026-08-07 - Friday, August 7th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 41 commits.** End-to-end compilation, module rejection and cycle-collection hooks; five library modules the reference compiles were being rejected outright. **31 of 52** modules byte-identical, corpus **785/785**. A shared test cache took one gate from 49.4s to **1.8s**.

**[aowli](https://aoughwl.github.io/docs/aowli) — 4 commits.** Nested acquisition of the machine-wide compile lock; one gate went from over 400 seconds to **146**.

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

**[aowljs](https://aoughwl.github.io/docs/aowljs) — 30 commits.** Value semantics on a reference-semantics target — assignment, equality, `in`/`find`, byte strings, and five statement kinds that had been dropped whole. Corpus 18 → **102/102**.

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

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) passed its 1000th commit** — 16 days after the first, **65 of them today**, all in the checker. **~32,500 lines** of self-hosted Nimony; byte-exact corpus **632 → 659**, no-false-positive gate **23 → 35**.

**The productive gate was a broad differential over real modules, not hand-written probes.** Compiling a real project and re-checking every module the reference produced output for found a day's work in a single run, after feature probes had gone several rounds finding nothing. 18 of 40 modules byte-exact, zero crashes, the rest quantified rather than guessed at.

**The dominant class was *when* a generic instance gets created**, and it came down to three rules:

* A generic **type**'s body can keep its arguments abstract; a generic **routine**'s signature cannot, because it is shared by every instantiation.
* Inside a generic declaration, a call over still-abstract operands must stay symbolic. Instantiating there dragged in the operator's entire lifetime-hook cascade — **5,922 tokens on a two-line program**. `std/sets`: 7,530 → 147.
* The "is this a type variable" test, consulted from around 25 places, **guessed from spelling** — one uppercase letter — so `BiTable*[Id, T]` had one of its two parameters recognised. Every type variable is now recorded when it is created, with spelling kept only as a fallback for imported generics. `std/bitabs`: 5,863 → 1,236.

**Commit #1000 fixed the ordering assumption underneath all of it.** Type instances are emitted in request order, and a dependency is requested by the body that needs it — so a `HashSet[T]` whose backing `Table` had not registered yet read its own field as unmanaged, and neither it nor anything holding one got lifetime hooks. Reordering is not the answer, because the reference emits in the same order; it decides from the *declaration*, so now we do too. `std/optcore`: 18,369 → 16,052.

**Smaller parity fixes, each pinned to a real program:** a `distinct` over a primitive keys its base's magic on its own symbol; an anonymous routine must never consume a name slot, or a lambda in a global initialiser takes the next proc's name; a user-declared lifetime hook suppresses field-wise synthesis; `{.push header: … .}` applies to parameters as well as declarations; a prefix operator can be a template; a named argument may skip a defaulted parameter; and four absent constant folds, one of which had been silently dropping the whole of `std/widestrs` — 5,009 → 415.

**One thing is written down as not reproducible rather than chased.** The reference lists an overload choice in an order that is not declaration order, not index order, and not sorted. We emit the right set, sorted, and the commit says so.


## 024 2026-07-30 - Thursday, July 30th 2026

[aowlcode](https://github.com/aoughwl/aowlcode) is now private indefinitely.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) 1.0 — the tool gate is on by default.** aowlcode fronts the Nim and Nimony toolchains for an agent: structured diagnostics, NIF slices and navigation instead of raw compiler output and 40KB single-line artifacts. The tools shipped months ago and were still bypassed for `grep -rn` + `sed -n`, so 1.0 inverts the default rather than the documentation.

**[Aowl mode](https://aoughwl.github.io/docs/aowlcode/aowl-mode), default `guided`.** A `PreToolUse` hook denies `Grep`, `Glob`, and Bash segments that are a code search, a source/NIF dump, a tree walk, or a raw `nim c` / `nimony c` / `nim check`. `git`, test scripts and running a built binary pass; `strict` denies Bash outright. Each denial carries a redirect table and appends to a ledger `/aowl-mode status` reports. No state file ⇒ `guided`; `off` is a written state, not its absence, and expires on the same 12h TTL, so a stale `strict` and a stale `off` both fall back to baseline. Escape hatches: `aowlcode-mode` commands always pass, `AOWLCODE_DEFAULT_MODE` moves the baseline, `AOWLCODE_NO_MODE_GATE=1` removes the hook, every hook fail-open.

**Four tools cover what the gate removes**, each replacing a habit whose failure mode is unbounded output — **`search`** (excludes generated trees and hidden dirs; `.claude/worktrees/` alone multiplied one repo's apparent source count ×10; caps and reports truncation), **`map`** (one-call orientation, parsing the build script's actual compiler invocation so a Nimony project with no `nimony.cfg` marker stops resolving as Nim), **`changes`** (`git diff` as per-file `+N -M` and hunk headers, ~1% of patch bytes), and **`run`** (output *middle* elided, head 30 / tail 60, so the failing assertion at the tail always survives).

**0.8, same cycle**, closed three gaps two agents had each hand-rolled in shell: **`nif_run`** executes a built `.s.nif` on [aowli](https://aoughwl.github.io/aowli) with its sibling modules, deriving the install name from the artifact's own `stmts` header (getting it wrong silently runs the oracle instead of the candidate); **`bisect`** runs ddmin over a flag matrix for the minimal reproducing toggle set, catching multi-flag interactions a linear scan misses; **`nif_diff mode=canon|semantic`** strips line info and framing and folds generic-instance hashes, replacing a hand-written `canon.py`. Plus 28 end-to-end checks over the real MCP loop.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) gained its second half: an [optimizer](https://github.com/aoughwl/aowlsem/blob/master/OPTIMIZER.md) on `.s.aif`.** **~30.5k lines**, **917 commits** (**67 today**), corpus **631 modules**. Separate command — `aowlsem m` checks and must match nimsem byte for byte; `aowlsem opt` rewrites and must only preserve meaning. Those claims cannot share an exit path, so the parity gate is structurally untouched.

**Twenty-one passes** to a fixpoint (nine sweeps max, tree strictly shrinks): constant folding over the twelve arithmetic/bitwise magics; comparison/`not`/`xor` of constants; short-circuit `and`/`or`; algebraic identities including operand-discarding ones (legal only once purity can be asked); redundant-conversion drop; constant `if`/`case` selection; `while false`; unreachable statements; dead and write-only locals; unreferenced private procs; constant and copy propagation, where the constant query sees *through* propagated locals — which is what lets folding and `case` selection fire at all. Inlining runs first each sweep in three shapes, alpha-renaming the inlined body since `.s.aif` symbols are module-wide unique. Two invariants cut across: **exported means live**, and **never drop work with effects**.

**The verification is the substantive part.** A dozen hand-written programs will call an optimizer green. A scale gate builds each real program three ways (nimsem's output, ours unoptimized, ours optimized), runs all three on aowli, and demands byte-identical stdout and exit. It **caught nine genuine miscompiles the small suite passed** — an expression-`if` deleted outright, an inliner accepting any three-statement proc as one-expression, `{.keepOverflowFlag.}` making arithmetic observable, inlined generic-instance bodies, statements pasted into expression position — each narrowed by `--no:PASS` sweep and pinned with a regression program. The gate went **103 → 344** of 609 candidates; one fix (deriving the install name from the artifact header) recovered 145 programs silently recorded as "did not run".

Measured payoff from `bench.sh`: three nested one-line procs in a hot loop, **360,003 calls → 3**, 505ms → 95ms (**5.3x**); one hot one-liner, 120,003 → 3, 212ms → 77ms (**2.8x**); a partly-constant loop body, 118ms → 64ms (**1.8x**). On whole library modules it removes ~1–3% of nodes, and the doc says so — a library is nearly all exported surface.

**Anonymous sum types closed** — construction and `of`-pattern matching, including failures that only appear across a module boundary: instantiating an imported generic sum type (`Opt[T]`, `Result[T, E]`) left pattern bindings holding a field's *address* rather than its value, and the family's shared tag type was re-declared in every importing module instead of being recognised as foreign by its mangled module segment. That exposed a wider gap worth more than the feature — a local initialised by a call returning a generic application had no type at all. `std/opt` and `std/result` check byte-exact both as the defining module and from an importing one.

## 023 2026-07-29 - Wednesday, July 29th 2026

**The [playground](https://aoughwl.github.io/playground/) grew into a real in-browser IDE** — still the whole toolchain (parser, checker, interpreter, debugger) compiled to JavaScript, running entirely in the tab.

* **Multi-file projects + explorer.** Dockable tree with context menus, multi-select, drag-to-move, **preview tabs** (single-click italic preview, double-click or edit keeps it), and **navigation history** on the mouse back/forward buttons (or Alt+←/→).
* **Clone a repo, or share a workspace, from a link.** Type `owner/repo` to clone a public GitHub repo client-side, or hand someone a `#clone=owner/repo` link. **Share** packs the *entire* workspace — every project and file — into one compressed link, not just the active buffer.
* **The [aowli](https://aoughwl.github.io/aowli) debugger, live in the browser.** Step through a program on a **flame / depth timeline**: every statement a cell, call depth stacked into lanes, per-routine colour, zoomable slice and full-run minimap — scrub, reverse-step, jump anywhere, auto-captured on open. (Fixing the current-line highlight traced a neat root cause: `echo` is a *template*, so its expansion carries the stdlib's line info, not your call site — the debugger is now file-aware.)
* **Split editors + stdlib browsing.** Drag a tab to any edge for side-by-side or stacked. Ctrl-click or F12 on an `import` opens the real std source. `.json` / `.js` / `.c` / `.nif` get native highlighting — including a proper **NIF** grammar — and skip the nimony pipeline, so only `.nim` / `.aowl` are checked and run.
* **Latest bundles**: obfuscated **aowlsem** and the **aowli** interpreter + debugger refreshed.

Every doc page for a runnable library now carries a **"▶ Try it live in the Playground"** link.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) spent the day on the half of a checker that never shows up in its output: deciding which programs are *wrong*.** Byte-for-byte agreement on valid programs says nothing about invalid ones, and a checker that quietly accepts a broken program is worse than one emitting a slightly different tree for a good one. The method is a checked-in tool: ten small programs around **one theme** — arguments, literals, control flow, generics and closures, declarations, numeric types, exceptions — through both checkers, verdicts side by side. Rejecting what the reference accepts is the urgent kind; accepting what it rejects is a missing check; occasionally the reference is wrong.

**About thirty checks landed.** A sample of what now errors instead of passing silently: a named argument no parameter answers to (with a did-you-mean); `for a, b in 0 ..< 3`, where the range yields one value per step; assigning to the result of a call; a `case` on a float; the branches of an `if`-*expression* disagreeing on type; a variant constructor setting a field from an unselected branch; a nested `proc` reading its enclosing local without being a closure; arithmetic on types that have none (`true * false`, `'z' - 'a'`, `"a" + "a"`); indexing with a non-number; mixing signed and unsigned; a `set` over a non-ordinal; deriving from an object never made a base type; the wrong number of type arguments; a `converter` not taking exactly one parameter; a pragma that is not one (checked against the whole vocabulary plus your own); and an entire family that had been silently accepted — **an undeclared type name in any position**: field, parameter, local, parent, generic argument, `except` filter.

**Four false positives came out of the same loop, and mattered more than the gaps.** Two `method`s along one inheritance chain reported as ambiguous — the subtype relation made the signatures look identical. Shadowing a parameter (`proc f(a: int) = let a = a + 1`), ordinary Nim, reported as redeclaration because parameters share a scope with the body. Both directions of an enum conversion rejected as impossible. A `for` over an enum range mis-flagged as iterating a non-collection.

That last pair had been **hiding**: the probe programs also tripped a real error from the reference, so the verdicts "agreed" and the tool said nothing. It now prints *why* each side rejected, and every new check was confirmed to fire for the same reason rather than by coincidence. Re-running the day's probes through that lens found five more rejected for the wrong reason — three fixed, two written down as open.

Gates: corpus **618 modules**, accept/reject agreement **76 → 139**, error-message snapshots **64 → 97**, and every one of the **71** diagnostic codes has a long-form `--explain` article. A third case joined the set where aowlsem is right and the reference is not: `proc maxOf[T](a, b: T): T = if a > b: a else: b`, textbook Nim the reference cannot instantiate.

## 022 2026-07-28 - Tuesday, July 28th 2026

[aowli-release](https://github.com/aoughwl/aowli-release) is now private indefinitely.

**Debugging a *big* program under [aowli](https://aoughwl.github.io/aowli) stopped meaning "recompile it every time."** Pointing the debugger at [aowlsem](https://aoughwl.github.io/docs/aowlsem) took minutes per run, but the interpret is ~1 second — the minutes were [aowlcode](https://aoughwl.github.io/docs/aowlcode)'s `debug`/`trace` recompiling the whole ~20k-line compiler plus stdlib from scratch with `-f`, then deleting it. The obvious "persistent cache → incremental rebuild" fix was measured and **does not help**: a warm no-`-f` rebuild costs the same ~47s. The real fix is to skip the compiler when nothing changed — reuse the built `.s.nif`, recompile only on an actual source edit. First debug of a session ~47s; every one after **~1 second**. (Or hand the tools a prebuilt `.s.nif`.)

**Released [aowli v0.3.3](https://github.com/aoughwl/aowli-release/releases/tag/v0.3.3) — hybrid-native mode crosses ref/seq-bearing data.** Hybrid runs the modules you are *not* debugging as compiled code while interpreting the one you are; a shared-memory **arena** lays a live value graph out at native layout, so calls taking `ref` objects, nested ref graphs and `seq[T]` fields (including seq-of-object) cross too — the native side reads and mutates the same memory, synced back. Additive and dormant: without the flag, execution is byte-for-byte v0.3.2, and anything not safely marshalable falls back to interpretation.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) spent the day closing byte-level gaps against the reference's typed output.** Method: a small *valid* program per feature, both checkers, diff token-for-token; every difference is a bug or a recorded lowering choice. **~21.7k lines**, **700+ commits**, corpus **500/500**, accept/reject **10/10**, `std/system` clean.

* **Generic `ref object` types reached full byte-identity.** `Container[int](…)` constructs a real heap `ref` (`newobj`) instead of a value; a generic instance's synthesized lifetime hooks no longer bake in the defining module (the instance is content-addressed already); the object half numbers its type parameter `T.1` to the alias's `T.0`, matching how the reference counts a `ref object`'s two declarations.
* **Value objects that carry methods.** An inheritable object with managed fields that *also* declares `method`s emitted the full four-hook lifetime form; the reference emits **only** the user-method vtable, because a type with a real vtable routes its own destruction through it. The trigger is the presence of a user method, not inheritability.
* **Smaller parity fixes.** Generic variants resolve named-branch fields; `{.borrow.}` operators returning a distinct type convert the result back; `untyped`/`typed` template parameters are wildcards, so `template twice(x: untyped)` *inlines* at the call site; bool `case` labels emit literal `(true)`/`(false)` tags.
* **Reading a variable before it is set is now an error.** `var x: int; return x` is rejected, as by the reference (also `discard x`, `s.add …` on an untouched `var s: seq`). The definite-assignment analysis existed for a single-assignment check; today it started *reporting*. A branch initializes only when **every** path does, so a value set in one arm of an `if` with no `else` is flagged while an exhaustive `case` or `if`/`else` is accepted. This is what lifts accept/reject to **10/10**.
* **`var`-returning calls as assignment targets.** `first(c) = 99` writes *through* the location the call yields; a `var`-returning proc forwarding another such call emits the bare pointer-to-pointer copy instead of address-of-a-dereference. (Both emission sites were pinned by stepping aowlsem itself under aowli's interactive debugger.)

Earlier the same grind landed lambdas as expressions, cross-scope iterator resolution, custom `[]`/`[]=`/`{}`/`contains`, multi-index `x[i, j]` read and write (two assertion crashes fixed), cross-module import-resolution fixes, and a relative `include` resolving straight from its parsed artifact with no source file on disk.

## 021 2026-07-27 - Monday, July 27th 2026

**[aowli](https://aoughwl.github.io/aowli)'s debugger can now pause a running program and step through it interactively**, instead of only printing breakpoint snapshots after a run finishes. Three additions, all in [aowlcode](https://aoughwl.github.io/docs/aowlcode) **0.6.13** and documented under [Debugging](https://aoughwl.github.io/aowli/debugging):

* **Interactive stepping (`--session`).** Run a program once and keep it paused between commands: step into a call, step over it, run until the current routine returns, or continue to the next breakpoint. You can set breakpoints while it's paused and inspect the current frame — without re-running the program for each look. In the plugin this is the new **`debug_session`** tool.
* **Readable output for big values.** A large local — say a compiler's context object full of lookup tables — used to print as thousands of lines. Values are now rendered under a size budget and the rest is elided with a marker, so a frame dump stays readable regardless of how large the values are.
* **Drill into one field.** Rather than print a whole value, name the part you want — `expand c.currentModule.name`, `expand xs.3.field` — and only that piece is shown. Object fields resolve by name, seq/array elements by index.

Also fixed a build issue where a rebuilt debugger binary could be shadowed by an older copy earlier on the lookup path. The binary now reports its build version (`aowli-dbg --version`) and installs to one canonical location. Full command reference: [aowlcode → Execution](https://aoughwl.github.io/docs/aowlcode/execution).

**Released [aowli](https://aoughwl.github.io/aowli) [v0.3.2](https://github.com/aoughwl/aowli-release/releases/tag/v0.3.2)** — two shipped-runtime correctness fixes surfaced by running a real argument parser under the interpreter: `s[a..b]` / `s[a..<b]` slices returned only the first element instead of the substring, and a non-string value (a `nil`/default) could compare `==` equal to a string. Both fixed; byte-identical to a native compile on the repro, and the differential corpus stays at 77/77. Hardened binaries (obfuscated IR + licence gate + stripped) with SHA256 are on the [release page](https://github.com/aoughwl/aowli-release/releases/tag/v0.3.2).

**[aowlsem](https://aoughwl.github.io/docs/aowlsem), the from-scratch semantic checker, keeps closing on full parity with the reference compiler.** It is now **~18.6k lines** of self-hosted Nimony across **550+ commits**, and its byte-exact differential corpus stands at **498/498** modules matching nimony's own typed output, with the entire `std/system` checking clean (0 diagnostics). Today's work brought **generic type instantiation** in line with the compiler's own behavior:

* **Generic sum types construct by inference.** `let d = Some(99)` works out `Option[int]` from the argument, so `d.val` is an `int` and `d.val == 99` resolves to a single integer comparison instead of a 25-way overload set — the same inference drives annotated conversions (`Option[int](x)`) and two-parameter sums like `Either[int, string]`.
* **Plain generic value objects infer their instance too** — `Pair(first: 1, second: 2)` picks `Pair[int]` straight from its field values.
* **Generic `ref object` types instantiate in full.** A recursive `Tree[T] = ref object` variant now emits *both* halves the compiler expects — the reference alias and its underlying object type — each carrying its own per-instance lifetime hooks (destroy / move / copy), with matching typevar numbering, and its constructors (`Branch(…)`, `Leaf(…)`) build the concrete instance rather than the generic origin.

## 020 2026-07-26 - Sunday, July 26th 2026

**[aowlmcp](https://aoughwl.github.io/docs/aowlmcp) now speaks the [MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) spec — the biggest MCP revision since launch, and a clean break with its stateful past.** The library serves **both** protocol versions, negotiated per request, so upgrading a client is never a flag day:

* **Stateless core.** No `initialize` handshake and no `Mcp-Session-Id`: every request carries its own context in `_meta` (`protocolVersion` / `clientInfo` / `clientCapabilities`), and a new **`server/discover`** RPC advertises capabilities up front (it doubles as the stdio back-compat probe). Any instance can serve any request.
* **Multi-Round-Trip Requests (MRTR).** A tool can return an `InputRequiredResult` to elicit user input mid-call; the client re-issues with `inputResponses` and the echoed `requestState`. `registerToolMRTR` + `newInputRequired`.
* **Tasks extension.** `registerTaskTool` returns a task handle; `tasks/get` / `tasks/cancel` / `tasks/update` drive it — advertised in `server/discover` only when a task tool exists.
* **Caching + routing.** `tools/list` gains `ttlMs` / `cacheScope`; the Streamable-HTTP `Mcp-Method` / `Mcp-Name` routing headers are accepted. Roots / Sampling / Logging are deprecated (aowlmcp never shipped them).

Every new flow is proven **over all three transports** — stdio, HTTP, and HTTP/3 (QUIC) — because they share one transport-agnostic dispatch core: **stdio 27/27, HTTP 15/15 (routing headers + MRTR + Tasks over the wire), HTTP/3 4/4.** Docs updated alongside.

<br>

**Also released [aowli](https://aoughwl.github.io/aowli) [v0.3.1](https://github.com/aoughwl/aowli-release/releases/tag/v0.3.1) — the interpreter now runs the Nimony *semantic checker itself*, byte-identical to a native compile.** Pointing the interpreter at [aowlsem](https://aoughwl.github.io/docs/aowlsem) — a real, compiler-grade program — and diffing against native turned up three root-cause bugs; fixing them brought the run to **520/520 tokens identical**. This means [aowlcode](https://aoughwl.github.io/docs/aowlcode)'s `debug`/`trace` can now be aimed at the compiler's own passes.

* **Fully-initialised pointer values.** Constructing an interior `ptr` left its flat-memory view fields (`region`/`foff`/`elemBits`/`base`) uninitialised, so a later read saw garbage — a genuine memory-safety class, not a cosmetic gap. Caught with **valgrind running under mimalloc's Valgrind-tracking build** (mimalloc otherwise bypasses the sanitizer); every pointer construction now initialises all fields.
* **`seq` append value-copy.** `s.add x` now copies `x` on the way in — the same `=copy` envelope semantics v0.3.0 gave assignment — so mutating the appended element never aliases the source.
* **Content-addressed tag dedup.** `StringView.==` is gated so NIF tag interning deduplicates by identity, the way `TokenBuf`-style content-addressed programs expect.

**The debugger got sharper alongside it.** `--break-func:NAME` and file-scoped `--break:file.nim:LINE` resolve routines through the include chain (a bare line number is ambiguous once modules are merged), and `program_args` forward to the interpreted program's `commandLineParams()` — so a breakpoint can land inside `semCall` while the checker runs on a real input.

**A plugin-packaging note.** The [aowlcode](https://aoughwl.github.io/docs/aowlcode) MCP server a session runs isn't the marketplace checkout or the newest cached build — it's the exact version pinned in `installed_plugins.json`. Ours was stuck several versions back at 0.6.0, which silently dropped any newer argument (like `program_args`) before it reached the handler. The fix is a one-line pin bump (to **0.6.9**) plus a restart; the thing to watch for is a parameter that's present in the source but missing from the live tool's schema.

## 019 2026-07-25 - Saturday, July 25th 2026
Created [aoughwlup](https://aoughwl.github.io/docs/aoughwlup) and [aoughwl](https://aoughwl.github.io/docs/aoughwl)<br>
Created [aoughwl-code](https://aoughwl.github.io/docs/aoughwl-code) and [aoughwl-code-release](https://github.com/aoughwl/code-release)<br>

**Released [aowli](https://aoughwl.github.io/aowli) [v0.3.0](https://github.com/aoughwl/aowli-release/releases/tag/v0.3.0) — the correctness-complete build.** Both engines — the tree-walker behind the public `aowli-interp` / `aowli-dbg`, and the internal bytecode VM — now hit **zero in-scope divergence across a 423-program differential corpus** run against the nimony compiler. The engines agree with each other and with native, program for program.

**Value semantics landed.** Assigning or binding a value object / tuple / value-array now copies the envelope (refs stay shared) — `var x = a; x.a = 999` no longer reaches back and mutates `a`. This was the last big place aowli's aliasing quietly disagreed with the real `=copy`.

**The last OS-boundary gaps closed.** Real host `stat` / `lstat` (so `fileExists` / `dirExists` are correct), pointer identity in `==` / `!=`, `cast[int](ptr)` round-tripping through flat memory, and VM argv / stdin seeding. Plus a sweep of narrower fixes: float→int conversion, block-expression values, cyclic-import init order, a self-nested-iterator hang, and `Table` element write-back.

The one boundary the pure value interpreter can't cross by itself is literal-C: `{.emit.}` and C FFI have no C to run inside the value model. **That's exactly what hybrid-native mode absorbs — and today it ran real foreign C for the first time.**

**Hybrid-native executed real C-FFI.** aowli's hybrid mode — interpret most modules, run selected ones as native code — now offloads a header-backed `{.importc.}` proc to a compiled shim and calls into *genuine* C: a `static inline` `cadd` crossed the boundary, ran natively, and marshaled its result back into the interpreter byte-identical to native. The proc-offload path (pure-nimony procs run native) also picked up a permanent regression lane. This is interpreter-development progress, not yet in the public v0.3.0 binary; the remaining piece is top-level `{.emit.}` / importc-var in the *main* module.

**Playground refresh.** The in-browser [playground](https://aoughwl.github.io/playground/) got a round of work: rebuilt engine bundles (fixing a stale-bundle bug where Bytecode-VM and Native-JS runs showed no output), a unified **Pipeline** config panel (parser · checker · lowering · engine), aowlsem rebuilt from latest, the two source-pane toolbars merged into one, a clearer footer with an inline engine picker, and curly-brace block mode no longer false-flags a `{ … }` body as "not a Nim block."

## 018 2026-07-24 - Friday, July 24th 2026

**Gave the whole stack one source of truth for how values are laid out: [aowlabi](https://github.com/aoughwl/aowlabi).** Three places each kept their own copy of *how is a `string` / `seq` / `object` / `ref` actually represented* — the interpreter, the C backend, the JS backend — and they had quietly drifted. aowlabi is now the single canonical answer:

* the size / alignment / field-offset engine — one implementation of the C-struct layout rules, parameterized by pointer size
* the canonical heap-block spec — string SSO + `LongString{fullLen,rc,cap,data}`, seq `{len,data}`, the ARC ref box `{rc,data}` — as named offset constants, one truth
* the marshal matrix — which types cross a native boundary by value / by buffer / by fallback, plus the JS representation mapping (fast `number` vs faithful `bigint`, char, tuple, and so on)

[aowlc](https://aoughwl.github.io/docs/aowlc), [aowljs](https://aoughwl.github.io/docs/aowljs) and [aowli](https://aoughwl.github.io/aowli) all read the same spec now instead of re-deriving it.

**[aowli](https://aoughwl.github.io/aowli) grew a real runtime layer.** The scattered places where the interpreter crossed from its value world into a faster / foreign executor — host natives, flat memory, syscalls, the miss policy — are one spine now: a **provider registry** (interpret · host-native · syscall · hybrid-native), a **codec** (identity · flat C-ABI · JS value), and a **policy** that is *never silently wrong* — an unsupported crossing fails loud or falls back to interpret, never a wrong answer.

**And the payoff — hybrid execution.** aowli can now interpret only the file you care about and run *every other module as natively-compiled code at full speed*. Debug one file slowly, with full observability, while its libraries run native. aowli auto-generates C-callable shims for the cross-boundary calls, marshals scalars, POD objects / tuples, strings and seqs across using aowlabi's layout, and dispatches at the call site. Every result is **byte-identical to the fully-native build**; anything that can't be safely marshaled (refs, closures) transparently falls back to the interpreter — so it is faster where it can be and correct everywhere.

```
aowli --hybrid --interpret:mymod prog     # mymod stays observable, everything else runs native
```

## 017 2026-07-23 - Thursday, July 23th 2026

**Rebuilt the [net stack](https://aoughwl.github.io/docs/net-stack) around a single-threaded async reactor:** one OS thread, `epoll`, passive-proc coroutines, no `std` async or thread pool.

* HTTP/1.1: keep-alive, chunked, 300/300 concurrent
* WebSocket: masking, frame/control validation, fragmentation, incremental UTF-8, close validation, `permessage-deflate`; 19/19 conformance, 160/160 echo
* HTTP/3: ngtcp2 + nghttp3 + GnuTLS behind a small pull API; 20 QUIC clients, one thread, ASan/LSan clean
* RFC 9221 datagrams + [WebTransport](https://aoughwl.github.io/docs/net-stack/reactor) datagrams over H3; streams remain

Created **[aowljson](https://aoughwl.github.io/docs/aowljson)**: reusable JSON values, error-as-value parsing, serializer, builders, `v{"key"}`, `v.at(i)`.

Created **[aowlmcp](https://aoughwl.github.io/docs/aowlmcp)**: transport-independent MCP dispatch over stdio, HTTP, and HTTP/3. Tests: 13/13, 6/6, 4/4. Includes compile diagnostics and NIF outlines through [aowlcode](https://aoughwl.github.io/docs/aowlcode).

**aowli became an actual runtime:** flat memory, casts, `copyMem`, allocation, unchecked arrays, fd-backed file I/O, env access, ownership hooks, refcounted `ref` objects, and fail-fast unsupported stdlib calls. It now runs about **92% of compiler-buildable programs**, with no known silent wrong-result cases. Remaining: some OS/VM gaps, threads, async.

## 016 2026-07-22 - Wednesday, July 22th 2026

Released **[aowli-release](https://github.com/aoughwl/aowli-release) [v0.1.0](https://github.com/aoughwl/aowli-release/releases/tag/v0.1.0)** with:

* `aowli-interp`: run typed NIF, optional call-tree trace
* `aowli-dbg`: batch breakpoints and structured frame dumps
* stripped binaries, fail-closed licence gate, SHA256, VirusTotal links
* no source paths or internal proc/type names

Updated **[aowlcode](https://aoughwl.github.io/docs/aowlcode)** with trace/debug tools, `/land`, Haiku appliers, and parallel edit application.

## 015 2026-07-21 - Tuesday, July 21th 2026
Back to work after a couple of quiet days.

## 014 2026-07-20 - Monday, July 20th 2026
A quiet day.<br><br>

Shout-out to a fellow Nim'er's project — [3code](https://3code.capocasa.dev/), worth a look.

## 013 2026-07-19 - Sunday, July 19th 2026

More **aowlsem** — the whole day is a generics push. The semchecker now instantiates and preserves generic constructs end to end: typevar calls and signatures, generic object applications with substituted field types and attached hooks, generic array bounds and range iterators, generic seq index reads, `var` forwarding through generic params, late-bound generic hook calls, and quoted generic operators. Around it: `out` parameter type resolution, `sink`/`source` normalization, typed pointer comparisons lowered to magics, unchecked-pointer index assignments wrapped, `requires` pragma expression checking, and `threadvar` globals emitted. Steady, surgical commits — aowlsem is now **past 340 total commits** since Tuesday.

## 012 2026-07-18 - Saturday, July 18th 2026

**A major day for [aowlsem](https://aoughwl.github.io/docs/aowlsem)** — 126 commits landing the clean-room semchecker's core. It now passes **397/397 corpus fixtures byte-exact** against the nimony oracle, and — the milestone — it does a **complete zero-diagnostic traversal of the full `std/system`**: the whole `system.nim` plus its included `std/system/*.nim` set, ~6,383 lines, semcheck with **0 errors and 0 log lines**. Full-system parity against nimony's own output is down to ~33k canonical diff lines from an earliest baseline of ~62k — a **46.5% reduction**, with the first mismatch now a third of the way into the semantic output.

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
Took [nifi](https://github.com/aoughwl/nifi) private.<br>
Updated [nifi](https://github.com/aoughwl/nifi) — 6–10× performance gain.

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
