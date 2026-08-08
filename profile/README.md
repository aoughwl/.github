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

## 033 2026-08-08 - Saturday, August 8th 2026

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 21 commits.** Steering a fleet of long-running Claude Code sessions from a phone, and then finding that the thing reporting on them was lying about what they were doing.

- **Sessions running overnight had no supervision and no way to reach a human.** A supervisor now restarts them, caps the restarts so a crashing one becomes a message rather than a fork bomb, and hands them anything queued for them; a chat bot carries the items that need a person, filtered to five kinds so the channel does not get muted. Everything rides an on-disk mailbox, so nothing is lost while the bot is down.
- **The status view called a session up on a flag the supervisor writes and nothing clears when the supervisor dies** — a session whose last output was twelve hours old rendered green. The process table is the authority now; the first attempt reported everything alive, because the check shells out and the shell's own command line contained the pattern it was searching for.
- **The activity view printed a list of tool names with no timestamps,** so a session mid-command and one that stopped an hour ago rendered identically. Every line now carries its own age spelled out — "~25 seconds ago" — read from the timestamp on each record of the session's output stream.
- **Anyone in a group chat could drive the fleet, and the bot's API token sat in a world-readable file.** Pairing recorded the channel a message arrived in, which is a property of a place rather than a person; it now records the account. The token's permissions were set once at creation and lost on the next rewrite, which takes the process umask.
- **Starting work is a sentence now, and a session is started once.** "work on aowlsem" starts one and "3 agents on aowlsem" widens it; asking again reports how long it has been up instead of restarting it. Every boot begins with zero sessions — except one whose process is still alive, which is adopted, since the supervisor's children outlive it.

**Where it stands.** Gates **33/33** and **25/25**, both asserting the negative direction: sentences that must *not* become commands ("the aowlsem gate is flaking, can you stop that from happening" is not a stop command), and a boot that must *not* drop a session still running. The sentence layer fails silently by construction — anything it declines goes to a chat session and comes back with a plausible answer — so the negative cases run first.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 6 commits.** Programs checked by our checker now compile, link and run.

- **Four programs run end to end for the first time — 0/6 to 4/6.** The blocker was a single node naming the C file the runtime needs compiled in: the `{.compile.}` pragma travels only in the dependency sidecar, never in the main output, so every program reached the linker and died on an undefined `mi_malloc`.
- **A cached result was published even when the run that produced it failed,** so a second run of the differential gate scored lower than the first — 787, then 786, then 785, on unchanged input. Publishing only on success makes it 787 three times.

