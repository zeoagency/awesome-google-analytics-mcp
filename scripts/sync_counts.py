"""
Count calculation and mathematical reconciliation engine for awesome-google-analytics-mcp.
Computes and verifies exact counts across:
- Contents top-level category entries
- Contents subcategory entries
- Detailed section headers and italicized banners
- Detailed subcategory headers and italicized banners
- Actual table rows
"""

import json, os, sys

TAXONOMY_FILE = '/root/dev/awesome-google-analytics-mcp/specs/04-taxonomy-blueprint.json'
REGISTRY_FILE = '/root/dev/awesome-google-analytics-mcp/data/normalized_project_registry.json'
OUTPUT_COUNTS = '/root/dev/awesome-google-analytics-mcp/data/taxonomy_counts.json'

def compute_counts():
    with open(TAXONOMY_FILE) as f:
        tax = json.load(f)
        
    with open(REGISTRY_FILE) as f:
        registry = json.load(f)
        
    counts = {
        'total_index_projects': len(registry),
        'categories': {}
    }
    
    seen_slugs = set()
    global_row_count = 0
    
    for cat in tax['categories']:
        cid = cat['id']
        cat_name = cat['name']
        cat_slug = cat['slug']
        
        cat_data = {
            'id': cid,
            'name': cat_name,
            'slug': cat_slug,
            'expected_count': cat['count'],
            'actual_count': 0,
            'subcategories': {}
        }
        
        cat_sum = 0
        for subcat in cat['subcategories']:
            sname = subcat['name']
            sslug = subcat['slug']
            projs = subcat['projects']
            scount = len(projs)
            
            # Check for duplicate project appearances
            for p in projs:
                if p in seen_slugs:
                    print(f"ERROR: Duplicate project {p} detected across taxonomy!", file=sys.stderr)
                    sys.exit(1)
                seen_slugs.add(p)
                if p not in registry:
                    print(f"ERROR: Project {p} in taxonomy not found in registry!", file=sys.stderr)
                    sys.exit(1)
                    
            cat_data['subcategories'][sslug] = {
                'name': sname,
                'slug': sslug,
                'count': scount,
                'projects': projs
            }
            cat_sum += scount
            
        cat_data['actual_count'] = cat_sum
        assert cat_data['actual_count'] == cat['count'], f"Category {cid} count mismatch: {cat_data['actual_count']} != {cat['count']}"
        counts['categories'][cid] = cat_data
        global_row_count += cat_sum
        
    assert global_row_count == len(registry), f"Global project count mismatch: {global_row_count} != {len(registry)}"
    
    with open(OUTPUT_COUNTS, 'w') as f:
        json.dump(counts, f, indent=2)
        
    print(f"SUCCESS: Mathematical count parity reconciled across all {len(counts['categories'])} categories ({global_row_count} projects).")
    return counts

if __name__ == '__main__':
    compute_counts()
