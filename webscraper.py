import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    # Specify the URL to scrape
    url = 'http://quotes.toscrape.com'
    
    # Make a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        # Extract information from the HTML
        quotes = []
        for quote in soup.find_all('span', class_='text'):
            quotes.append(quote.get_text())

        authors = []
        for author in soup.find_all('small', class_='author'):
            authors.append(author.get_text())

        # Print the scraped data
        for i in range(len(quotes)):
            print(f"{authors[i]}: {quotes[i]}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_quotes()