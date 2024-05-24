# HypercrawlTurbo

HypercrawlTurbo is a turbocharged web scraper for extracting URLs from a webpage.

## Installation

You can install HypercrawlTurbo via pip:

```bash
pip install hypercrawlturbo

Usage
HyperCrawl Turbo
​
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
​
​
​
HyperCrawl 
​
from hypercrawl import DomainScraper
​
# Define the target domain
domain = "http://example.com"  # Replace with your target domain
​
# Create a DomainScraper instance with optional parameters
scraper = DomainScraper(domain, max_concurrency=100, request_timeout=10)
​
# Get all URLs within the specified domain
urls = scraper.get_all_urls()
​
# Print the found URLs
print(f"All URLs found in the domain {domain}:")
for url in urls:
    print(url)
​
