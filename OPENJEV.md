# OpenJEV support

This fork of [jgrep](https://github.com/keltokhy/jgrep) adds optional support for
[OpenJEV](https://openjev.sh), a free community gateway to TypeSafe's Jev model.
TypeSafe remains the default; anyone with a `TYPESAFE_API_KEY` sees no behaviour change.

## What was added

- **`src/jgrep/core.py`** — a new `openjev` provider entry in the JevKit catalog,
  alongside the existing `typesafe`, `openrouter`, `gateway`, and local-server
  providers. Endpoint `https://api.openjev.sh/v1/systemone`, model `openjev`,
  key env `OPENJEV_API_KEY`.
- **`tests/test_cli.py`** — `OPENJEV_API_KEY` added to the test env-cleanup list
  so it never leaks from the host environment into tests.
- **`README.md`** — OpenJEV note after the intro, a row in the API-keys table, and
  `openjev.key` listed among the config-file key locations.

## Provider selection rule

1. **Explicit choice wins** — `--api openjev` or `JEV_API=openjev` forces OpenJEV.
2. **TypeSafe if its key is set** — unchanged default; `TYPESAFE_API_KEY` is tried
   first.
3. **OpenRouter if its key is set** — existing second priority, unchanged.
4. **OpenJEV if only `OPENJEV_API_KEY` is set** — the new fallback when no other
   hosted provider has a key.

Anyone with a TypeSafe key (or an OpenRouter key) sees zero behaviour change.

## How to configure

```bash
export OPENJEV_API_KEY=...          # or put it in ~/.config/jev/openjev.key
jgrep "a stack trace" build.log     # picked automatically when it is the only key set
jgrep --api openjev "a stack trace" build.log   # force it explicitly
```

Requests use the same `{model, state, questions}` body as TypeSafe. The model id
sent to OpenJEV is `openjev`; override it with `--model` if needed.

## How it was verified

- One live `POST https://api.openjev.sh/v1/systemone` request with the forwarded
  OpenJEV key, model `openjev`, state `ping`, one noul question — returned HTTP 200.
- A grep confirmed no hardcoded `api.typesafe.ai` URL was introduced or left as a
  default in jgrep's own source (the TypeSafe endpoint lives in `jevkit-runtime`,
  unchanged).

## Upstream

Original project: https://github.com/keltokhy/jgrep by @keltokhy.
