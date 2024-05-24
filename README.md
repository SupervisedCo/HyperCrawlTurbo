# HypercrawlTurbo

HypercrawlTurbo is a turbocharged web scraper for extracting URLs from a webpage.

## Documentations

Read complete documentations here : https://hyperllm.gitbook.io/hypercrawl/

# Pip & Installation

Read more here : https://pypi.org/project/hypercrawlturbo/

## Installation

You can install HypercrawlTurbo via pip:

```bash
pip install hypercrawlturbo
```


## Usage

```bash
from hypercrawlturbo import scraper
​
# Define the URL of the webpage to scrape
url_to_scrape = "https://example.com"
​
# Call the scrape_urls function and pass in the URL
extracted_urls = scraper.scrape_urls(url_to_scrape)
​
# Process the extracted URLs
for url in extracted_urls:
    print(url)
    # Here you can perform further processing on each URL, such as visiting it or storing it in a database
```​
​
for url in urls:
    print(url)
​
