import sys, asyncio
from crawl import crawl_site_async

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
    for page in craw.values():
        if page is None: continue
        print(page["url"])
    print(len(craw))



    #for page in craw.values():
     #   if page: print(page["url"])
# the code above sends the links found but since print gives them when found I don't see the point of also getting a copy at the end


if __name__ == "__main__":
    #main()
    asyncio.run(main_async())