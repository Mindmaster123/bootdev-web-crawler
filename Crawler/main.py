import sys, asyncio
from crawl import crawl_site_async
from json_report import write_json_report

async def main_async():
    if len(sys.argv) < 4:
        print("no website provided or wrong number of arguments")
        sys.exit(1)
    if len(sys.argv) > 4:
        print("too many arguments provided")
        sys.exit(1)
    if len(sys.argv) == 2:
        print(f"starting crawl of: {sys.argv[1]}")
    #craw = crawl_page(sys.argv[1])
    max_concurrency = int(sys.argv[2])
    max_pages = int(sys.argv[3])
    craw = await crawl_site_async(sys.argv[1], max_concurrency, max_pages)
    print(len(craw))
    write_json_report(craw)

if __name__ == "__main__":
    asyncio.run(main_async())