## 1. Document the convention in methodology

- [x] 1.1 Add a **File Naming** section to `docs/methodology.md` covering the `responses/` pattern (`<platform>-<prompt-type>.md`), the `search_logs/` pattern (`<platform>.md`), allowed characters, the `vs` join for comparisons, the scope-descriptor variant for broad discovery sessions, and the overwrite-with-git-history policy

## 2. Sync specs and update prompt usage headers

- [x] 2.1 Create `openspec/specs/output-file-naming/spec.md` with the synced requirements from the delta spec
- [x] 2.2 Sync delta spec: merge the new requirement into `openspec/specs/platform-discovery-prompt/spec.md`
- [x] 2.3 Sync delta spec: merge the new requirement into `openspec/specs/platform-comparison-prompt/spec.md`
- [x] 2.4 Sync delta spec: merge the new requirement into `openspec/specs/license-analysis-prompt/spec.md`
- [x] 2.5 Add save-as filename instruction to `prompts/platform-discovery.md` usage header — pattern `responses/<platform>-discovery.md` with scope-descriptor variant example
- [x] 2.6 Add save-as filename instruction to `prompts/platform-comparison.md` usage header — pattern `responses/<platform-a>-vs-<platform-b>-comparison.md`
- [x] 2.7 Add save-as filename instruction to `prompts/license-analysis.md` usage header — pattern `responses/<platform>-license.md`
