
# Agent notes (library blueprint)

- Keep this package free of Home Assistant dependencies.
- Prefer small, typed modules: auth, client, models, exceptions.
- Control writes that hit hardware must validate ranges before send.
- Version bumps are via release-please only (do not hand-edit for releases).
