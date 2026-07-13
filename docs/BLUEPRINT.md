
# Blueprint checklist (Python library)

- [ ] `src/<pkg>/` layout + `py.typed`
- [ ] Async public API; sync wrappers only if truly needed
- [ ] Exception taxonomy mapped cleanly by HA (`AuthError` → reauth)
- [ ] Injected HTTP session
- [ ] Multi-version CI (3.12 / 3.13+)
- [ ] release-please + PyPI trusted publishing
- [ ] Exact version pin from the companion HA integration
- [ ] Changelog from conventional commits
- [ ] Optional: cassette-based tests for live HTTP (VCR / respx / aioresponses)
