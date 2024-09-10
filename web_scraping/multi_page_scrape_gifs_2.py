import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import re

# Custom headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}


def download_gif(session, gif_url, save_dir):
    """
    Downloads a GIF from the given URL and saves it to the specified directory.
    """
    try:
        # Extract the filename from the URL
        parsed_url = urlparse(gif_url)
        gif_filename = os.path.basename(parsed_url.path)

        # Complete path for saving the GIF
        gif_filepath = os.path.join(save_dir, gif_filename)

        # Check if file already exists
        if os.path.exists(gif_filepath):
            print(f"File already exists: {gif_filepath}")
            return

        # Download the content
        response = session.get(
            gif_url, headers=HEADERS, stream=True, allow_redirects=True
        )
        response.raise_for_status()

        # Check the Content-Type
        content_type = response.headers.get("Content-Type", "").lower()
        if "image/gif" not in content_type:
            print(f"Skipping: Content-Type is not 'image/gif'. URL: {gif_url}")
            return

        # Save the content
        with open(gif_filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Downloaded: {gif_filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading GIF {gif_url}: {e}")


def crawl_and_download_gifs(start_url, save_dir):
    """
    Crawls a website starting from the given URL and downloads all GIFs encountered.
    """
    session = requests.Session()
    visited = set()
    to_visit = [start_url]
    gif_pattern = re.compile(r".*\.gif$", re.IGNORECASE)

    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue

        visited.add(url)
        print(f"Visiting: {url}")

        try:
            response = session.get(url, headers=HEADERS)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all GIF images
            for img in soup.find_all("img", src=gif_pattern):
                gif_url = urljoin(url, img["src"])
                download_gif(session, gif_url, save_dir)

            # Find all links
            for link in soup.find_all("a", href=True):
                href = link["href"]
                full_url = urljoin(url, href)
                if full_url.startswith(start_url) and full_url not in visited:
                    to_visit.append(full_url)

            # Be polite and don't hammer the server
            time.sleep(1)

        except requests.exceptions.RequestException as e:
            print(f"Error crawling {url}: {e}")

    print("Crawling completed.")


# Usage
start_url = "https://www.inspireusafoundation.org/"
save_directory = os.path.expanduser("~/exercise-gifs-2")

# Ensure the save directory exists
os.makedirs(save_directory, exist_ok=True)

# Start crawling and downloading
crawl_and_download_gifs(start_url, save_directory)
