import requests
from bs4 import BeautifulSoup
import json

def scrape_ui_elements(url):
    """Scrapes UI elements from a given website URL and saves them to a JSON file."""
    
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract UI elements
    elements = {
        "buttons": [
            {"text": btn.get_text(strip=True), "id": btn.get("id"), "class": btn.get("class")}
            for btn in soup.find_all("button")
        ],
        "links": [
            {"text": link.get_text(strip=True), "href": link.get("href")}
            for link in soup.find_all("a")
        ],
        "inputs": [
            {"type": inp.get("type"), "name": inp.get("name"), "id": inp.get("id"), "placeholder": inp.get("placeholder")}
            for inp in soup.find_all("input")
        ],
        "forms": [
            {"action": form.get("action"), "method": form.get("method"), 
             "inputs": [inp.get("name") for inp in form.find_all("input") if inp.get("name")]}
            for form in soup.find_all("form")
        ]
    }

    # Save to JSON file
    with open("elements.json", "w", encoding="utf-8") as f:
        json.dump(elements, f, indent=4)

    print("Elements extracted and saved to elements.json")

# Define target URL
url = "https://demoblaze.com" 
scrape_ui_elements(url)
