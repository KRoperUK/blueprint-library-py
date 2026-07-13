
# Contributing

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/). release-please opens a release PR from `feat` / `fix` / breaking changes.

## Local development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
ruff check src tests && ruff format --check src tests
mypy
pytest --cov=src/example_client
```

## Design rules

1. **No Home Assistant imports** in this package.
2. Public exceptions are stable and small (`AuthError`, `ClientError`, …).
3. Accept an injected `aiohttp.ClientSession` (do not create a global session).
4. Prefer explicit types; ship `py.typed`.
5. Never log secrets; redact in any debug helpers.
