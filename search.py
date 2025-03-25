import webbrowser
import requests

query = "Nike Shoes"
flipkart_search_url = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
amazon_search_url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
flipkart_search = requests.get(flipkart_search_url);
amazon_search = requests.get(amazon_search_url);    
print(flipkart_search.text) 
print(amazon_search.text)   
# Open in browser
# webbrowser.open(flipkart_search_url)
# webbrowser.open(amazon_search_url)
