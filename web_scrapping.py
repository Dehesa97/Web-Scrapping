

#TODO: Web scraped data from Internet using APIS
#Scrape numeric data using the APIS
#COINGECKO
import requests
import json
import os

#current Bitcoin price
coins1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").text
coins = json.loads(coins1)
price = int(coins["bitcoin"]["usd"])
print(price)

#Scrape text data using the APIS

#------------------------------------------------------------

#TODO: Web scraped data from Internet using alternative methods.

