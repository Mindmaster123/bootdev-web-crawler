# Web Scraper

Built as part of the [Boot.dev Web Scraper course](https://www.boot.dev/courses/build-web-scraper-python).

## Requirements

- Python 3.x
- [uv](https://github.com/astral-sh/uv)

## Setup

uv sync

## Usage

uv run main.py <base_url> <max_concurrency> <max_pages>

## Example

uv run main.py "https://wagslane.dev" 4 32
