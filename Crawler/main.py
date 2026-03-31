import sys
from crawl import crawl_page

def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)
    if len(sys.argv) == 2:
        print(f"starting crawl of: {sys.argv[1]}")
    craw = crawl_page(sys.argv[1])
    print(len(craw))
    for page in craw.values():
        if page: print(page["url"])

if __name__ == "__main__":
    main()
