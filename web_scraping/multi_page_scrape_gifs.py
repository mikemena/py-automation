import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

# Custom headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}

# List of URLs to exclude from crawling
exclude_urls = [
    "https://newlife.com.cy/cart/",
    "https://newlife.com.cy/swimming-pool/pool-rules/",
    "https://newlife.com.cy/new-life-gym/sauna/",
    "https://newlife.com.cy/product-category/supplements/",
    "http://newlife.com.cy/360/",
    # Add more URLs you want to exclude
]

visited_urls = set()  # Track URLs that have already been crawled
downloaded_gif_urls = set()  # Track GIF URLs that have already been downloaded


def extract_gif_from_page(url):
    """
    Extracts GIFs from a specific page URL.

    Args:
        url (str): The URL of the page to scan for GIFs.

    Returns:
        list: A list of URLs for all GIF images found on the page.
    """
    gif_urls = []
    try:
        # Send the request with custom headers
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise error for bad responses
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract all <img> tags
        for img in soup.find_all("img"):
            src = img.get("src")
            if src and src.lower().endswith(".gif"):
                # Join the relative URL with the base URL (if applicable)
                full_url = urljoin(url, src)
                if full_url not in downloaded_gif_urls:  # Avoid re-downloading
                    gif_urls.append(full_url)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {url}: {e}")

    return gif_urls


def format_filename(original_filename):
    """
    Formats the filename by removing numbers, a leading dash, '_360', and converting to lowercase.

    Args:
        original_filename (str): The original file name.

    Returns:
        str: The formatted file name.
    """
    # Remove numbers and any dash that comes before numbers
    formatted = re.sub(r"\d+-", "", original_filename)

    # Remove the "_360" at the end
    formatted = re.sub(r"_360$", "", formatted)

    # Convert to lowercase
    formatted = formatted.lower()

    return formatted


def download_gif(gif_url, save_dir, referer_url):
    """
    Downloads a GIF from the given URL and saves it to the specified directory with a formatted filename.

    Args:
        gif_url (str): The URL of the GIF to download.
        save_dir (str): The directory where the GIF should be saved.
        referer_url (str): The URL of the page where the GIF was found (used as the Referer header).
    """
    if gif_url in downloaded_gif_urls:
        return  # Skip if already downloaded

    try:
        # Ensure the directory exists
        os.makedirs(save_dir, exist_ok=True)

        # Extract the original filename from the URL
        original_filename = os.path.basename(gif_url).replace(".gif", "")

        # Format the filename as per requirements
        formatted_filename = format_filename(original_filename) + ".gif"

        # Complete path for saving the GIF
        gif_filepath = os.path.join(save_dir, formatted_filename)

        # Add the referer to the headers
        download_headers = HEADERS.copy()
        download_headers["Referer"] = referer_url

        # Send the request to download the GIF with the headers
        response = requests.get(gif_url, headers=download_headers, stream=True)
        response.raise_for_status()

        # Write the GIF to the file
        with open(gif_filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"Downloaded and saved GIF: {gif_filepath}")

        # Add to the downloaded GIF set
        downloaded_gif_urls.add(gif_url)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading GIF {gif_url}: {e}")


def get_all_links(url, domain):
    """
    Extracts all internal links from a page that are under the given domain.

    Args:
        url (str): The URL of the page to extract links from.
        domain (str): The domain to limit the search to.

    Returns:
        list: A list of URLs found on the page that are under the same domain.
    """
    links = set()  # Use a set to avoid duplicates
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            full_url = urljoin(url, href)
            parsed_url = urlparse(full_url)

            # Only keep links that are under the same domain
            if parsed_url.netloc == domain:
                links.add(full_url)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {url}: {e}")

    return links


def crawl_website_for_gifs(start_url, save_dir):
    """
    Crawls a website starting from the given URL and extracts GIFs from all internal pages.

    Args:
        start_url (str): The starting URL of the website to crawl.
        save_dir (str): The directory to save the GIF images.
    """
    domain = urlparse(start_url).netloc  # Extract the domain from the URL
    urls_to_visit = {start_url}  # A set of URLs to visit, starting with the homepage

    os.makedirs(save_dir, exist_ok=True)  # Ensure the directory exists

    while urls_to_visit:
        current_url = urls_to_visit.pop()

        # Skip the URL if it's in the exclusion list or has been visited
        if current_url in exclude_urls or current_url in visited_urls:
            print(f"Skipping: {current_url}")
            continue

        print(f"Crawling: {current_url}")
        visited_urls.add(current_url)  # Mark this URL as visited

        # Extract GIFs from the current page
        gifs_on_page = extract_gif_from_page(current_url)

        # Download each GIF and save it to the specified directory
        for gif_url in gifs_on_page:
            download_gif(gif_url, save_dir, current_url)

        # Find all internal links to continue crawling
        internal_links = get_all_links(current_url, domain)
        urls_to_visit.update(
            internal_links - visited_urls
        )  # Add only new, unvisited links

        # Be polite by sleeping briefly between requests
        time.sleep(1)


# Starting point for the website
start_url = "https://newlife.com.cy/"
# Directory where GIFs will be saved
save_directory = os.path.expanduser("~/exercise-gifs")

# Start crawling the website for GIFs
crawl_website_for_gifs(start_url, save_directory)
