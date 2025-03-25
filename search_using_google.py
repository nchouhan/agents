import requests

def google_site_search(query, site):
    search_url = f"https://www.google.com/search?q=site:{site}+{query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        return response.text  # This returns the raw HTML of the search results
    else:
        return "Failed to fetch search results"

query = "Nike shoes"
flipkart_results = google_site_search(query, "flipkart.com")
amazon_results = google_site_search(query, "amazon.in")

print(flipkart_results)  # You need to parse the HTML to extract links
print(amazon_results)
