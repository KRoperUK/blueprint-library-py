# blueprint-library-py

Template for a **Python client library** that backs a Home Assistant integration (or any asyncio consumer). Distilled from:

- [pysolarcloud](https://github.com/KRoperUK/pysolarcloud) / `sungrow-isolarcloud`
- [dimplex-controller-py](https://github.com/KRoperUK/dimplex-controller-py)

## What this blueprint includes

| Area | Pattern |
| --- | --- |
| **Layout** | `src/<package>/` + `tests/` + `py.typed` |
| **Build** | `pyproject.toml` (setuptools or hatchling), wheel + sdist |
| **Quality** | ruff, mypy, pytest (+asyncio), coverage |
| **CI** | lint + multi-Python test matrix on PR/push |
| **Release** | release-please (conventional commits) → GitHub Release + tag `v*` |
| **Publish** | PyPI Trusted Publishing (`id-token: write`) on tags / release-please |
| **API design** | async-first, typed public surface, explicit exceptions |
| **HA-friendly** | no Home Assistant imports; pin from integration `manifest.json` |

## Create a new library from this blueprint

1. Use as GitHub template (or clone + re-init).
2. Rename placeholders:

   | Placeholder | Example |
   | --- | --- |
   | `example_client` | import package |
   | `example-client` | PyPI distribution name |
   | `KRoperUK/blueprint-library-py` | GitHub repo |

   ```bash
   rg -l 'example_client|example-client|blueprint-library-py' | xargs sed -i '' \
     -e 's/blueprint-library-py/my-device-py/g' \
     -e 's/example_client/my_device/g' \
     -e 's/example-client/my-device/g'
   mv src/example_client src/my_device
   ```

3. Configure **PyPI Trusted Publishing** for this repo (environment `pypi`) — see [PyPA docs](https://docs.pypi.org/trusted-publishers/).
4. Use conventional commits; merge the release-please PR to cut `vX.Y.Z` and publish.

## Integration pairing

Keep protocol/auth/transport **here**. The HA custom component should:

- depend on an **exact** version: `"example-client==0.1.0"` in `manifest.json`
- own only HA concepts (config entries, entities, repairs, diagnostics)

See also [blueprint-integration-hass](https://github.com/KRoperUK/blueprint-integration-hass).

## License

MIT
