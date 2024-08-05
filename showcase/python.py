import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.page = None
        self.soup = None

    def fetch_page(self):
        try:
            self.page = requests.get(self.url)
            self.page.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def parse_headings(self):
        headings = self.soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        for heading in headings:
            print(f"{heading.name}: {heading.text.strip()}")

    def parse_links(self):
        links = self.soup.find_all("a", href=True)
        for link in links:
            print(f"Text: {link.text.strip()}, URL: {link['href']}")

    def run(self):
        self.fetch_page()
        print("Headings:")
        self.parse_headings()
        print("\nLinks:")
        self.parse_links()


if __name__ == "__main__":
    url = "https://example.com"
    scraper = WebScraper(url)
    scraper.run()
