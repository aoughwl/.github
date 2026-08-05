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

## 030 2026-08-05 - Wednesday, August 5th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 23 commits.** One class dominated the night: a component of a type's identity dropped, so two distinct types shared a generic instance.

- **Eight identity components were missing from `typeKey`/`sameType`** — float WIDTH, tuple FIELD NAMES, importc C-spelling, array `lo`, array INDEX BASE, proc SHAPE. `readFloat64` read 4 bytes, `array[Color,int]`/`array[Shade,int]` shared a body, and the dropped `lo` produced a **false E0203 on valid code**. `FIXQUEUE.md` Q28, eight landed of nine.
- **Two segfaults, both masked until moddiff stopped retrying wide.** sequtils' `foldl`/`allIt` runnableExamples call the template itself — a 3239-frame overflow, bounded at `c.inImportedTmpl <= 8`; and a bound callee symbol re-routed through the by-NAME imported-template table re-expanded system's `[]`. sig11 → DIFF for both.
- **`S = ref SObj` declared before `SObj` emitted an `=destroy_Aref` holding only `deallocFixed`** — a leaked destructor, hit for real by `StringStream`. `queueRefAliasHooks` reads `instDestroyHook` eagerly; the alias now reserves its slots and rebuilds at module flush.
- **`args: openArray[string] = []` never inferred T, and an opaque `{.importc.}` object zeroed as `(suf 0 "")`.** The `[]` gap fill exists at three sites, and fixing one regressed osproc 119 → 330 by emitting a third `toOpenArray` converter; all three now share a helper. 119 → 39.

**Standing.** Corpus 745/745 → **761/761**, `noabort.sh` 46/46 with 0 crashed, reference modules flat. Open: `sizeof(CB)` on a typedesc still emits a bare `.` — two guards tried and measured inert, written up in `tests/pending/sizeof_proctype_typedesc.diagnosis.md`.

<br>

## 029 2026-08-04 - Tuesday, August 4th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 121 commits.** Module-scale parity **73809 → 48579 tokens (−34%)** across the 46 stdlib modules; **30 are now byte-exact**, up from 20.

- **A resolved dot re-entering `semDot` came back out degraded**, and a `var` template param arrived as the value context's `(hderef …)` instead of a location. An untyped imported template's expansion is semchecked twice, and the second pass replaced each mangle with `sourceNameOf` of itself. `semcore.nim` **32104 → 19737**.
- **Merging a parallel 33-commit branch silently dropped fixes while importing their tests.** Git auto-merged in `HEAD`'s favour with no conflict markers: it kept `semcore.nim`'s `constMagic` table and dropped every site that populated it, and kept a comment describing a guard it had deleted. 14 corpus failures and a `memlzdyby` abort; ported back against the failing tests, which are the only reliable oracle for what survived.
- **`semExpr` is called on statement nodes 11500+ times and does not recognise its own output 8300+ times.** Found by instrumenting every verbatim-copy fallback — 24349 firings over 46 modules. `(stmts)(asgn)(ret)` reaching an expression checker is a dispatch bug, which is why adding expression rules kept not fixing it.
- **`moddiff.sh` computed per-module token counts and compared them to nothing.** `tests/moddiff.baseline` now judges each of 46 modules; it caught four changes that were green on the 741-case corpus and on noabort while regressing whole modules, each reverted with its numbers written down.

**Standing — how done is it.** **1312 commits**, 121 today; **40147 lines** of Nim across 19 `src/` files, 12376 lines of test cases, 5351 of harness. Against nimsem on the 46 stdlib modules aowlsem now emits **1146554 of 1195133 canonical tokens byte-identically — 95.94%**, with **30 of 46 modules (65%) byte-exact end to end**. That figure is agreement with ONE FROZEN oracle (the Jul 17 nimony binary) and presumes it correct in all 48579 differing tokens — `check.oraclebroken` exists because that presumption is false, holds 2 entries, and both are verdict-side; there is no emission-side equivalent yet. Verdict agreement `check.sh` 407/409 (99.5%, both remainders nimony-side C-backend bugs); corpus `diff.sh` 737/741 (99.5%); `noabort.sh` 46/46, 0 crashed.

**Not done.** The last 4.06% is 48579 tokens and it is not evenly spread: `semcore.nim` alone holds 19737 of them (40.6%), and it is aowlsem's own source, so it moves whenever the compiler grows. The four open corpus cases are one shape — a missing `hderef` on the `pairs` tuple yield. `SHAPES.md` ranks the remainder by expected value and names the two structural causes (`semExpr` dispatched on statement nodes; `semExpr` not recognising its own resolved output); `FIXQUEUE.md` holds 26 items that each carry a verified repro and a named fix site.

