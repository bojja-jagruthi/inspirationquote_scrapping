from bs4 import BeautifulSoup
import requests
import datetime
import urllib.request
import time
def scrap_quote():
	URL = 'https://www.goodreads.com/quotes/tag/inspirational?page=1'
	try:	
		webpage = requests.get(URL)  
		if webpage.status_code==200:
			soup = BeautifulSoup(webpage.text, "html.parser")
			quoteText = soup.find_all('div', attrs={'class':'quoteText'}) 
			if quoteText:
				for i in quoteText:
					quote = i.text.strip().split('\n')[0]
					return quote
					break
			else:
				raise Exception("Unable to find the quote element on the page.")
		else:
			raise Exception(f"Failed to retrieve the page. Status code: {webpage.status_code}")

	except Exception as e:
		return "Error:{e}"
quote=scrap_quote()
print(quote)
log_file = "quote_log.txt"
with open(log_file, "a") as file:
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	file.write(f"{timestamp}\n{quote}\n\n")
	print(f"\nQuote logged to {log_file}.")