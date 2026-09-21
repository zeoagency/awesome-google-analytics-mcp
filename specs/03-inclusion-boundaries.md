# Specification: Deterministic Inclusion & Exclusion Boundaries

**Document ID:** `SPEC-GA4-MCP-003`  
**Status:** Authoritative  
**Target Repository:** `/root/dev/awesome-google-analytics-mcp`  

---

## 1. Primary Qualification Criteria

A project qualifies for inclusion in `awesome-google-analytics-mcp` if and only if it satisfies all three primary criteria:

1. **Explicit Google Analytics Technical Target**:
   - Must interact directly with official Google Analytics APIs:
     - GA4 Data API v1beta (`runReport`, `batchRunReports`, `runPivotReport`)
     - GA4 Realtime API (`runRealtimeReport`)
     - GA4 Funnel API v1alpha (`runFunnelReport`)
     - GA4 Admin API v1beta (`accounts`, `properties`, `dataStreams`, `customDimensions`, `customMetrics`)
     - GA4 Measurement Protocol v2 (`/mp/collect`, `/debug/mp/collect`)
     - Direct BigQuery GA4 Event Export queries (`analytics_XXXXXXXXX.events_*`)
2. **Model Context Protocol (MCP) or Autonomous Agent Interface**:
   - Must expose tools, resources, or prompts conforming to the Model Context Protocol (via `stdio`, `sse`, or `streamable-http`) or provide a structured agent skill/adapter explicitly driving GA4 for an LLM runtime.
3. **Public, Verifiable Implementation**:
   - Must have an accessible source repository containing verifiable code, or a published package on PyPI, npm, Docker Hub, or Crates.io.

---

## 2. Boundary Edge-Case Policies

### 2.1 Multi-Service Marketing Suites (GA4 + GSC + Ads + GTM)

- **Policy**: Qualifies **only if** GA4 is a first-class, verified subsystem with dedicated tools, rather than a generic pass-through.
- **Classification**: Placed in Category 3 (*Multi-Platform Marketing Intelligence & Attribution*).
- **Description Rule**: Description must clearly state that it unifies GA4 with complementary platforms (e.g. Google Search Console or Google Ads).

### 2.2 BigQuery-Only Consumers

- **Policy**: Generic BigQuery MCP servers with no built-in GA4 awareness are **strictly excluded**.
- **Exception**: Tools that include pre-built GA4 event schema mappings, session unnesting models, or conversion attribution templates specifically for `events_*` tables qualify as supporting analytics infrastructure.

### 2.3 Universal Analytics (UA / GA3) Legacy Repositories

- **Policy**: Repositories exclusively targeting deprecated Universal Analytics endpoints (`analytics:v3` or `analyticsreporting:v4`) without GA4 Data API support are **strictly excluded**.
- **Exception**: Dual-compatibility servers supporting both GA4 and legacy UA qualify, but must be explicitly documented with their legacy support flags.

### 2.4 Forks, Mirrors, and Clones

- **Policy**: Direct forks or 1-commit mirrors of official or popular community repositories are **excluded** to prevent index inflation.
- **Canonical Selection Rule**: The original upstream repository is cataloged. A fork is eligible *only* if it introduces substantial, code-verified architectural features (e.g. adding local DuckDB ingestion, OAuth PKCE, or Dockerization).

### 2.5 Disposable AI Stock & Abandoned Stubs

- **Policy**: Repositories containing only uncurated boilerplate without working tool registrations, broken dependencies, or empty directories are excluded.
- **Quarantine Domain**: Incomplete but technically instructive experiments, prototypes, or early architecture designs are quarantined in Category 7 (*Scaffolds, Setup Templates & Experimental Concepts*).

### 2.6 Unsupported Claims

- **Policy**: Capabilities claimed in READMEs that are refuted by AST source-code inspection (e.g., claiming Measurement Protocol event write-back when code only calls `runReport`) are stripped from descriptions and marked as absent in the comparison matrix.