**[aowli](https://aoughwl.github.io/docs/aowli) — 4 commits.** The interpreter can run the networking stack, TLS included.

- **A signature-driven foreign-function crossing replaced hand-written bindings**, so a C library call is described once rather than wrapped; TLS now runs interpreted, and future bindings cost nothing.
- **The POSIX socket, `fcntl` and `poll` constants were missing,** which is why the net stack could not be debugged interpreted at all.

**[discord](https://aoughwl.github.io/docs/discord) · [colors](https://aoughwl.github.io/docs/colors) · [json](https://aoughwl.github.io/docs/aowljson) · [mcp](https://aoughwl.github.io/docs/aowlmcp) — 8 commits.** A Discord bot client written in Nimony, and the JSON bug it exposed.

- **A Discord client on our own network stack** — gateway WebSocket in, REST out, slash commands with the deferred acknowledgement Discord requires within three seconds, and a typing indicator.
- **A missing JSON key returned a non-nil null,** so every `!= nil` guard written against it was dead code. In the bot that meant every plain chat message took the button-press branch and was answered with nothing, while the read position still advanced.

<br>

## 032 2026-08-07 - Friday, August 7th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 35 commits.** The one gate that compiles our output past the checker had never run the checker, and fixing that exposed a run of defects that byte-comparison structurally cannot see.

- **The end-to-end gate passed with the checker replaced by `/bin/false`.** Its harness symlinked the toolchain into a scratch directory, but a compiler locates its sibling tools through `/proc/self/exe`, which the kernel resolves through the symlink and back into the real tree — so the reference checker ran and reported on ours. Rebuilt with hard links, it reports **0/6** and stays red.
- **Two defects existed only when the real driver invoked us, not when we were invoked directly.** Every dependency sidecar we wrote was empty, so the next phase received 2 modules where the reference gives it 4 and asserted; and `echo "a", 1` came out unexpanded, with an unresolved nine-way overload set inside it. `echo` is a varargs template whose body loops over its arguments, and our unroller assumed that loop is the template's first statement — true direct, false under the driver.
- **Objects owning an imported `ref` field got no cycle-collection hooks**, because the guard asked whether the type had a destroy hook when it needed to ask whether we had built the helper family for it. **415 fewer differing tokens**, measured against the pre-fix binary over the same source — comparing against the recorded baseline instead credited it with 3,897 that belonged to a different change.
- **Five modules of the compiler's own library were rejected outright**, code the reference compiles. The causes were unrelated: a branch ending in a call that never returns was still intersected into the initialised-variable state; `{.raises.}` was known but not `.canRaise.`, its own alias; a generic that could not bind its type parameters outranked the concrete overloads; `nifstreams.open` bound to `nifreader.open` because a module qualifier was dropped whenever both modules export the name; and **`c.p[].info = x` was rejected on an immutable parameter** — before typing, `x[]` and `x[i]` are the same node, told apart only by child count, so a write *through* a pointer field read as a write *to* it.
- **A test cache kept per working copy made every parallel checkout recompile what another already had.** Cold versus shared, same file and same verdict: **49.4s → 1.8s, with 1.7s of user CPU either way** — all of the difference was waiting on the machine-wide compile lock to redo finished work. One gate had been taking 24 minutes for the same reason.

**Where it stands.** **1,531 commits**, 42,567 lines of Nim across 19 files. Against the reference checker, **31 of 52 library modules are byte-identical — 59.6%** — with 30,916 differing tokens across the other 21; byte-identity is the strictest measure available and says nothing about whether a differing module is *wrong*, only that it is not the same. Differential corpus **785/785** across our own cases. Two of the 52 are aowlsem's own source, so they move whenever we add code. The five rejections above are fixed on branches and the last module now produces output; the full-gate confirmation is pending. End-to-end stays **0/6**: two cases now reach the linker.

**[aowli](https://aoughwl.github.io/docs/aowli) — 1 commit.** A build holding the machine-wide compile lock could not spawn a child that needed it.

- **A nested lock acquisition waited out the full 900-second timeout and then ran unserialised.** The lock had no marker saying it was already held, so a descendant contended for a lock its own ancestor was holding and could not release until the descendant returned. Two lines; the end-to-end gate went from over 400 seconds to 146.

<br>

## 031 2026-08-06 - Thursday, August 6th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 37 commits.** Five wrong-output bugs with one shape: a type or a field the checker could see but could not look up, so it quietly picked the wrong thing instead of failing.

- **A generic type's own fields were unreachable from the module that instantiated it,** so `len(t.keys)` on a field of a `var` parameter resolved to the *set cardinality* builtin and emitted a spurious function for it. Field tables for instances of a generic with private fields were filed where the field lookup never looked.
- **An instance created in the current module never recorded which generic it came from,** so overload resolution saw a bare symbol and fell back to matching on argument count — the exact mechanism two earlier fixes had each switched on for *imported* instances only. One line; **1,133 fewer differing tokens** across three standard-library modules.
- **`.len` on an `openArray` called a function where the reference compiler reads the view's length field.** An `openArray` is a pointer plus a length, so the length is already present; the call also instantiated a `len` the reference emits but never calls.
- **Two generic bodies emitted the wrong thing:** `var s: seq[T] = @[]` produced an empty expression node — not a zero-length seq, nothing at all — and comparing two objects field by field left the loop in place where the reference unrolls it one block per field. **449 fewer differing tokens.**
- **Re-baselining deleted 130 of the baseline file's 189 lines** — every recorded reason a number is what it is, including one that deliberately absorbs a known regression — and exited 0. Separately, two comments cited a test file that had never existed; a new check fails on any test file named in a comment but absent, and found five.

**Where it stands.** Differential corpus **772/772** against the reference checker's own output; no standard-library module falls back to aborting, **46/46**; std/envvars is now byte-identical. Two thirds of what remains is the checker compiling its *own* source, so ranking work by which construct differs most keeps pointing at that one file rather than at the standard library.


**[aowlc](https://aoughwl.github.io/docs/aowlc) — 20 commits.** This backend has two C printers and nothing had ever compared them, so a fix could land in one and leave the other wrong with every gate still green.

- **Three miscompiles lived only in the hand-written printer**, each already fixed in the other: `{.packed.}` dropped, an unpadded octal escape so `"\n7"` printed as `W`, and strings walked by code point where a nimony string is bytes. Both are now compared against nimony's own output, so the gate says which one is wrong rather than only that they differ — **73/73**, exemption list empty.
- **The end-to-end gate's `-Wall -Wextra` was switched off by the C it was compiling.** An in-file `#pragma GCC diagnostic ignored` beats the command line, so the warnings those flags asked for could never appear; it now also compiles a copy with the pragmas stripped.
- **An `{.importc.}` global got no declaration,** so a module referencing one did not compile. Per-module output now emits prototypes for procs a sibling module defines, and every translation unit compiles *and* links on its own.
- **`npm test` read committed artifacts and never the sources beside them,** so fixtures could drift unnoticed; a skipped case also shrank the denominator, which reads exactly like a pass.
- **Seven `nimony` invocations ran without the machine-wide compile lock.** Two compiles at once corrupt each other's link through a shared object that a private cache does not cover — never a false green, but a red could be someone else's build, and no run was repeatable.

**Where it stands.** Printers agree 73/73; end-to-end 73/77 against nimony's own output with 4 declared vacuous; every module compiles alone 77/77; npm 24/24, units 5/5, static initialisers 10/10.

**[aowlabi](https://aoughwl.github.io/docs/aowlabi) — 20 commits.** An ABI is only canonical if the things that re-spell it are checked against it. Three were not.

- **The JavaScript backend's value representation is now gated against the matrix that specifies it** — one probe per abstract type kind, classified structurally rather than by matching the emitter's own output text, **20/20** in both modes. The pointer row had no probe at all despite being the kind the matrix describes most precisely.
- **The C runtime hand-copies the same heap offsets and five bare magic numbers,** and nothing compared the two. It does now, along with a third spelling — the struct definitions the driver injects at build time. Including that runtime's header beside the backend's prelude worked in only one of the two orders; both compile.
- **Two 32-bit sizes had never been checked against anything,** held out precisely because the one available oracle disagreed with them. `gcc -m32 -fsyntax-only` against a freestanding header shim settles both: the ABI is right and the compiler's constant folder is wrong. **11/11.**
- **One row is held out on purpose:** `-m32` means i386, which aligns `double` to 4 where every other 32-bit target uses 8, so gcc is answering for a different target than the question asked. The exemption is written as an *inverted* assertion — if the row ever starts agreeing, the build fails and says to drop it.

**Where it stands.** 122/122 layout, 208/208 heap layout, 1269/1269 marshalling, 26/26 against gcc on each of the two C printers, 21/21 at 32 bits plus 11/11 against `gcc -m32`, 20/20 JavaScript representation.

**[aowljs](https://aoughwl.github.io/docs/aowljs) — 9 commits.** `sizeof` of anything that was not a scalar refused to answer, and the engine that could answer it already existed.

- **`sizeof` of an object, tuple, array, variant or packed type now comes from the ABI layout engine,** mapped from the compiler's own typed IR — this backend holds no layout arithmetic of its own. The alternative was a third implementation of C struct layout, which is the shape that lets a padding bug be fixed in one place and survive in two.
- **Deleting the scalar-width table it replaced fixed a wrong answer.** `sizeof(cstring)` returned 16 where nimony says 8, because `cstring` sat with `string` on the two-word arm: not an aggregate, never reported, an ordinary expression silently wrong.
- **The two backends' corpora are cross-checked by running each program through the other backend,** rather than by a name map asserting that two fixtures test the same thing. Three outcomes, a declared denominator, a deterministic sample.
- **The README called the hand-written JavaScript seed a differential oracle; measured, it agrees on 15 of 61 programs** — it predates methods, exceptions, iterators, variant objects, value semantics and byte strings.

**Where it stands.** Corpus **124/124**, 0 failed, 3 blocked by the reference toolchain itself; the `sizeof` fixture is 26/26 in both modes against nimony's own folded answer.

**[aowli](https://aoughwl.github.io/docs/aowli) — 8 commits.** A released wrong-answer fix, two gates that scored real failures as noise, and the load check's last rule that was still written out once per engine.

- **The public binary returned the wrong substring for an open-ended slice.** `s[a .. ^k]` — from index `a` to `k` characters before the end — read the raw `k` as the upper bound instead of counting from the end, silently dropping or keeping the wrong characters; fixed and released as v0.3.5.
- **A gate scored a failed C compile and a crashed interpreter as the same "eligible but didn't cross" verdict** its own header calls a real defect, because it threw away the exit code and the marker printed on the very line it read. Both are now distinct results — build-failed and crash — each carrying the tail of the log.
- **Another gate classified every non-zero exit of the interpreter as infrastructure noise,** so a run that executed 52,186 native calls and then crashed would never count as a failure. Only a timeout or a missing measurement is infrastructure now; anything that ran and then exited non-zero is a failure.
- **The stale-artifact load check had its type-mismatch rule written out once per engine,** so the two interpreters could drift on whether to reject a correct program. Pulled into one shared function — the argument-count half was already shared.
- **Cutting the release copied 7.1 GB to compile 1.6 MB of source, and the build overwrote the release's public README with a ten-line stub.** The copy is now 218 MB; the stub goes to its own file and an existing README is never touched.

**Where it stands.** v0.3.5 is public; both engines re-verified against the reference compiler at 461/461 across all 53 categories, zero divergences.

<br>

## 030 2026-08-05 - Wednesday, August 5th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 26 commits.** One class of bug dominated the day: parts of a type's identity were being ignored, so two genuinely different types could end up sharing a single generic instance.

- **Eight details were missing from the type-identity check** — float width, tuple field names, the C name given by `{.importc.}`, an array's lower bound and its index type, a proc's calling convention. Effects ranged from a 64-bit read taking four bytes, to `array[Color, int]` and `array[Shade, int]` sharing one body, to valid code being *rejected*. Eight of the nine known cases are closed.
- **Two crashes, both masked until the harness stopped retrying around them.** `sequtils`' own documentation examples call the templates they document, recursing 3,239 frames deep; separately, a resolved symbol was re-routed through a name-keyed table and re-expanded `system`'s `[]`. Both now surface as a reportable difference rather than a signal 11.
- **A `ref` alias declared before its object type got a destructor that freed the box but not its contents** — a real leak, hit by `StringStream`. The alias now reserves its lifetime hooks and fills them in when the module closes.
- **A proc taking `openArray[string] = []` never inferred its element type.** That gap exists at three separate sites, and fixing one in isolation made `osproc` three times worse; all three now share one implementation. `osproc` divergence 119 → 39 tokens.
- **Two lookups were keyed on a name that is never used as a key** — `sizeof` on a proc-type alias, and a deferred `+` inside a generic body that saw 11 of `system`'s 17 overloads and silently dropped the six unary ones.

**Where it stands.** Differential corpus 745 → **762/762**. Divergence from the reference compiler across the 46 standard-library modules fell 48,579 → **42,190 tokens**, so **96.54%** of 1,220,605 tokens now match byte for byte. About 5,000 of that drop is a re-baseline of the previous day's work rather than new ground. Next is the `seq[T]` instance family, which is wrong in both directions.

**[aowli](https://aoughwl.github.io/docs/aowli) — 50 commits.** Gates that were confident about code they had never actually entered, and the last remaining exclusion in the foreign-function boundary.

- **Hot-swapping a module could bind an argument to the wrong type and answer anyway.** Two overloads of the same arity renumber identically, so neither drift check caught it — a live demo server had been serving HTTP 200 with a string bound to an `int` parameter. The swap now refuses, and the call raises.
- **A cache-pruning tool never entered the directory it claimed to empty,** and its keep-rule was wrong for 23 of 490 entries. 481 MB reclaimed once it did.
- **A `cstring` returned from native code had nowhere to live** — every memory region the interpreter models is either interpreter-owned bytes or a view onto them. Foreign pointers now carry the foreign address and compare by it; copying the bytes instead would have made `f() == f()` answer false where a native build answers true.
- **A gate's freshness check was reading a build input out of a sibling repository's working tree,** so it measured the machine rather than the commit. Split into a real assertion and an infrastructure warning.

**Where it stands.** Every open interpreter issue is closed, and the last foreign-function exclusion now crosses the boundary. Hybrid mode 24/24 over 22 directories, foreign-function hybrid 10/10, corpus 460/460 across all 53 categories, cross-engine divergences 0, destructor mode 18/18 on both engines, browser bundles 28 passing. One gate printed its own coverage from a hard-coded literal, so a 22nd directory could be added and still read "21 of 21" — computed now.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 2 commits.**

- **The message-bus loop guard counted a session's own sends,** so a long-running session would eventually refuse to send anything at all.
- **The tool gate read `grep`'s regex as a file path**: in `grep -q .` the only non-flag token is the pattern, and `.` resolves to the current directory. Scope tests 30 → 35.

**[aowljs](https://aoughwl.github.io/docs/aowljs) — 30 commits.** Mapping nimony onto native JS values is lossy wherever the target's semantics differ, and every such place was silently wrong.

- **Objects, tuples, arrays and seqs assigned by reference where nimony copies, and compared by reference where nimony compares by value.** 6 of 12 aliasing answers and 9 of 16 equality answers were wrong; `in`/`find` inherited it. `__cp`/`__eq`/`__has` are type-gated, and `__ref` on `newobj` stops both at a `ref object`, whose identity semantics are the mirror bug.
- **`method`, `block`, `discard`, `incl`/`excl` and `dec` had no branch in emitStmt** and were dropped whole. A `block outer:` fixture had passed because dropping the block and taking the `break` skip the same `echo`.
- **A nimony string is bytes and a JS string is UTF-16**, so `"h\xC3\xA9llo".len` answered 5. Literals emit one code unit per byte; `jsFlush` decodes once at the end.
- **`bin/aowljs` was a commit behind `src/`** — no build script existed, so every green run measured an unrebuilt emitter. `build.sh` now runs first.

**Gates.** Corpus 18 → **102/102**, 0 failed, 2 blocked (51 single-module + 2 multi-module × 2 modes); faithful **6/6**. BLOCKED is a third outcome for what nimony itself cannot run.

**Standing.** Three nimony defects filed to `aowlsem`: `x of T` is true when echoed and false when bound or branched on; a nested proc containing a `defer` crashes `derefs.nim trTry`; two `defer`s in one proc emit C that does not compile.

**[aowlc](https://aoughwl.github.io/docs/aowlc) — 21 commits.** Three miscompiles, all invisible because the gate could not hear gcc.

- **`gcc … 2>&1 | head -1` killed gcc with SIGPIPE**, so two lines of *warnings* produced no binary and reported COMPILE-FAIL. The first defect below had been in that output all along.
- **`(ret .)` emitted a bare `return;` from a non-void function** — undefined behaviour, survived only because a struct return goes through a hidden pointer.
- **An uninitialised local was indeterminate where nimony says zero**, and **`{.packed.}` was dropped entirely**, so a packed object was 24 bytes against nimony's 10 with every field after the first at a different offset.

**Gates.** e2e 8/12 → **54/58** compared against nimony's own output, 4 vacuous, now under `-Wall -Wextra`; units 5/5, staticinit 10/10, npm 24/24.

**[aowlabi](https://aoughwl.github.io/docs/aowlabi) — 5 commits.** Every existing gate measured nimony's sem-level `sizeof`, not the struct that reaches a binary.

- **`tests/cbackend.sh` diffs the layout model against gcc's `sizeof`/`offsetof` on the C aowlc emits** — 22 rows covering padding, variants (anonymous union), packed, union, a 3-deep chain, sets, refs, proc fields, ranges, distinct and empty fields. It found the `{.packed.}` bug on its first extended run.
- **Falsified from both sides, and two attempts proved nothing**: reordering a variant's common fields and swapping a `set` for `array[4, char]` both leave every number identical. A perturbation that does not move the expected output is not a test.

**Gates.** 122/122 layout, 208/208 heapspec, 1269/1269 marshal, **22/22 C-backend** (new), 21/21 at 32 bits.

<br>

## 029 2026-08-04 - Tuesday, August 4th 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 121 commits.** Divergence across the 46 standard-library modules fell **73,809 → 48,579 tokens (−34%)**; **30 modules are now byte-exact**, up from 20.

- **The checker's own source file accounted for a third of the remaining gap.** Two causes: a resolved field access came back out degraded when it passed through the checker a second time, and a `var` template parameter arrived as a value rather than as a location. 32,104 → 19,737 tokens.
- **Merging a parallel 33-commit branch silently dropped fixes while importing their tests.** Git merged cleanly, no conflict markers, in favour of the wrong side — it kept a lookup table and deleted every line that filled it, and kept a comment describing a guard it had removed. Recovered against the failing tests, which were the only reliable evidence of what had survived.
- **The expression checker is called on statements 11,500+ times per run, and fails to recognise its own output 8,300+ times.** Instrumenting every fall-through recorded 24,349 such events across 46 modules. That is a dispatch problem, which is why adding more expression rules kept not fixing it.
- **The module-scale harness computed per-module numbers and compared them to nothing.** It now judges each module against a recorded baseline, and immediately caught four changes that were green on the 741-case corpus while regressing whole modules.

**How done is it.** **1,312 commits**; **40,147 lines** of Nim across 19 source files, plus 12,376 lines of test cases and 5,351 of harness. Against the reference checker on the 46 standard-library modules, aowlsem emits **1,146,554 of 1,195,133 tokens byte-identically — 95.94%** — with **30 of 46 modules (65%)** exact end to end. That figure is agreement with one frozen reference build, and presumes it correct in all 48,579 differing tokens; two cases are already recorded where it is not. Accept/reject agreement 407/409, corpus 737/741, no module crashes.

**What is not done.** The remaining 4% is not evenly spread: aowlsem's own source holds 40% of it, and that file grows as the compiler does. The four open corpus cases are all one shape. A ranked list of the remainder, and 26 items each carrying a verified reproduction and a named fix site, are checked in.

**[aowli](https://aoughwl.github.io/aowli) — 47 commits.** Capability grants applied at the wrong granularity, a destructor that never ran on the error path, and a just-in-time compiler whose in-process route was three bugs deep behind a silent fallback.

- **One shim revoked every no-dereference grant in the build.** Giving those candidates their own module took whole-program checking from 334,381 revoked / 0 honoured to 270,800 honoured / 0 revoked, and native calls from 100,528 to 371,328 — byte-identical output.
- **A local passed through a raising call was never destroyed.** Both engines unwound through their own error channel, which made the scope-exit destructor dead code.
- **The JIT's in-process route had three bugs, each hidden by the one before it** — emitter caches outliving their reset, globals emitted after the bodies referencing them, and a missing runtime declaration. Every assertion passed on either route, so nothing ever failed; the gate now names which route ran.
- **All four committed browser bundles were dead,** predating a change to the glue code. Each bundle's behaviour is now gated, rather than its existence.

**[aowlc](https://aoughwl.github.io/docs/aowlc) — 2 commits.** A translation unit referenced a global before defining it.

- **An inlined proc copied in from another module names *this* module's string literals,** and globals were emitted after those bodies. The reverse dependency cannot occur, so the ordering is settled rather than negotiated.
- **A module-level `const` was emitted `static`,** while string literals are referenced across modules by `extern`. The linker accepts both silently; only the consumer's `dlopen` fails.

<br>

## 028 2026-08-03 - Monday, August 3rd 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 36 commits.** Imported templates were invisible to overload resolution, two compile-time predicates answered in only one of the two positions they occur in, and then an audit of what the test gates actually assert.

- **An imported template carried no scope entry, so no call could ever select one.** They are now merged into the candidate set *after* the arity filter — an imported template has no recorded parameters, so an arity test drops them all.
- **`declared()` and `compiles()` folded only inside `when` conditions.** In a `const` initialiser they reached neither path, so `const a = compiles(known(1))` folded to false — correct for every negative case, which is exactly why it went unseen.
- **Three type-classification gaps.** An imported generic's field type was unrecoverable at the use site; `nil ptr T` written in its infix form classified as unknown in both classifiers that are not the main type checker; and `bitand`/`bitor`/`bitxor` widened the typed operand to match an untyped literal instead of narrowing the literal.
- **A `const` element of a set literal inlines to its value,** so on POSIX — where `DirSep` and `AltSep` are both `'/'` — the duplicate-element check fired on valid code and stopped a whole standard-library module.

- **The gate binary was 14 hours stale, and every gate defaulted to it.** Every other measurement bug mis-scores a component; this one mis-scores the subject, and fails both ways — a fix missing from the binary reads as "still broken", and a regression missing from it ships. Gates now refuse a stale binary and print its path and timestamp on every run.
- **Two gates claimed to check a recorded token count and compared nothing.** The numbers sat in a header comment, and one counted any non-zero difference as a pass — so two evaluators folding the same *wrong* constant read as agreement.
- **`n/n` is true at zero.** A documentation gate printed "1/1 codes documented" with an entire family of error sites unchecked, because its denominator was scraped rather than declared. Floored in five places.

**Gates.** Corpus **718/718**, accept/reject 403/403, no-crash 45/45, no-false-positive 35/35, diagnostics 175/175, explanations 94/94, macros 6/6, const evaluation 18/18, compile-time policy 7/7, index 16/16, end-to-end 6/6, imports 5/5 → **10/10**. All re-run on a binary verified fresh.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 3 commits.** The token-thrift claim measured for the first time, then the defects that measuring exposed.

- **The accounting tool over-counted one tool 515×,** sizing an internal payload rather than what actually reaches the model — hiding the real cost driver behind one that does not exist.
- **File reads are 52.9% of context drain, shell 27.4%, all 26 language tools 15.1%,** at 355× amplification. Neither is being abused — three quarters of read bytes were already windowed — so the lever is substituting a declaration lookup for the 857 reads that wanted exactly one declaration.
- **Terse output was inert or absent on the tools that cost the most.** It is now the default rather than an opt-in: outlines −43.8%, builds −68.9%, search gained it at −19.5%.
- **A guard failed open on any file with more than 80 declarations,** disabling itself on exactly the files it exists for.

**[aowltest](https://aoughwl.github.io/docs/aowltest) — 1 commit.** The gate was 35 assertions welded to one binary; it is now a corpus any implementation can be run against.

- **Extracted into nine cases in a small step language,** executed by a runner that knows no implementation, with everything specific behind a three-verb adapter and a line-oriented observation record.
- **35 → 72 assertions from the extraction alone.** Per-test status, input sets and key stability are record fields; grepping formatted human output could never reach them.

**[aowlmony](https://aoughwl.github.io/docs/aowlmony) — 3 commits.** `verify --memory` catches dangling pointers, witnessed by a real destructor-enabled run.

- **The finding is structural and the run only witnesses it** — a destructor at the blamed scope, the use site reached — so each result is labelled confirmed or structural rather than simply asserted.
- **It needed a real artifact reader; the driver had only ever used regular expressions.** Line-information deltas are relative to the enclosing node rather than the previous sibling, so an escaping address anchors on the `addr` and not on the proc header.
- **The trace parser had silently stopped understanding the interpreter's output.** Every operation parsed at line 0 and attribution degraded to "no source location" while reporting nothing wrong.
- **The driver compiled without the machine-wide toolchain lock,** so three consecutive gate runs gave 64/64, 62/64 and 59/64. `npm test` 41/41 → **64/64**, clean on the first full run after the lock.

**[aowli](https://aoughwl.github.io/docs/aowli) — 37 commits.** An object could not live in flat allocated memory — which is the storage the compiler's own token buffers actually use. Now it can, and the interpreter grew record/replay, coverage and a sampling profiler.

- **An object stored into raw memory read back as zero, on both engines, exit 0.** Fields are now placed at C-ABI offsets and resolved individually, retiring an overlay that aliased every element.
- **`sizeof` answered 4 for every variant object, against a native build's 12** — the size calculation skipped the `case` section whole, counting neither the discriminator nor any branch.
- **A `distinct`-typed return value came back as 0,** while the same type crossed correctly as a parameter.
- **Record/replay, coverage and a sampling profiler, with no instrumentation pass.** The journal serves filesystem, environment, clock, argv and stdin from a portable text log, so a recorded run reproduces elsewhere.

**Gates.** Replay 19/19, coverage 41/41, debugger 21 → 40/40, cross-engine 189 agreeing / **0 diverging** over 16 categories. The interpreter now runs the real compiler end to end: 20.9s interpreted against 0.013s native on a three-line input, byte-identical, and 23.4s on a 57-line one — a startup floor, not a slope.

**[aowlabi](https://aoughwl.github.io/docs/aowlabi) — 16 commits.** The canonical-layout claim had never been checked against the compiler it speaks for. Checking it found every inherited field at the wrong offset.

- **`object of RootObj` started its own fields at offset 0 rather than one pointer in.** An inheritable root carries a hidden runtime-type word, so every offset and every size of every inheriting object was wrong.
- **The gate is a differential**: one program prints what the compiler actually lays out, another computes it from the model with no `sizeof` anywhere. The compiler implements neither `alignof` nor `offsetof`, so alignment is recovered from a probe object.
- **Sets, `{.packed.}`, `{.union.}`, range types and `UncheckedArray[T]` had no model at all.**
- **String literals do not walk the runtime's small-string tiers,** so a 10-character value is stored one way if built at runtime and another if written as a literal.

**Gates.** 96/96 layout checks diffed against the compiler, 153/153 heap offsets, 857/857 marshalling invariants, ~25 seconds. Every rule was falsified before being trusted — removing the hidden word, shifting an offset by one word, or sizing a set by width instead of range each turns the expected rows red.

<br>

## 027 2026-08-02 - Sunday, August 2nd 2026

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 29 commits.** Compile-time evaluation moved beyond `const` initialisers — and then got bounded by a capability policy.

- **Four sites treated "cannot compute" as a definite answer; three miscompiled silently.** `when big():` took the wrong branch with no diagnostic in all three contexts it can appear, including type bodies, where a wrong branch means a wrong type. An enum member given a computed value kept its auto-increment ordinal instead.
- **A `const` inside a proc forked the compiler until it was killed** — the stop condition matched only top-level declarations, so every child regenerated the evaluator. Bounded by depth as well as by budget.
- **Aggregate constants now fold** — arrays, `seq[int]`, and all-integer objects — with the value bound once so the initialiser runs a single time. A wrong element count fails rather than folding a partial answer.
- **Compile-time code now runs under a capability policy.** A macro or const evaluator is granted read and write on its own working directory and nothing else; a denial halts the compile rather than returning a substitute value. Each granted read is *recorded* with a hash, so `ctfe-check` answers whether a compiled artifact is still current — as an exit code, so the build tools need not parse anything.
- **`--lens:` publishes what the checker resolved** — declarations with position, type and signature, occurrences naming the symbol they bound, and member tables with inheritance and visibility. Positions have to be recorded *during* checking: the typed output carries one only where a subtree was copied verbatim, so every symbol the checker mints has none.

**Gates.** Corpus 685 → **701/701**, accept/reject 401/401. A new const-evaluation gate is **18/18** — both executors match the reference *and* each other, and each is proved to have actually evaluated, since the shape folds would otherwise let a no-op run look green. New compile-time-policy gate **7/7**, every grant paired with its denial.

**[aowllens](https://aoughwl.github.io/docs/aowllens) — 2 commits.** Reads the checker's index instead of reconstructing it from the tree: an occurrence at a position already names its symbol, so shadowing becomes the checker's answer rather than a guess. The fallback is per question, not per run — no index, or nothing in it for this question, and the existing walk answers exactly as before.

**[aowlmony](https://aoughwl.github.io/docs/aowlmony) — 3 commits.** `verify` diffs a native build against an interpreted one off a single front end. Its first two findings were both artefacts of *which binary ran*, not backend defects — so every verdict now names both implementations with their build dates, and "compile failed" was split out from "the backends disagree". `npm test` 25/25 → **41/41**. One genuine finding: `7 div 0` returned 0 with exit 0, fixed in the interpreter.

**[aowltest](https://github.com/aoughwl/aowltest) — new repo, 3 commits.** Test results keyed by the hash of their transitive inputs: an unchanged closure is never re-run.

- **Content-hashed, never timestamped,** so restoring bytes restores the key and a branch switch re-hits the cache. The import scan is deliberately lexical and over-approximates — that costs a re-run, never a wrong skip.
- **A compile-time read is an input no static scan can find.** Merging the compiler's recorded reads into the cache entry makes a moved schema file a miss with identical source bytes. Off unless asked for: guessing wrong would silently skip a changed test.

**Gates.** 35 → **41/41** over the cache decision itself — editing a base module re-runs its two dependents and leaves the third cached; restoring the bytes returns 100%. The compile-time cases carry the control that matters: without the recorded reads the same moved schema is invisible and the run hits, so the re-run is attributable.

**[aowlrepl](https://github.com/aoughwl/aowlrepl) — new repo, 4 commits.** A REPL for the language, on the interpreter. State persists because the session is one module, re-run from the top on every cell — cold 2.15s, warm 0.19s, run 1ms.

- **Completion reads the session's own typed output,** which the REPL just compiled, so `xs.l` narrows to `len` because the artifact says `xs` is a `seq`. The same two queries that back the language server.
- **Highlighting and cell-completeness both ran on a hand-rolled scanner** and now use the real tokenizer, so `echo "a:b"`, `echo '('` and `echo 1'u8` are complete and an unterminated literal is not.
- **Three silent-wrong-answer defects,** the worst of which ran the *previous* cell's artifact when a compile failed in an unparseable way.

**[aowli](https://aoughwl.github.io/docs/aowli-release) — 11 commits.** Interpreted code is now replaceable *and* compilable while the process runs, and bounded by a capability policy.

- **Hot module swap.** Re-read a module and publish each declaration over the same identities. Module-level variables are not re-run, so state survives the code change — demonstrated on a live HTTP handler: same process, same socket, the request counter keeps counting.
- **Mid-run JIT.** Hot procs are compiled to a shared library and loaded while the program is still running. Collatz over 30,000 inputs: interpreted 3.467s, JIT **0.336s** including the mid-run compile, native 0.006s, byte-identical.
- **A native call is the only door out of the value model, which makes it a complete capability boundary.** Grants are a bitmask plus path prefixes; a denial halts uncatchably and never returns a substitute value. Unrestricted runs are unchanged.
- **`7 div 0` returned 0 with exit 0** — the divisor reached a wide integer type whose division answers NaN, which narrowed back to an ordinary 0. Both engines now raise.

**Gates.** Full corpus **449/449**. New hot-swap 9/9 and JIT 6/6 suites, each with a negative control, because a same-answer assertion also passes when nothing happened. New policy gate 11/11, every grant paired with its denial.

**[aowlhost](https://aoughwl.github.io/docs/aowlhost) — new repo, 4 commits.** Runs a module as a plugin under a capability policy, embedding the interpreter as a library rather than shelling out. The default grant is nothing, and a denied call exits 77. A plugin can wrap its `readFile` in `try`/`except` and the `except` arm never runs — the halt is below the language. Gate 9/9, every denial paired with a granted control, since a trap alone cannot be told apart from a read that never worked.

**[aowlc](https://aoughwl.github.io/docs/aowlc) — 3 commits.** `build` and `run` emitted a single translation unit, so nothing that touched stdout would link — any program calling `echo` failed on a missing *type*, which reads as a code-generation bug. Both now route through whole-program compilation; `--single` opts out, and `--emit-only` writes the linked C without invoking a compiler.

**[web](https://aoughwl.github.io/docs/web) · [css](https://aoughwl.github.io/docs/css) · [web-state](https://github.com/aoughwl/web-state) · [aowlui](https://github.com/aoughwl/aowlui) — 13 commits.** The typed HTML and CSS surfaces, and the reactive DOM layer.

- **`component` gives a tree typed parameters,** and both surfaces now share one lowering engine instead of two that drift. A bare identifier naming an HTML tag was being read as an element, so `h1 title` rendered `<h1><title></title></h1>` — `title`, `label`, `footer`, `form` and `time` are tags *and* ordinary parameter names.
- **Styling by value, not property soup.** A `Style` is an ordered set of validated declarations merged right-wins, so a theme is a proc returning a value and merging keeps every property it does not name. Declaring the same selector twice merges rather than shadows.
- **A reactive effect could not know which node to update** — the JS callback types carry no captured environment, so an effect could only touch globals. Context capture by value now backs text binding, and the test counts runs per binding, so a whole-tree re-render fails instead of passing.
- **A 3,055-line lab stylesheet ingested as values:** 429 selectors into 195 components and 64 kept verbatim, so the raw count measures the model instead of hiding the gap. An earlier pass collapsed two distinct selector forms while declaration counts matched exactly, 1,739 = 1,739, and the design broke anyway — the gate now compares the declaration multiset both ways.

<br>

## 026 2026-08-01 - Saturday, August 1st 2026

**[aowli](https://aoughwl.github.io/docs/aowli-release) — 18 commits.** Every defect this day was a silent wrong answer: plausible output, exit 0, empty stderr.

- **Control flow leaking through expressions.** A nested `return` lost its value to the enclosing `case` expression, and a statement-list expression discarded `return` / `raise` / `break` and carried on to its trailing value.
- **Pointers into cell-backed storage had no address at all** (`cast[uint](addr s[i])` gave 0), and a `cast[ptr T]` to a non-scalar pointee had no conversion, so an integer stayed an integer and read as 0.
- **The hybrid boundary failed open:** aggregates containing pointers crossed by value and segfaulted.
- **The build script always returned 0.** It now exits non-zero, keeps the linker output, and retries once on intermittent errors.

**Gates.** The runner defaulted to 6 of ~45 categories and still printed a clean N/N. Real figures with `all`: **414/414**, later 434/434; three-way cross-check 0 divergences; hybrid 6/6; new debugger and async lanes 15/15 and 9/9.

**[aowlcode](https://aoughwl.github.io/docs/aowlcode) — 44 commits.** One question asked of every tool: what is its verdict actually resting on?

- **The compiler exits 0 on rejected arguments,** so a usage banner had been reading as a clean compile. Now treated as failure.
- **`explain_failure` answered "OK: compiles clean" for failing compiles,** and the equivalence tools reported "identical" for runs that never ran or that both crashed.
- **Reduction and bisection were unbounded in time,** and killed runs counted as reproducing.
- **A stale server binary answered while every signal said healthy.** Diagnosis now identifies the live build and reports paused sessions that were swapped underneath.
- **Concurrent builds raced on a shared cache directory;** every invocation now serialises through one lock.

**Gates.** The differential harness had been comparing tool *names* only — 6 of 26 tools differed in contract. Now 197 curated plus 116 swept cases, 107 unit, 39 end-to-end, all 8 hooks smoke-tested.

**Messaging.** Instances can now be addressed: a maildir transport turns messages into events, one inbox per domain, a heartbeat that distinguishes live from wedged from dead, and chain-depth and rate limits that break reply loops.

**[serve](https://aoughwl.github.io/docs/net-stack/serve) — 25 commits.** h2spec 95/146 → **146/146** — and the 95 was concurrency, not protocol.

- **The accept loop ran a whole session before accepting again,** which only shows up in aggregate as timeouts.
- **A return value from the HTTP/2 session was ignored,** dropping frames left in the read tail; and `close()` with unread bytes sent RST where it should have sent GOAWAY.
- **The reactor gained TLS, timers, stop, an outbound client and produced bodies** — one thread now serves HTTP/1.1, HTTP/2 and HTTP/3 on one port, with TLS, timeouts, graceful shutdown, streaming and static serving with ETag, 304 and ranges.

**Gates.** h2spec 146/146 over both h2c and TLS. Streaming: 128 MiB byte-exact at 6 MB peak RSS. Proxy: 12 concurrent half-second upstreams in 0.53s.

**[aowlsem](https://aoughwl.github.io/docs/aowlsem) — 71 commits.** Macros and `const` initialisers stopped being matched by shape and started being *run*.

- **Macros are now executed, not pattern-matched.** The body is lowered into a plugin module, built, and run per call site with the argument trees marshalled in and the expansion read back — with two independent executors, one interpreting and one compiling, each asserted against the reference *and* against each other.
- **A `const` no fold recognised was emitted unchanged inside a wrapper that promises a literal.** Such constants are now evaluated by generating a module from the host's own declarations and running it; the value comes back through a machine format rather than `echo`, which renders for humans and loses float digits.
- **The whole transitive import closure was one flat scope,** so `bindSym("add")` in a module importing two std modules froze several unrelated `add`s into the choice. Visibility is now a fixpoint over the real import graph, seeded from direct imports and extended across export edges.
- **A generic type argument was substituted only when bare, never recursively** — `Table[string, int]`'s backing storage kept `std/tables`' own type variables, so two instances differing only in hash were a provable clash.

**Gates.** Corpus 677/677, accept/reject 400/400, no-false-positive 35/35, diagnostics 175/175, explanations 93/93.

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
