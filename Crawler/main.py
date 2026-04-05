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
    #for page in craw.values(): #this shit is broken cause page is none well its not broken if u don't limit pages so something fucky example if site has 32 links and u limit it to 32 it works fine but limit it to 31 and u get 2 of the 31 links in this test case
     #   if page is None: continue #this needs to not be here for pending to work tho since it skips none wish is what becomes pending
      #  print(page["url"] if page else "pending") # this makes it say pending instead of nothing wish is bad? good?
    print(len(craw))
    #could not all this be done inside crawl.py ?_?
    write_json_report(craw)

    #for page in craw.values():
     #   if page: print(page["url"])
# the code above sends the links found but since print gives them when found I don't see the point of also getting a copy at the end


if __name__ == "__main__":
    #main()
    asyncio.run(main_async())