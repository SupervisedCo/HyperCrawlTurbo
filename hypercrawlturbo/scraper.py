import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_urls(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all anchor tags <a> which contain href attribute
        links = soup.find_all('a', href=True)
        
        # Extract URLs and store them in a list
        urls_list = []
        for link in links:
            href = link['href']
            # Join the relative URL with the base URL
            absolute_url = urljoin(url, href)
            urls_list.append(absolute_url)
        
        # Return the list of URLs
        return urls_list
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

# Example usage:
# urls = scrape_urls("https://example.com")
# print(urls)