**[aowli](https://aoughwl.github.io/aowli) — 47 commits.** The hybrid attest was per module while its grants are per crossing; a destructor on the raise path never fired; the JIT's in-process route was three errors deep behind a silent fallback.

- **One hook-bearing shim revoked every no-deref grant in the build.** `mayEmitArcHooks`/`buildShimGroups` give those candidates their own module and attest: whole-program aowlsem `honoured=0 revoked=334,381` → `270,800/0`, native calls 100,528 → 371,328, byte-identical.
- **A local left through a raising call was never destroyed.** eraiser lowers every `.raises` call to `if failed(tmp): <destroys>; raise tmp`, and both engines unwound through their own channel, so the destroyer's scope-exit `=destroy` was dead code — `OPEN.md` #2, closed with the finally/destroy ordering.
- **The JIT's in-process route had three errors, each hidden by the previous.** aowlc's emitter caches outlived their reset, its globals were emitted after the cross-module inline bodies that reference them, and the string shim declared no `borrowCStringUnsafe`. Every gate assertion passed on either route; the gate now names the route.
- **All four committed browser bundles were dead, and the glue was half a contract.** They predated `jsenv.js`; `run.js` never set `__aowli_mods`, so the VM bundle died on `expected 'index' tag`. `web.sh` now gates each bundle's behaviour.

**Standing.** `OPEN.md` items 1–8 all closed. hybrid 20/20, web 8/8, fin 15/15 both engines, crosscheck 78/78 DIVERGE 0, corpus 202/202 over 15 categories, hotjit 34/34.

**[aowlc](https://aoughwl.github.io/docs/aowlc) — 2 commits, plus `session/jit` fast-forwarded into `main`.** A translation unit referenced a global before defining it.

- **A `static inline` proc copied in from another module names THIS module's string literals**, and the globals section was emitted after those bodies: `error: 'strlit_0_I…' undeclared`. The reverse dependency cannot occur — a global's initializer is a constant expression.
- **A module-level const was `static`, and nimony references each strlit cross-module by `extern`.** Same four JIT units either way: `const` → dlopen ok, `static const` → `undefined symbol: strlit_0_I…`. `gcc -shared` links both silently, so only the consumer's dlopen fails.

<br>

## 028 2026-08-03 - Monday, August 3rd 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 36 commits.** Imported templates were invisible to overload resolution, and two compile-time magics answered in only one of the two positions they occur in. Then three type-classification defects, two of them the same `nil` guard in a classifier that is not `semType`. Then an audit of what the gates actually assert.

- **An imported template carries no scope overload entry**, so no call could select one. Merged into `cands` *after* the arity filter — imported templates have empty `paramTypes`, so an arity test drops them all — plus `semPrefix` expansion and `semIndex` selecting the `[]` overload by index type **and** receiver (system declares it three times).
- **`declared()` and `compiles()` folded only as `when` conditions.** A const initialiser reaches neither `evalCond` nor `emitWhenCond`, so `const a = compiles(known(1))` folded to false — correct for every negative case, which is why it went unseen. `foldCompiles` in `calls.nim` now serves both positions; `isCompilesCall`/`cursorHasOchoice` moved there from `stmts.nim`.
- **An imported generic's field type was unrecoverable at use.** `fieldsOf` drops an imported type's private fields, and `Field.typ` is resolved at LOAD time with typevars unbound, so `seq[(K, V)]` was recorded `tyUnknown`. `copyArgType` falls back to `allFieldsOf`, and `genericFieldType` re-reads the type from the decl and substitutes there.
- **A const element of a set literal inlines to its value** inside another const's initialiser: `(setconstr (set (c 8)) '/' '\5C')`. Folding before the E0223 duplicate check made `DirSep`/`AltSep` — both `'/'` on POSIX — a false duplicate and stopped `std/private/ospaths2`.
- **`nil ptr T` classified as unknown in both classifiers that are not `semType`.** `typeOfExpr` had no `infix` arm, so an `UncheckedArray` element emitted `.`; `registerTypeName`'s alias tag list omitted `infix`, so every use emitted the alias symbol. The plain `ptr T` spelling was right in both.
- **`bitand`/`bitor`/`bitxor` took the wider operand, and an untyped literal's type is the default i64.** `s and 0xFF00` with `s: cint` widened `s` up instead of narrowing the literal; `shr` follows its shifted value, so `ashr` corrected with it. Operator slots also needed `withoutImportc`.
- **An identical proc TYPE re-emitted its own param symdefs.** nimsem memoises the rendered `(proctype …)` under `typeToCanon`, which erases every SymbolDef, and consults it only for a param carrying a default. `procTypeStructKey`/`procTypeStructMem`; `std/lib/vfs`'s whole 2-token diff.

- **`bin/aowlsem` was 14 hours stale and every gate defaulted to it.** Dated Aug 2 15:47 against newer `src/`, including three of that day's own sem commits. Every other mis-scoring defect mis-scores a component; this one mis-scores the subject and fails both ways — a fix absent from the binary reads as "still broken", a regression absent from it ships. `tests/binfresh.sh` refuses, and prints binary path+mtime every run.
- **Both plugin gates claimed to check a "recorded token count" and compared nothing** — the numbers were in a header comment, and `consteval.sh` incremented `$pass` for any nonzero diff, so two executors folding the same wrong constant read as agreement. `tests/baseline.sh` + `macros.baseline` (`tcollect 4`, `tbindsym_choice 4`); `consteval.baseline` is empty, meaning nothing may differ.
- **`$n/$n` is true at zero.** `explain_gate.sh` printed `1/1 codes documented` with the whole `addError` family unchecked once those sites moved behind a helper; its denominator is scraped by `grep`. Floored per-scrape there and in `macros`/`e2e`/`lens`/`unit`/`equivbig`.
- **A plugin build losing the `static.o` race surfaces as a semantic diff, not a build error.** The evaluator never links, the const stays unfolded: `DIVERGE ctfe_const_object_call interp=0 compiled=21`, byte-exact alone. `tests/infra.sh` classifies it, diagnostic-first; its predicate named `collect2: error:` in prose while matching it in no pattern — a bare link failure scored ACCEPT.

**Gates.** diff **718/718**, check 403/403, noabort 45/45, nofp 35/35, diag 175/175, explain 94/94, macros **6/6**, consteval 18/18, ctfe 7/7, lens 16/16, e2e 6/6, `tests/imports.sh` 5/5 → **10/10** — `{.cyclic.}` cycles byte-exact both directions, negative half asserted from artifacts since `{.cyclic.}` *also* prints `cycle detected:` and nimony exits 1, not 0. All re-run on a non-stale binary.

**Standing.** `imported_tmpl_block_arg`'s header was stale from the day after it was written: the `strVal on SymbolDef` assertion it told readers to expect no longer occurs anywhere. Dropping `and not blockArg` (`exprs.nim:4992`) takes the probe 9 → 4 tokens with the corpus green, but aborts `optcore` and `aowlsem` — the scope keys on the source base name (`calls.nim:6290/6777/6789`), undoing `substCopySym`'s re-mangling, and the block is semchecked twice with diagnostics rolled back and `define()` side effects kept. Dropping `or bodyHasDef` buys nothing and breaks `memfiles`. `COVERAGE.md`'s cyclic-module row was ⬜ on an aspiration nobody ran: unannotated cycles never reach nimsem, `{.cyclic.}` is byte-exact. `--macros:compiled` bypasses `ctfePolicyArgs`/`ctfeRecordAudit`, so `<out>.ctfe-reads` is empty and `ctfe-check` answers CURRENT for a changed compile — `tests/ctfe.sh` drives all 7 properties under `interp` only. `consteval.sh` is 462s CPU, 69% of it `mpSeedHostStdlib` running 36 times in an 18-case run, 21% the per-const `nimony s` builds.

`imported_generic_tuple_elem` closed at 4 tokens, not fixed: the module segment of an instance symbol is what `typeToCanon` strips and DCE merges, and `newInstSymId` always stamps `thisModuleSuffix`. All 10 remote branches were already merged; deleted, repo is `main` only. On `tests/moddiff.sh` (23 byte-exact / 22 differing of 45) posix went 245 → 10 tokens and osproc 3552 → 1375; a `seq` alias still resolves to `(at seq (i 64))` where nimsem emits the instance symbol `seq.0.I·.`.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 3 commits, 3 on the docs site. The thrift claim measured for the first time, then the defects that measuring exposed fixed.**

- **`aowl-ledger` over-counted `Edit` 515×.** It sized the PostToolUse payload, which carries `originalFile`: 79.3KB/call recorded against 154B in context, hiding `Read` behind a cost that does not exist.
- **`Read` is 52.9% of context drain, `Bash` 27.4%, all 26 `nimlang` tools 15.1%; amplification 355×.** Neither is abused — 75.3% of read bytes were already windowed — so the lever is `decl_of` substitution on the 857 one-declaration reads.
- **`terse` was inert or absent on the tools that cost most.** Now the default rather than an `NIMLANG_AGGRESSIVE` opt-in: `nif_outline` −43.8% (it had been saving 10 bytes of 3,239), `build` −68.9%, `search` gained it at −19.5%.
- **The `Read` guard failed open on any file with >80 declarations.** `SYMBOL_CAP` truncation ran the last symbol's end to EOF, which reads as a 91% span and trips the "this map narrows nothing" test — disabling the guard on exactly the files it exists for.

**Standing.** 17 never-invoked commands hidden from the per-request listing (~435 tok/req); `trim-build-output` replaces its result instead of appending to it. Tool-surface consolidation (~1,898 tok/req for 10 tools never called) is planned, not shipped — `FIX-PLAN.md`.

**[aowltest](https://aoughwl.github.io/docs/aowltest) — 1 commit. The gate was 35 assertions welded to one binary; it is now a corpus any implementation can be run against.**

- **`tests/run.sh` shelled out to `$AOWLTEST` and parsed its human output inline.** Extracted to `conformance/`: nine `cases/*.case` in a step language (`use`/`append`/`save`/`restore`/`run`/`expect`), executed by a `run.sh` that knows no implementation.
- **Everything implementation-specific sits behind a three-verb adapter** — `capabilities`, `run <root> <cache> <cmd> [neutral-opt…]`, `ctfe-sidecar` — over a neutral option vocabulary and a line-oriented observation record (`ran`/`cached`/`hitrate`, `test <path> <status>`, `explain <kind> <subject>`).
- **35 → 72 assertions from the extraction alone.** Per-test status, `inputs=`/`external=` and key stability are record fields; grepping formatted output could not reach them. `requires` skips a case whose token the adapter does not declare.
- **Negative control fixed in the README.** An adapter that silently drops `salt=`/`ctfe-dir=` must fail exactly `050-key-material` and `090-compile-time-reads`, nothing else.

**[aowlmony](https://aoughwl.github.io/docs/aowlmony) — 3 commits.** `verify --memory` traps dangling pointers under `--fin`. The driver's own gate had been flickering because it compiled without the machine-wide lock.

- **`--fin --trace` renders every object argument as `(object)`** — no identity, so it cannot say which storage died or who still points at it. The defect is found structurally in the `.s.nif`; the `--fin` run only *witnesses* it (a `=destroy` at the blamed scope, the use site reached), and each finding is labelled confirmed or structural.
- **Needed a real NIF reader — the driver had only ever regexed `.nif`.** Line-info deltas are base62 and relative to the *enclosing parent node*, not the previous sibling; a filename makes the position absolute. A lowered `ret` carries none and inherits the routine's, so an escaping address anchors on the `addr`, not the `proc` header.
- **`parseTrace` had silently stopped understanding aowli's traces.** aowli now emits `  <file>:<line>`, the regex matched only `  :<line>`, so every op parsed at line 0 and attribution degraded to "no source location" while claiming nothing was wrong. `locateOp` now decides user-code by file, not by line range.
- **The driver shelled `nimony c` without `~/.aowl/bin/nimlock`.** `nimony c` regenerates `~/nimony/nimcache_static/static.o` whatever `--nimcache:` says, so it both suffered and caused the race — three consecutive gate runs gave 64/64, 62/64, 59/64, every failure `ld: cannot find .../static.o`.

**Gates.** `npm test` 41/41 → **64/64**, clean on the first full run after the lock, against 59–64 of 64 before it. Six `addr`-using `nimony/tests` modules report no finding; the two negative cases in the suite — same-scope borrow, pointer rebound after the scope — are what keep the check from being a noise generator.

**Standing.** A clean verdict prints its coverage — `N address-taking sites · M bound to a named pointer` — because a sound program and a walk that never reached the module otherwise print the same tick. Those counters expose the limit: intraprocedural, so `tests/nimony/arc/tdup.nim` is 9 sites / 0 tracked. Filed to `aowli`: an address in trace args would make the check fully dynamic.

**[aowli](https://aoughwl.github.io/docs/aowli) — 37 commits. An object could not live in `alloc`'d flat memory, which is the storage aowlsem's TokenBuf actually has. Now it can, and the interpreter grew record/replay, coverage and a sampling profiler.**

- **An object stored into an `rkBytes` region read back as 0, both engines, exit 0.** `parsePtrElem` sizes an object pointee `sizeOfSym(T)*8`; `flScatterObj`/`flLoadObj` place fields at C-ABI offsets and `flFieldSlot` resolves `data[i].f` to its own bytes, retiring the one-ObjBox-per-region overlay that aliased every element. `isFlatPodType` keeps a `ref`/seq/string leaf on it.
- **`sizeof` answered 4 for every variant object against native's 12.** `sizeAlignOfType` skipped `(case …)` whole, counting neither discriminator nor branch; it now emits the discriminator as an ordinary member and the branches as a union, `collectOwnFields` placing branch fields at their overlaid offsets by work list.
- **A `distinct`-typed return came back as 0** — `scalarFromBits` had no `akDistinct` arm and fell to `vNil()`, while the same type crossed as a *parameter* correctly. `examples/hybrid_arenapeek` pins it: in one returned POD the plain field survives and the distinct field does not.
- **`--record:FILE`/`--replay:FILE`, `--coverage`, `--profile-sample`, no instrumentation pass.** The journal serves fs/env/clock/argv/stdin from a portable text log (`<cwd>`/`<home>` folded, bytes `\xHH`-escaped); coverage and the sampler ride the existing per-statement site and `routineStack`.

**Gates.** `tests/replay.sh` **19/19**, `tests/coverage.sh` **41/41**, `tests/dbg.sh` 21 → **40/40**, `tests/crosscheck.sh` over 16 categories **DIVERGE 0 / AGREE-PASS 189**, `tests/run.sh` 11 categories 146/146 (tree-walker only — the VM is `crosscheck.sh` alone).

**Standing.** `tools/aowlsem-under-aowli.sh` runs the real compiler under the interpreter — `aowlsem/bin` is stripped of the `.s.idx.nif` sidecars, its build nimcache is not. First baseline: 20.9s interpreted against 0.013s native on a 3-line input, byte-identical, and 23.4s on a 57-line one — a startup floor, not a slope. `--trace-profile`: 5,726,833 calls over 319 routines, headed by `nifcore`'s `inc`/`[]`/`load`/`kind`/`cursorAt`.

**[aowlabi](https://aoughwl.github.io/docs/aowlabi) — 16 commits. The canonical-layout claim was never checked against the compiler it speaks for; checking it found the engine placing every inherited field at the wrong offset.**

- **`object of RootObj` started its own fields at 0, not `ptrSize`.** An `{.inheritable.}` root carries a hidden `ptr Rtti` word (hexer `lengcgen.addRttiField`), so every offset and size of every inheriting object was wrong. `TypeDesc.rtti` + `objectPrefix`.
- **`tests/run.sh` is a differential**: `oracle.nim` prints what nimony lays out, `model.nim` what `layout` computes from `TypeDesc`s with no `sizeof` anywhere. nimony implements neither `alignof` nor `offsetof` (`sem.nim:5325`), so alignment comes from an `object (c: char, t: T)` probe — the offset of `t` *is* `alignof(T)`. `objectDesc`'s `base: TypeDesc = nil` did not compile under nimony at all — nobody had ever called it.
- **`set[T]`, `{.packed.}`, `{.union.}`, range types and `UncheckedArray[T]` had no `AbiKind`.** A set is sized by the base's *range*, align 1 (`expreval.bitsetSizeInBytes`); `{.packed.}` is nimony's `maxAlign == 0` sentinel; `UncheckedArray` adds zero size but imposes its element's alignment, making `LongString`'s four offsets computable from `heapspec.longStringDesc()` rather than restated.
- **String literals do not walk the runtime SSO tiers.** A runtime string flips to `StrHeapSlen` at 15; a literal inlines only to `StrAlwaysAvail`(7) then becomes a static `LongString`, so a 10-char value is medium if built and static if written.

**Gates.** `tests/run.sh` **96/96** layout (diffed against the compiler), **153/153** heapspec byte offsets, **857/857** marshal invariants, ~25s — the corpus reaches `enumSizeAlign`'s `enumLo < 0` arm for the first time, every enum before it starting at 0. Every rule was falsified before being trusted: removing `rtti` reddens `Base`/`Derived`, shifting `LongStringDataOffset` one word reddens the string checks, sizing a set by width instead of range reddens nine rows, relaxing `isArenaAggregate`'s seq-element restriction reddens exactly `seq-of-string` and `seq-of-ref`.

**Standing.** No 32-bit oracle — `--passc:-m32` dies on missing multilib — so the width checks are invariance-only across 4/8/16, not verification against a 32-bit target. `isArenaAggregate` (ARENA-PLAN slice 5d, the TokenBuf shape) landed without coverage and is now gated. Filed to `aowli`: it computes layout twice, `sizeofcalc.sizeAlignOfType` over cursors and `aowlabi.sizeAlign` via `typeDescOf`, with nothing checking they agree; the range-less-enum descriptor `layout.validate` named was one instance and is already fixed there.

<br>

## 027 2026-08-02 - Sunday, August 2nd 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 29 commits.** Compile-time evaluation beyond const initialisers, then bounded by a capability policy. Four sites treated "cannot compute" as a definite answer; three miscompiled silently.

- `when big():` took the wrong branch, no diagnostic — `evalCond` returns unknown, an unknown `elif` is not taken, `else` is unconditional. Three sites: `semWhen` module-level, `semWhen` in-proc, `whenTakenBody` (type bodies — wrong field, so a wrong type). All now run the condition.
- Enum explicit value kept the auto-increment ordinal unless a bare `IntLit`: `b = v()` → 2, nimony 7. `foldRawArrayDim` handles `1 + 4`; `c = K * 10` needs `ceEvalInt(force = true)` — the contains-a-call guard assumes cheaper folding, false here because the prescan precedes `constVals`.
- A `const` inside a proc forked aowlsem until killed. `ceDeclaresName` matched only top-level `(const …)`, so the copy never stopped, the enclosing proc came in whole still holding it, each child regenerated the evaluator; `ceBudget` is per-process. Recursive `ceDeclaresName` restored the stop, `--ceDepth:` (max 4) backstops.
- `array[sz(), int]` emitted `(array (i 64) (call sz))`. `ceTypeNeedsEval` keeps a `var`/`let` whose own type awaits evaluation out of its evaluator — `varT` is in `ceIsDecl`, so it re-entered.
- Const evaluator had one executor, macro plugins two; `--macros:interp|compiled` now drives both. Compiled path exposed: `std/writenif` import only in `.p.deps.nif` (`aowlsem m` reads deps, `nimony s` the body) → `undeclared identifier: 'setup'`; `-o:<nimcache>/<base>` collided with nimony's per-module directory.
- Aggregate consts fold: `array[N,int]`/`array[N,float]` unrolled, `seq[int]` looped to `len`, all-`int` objects by field name. Value bound to a `let` so the initialiser runs once; caller rebuilds `(aconstr …)`/`(oconstr …)`. Wrong count fails rather than folding a partial.
- Inferred `const` type named the bare generic: `const S = firstN(3)` → `(at seq (i 64))`, the same call under `let` → `seq.0.I·.`. `semConst` lacked `semLetVar`'s resolution; the seq materialisation keys off it, so folding was off too.
- `writeNifInt(<a seq>)` semchecked clean — nimony: `expected: int64 but got: seq`. `reliable` declines any pair with a collection either side; mirror of `containerParam` added.
- Earlier: a copied instance resolves an `ochoice` callee; an assignment spells its ref upcast; a range is iterable whatever its bounds resolved to.
- **Compile-time code runs under aowli's policy.** `mpRun` and `ceRunInterp` pass `--allow: --allow-path:<nifcache>=fs.read,fs.write,fs.meta` — a plugin must read its input NIF and write its answer, and gets nothing else. `--ctfe-allow:PATH` grants one file; exit 77 becomes `STOPPED by the compile-time policy`; `--ctfe-policy:off` is the escape hatch.
- **A granted read is recorded, not just permitted**: `<out>.s.nif.ctfe-reads` carries `read<TAB>path<TAB>hash<TAB>size`, and `aowlsem ctfe-check <out.s.nif>` exits 0 current / 1 stale (naming the changed file) / 2 no record — an exit code, so nifmake, aowltest and aowlmony need not parse the format.
- **`--lens:<out.lens.nif>` publishes what the checker resolved.** `(d …)` declarations with position, type and signature; `(u …)` occurrences naming the symbol they bound; `(t …)` object/enum member tables with inheritance depth and visibility. Plain NIF.
- **Positions are recorded during checking, not read back.** The `.s.nif` carries one only where a subtree was copied verbatim, so every minted symbol has none; `tests/diff.sh` canonicalises line info away, so nothing measured that gap. Seams: `define`, `lensAt`, `lensUse`.
- **`(u …)` carries `owner` and `role`, `(d …)` carries `recv`**, so call edges and UFCS candidates are index filters, not tree walks. `owner` needed a routine stack `semProc` now pushes; `recv` came from `Sym.paramTypes`.

**Gates.** diff 685/685 → **701/701**, check 400/400 → **401/401**. New `tests/consteval.sh` **18/18** in `all.sh`: both executors match the oracle and each other, and each actually evaluated — proved by the serialized value file, since the shape folds otherwise make a no-eval run look green. nofp 35/35, diag 175/175, explain 93/93, e2e 6/6. New `tests/ctfe.sh` **7/7**: an ungranted read traps and folds nothing, the same read granted folds, the hash moves when the file does, `ctfe-check` reads stale on the outdated compile and current on the fresh one, and the digest aowli recorded equals what `aowltest --ctfe-hash` computes — three copies of FNV-1a/64 with nothing else asserting they agree.

**Cost.** In-proc `when` nests to `--ceDepth`: 1 condition 20s, 4 → 32s, no per-condition branching (`ctfe_when_call_multi.nim`). `whenTakenBody` is in the prescan over every module; plain corpus file 1.78s → 1.82s — `when defined(…)`/`x is T` fold in `evalCond`.

**Standing.** `scanFeatures` has the same shape but only gates feature scanning. Upstream rejects `static:`, `of v():`, generic-routine const calls. `selectedWhenBody` can't call the evaluator (non-`var` context) but no longer disagrees with `semWhen`. New `tests/lens.sh` **16/16**; corpus **705/705** on the `uncolored-async` branch with the index build.

**[aowllens](https://aoughwl.github.io/docs/aowllens) — 2 commits.** Reads aowlsem's index instead of reconstructing it from the tree.

- **`typeat` could not answer on an aowlsem artifact** — it reads positions off emitted tokens, which aowlsem mints without them. `lens.nim` parses the sidecar; the occurrence at a position already names its symbol, so shadowing is the checker's answer, not a guess.
- **`members` takes fields from the index** (inheritance already flattened, per-member visibility) and UFCS candidates by `recv`; **`calls` reads edges** from `call`-role records paired with `owner`, carrying the call site.
- Fallback is per-answer, not per-run: no sidecar, or nothing in it for this question, and the existing walk answers exactly as before.

**Gates.** New `tests/lens.sh` **5/5**, including the negative control — hide the sidecar and 7:29 goes back to `{}`. `difftest.sh` 5/5 and `newcmds.sh` 15/15 unchanged.

**Standing.** Nothing writes the sidecar in a normal build: nimony's driver invokes `nimsem`, aowllsp drives `nimony check`. Two implementations now answer the same questions with no differential between them.

**[aowlmony](https://aoughwl.github.io/docs/aowlmony) — 3 commits.** `verify` diffs native against interpreted off one front end. Its first two findings were both artefacts of *which binary ran*, not backend defects.

- **`aowlmony verify` added.** On a mismatch it re-runs the interpreted leg under `aowli --trace`, rebuilds stdout from the `write(stdout, …)` args, and names the op owning the first divergent byte. Default `--native:nimony` reuses the binary `nimony c` already linked at `<nimcache>/<mainHash>/<srcStem>`.
- **Reported `s[2..5]` → `"a"` as an aowli defect. It was a stale install.** The registry resolves interp to `~/.aowl/bin/aowli-interp` (07-26), shadowing a fixed `~/aowli/bin` (08-02); same `.s.aif`, different answer. Every verdict now names both realizers with build dates, and `newerBuildThan()` prints the newer build plus the `AOWLMONY_NIFI=` re-run.
- **Exit 1 meant both "backends disagree" and "compile failed"**, so a shared `nimcache_static` link race read as a divergence. `COMPILE_FAIL_CODE=2` puts it with the could-not-run cases; 1 is now that one claim.
- **`locateOp` walked ancestor frames only**, so a top-level `echo` — `write(stdout, …)` recorded at system's line, no user frame above it — had no location. Falls back to the last op run at a line in the entry module, a preceding sibling.

**Gates.** `npm test` 25/25 → **41/41**, twice clean. The slice case asserted a stale-binary artefact and is gone; the `--native:aowlc` case asserts the invariant (never exit 1) since aowlc gained multi-module linking mid-session.

**Standing.** Genuine: `7 div 0` returned 0 and exit 0, fixed in aowli, which now raises `division by zero`. Native SIGFPEs and loses buffered stdout, so it stays an expected divergence, not a match.

**[aowltest](https://github.com/aoughwl/aowltest) — new repo, 3 commits.** Test results keyed by transitive input hash; an unchanged closure is never re-run, and a compile-time read counts as an input.

- **Key is `sha1` of a sorted manifest**: `dep <path> <sha1>` per transitive local import, `ext <name>` for unresolved stdlib specs, `gdep` for `--dep` globals, the command line, `--salt`. Entry present ⇒ skip.
- **Content-hashed, never mtime.** Restoring bytes restores the key, so a branch switch re-hits. `--explain` diffs a miss against `last/<sha1(testpath)>` and names the input that moved.
- **`isFile` as "try `open`" called every directory a file** — glibc `fopen()` succeeds on directories, so the test root read as one test; 19 of 34 assertions failed at once. `std/private/oscommons.fileExists` stats; `std/files` resolves to Nim 2's lib, not nimony's.
- **Import scan is lexical** — `std/[a,b]`, `from … import`, block and comma continuation, `include`; no `when` evaluation, so it over-approximates: costs a re-run, never a wrong skip.

- **A compile-time read is an input no static scan can find.** `--ctfe-dir:DIR` merges the `*.ctfe-reads` aowlsem wrote into `disc/<key>` after a run; a later hit on the same static key re-hashes each one first, so a moved schema is a miss with identical source bytes. Off unless asked — a wrong guess at the sidecar location would silently skip a changed test.

**Gates.** `tests/run.sh` **35/35 → 41/41** over the cache decision itself: editing `lib/base.nim` re-runs its two dependents and leaves the third cached at 33.3%; restoring the bytes returns 100%. The six CTFE cases carry the control that matters — **without** `--ctfe-dir` the same moved schema is invisible and the run hits, so the re-run is attributable to the record.

**[aowlrepl](https://github.com/aoughwl/aowlrepl) — new repo, 4 commits.** A nimony REPL on aowli. State persists because the session is one module, re-run from the top on every cell.

- **Imports hoisted, everything else in entry order**, then `nimony c --nimcache:<dir>` and `aowli-interp` on the main `.s.nif` — stable across cells because its name hashes the module path. Cold 2.15s, warm 0.19s, run 1ms; only the stdout suffix the previous run did not produce is printed.
- **Completion reads the session's own typed NIF**, which the REPL just compiled: `aowllens decls` per successful compile, `aowllens members <recv>` memoised — the two queries backing aowllsp. `xs.l` narrows to `len` because the NIF says `xs` is a `seq`. Raw-mode editor over `tcsetattr` (`std/terminal` stops at `isatty`), ghost text, menu, history.
- **Highlighting and cell-completeness both ran on a hand-rolled scanner; both now use aowlparser `tokenize`**, so `echo "a:b"`, `echo '('` and `echo 1'u8` are complete and an unterminated literal is not. `aowlparser check` cannot answer completeness — `[]` for `type`, `if x > 1:`, `proc f(): int =`, and `expression-expected` sits in the driver's `collectDiags` (`aowlparser.nim:1188`), not the library. Filed.
- **Three silent-wrong-answer defects.** `compile` counted a non-zero nimony exit with unparseable output as success, so the REPL ran the *previous* session's NIF; `snifIsFresh` now refuses a NIF older than the module just written. `:reset-cache` never worked — `std/dirs.removeDir` is `rmdir(2)`, ENOTEMPTY on a populated nimcache — which wedged a session once that guard fired.

**Gates.** New `tests/run.sh` **8/8**: 5 golden transcripts, 22 reader verdicts (`--analyze`), the candidate set (`--complete`), and the stale-`.s.nif` guard put back with `NIMONY=/bin/true`.

**Standing.** `~/nimony/nimcache_static` is shared by every nimony on the machine whatever `--nimcache:` says, so any concurrent build, test run or LSP deletes `static.o` mid-link; those processes take no lock, so `compile` and `build.sh` take the lock *and* retry on the signature. Installing to `~/.aowl/bin` leaves nothing on `PATH` — the build now symlinks into `~/.local/bin`.

**[aowli](https://aoughwl.github.io/docs/aowli-release) — 11 commits.** Interpreted code is now replaceable *and* compilable while the process runs, and bounded by a capability policy.

- **Hot module swap.** `tryLoadSym` answers from `prog.mem` before touching a file, so `swapHot` re-reads the `.s.nif` and `publish`es each decl over the same SymIds. Clears `callCache` and the for/if/case layout caches — those key on a buffer *address*, which a reallocated buffer reuses.
- **Module-level `var`s are not re-run**, so state survives the code change; a global *added* by the new version is never initialised. Demoed on a live aowlserve io_uring handler: same pid, same socket, `hits` keeps counting.
- **Mid-run JIT via aowlc.** `hybridgen` runs `nimony c --app:lib` — seconds, so startup-only. `aowlcjit.nim` emits the same uniform shim ABI from the `.c.nif` plus one `gcc -shared -fPIC`; `--jit:N` compiles on the first crossing. Scalar tier, own-module procs; everything else declines to interpret.
- **`7 div 0` returned 0, exit 0** — the divisor reached `xint`, whose `div` answers NaN, which `mask` narrowed to an ordinary 0. `isDivByZero` raises in both engines, integer only. `build.sh` now verifies the artifact, not the exit status: a "clean-cache rebuild SUCCEEDED" had left no binary.

- **A native is the only door out of the value model, so `nativeCall` is a complete capability boundary.** `iopolicy.nim` gates it on an int bitmask (`fs.read`/`fs.write`/`fs.meta`/`process`/`env`) plus `--allow-path:PREFIX=CAPS`; a denial halts through `doQuit`, so it is not catchable and never returns a substitute value. `--audit-reads:FILE` records each granted read as path + FNV-1a/64 + size, written by the driver. `policyOn()` is false until `restrictTo`, so an unrestricted run is unchanged.
- **The `hostOpen` backstop demanded fs.read AND fs.write**, vetoing a `writeFile` under a write-only grant that `nativeCall` had already allowed. `capsDeniedOn(need, path)` is now the single decision the gate and the hostfd/hostdir backstops share, and the backstop asks for *either* — its job is catching a syscall that bypassed the gate, not re-deciding it.

**Gates.** `tests/run.sh all` **449/449** with the raise in. New `demo/hotswap/test.sh` **9/9** and `demo/hotjit/test.sh` **6/6**; both carry a negative control (`--frozen`, `--jit` off) because the same-answer assertion passes even when nothing happened, and hotjit also asserts `hybridNativeCalls > 0`. Collatz over 30k inputs: interpreted 3.467s, JIT **0.336s** including the mid-run compile, native 0.006s, byte-identical. New `tests/policy.sh` **11/11**, every grant paired with its denial control.

**[aowlhost](https://aoughwl.github.io/docs/aowlhost) — new repo, 4 commits.** Runs an aowl module as a plugin under a capability policy. Default grant is nothing.

- **Embeds aowli as a library** rather than shelling out: parses the plugin `.s.nif`, replays imported modules in dependency order, installs the policy before any plugin code runs, and owns its stdout/stderr and exit code. A denied call exits **77**.
- **`--allow-path:/etc/hostname=fs.read` reads that file while a sibling under the same policy is denied and named.** `plugins/snoop.nim` wraps its `readFile` in try/except and the except arm never runs — the halt is below the language.

**Gates.** New `tests/run.sh` **9/9**; every denial paired with its granted control, since a trap alone cannot be told from a read that never worked. The write case checks the filesystem afterwards: the absent file is what proves the syscall was never issued.

**[aowlc](https://aoughwl.github.io/docs/aowlc) — 3 commits.** `build`/`run` emitted one translation unit; nothing that touched stdout linked.

- **`unknown type name 'LongString_0_<system>'` on any program calling `echo`.** `compileModule` stubs missing externs, which covers a function and cannot cover a *type*. `build`/`run` now route through `compileProgram` over the sibling `.c.nif` files, entry module last; `--single` opts out. `exec --entry` was unaffected, so it read as a codegen bug.
- **`--emit-only`** writes the linked C without running `cc` — what aowli's JIT consumes before appending shims. `test/driver.sh` covers `build`+`exec`; `test/single.sh` compiles one TU alone, separating a codegen failure from a missing link step.

**[web](https://aoughwl.github.io/docs/web) — 6 commits.** `component` gives a tree typed parameters; one lowering engine now backs both surfaces.

- **`h1 title` rendered `<h1><title></title></h1>`.** A bare ident naming an HTML tag was read as an element, and `title`/`label`/`footer`/`data`/`form`/`summary`/`time`/`code` are tags *and* ordinary parameter names. Only `call`/`cmd` forms are elements now.
- **`web:` and `component:` share `deps/weblower`** instead of two lowerings that drift; `web:` gained `for`/`if`/`while` and runtime children. A child's meaning comes from its type — overloaded `webAppend(string|HTMLNode|HTML)` — and a call is an element iff `html`'s registry knows its name.
- **`[placeholder]:` lowered to `:placeholder`** — one colon on a pseudo-element selects nothing, so the rule silently never applied. `::` for placeholder/before/after/selection/marker/backdrop. `[hover]:`/`[disabled]:` get their own class, and the suffix joins the hash so a state and a base block with equal declarations stop colliding.
- **`@style` with no enclosing element emitted nothing** and the page rendered unstyled; it now fails as `directiveNeedsAnEnclosingElement`. `document()` adds doctype/charset/viewport/embedded CSS, escapes the title, and emits `<` as `\3c ` so a declaration cannot close `<style>` early.

**Gates.** New `tests/run.sh` **6/6** (tweb, tcomponent, tsheet, tescape, tdocument, tstates). `tescape` asserts a component input escaped in both positions it lands in — text child and attribute value — with `rawNode` the only opt-out.

**[css](https://aoughwl.github.io/docs/css) — 2 commits.** Styling by value, not by property soup.

- **`Style`** is an ordered set of validated declarations merged right-wins by `&`, so a theme is a proc returning a value and `theme & declare("color","red")` keeps every property it does not name.
- **`Stylesheet`** maps selector → `Style`: declaring `.btn` twice merges rather than shadows, `sheet[".btn"]` returns a `Style` reusable per element, selectors go through `validateSelector`, and `useStylesheet` installs one process-wide.

**[web-state](https://github.com/aoughwl/web-state) — 2 commits**, plus 1 in [js](https://github.com/aoughwl/js). Fine-grained DOM binding; the blocker was structural, not scheduling.

- **An effect could not know which node to update.** `JsProc0`/`JsProc1` are `{.nimcall.}` and carry no captured environment, so an effect could only touch globals. `toJsWith(p, ctx)` — `_fnToJsCtx`, context captured by value — backs `effectWith`, then `web_state/dom`'s `bindText`.
- **`tests/tdom` counts runs per binding**, not output: writing `count` leaves the name binding at 1 run and a no-op write re-runs neither, so a whole-tree re-render fails the test instead of passing it.
- **`run.sh` hid its failures** — every compile error printed as `no .c.nif`, and a missing `.output` was a silent skip. Both now report what happened.

**Gates.** 3/3 (tauto, tdom, treactive).

**[aowlui](https://github.com/aoughwl/aowlui) — 3 commits.** The lab's 3055-line stylesheet and its page, as values, both gated.

- **`tools/ingest` classifies 429 selectors → 195 components + 64 raw.** A selector the model does not explain becomes `stRaw` verbatim, so the raw count measures the model instead of hiding the gap.
- **Trimming collapsed `.a .b` and `.a.b`**, ingesting every `.owner .part` as a modifier class — declaration counts matched exactly, 1739 = 1739, while the design broke. `tround` compares the declaration multiset both ways: 0 missing, 0 invented.
- **`.aowl` → `.nim` and the pack compiles.** 144 errors were one: imports still named `aoughwl/web`, so every `web:` block was semchecked as ordinary code. The genuinely missing `field`, `name = value`, `webClass`, `webSlot` landed in `web`.
- **`shell.nim` ports `index.html`**; `tshell` reads the kernel script order out of the reference at test time rather than transcribing it, so the gate cannot drift from what it checks.

**Gates.** 3/3 (tround, tshell, tpage).

**Standing.** `serve` does not build here: `~/nimony` combined-prs keeps the posix modules under `src/lib/posix/` where the transport deps expect `src/lib/`, and forcing that path pulls a second stdlib (`type mismatch: got string but wanted string`). Reproduced on an untouched `reactor_http.nim`, so `examples/web_page.nim` is committed unverified.


<br>

## 026 2026-08-01 - Saturday, August 1st 2026

**[aowli](https://aoughwl.github.io/docs/aowli-release) — 18 commits.** Every defect was a silent wrong answer: plausible output, exit 0, empty stderr.

- Nested `return` lost its value to the enclosing case expression (tree-walker only). Outer `ret` overwrote the result.
- `(expr STMT… VALUE)` discarded `flReturn`/`flRaise`/`flBreak` and continued to the trailing value.
- Cell-backed pointers had no address (`cast[uint](addr s[i])` → 0). Stable synthetic addresses added.
- No conversion op for `cast[ptr T]` with non-scalar pointee; integer stayed integer and read as 0.
- Loud-halt not byte-identical across engines; post-`quit` stdout now dropped at shared sink.
- Hybrid boundary failed open: aggregates containing pointers crossed by value and segfaulted. Fixed in aowlabi.
- `build.sh` always returned 0; now exits non-zero, keeps linker lines, retries once on intermittent errors.
- Debugger: unmatched breakpoints report nearest executed lines; DAG reported as `<cycle>`; tuples unreachable by expand.
- `advance()`/`complete()` returned nothing — neither engine could call an imported global as callee. Both now fall back to lazy imported-global slot.
- VM compiled `complete` as unconditional `opCallNative`; now gated on `vkCont`.
- `setScheduler` wrote only engine state, never system’s global. Both engines now update both views.
- `--break-func` fired once per statement; now once per invocation.
- `readFile` failed on correct paths because aowli launched from temp nimcache. `--cwd`/`AOWLI_CWD` tried after cwd-relative open fails.

**Gates.** `run.sh` defaulted to 6 of ~45 categories. Now takes `all`. Real figures: 414/414 → later 434/434 all categories, three-way crosscheck 0 divergences, hybrid 6/6. New lanes: semantics.sh, dbg.sh 15/15, async.sh 9/9. Crosscheck/run defaulted to absolute master paths; now `$NIFI_ROOT/bin`. On complete-integration: 457 AGREE-PASS / 19 AGREE-FAIL / 0 DIVERGE.

`c3b572c` does not compile alone (definition lands in next commit). Pair must move together. Both engines agree on every runnable test. master and complete-integration each carry fixes the other lacks; convergence is a merge with behavioural gate. Arena slices 1–5a in; 5b (Cursor interior pointers) remains the blocker.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 44 commits.** One question for every tool: what is its verdict actually resting on?

- `nimony` exits 0 on rejected arguments; usage banner now treated as failure.
- `explain_failure` answered “OK: compiles clean” for failing compiles; verdict now from compile’s own `ok`.
- Equivalence tools reported identical/preserved for runs that never ran or both crashed.
- ddmin/bisect unbounded by time; total budget added, killed runs no longer count as reproducing.
- Stale server binary answered while signals said healthy; `doctor.server_stale` + build-wait on launch.
- aowli binaries already hot-swap; doctor now identifies live build and reports swapped paused sessions.
- Concurrent nimony builds raced on shared nimcache_static; every invocation now serialises through one flock.

**Gates.** Differential harness compared tool names only (6 of 26 differed in contract). Now 197 curated + 116 sweep cases, 107 unit, 39 e2e, all 8 hooks smoke-tested.

**Messaging.** `/listen <label>` + maildir transport; messages become events. One inbox per repo; `/work <repo>` drains backlog then works. Heartbeat distinguishes live/wedged/dead; `--ping` is proof without costing tokens. Chain depth + rate limits break reply loops.

**[serve](https://aoughwl.github.io/docs/net-stack/serve) — 25 commits.** h2spec 95/146 → 146/146: the 95 was concurrency, not protocol.

- Accept loop ran whole session before accepting again → timeouts in aggregate. Fixed.
- `nghttp2_session_mem_recv` return ignored; frames in read tail dropped.
- `close()` with unread bytes sent RST instead of GOAWAY; now close_notify → shutdown write → drain.
- Stream-id reuse never reached on_begin_headers; tracked and terminates with PROTOCOL_ERROR.
- Reactor gained TLS, timers, stop, outbound client, produced bodies. Idle timeout via CLOCK_MONOTONIC; graceful stop via eventfd.
- All TLS entry points now take context overload. Streaming bodies via pull producer; static serving gained ETag/304/ranges.
- WebTransport streams closed out; QUIC shim counts resource overflows.

**Gates.** h2spec 146/146 h2c and TLS. Streaming e2e: 128 MiB byte-exact at 6 MB peak RSS. Proxy e2e: 12 concurrent 0.5 s upstreams in 0.53 s. One thread serves HTTP/1.1 + 2 + 3 on one port with TLS, timeouts, shutdown, client, streaming.

**[http](https://aoughwl.github.io/docs/net-stack/http) — 2 commits.** Added `parseResponse` (mirror of Request). Header count and body size now bounded (128 headers, 64 MiB).

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 71 commits.** Macros and `const` initialisers stopped being matched by shape and started being run.

- Macros were expanded by matching shapes. Now executed: the body is lowered to a plugin module, built, and run per call site with argument trees marshalled in and the expansion read back. Two executors for the same module — `--macros:interp` semchecks to `.s.nif` and runs it under aowli, `compiled` builds a host-native binary with `nimony s`. `tests/macros.sh` asserts each matches the nimsem oracle *and* that the two match each other.
- A `const` no fold recognised was emitted unchanged inside its `(suf … "i64")` wrapper — a call where the wrapper promises a literal. Now evaluated by generating a module from the host's own declarations up to that const and running it; the value returns through `std/writenif`, not `echo`, which renders for a human and loses float digits. Covers int, bool, float, string; 64 evaluations per module.
- The whole transitive import closure was one flat scope, so `bindSym("add")` in a module importing only std/syncio and std/macros froze std/paths' and std/strutils' `add` into the choice. Visibility is now a fixpoint over `(import (kv <suffix> "<path>") …)`, seeded from direct imports and extended across export edges.
- A template selected itself; a module's own declarations, reached back through an import, counted as rivals; the imported-template merge skipped the self-import filter.
- Untyped imported generics left dirty templates unexpanded; `emitInstanceUntyped` now semchecks body. Multiple template overloads kept. Hygienic rename of template locals.
- A generic type argument was substituted only when bare, not recursively — `Table[string, int]`'s backing `seq[(K, V)]` kept std/tables' own typevars. Two instances of one generic differing only in hash are no longer a provable clash.
- Concepts parsed/emitted but never enforced; requirements now checked at instantiation (E0282).
- Nested generic instances drained at module level (enclosing locals missing); now spliced in place.
- `build.sh` installed newest binary, not the one just linked; now asserts artifact newer than sources.
- `typeof(expr)` copied as tree; now demands `typeOfValue` and emits answer. Macro bodies: parameterised stay raw, zero-arg semchecked.
- A `try` body is a scope. An imported type's base class is recorded, so an upcast is recognised. User pragma-aliases kept and expanded at the use site. E0410 addr suppression narrowed to object-constructor field values; E0100 for a call-shaped type whose callee names nothing.

**Gates.** diff.sh 677/677. check 400/400, beat 4/4, nofp 35/35, diag 175/175, explain 93/93, e2e 4/4. `defined()` byte-exact; `compiles()`/`declared()` still open.
<br>

## 025 2026-07-31 - Friday, July 31st 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) passed its 1000th commit** — 16 days after the first, **65 landed today**, all in the checker. **~32.5k lines** of self-hosted Nimony; byte-exact differential corpus **632 → 659**, no-false-positive gate **23 → 35**.

**The productive gate was the broad-module differential, not hand-written probes.** `tests/moddiff.sh` compiles a real project into a fresh nimcache, re-semchecks every module the oracle produced both a `.p.nif` and a `.s.nif` for, and canon-diffs each. Feature probes had gone several rounds finding nothing — that seam is saturated; forty real modules found a day's work in one run. **18/40 byte-exact, 0 crashes**, the rest quantified in tokens.

**The dominant class was *when* an instance gets minted**, three rules:

* A generic **type** decl's body keeps `(at G …)` raw; a generic **routine's signature** cannot, being shared by every instantiation — `proc parseNum[T: SomeInteger](s: openArray[char])` instantiates `openArray[char]` at decl time.
* Inside a generic decl, a call over still-abstract operands stays **symbolic**: `t[k] = v` in `proc addTo[K: Keyable, V](t: var Table[K, V]; …)` is the generic symbol, no instance, no `haddr`. Instantiating there dragged in the operator's whole lifetime-hook cascade — **5922 tokens on a two-line program**; `std/sets` **7530 → 147**.
* `typeVarLike`, consulted from ~25 places, **guessed from spelling** — one uppercase letter, so `BiTable*[Id, T]` had one of two parameters recognised. Every typevar mint is now recorded, spelling kept only as fallback for imported generics. `std/bitabs` **5863 → 1236**.

**Commit #1000 fixed the ordering assumption underneath.** Type instances emit in *request* order and a dependency is requested *by* the body needing it, so `HashSet[T] = object; t: Table[T, bool]` had its field scanned before `Table[TagId, bool]` registered hooks: the field read unmanaged, and neither HashSet nor anything holding one got lifetime hooks. Reordering is not the answer — the oracle emits in the same order. nimsem decides off the *declaration*, so we now do: a generic whose body structurally holds a lifetime pre-registers its instance's hook names at request time. `std/optcore` **18369 → 16052**.

**A module-qualified name was unhandled in three emitters** — `typeOfExpr` (no `dot` case at all), `semType`, and the `case` of-value list. One shared test resolves all three: the left of the dot is nothing in scope, which is what an import name is. Relatedly `from std/dirs import walkDir` is now really selective — loading the whole module registered `dirs.getCurrentDir(): Path` alongside `ospaths2.getCurrentDir(): string`.

**Smaller parity fixes, each pinned to a real program:** a `distinct` over a primitive keys the base's magic on its own symbol, and `!=`/`>`/`>=` cancel on the operator they derive from; an anonymous routine must never consume a prescan slot, or a lambda in a global initializer takes the next proc's name; proc-type parameters are numbered at the type decl's position; a user-declared lifetime hook suppresses fieldwise synthesis; `{.push header: … .}` applies to every decl *and* parameter; ordering two pointers is an address compare; a prefix operator can be a template; a named argument may skip a defaulted parameter; and four absent folds — set consts by name, float consts, `(par …)` in a `when` condition (`not (defined(cpu16) or defined(cpu8))` was dropping all of `std/widestrs`, **5009 → 415**), and an `{.untyped.}` template body.

**One thing is written down as not reproducible rather than chased.** nimsem lists an `(ochoice …)` in a hash order — system's `+` comes out `3, 6, 12, 10, 14, 0, …`, which is not declaration order, not `.s.idx.nif` order, and not sorted. We emit the right set, sorted, and the commit says so.

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
