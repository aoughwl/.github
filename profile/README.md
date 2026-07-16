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
| **net stack** — `tcp`·`net`·`tls`·`http`·`compress`·`serve`·`ws`·`requests` — TLS 1.3, HTTP/1.1+2, WebSocket, HTTP/3 | [docs](https://aoughwl.github.io/docs/net-stack) |
| **web / html / css** — typed HTML5 + MDN CSS engine + DSL | [docs](https://aoughwl.github.io/docs/web) |
| **ws** — RFC 6455 WebSocket (server + client, `ws://` + `wss://`) | [docs](https://aoughwl.github.io/docs/net-stack/ws) |
| **nimony-ts / nimony-py / nimony-hl** — idiomatic TS/Py backends + shared HL-IR | [ts](https://aoughwl.github.io/docs/nimony-ts) · [py](https://aoughwl.github.io/docs/nimony-py) · [hl](https://aoughwl.github.io/docs/nimony-hl) |


<br><br><br>

# Daily Blog

<br>

## 009 2026-07-015 - Wednesday, July 15th 2026
Created [nifc](https://aoughwl.github.io/docs/nifjs)<br>
Created [nifjs](https://aoughwl.github.io/docs/nifjs)<br>
Created [nifjs-js](https://github.com/aoughwl/nifjs-js)<br>
Created [nifsem](https://github.com/aoughwl/nifsem)<br>
Updated [nifi](https://github.com/aoughwl/nifi)<br>
Updated [nifparser](https://github.com/aoughwl/nifi)<br>
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
