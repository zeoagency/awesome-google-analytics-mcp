# ankhangonline/mcp-ga4-team-server

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/ankhangonline/mcp-ga4-team-server) · [JSON](../../data/mcps/ankhangonline--mcp-ga4-team-server.json)

**1 tools:** 1 GA4, 0 other-service or server-support tools. Reviewed source: [`f7c3a3bc8961`](https://github.com/ankhangonline/mcp-ga4-team-server/tree/f7c3a3bc89610f3cf261d7aa9f637d488506d73c).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution, dependency installation or live/authenticated requests. Git HEAD matches the supplied revision.
- Registration is unconditional and contains exactly one tool; OAuth metadata/registration and SSE/message Express endpoints are not MCP tools.
- Token must arrive as a capitalized Bearer authorization header on the tool request. Google OAuth registration uses GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET environment values; PUBLIC_URL and PORT configure hosting.
- One global SSE transport is overwritten on each /sse connection and used for all /messages requests, so concurrent sessions are not isolated by this source.
- /oauth/register returns the configured Google client secret to callers without authentication in the source.
- Dockerfile uses Node 20 and directly runs index.js; package-lock pins MCP SDK 1.29.0. No definite installation blocker was established by source inspection.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`get_team_ga4_report`](#get_team_ga4_report) | GA4 | read |

## get_team_ga4_report

Reads a Bearer token from requestInfo headers, strips a properties/ prefix from propertyId, converts comma-separated metrics and dimensions into GA4 name arrays, builds one or two date ranges, optional orderBys, limit and AND-combined dimension/string or metric/numeric filters, and POSTs to <https://analyticsdata.googleapis.com/v1beta/properties/{propertyId}:runReport>. Returns the complete API response as formatted JSON text or an error text result.

<details>
<summary>Full registered description</summary>

```text
Lấy báo cáo dữ liệu phân tích từ Google Analytics 4
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `metrics` | No | string | Not declared |
| `dimensions` | No | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `compareStartDate` | No | string | Not declared |
| `compareEndDate` | No | string | Not declared |
| `orderBy` | No | string | Not declared |
| `limit` | No | number | Not declared |
| `dimensionFilter` | No | string | Not declared |
| `metricFilter` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "ID tài sản GA4 của bạn (chỉ gồm các chữ số, ví dụ: 123456789)"
    },
    "metrics": {
      "type": "string",
      "description": "Các chỉ số cần lấy, phân cách bằng dấu phẩy. Ví dụ: activeUsers,screenPageViews,sessions,conversions"
    },
    "dimensions": {
      "type": "string",
      "description": "Các chiều dữ liệu phân tích, phân cách bằng dấu phẩy. Ví dụ: date,country,sessionSource,sessionMedium"
    },
    "startDate": {
      "type": "string",
      "description": "Ngày bắt đầu, định dạng YYYY-MM-DD hoặc relative như '30daysAgo', 'yesterday' (Mặc định: 30daysAgo)"
    },
    "endDate": {
      "type": "string",
      "description": "Ngày kết thúc, định dạng YYYY-MM-DD hoặc 'today' (Mặc định: today)"
    },
    "compareStartDate": {
      "type": "string",
      "description": "(Tùy chọn) Ngày bắt đầu của kỳ so sánh, dùng khi cần đối chiếu 2 khoảng thời gian. Khi dùng phải có cả compareEndDate. Kết quả trả về sẽ có thêm cột 'dateRange' (date_range_0 = kỳ chính, date_range_1 = kỳ so sánh)"
    },
    "compareEndDate": {
      "type": "string",
      "description": "(Tùy chọn) Ngày kết thúc của kỳ so sánh, đi kèm compareStartDate"
    },
    "orderBy": {
      "type": "string",
      "description": "(Tùy chọn) Sắp xếp kết quả theo 1 metric hoặc dimension, định dạng '<tên> asc|desc'. Ví dụ: 'sessions desc'. Dùng kèm limit để lấy top N"
    },
    "limit": {
      "type": "number",
      "description": "(Tùy chọn) Giới hạn số dòng trả về, dùng cho truy vấn kiểu 'top N'. Ví dụ: 10"
    },
    "dimensionFilter": {
      "type": "string",
      "description": "(Tùy chọn) Lọc theo dimension (dạng chuỗi), định dạng '<tên>:<eq|contains|begins|ends>:<giá trị>'. Nhiều điều kiện cách nhau bằng dấu phẩy (các điều kiện được AND với nhau). Ví dụ: 'sessionSource:contains:facebook'"
    },
    "metricFilter": {
      "type": "string",
      "description": "(Tùy chọn) Lọc theo metric (dạng số), định dạng '<tên>:<eq|gt|gte|lt|lte>:<giá trị>'. Nhiều điều kiện cách nhau bằng dấu phẩy (AND). Ví dụ: 'conversions:gt:0'"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- Only propertyId is schema-required. No additionalProperties restriction, nested schemas, enums, format constraints or JSON Schema defaults are declared; filter syntax and examples are description text only.
- Handler defaults metrics to activeUsers,screenPageViews,sessions, dimensions to date, startDate to 30daysAgo and endDate to today when values are falsy.
- Comparison date range is included only when both compareStartDate and compareEndDate are truthy; a single comparison endpoint is silently ignored.
- orderBy is interpreted as metric sorting only if its name appears in requested metrics, otherwise dimension sorting; only desc selects descending order. limit is forwarded only when truthy, with no positivity or integer validation.
- Filters split on commas and AND multiple conditions. Unknown dimension operators default to EXACT and unknown metric operators default to EQUAL; metric values are parsed with parseFloat without validation.
- Missing Bearer token returns isError. Input parsing, propertyId.startsWith and filter building occur outside the try/catch, so malformed arguments can throw directly.

Source: [index.js:37](https://github.com/ankhangonline/mcp-ga4-team-server/blob/f7c3a3bc89610f3cf261d7aa9f637d488506d73c/index.js#L37-L63) · [index.js:65](https://github.com/ankhangonline/mcp-ga4-team-server/blob/f7c3a3bc89610f3cf261d7aa9f637d488506d73c/index.js#L65-L164).
