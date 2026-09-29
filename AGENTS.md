# Repository operating rules

- Read `.github/copilot-instructions.md` and relevant scoped instructions
  before changing code.
- Search for existing contracts and tests before introducing architecture
  components. Do not create speculative engine/OS/domain directories or
  registries.
- Keep changes compatible with the existing Python package and preserve
  historical behavior and raw evidence.
- Run the existing tests from the repository root:
  `python -m unittest discover -s tests -v`.
- No separate configured linter, build, database migration, or application
  launch command currently exists. Do not claim those checks ran.
- Update relevant architecture documentation when changing system contracts.
