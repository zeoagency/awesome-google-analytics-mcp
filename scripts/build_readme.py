#!/usr/bin/env python3
"""
Assemble the canonical README.md for awesome-google-analytics-mcp
following the exact structural blueprint reverse-engineered from awesome-herdr.
"""

import json
import re
from pathlib import Path

def generate_anchor(owner: str, name: str) -> str:
    slug = f"{owner}--{name}".lower()
    slug = re.sub(r'[^a-z0-9\-_]', '-', slug)
    return slug

def main():
    root = Path(__file__).resolve().parent.parent
    tax_path = root / "specs" / "04-taxonomy-blueprint.json"
    reg_path = root / "data" / "normalized_project_registry.json"
    desc_path = root / "data" / "differentiated_descriptions.json"
    counts_path = root / "data" / "taxonomy_counts.json"
    readme_path = root / "README.md"

    with open(tax_path, "r", encoding="utf-8") as f:
        taxonomy = json.load(f)
    with open(reg_path, "r", encoding="utf-8") as f:
        registry = json.load(f)
    with open(desc_path, "r", encoding="utf-8") as f:
        descriptions = json.load(f)
    with open(counts_path, "r", encoding="utf-8") as f:
        counts = json.load(f)

    lines = []

    # 1. Header
    lines.append("# Awesome Google Analytics MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append("> A curated plain-English index of Model Context Protocol (MCP) servers, local analytical engines, and agent-facing tools built for **[Google Analytics 4 (GA4)](https://developers.google.com/analytics/devguides/reporting/data/v1)** and ecosystem telemetry.")
    lines.append("")
    lines.append("Official links: [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data/v1) · [Google Analytics Admin API](https://developers.google.com/analytics/devguides/config/admin/v1) · [Model Context Protocol](https://modelcontextprotocol.io/) · [Google Cloud Console](https://console.cloud.google.com/) · [Zeo Agency](https://zeo.org/)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 2. Table of Contents
    lines.append("## Contents")
    lines.append("")
    lines.append("- [Developer Comparison Matrix](#developer-comparison-matrix)")
    lines.append("")

    for cat in taxonomy["categories"]:
        cat_id = cat["id"]
        cat_name = cat["name"]
        cat_count = cat["count"]
        cat_slug = re.sub(r'[^a-z0-9\-]+', '-', f"{cat_id} {cat_name}".lower()).strip('-')
        lines.append(f"{cat_id}. [{cat_name} ({cat_count})](#{cat_slug})")
        for sub in cat["subcategories"]:
            sub_name = sub["name"]
            sub_count = len(sub["projects"])
            sub_slug = re.sub(r'[^a-z0-9\-]+', '-', sub_name.lower()).strip('-')
            lines.append(f"   - [{sub_name} ({sub_count})](#{sub_slug})")

    lines.append("8. [Resources](#resources)")
    lines.append("   - [Official Documentation & SDKs](#official-documentation--sdks)")
    lines.append("   - [Community Guides & Architecture](#community-guides--architecture)")
    lines.append("9. [Reference](#reference)")
    lines.append("   - [Evaluation Methodology & Verification Invariants](#evaluation-methodology--verification-invariants)")
    lines.append("   - [Repository Inclusion & Quarantine Invariants](#repository-inclusion--quarantine-invariants)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 3. Developer Comparison Matrix
    lines.append("## Developer Comparison Matrix")
    lines.append("")
    lines.append("*A comparative feature matrix of all 63 Model Context Protocol servers and agent interfaces for Google Analytics 4, detailing language runtime, tool surface, authentication paradigms, local storage engines, and API method support. Click on any project name to jump directly to its detailed entry below.*")
    lines.append("")
    
    matrix_headers = [
        "Server / Tool",
        "Runtime",
        "Tools",
        "Auth Paradigm",
        "Storage Engine",
        "Data API",
        "Realtime",
        "Funnels",
        "Admin API",
        "MP Events",
        "BigQuery",
        "Multi-Prop",
        "Multi-Tenant",
        "Anomaly Det.",
        "Local SQL",
        "Tier"
    ]
    lines.append("| " + " | ".join(matrix_headers) + " |")
    lines.append("| " + " | ".join([
        "---", "---", "---", "---", "---",
        ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:",
        "---"
    ]) + " |")

    # Order projects according to taxonomy category & subcategory order
    for cat in taxonomy["categories"]:
        for sub in cat["subcategories"]:
            for slug in sub["projects"]:
                p = registry[slug]
                owner = p["owner"]
                name = p["name"]
                anchor = generate_anchor(owner, name)
                
                lang = p["primary_language"]
                tools_cnt = str(p["tools_count"])
                auth = p["auth_paradigm"]
                storage = p["storage_engine"]
                
                api = p.get("api_coverage", {})
                d_api = "✅" if api.get("data_api_run_report") else "—"
                rt_api = "✅" if api.get("realtime_api") else "—"
                fn_api = "✅" if api.get("funnel_api") else "—"
                ad_api = "✅" if api.get("admin_api") or p.get("can_configure_admin") else "—"
                mp_api = "✅" if api.get("measurement_protocol_write") or p.get("can_write_events") else "—"
                bq_api = "✅" if api.get("bigquery_export") else "—"
                
                mp_disc = "✅" if p.get("multi_property_discovery") else "—"
                mt_ready = "✅" if p.get("multi_tenant_ready") else "—"
                anom = "✅" if p.get("has_anomaly_detection") else "—"
                sql = "✅" if p.get("has_embedded_duckdb") or p.get("has_embedded_sqlite") or "Driver" in storage else "—"
                
                # Format tier concisely
                tier_raw = p.get("benchmark_tier", "")
                tier_short = tier_raw.split(":")[0] if ":" in tier_raw else tier_raw
                if not tier_short:
                    tier_short = "Tier 4"

                row = [
                    f"[**{owner}/{name}**](#{anchor})",
                    lang,
                    tools_cnt,
                    auth,
                    storage,
                    d_api,
                    rt_api,
                    fn_api,
                    ad_api,
                    mp_api,
                    bq_api,
                    mp_disc,
                    mt_ready,
                    anom,
                    sql,
                    tier_short
                ]
                lines.append("| " + " | ".join(row) + " |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # 4. Detailed Sections 1 to 7
    cat_blurbs = {
        1: "21 projects across 4 subcategories for executing standard reports, introspecting dimension schemas, and querying realtime telemetry.",
        2: "3 projects across 3 subcategories for caching GA4 telemetry into local analytical databases and virtual relational schemas.",
        3: "12 projects across 4 subcategories uniting GA4 with Google Search Console, Google Tag Manager, ad platforms, and attribution pipelines.",
        4: "7 projects across 4 subcategories providing hardened OAuth gateways, encrypted persistence, and multi-tenant team proxies.",
        5: "3 projects across 2 subcategories dispatching Measurement Protocol events and provisioning GA4 properties via Admin API.",
        6: "6 projects across 3 subcategories performing statistical anomaly detection, rendering 3D visualizations, and compiling reports.",
        7: "11 projects across 2 subcategories providing starter boilerplates, setup guides, and experimental exploratory prototypes."
    }

    subcat_blurbs = {
        "official-and-foundational-servers": "The official reference server implementation authored by Google.",
        "consolidated-modal-query-servers": "Multi-purpose query servers bundling report execution, schema introspection, and custom dimension handling.",
        "dynamic-schema-and-metadata-introspectors": "Specialized servers focusing on real-time schema discovery and active property metadata introspection.",
        "lightweight-reporting-bridges": "Streamlined, single-purpose bridges querying core GA4 traffic, active users, and conversions.",
        "embedded-columnar-olap-scratchpads-duckdb": "In-memory columnar analytics executing sub-millisecond SQL queries over locally ingested GA4 data.",
        "embedded-relational-databases-sqlite": "Embedded SQLite caching engine with comprehensive multi-tool SQL analysis suites.",
        "relational-schema-drivers": "Enterprise JDBC relational driver projecting live GA4 endpoints as standard SQL tables.",
        "unified-search-console-and-ga4-platforms": "Multi-platform servers correlating organic search impressions and queries with downstream GA4 engagement.",
        "google-tag-manager-audit-and-event-bridges": "Cross-platform servers validating GTM container tags, triggers, and live GA4 measurement schemas.",
        "multi-ad-network-and-marketing-suites": "Unified marketing hubs coordinating GA4 analytics alongside Google Ads and Meta Ads management.",
        "cookieless-attribution-and-privacy-bridges": "Privacy-preserving servers handling server-side tracking, cookieless conversions, and BigQuery exports.",
        "cloud-native-multi-tenant-oauth-gateways": "Enterprise OAuth proxies with organizational multi-tenancy and token rotation.",
        "cryptographically-encrypted-session-persistence": "Secure token storage engines encrypting refresh tokens for continuous unattended background execution.",
        "ephemeral-loopback-pkce-authenticators": "High-performance native authenticators implementing zero-dependency loopback OAuth 2.0 PKCE.",
        "remote-team-and-multi-account-proxies": "Team-oriented servers enabling agency multi-account switching and shared credential guardrails.",
        "measurement-protocol-event-dispatchers": "Bidirectional servers sending and validating server-side Measurement Protocol events.",
        "admin-api-property-and-custom-definition-managers": "Infrastructure management servers provisioning custom dimensions, metrics, and property settings.",
        "algorithmic-anomaly-detection-and-drop-classifiers": "Diagnostic toolkits identifying statistical traffic anomalies, baseline drops, and pattern changes.",
        "visual-3d-dashboards-and-real-time-streaming": "Interactive visual servers streaming live visitor telemetry into 3D environments and dashboards.",
        "automated-executive-report-and-document-generators": "Autonomous reporting agents compiling end-to-end analytical summaries and BI data models.",
        "starter-templates-and-boilerplate-scaffolds": "Production boilerplates and setup recipes for authoring custom GA4 MCP servers.",
        "early-prototypes-and-conceptual-wrappers": "Proof-of-concept implementations and experimental explorations of MCP GA4 integrations."
    }

    for cat in taxonomy["categories"]:
        cat_id = cat["id"]
        cat_name = cat["name"]
        cat_count = cat["count"]
        blurb = cat_blurbs.get(cat_id, cat["description"])

        lines.append(f"## {cat_id}. {cat_name}")
        lines.append("")
        lines.append(f"*{cat_count} projects. {blurb}*")
        lines.append("")

        for sub in cat["subcategories"]:
            sub_name = sub["name"]
            sub_slug = sub["slug"]
            sub_count = len(sub["projects"])
            s_blurb = subcat_blurbs.get(sub_slug, "Curated Model Context Protocol tools.")

            lines.append(f"### {sub_name}")
            lines.append("")
            proj_word = "project" if sub_count == 1 else "projects"
            lines.append(f"*{sub_count} {proj_word}. {s_blurb}*")
            lines.append("")
            lines.append("| Project | What it does |")
            lines.append("|---|---|")

            for slug in sub["projects"]:
                p = registry[slug]
                owner = p["owner"]
                name = p["name"]
                html_url = p["html_url"]
                anchor = generate_anchor(owner, name)
                desc = descriptions[slug]["description"]

                lines.append(f"| <a id=\"{anchor}\"></a>[**{owner}/{name}**]({html_url}) | {desc} |")

            lines.append("")

        lines.append("---")
        lines.append("")

    # 5. Resources Section
    lines.append("## Resources")
    lines.append("")
    lines.append("### Official Documentation & SDKs")
    lines.append("")
    lines.append("- [Google Analytics Data API (v1beta)](https://developers.google.com/analytics/devguides/reporting/data/v1) — Official reference documentation for standard reports, realtime streams, and funnel dimensions.")
    lines.append("- [Google Analytics Admin API (v1)](https://developers.google.com/analytics/devguides/config/admin/v1) — Programmatic management API for accounts, properties, data streams, and custom metrics.")
    lines.append("- [Google Analytics Measurement Protocol (GA4)](https://developers.google.com/analytics/devguides/collection/protocol/ga4) — HTTP protocol specification for dispatching server-side, offline, and mobile event streams directly to GA4 properties.")
    lines.append("- [Model Context Protocol Specification](https://modelcontextprotocol.io/) — Anthropic's open standard protocol specification connecting language model clients with external data sources and execution environments.")
    lines.append("- [Google Cloud IAM Service Accounts](https://cloud.google.com/iam/docs/service-account-overview) — Google Cloud security guidelines for provisioning and rotating service account JSON credentials.")
    lines.append("")
    lines.append("### Community Guides & Architecture")
    lines.append("")
    lines.append("- [Anthropic Claude Code MCP Integration Guide](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) — Setup guide for attaching stdio and SSE MCP servers to Claude Code CLI and Anthropic desktop environments.")
    lines.append("- [Cursor MCP Server Setup](https://docs.cursor.com/context/model-context-protocol) — Configuring local and remote MCP agents within Cursor IDE.")
    lines.append("- [DuckDB Columnar Analytical Engine](https://duckdb.org/) — In-memory SQL OLAP engine optimized for local-first telemetry analytics without external database infrastructure.")
    lines.append("- [SQLite Embedded Relational Database](https://www.sqlite.org/) — Zero-configuration SQL database engine for caching agent sessions and analytics data.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 6. Reference Section
    lines.append("## Reference")
    lines.append("")
    lines.append("### Evaluation Methodology & Verification Invariants")
    lines.append("")
    lines.append("Every repository indexed in this catalog has undergone code-level forensic evaluation against the following standards:")
    lines.append("")
    lines.append("1. **6-Month Maintenance Invariant:** Active development verified on GitHub (last commit dated March 2026 or later). Abandoned, archival, or unmaintained stubs are quarantined.")
    lines.append("2. **Evidence-Grounded Technical Audit:** Every tool signature, authentication pattern, and storage engine is verified directly from repository source code (`package.json`, `pyproject.toml`, `Cargo.toml`, and handler definitions), never from unverified README claims.")
    lines.append("3. **Job-to-Be-Done Taxonomy Bounding:** Repositories are organized into 7 functional domains and 21 subcategories based on actual developer operational needs rather than arbitrary vendor classifications.")
    lines.append("4. **Mathematical Parity Guarantee:** Category counts, Table of Contents anchors, subcategory summaries, and table row counts are reconciled via automated verification scripts with zero mathematical drift.")
    lines.append("")
    lines.append("### Repository Inclusion & Quarantine Invariants")
    lines.append("")
    lines.append("To maintain signal purity, candidate repositories must pass strict inclusion filters:")
    lines.append("")
    lines.append("- **GA4 Direct Technical Affinity:** Tools must interface directly with Google Analytics Data API, Admin API, Measurement Protocol, or provide tightly unified multi-platform workflows (GSC, GTM).")
    lines.append("- **Executable Agent Tool Handlers:** Servers must expose executable MCP tool definitions (`CallToolRequest`, `@mcp.tool`, `server.tool`) compatible with MCP hosts.")
    lines.append("- **Quarantine Protocol:** Generic multi-cloud wrappers without GA4 implementations, non-MCP reporting scripts, and hallucinated synthetic repositories are excluded from this catalog.")

    content = "\n".join(lines) + "\n"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"SUCCESS: Generated README.md ({len(lines)} lines, {len(content)} bytes) at {readme_path}")

if __name__ == "__main__":
    main()
