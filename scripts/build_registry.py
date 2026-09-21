import json, glob, os, yaml

DOSSIERS_DIR = '/root/dev/research/google-analytics-mcps/dossiers'
BENCHMARK_DIR = '/root/dev/research/google-analytics-mcps/benchmark'
TAXONOMY_FILE = '/root/dev/awesome-google-analytics-mcp/specs/04-taxonomy-blueprint.json'

with open(TAXONOMY_FILE) as f:
    tax = json.load(f)

# Build slug to taxonomy mapping
slug_to_cat = {}
for cat in tax['categories']:
    for subcat in cat['subcategories']:
        for p in subcat['projects']:
            slug_to_cat[p] = {
                'category_id': cat['id'],
                'category_name': cat['name'],
                'category_slug': cat['slug'],
                'subcategory_name': subcat['name'],
                'subcategory_slug': subcat['slug']
            }

with open(os.path.join(BENCHMARK_DIR, 'overall_benchmark.json')) as f:
    overall = json.load(f)

rankings_by_slug = {r['repo_slug']: r for r in overall['rankings']}

registry = {}
yaml_files = sorted(glob.glob(os.path.join(DOSSIERS_DIR, '*.yaml')))

for yf in yaml_files:
    slug = os.path.basename(yf)[:-5]
    with open(yf) as fp:
        y = yaml.safe_load(fp)
    md_path = yf[:-5] + '.md'
    with open(md_path) as fp:
        md_text = fp.read()
        
    bench = rankings_by_slug.get(slug, {})
    tax_info = slug_to_cat.get(slug, {})
    
    tools = y.get('tools', [])
    auth_methods = y.get('auth_methods', [])
    api_cov = y.get('ga4_api_coverage', {})
    
    # Determine capabilities
    has_duckdb = y.get('has_embedded_duckdb', False)
    has_sqlite = y.get('has_embedded_sqlite', False)
    has_cdata = 'cdata' in slug.lower()
    
    storage_type = "Stateless Proxy"
    if has_duckdb:
        storage_type = "Embedded DuckDB OLAP"
    elif has_sqlite:
        storage_type = "Embedded SQLite DB"
    elif has_cdata:
        storage_type = "Virtual Relational Driver"
        
    is_write = any(x in ' '.join(tools).lower() for x in ['send', 'track', 'collect', 'create', 'update', 'mp'])
    has_mp = 'leonardosepulvedat' in slug or any('collect' in t or 'send_event' in t for t in tools)
    
    auth_type = "Service Account"
    if any('oauth' in a.lower() for a in auth_methods) and any('service' in a.lower() for a in auth_methods):
        auth_type = "Dual (SA + OAuth PKCE)"
    elif any('oauth' in a.lower() for a in auth_methods):
        auth_type = "OAuth 2.0 PKCE"
        
    registry[slug] = {
        'repo_slug': slug,
        'repository': y.get('repository', slug),
        'owner': y.get('owner'),
        'name': y.get('name'),
        'html_url': y.get('html_url', f"https://github.com/{y.get('repository', slug)}"),
        'description': y.get('description', ''),
        'primary_language': y.get('primary_language', 'Python'),
        'stars': y.get('stars', 0),
        'commits': y.get('total_commits', 0),
        'last_commit_date': y.get('last_commit_date'),
        'developer_era': y.get('developer_era', ''),
        'quality_verdict': y.get('quality_verdict', ''),
        'benchmark_rank': bench.get('rank', 99),
        'benchmark_tier': bench.get('tier', 'Solid / Functional Community Baseline'),
        'overall_score_pct': bench.get('overall_score_percentage', 50.0),
        'overall_score_5pt': bench.get('overall_score_5pt', 2.5),
        'category_id': tax_info.get('category_id', 1),
        'category_name': tax_info.get('category_name', ''),
        'category_slug': tax_info.get('category_slug', ''),
        'subcategory_name': tax_info.get('subcategory_name', ''),
        'subcategory_slug': tax_info.get('subcategory_slug', ''),
        'tools_count': y.get('tool_count', len(tools)),
        'tools': tools,
        'auth_methods': auth_methods,
        'auth_paradigm': auth_type,
        'storage_mode': y.get('storage_mode', 'Direct Stateless API Proxy'),
        'storage_engine': storage_type,
        'has_embedded_duckdb': has_duckdb,
        'has_embedded_sqlite': has_sqlite,
        'has_cookie_extraction': y.get('has_cookie_extraction', False),
        'api_coverage': {
            'data_api_run_report': api_cov.get('data_api_run_report', True),
            'realtime_api': api_cov.get('data_api_realtime_report', False),
            'funnel_api': 'arcbaslow' in slug or 'sednalabs' in slug or 'funnel' in ' '.join(tools).lower(),
            'admin_api': api_cov.get('admin_api_properties', False) or any('list' in t or 'prop' in t for t in tools),
            'measurement_protocol_write': has_mp,
            'bigquery_export': 'henkisdabro' in slug or 'powerbi' in slug or 'bigquery' in md_text.lower()
        },
        'read_only': not is_write,
        'can_write_events': has_mp,
        'can_configure_admin': any(x in ' '.join(tools).lower() for x in ['create', 'update']) or 'codechap' in slug or 'arcbaslow' in slug,
        'multi_property_discovery': any('list' in t or 'prop' in t for t in tools) or 'dhawalshah' in slug or 'surendranb' in slug,
        'multi_tenant_ready': any(k in slug for k in ['dhawalshah', 'esgee-0562', 'minholi', 'gomarble']),
        'has_anomaly_detection': 'mario-hernandez' in slug or 'arcbaslow' in slug or 'onionst' in slug,
        'has_exporters': 'arcbaslow' in slug or 'thetechbasket' in slug or 'powerbi' in slug or 'sednalabs' in slug
    }

output_path = '/root/dev/awesome-google-analytics-mcp/data/normalized_project_registry.json'
with open(output_path, 'w') as f:
    json.dump(registry, f, indent=2)

print(f"Successfully compiled normalized project registry with {len(registry)} repositories to {output_path}")
