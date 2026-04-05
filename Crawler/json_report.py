import json

def write_json_report(page_data, filename="report.json"):
    pages = sorted([p for p in page_data.values() if p is not None], key=lambda p: p["url"])
    json.dump(pages, open(filename, "w"), indent=2)