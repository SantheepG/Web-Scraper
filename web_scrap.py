import requests
import json
from bs4 import BeautifulSoup

def compare_prices(product_laughs, product_glomark):

    # Send HTTP request and retrieve HTML content
    response_laughs = requests.get(product_laughs)
    response_glomark = requests.get(product_glomark)
    
    # Parsing retrieved content
    soup_laughs = BeautifulSoup(response_laughs.text, 'html.parser') # content instead text is applicable
    soup_glomark = BeautifulSoup(response_glomark.text, 'html.parser')

    # Finding the <span> tag containing the price & product name
    price_span = soup_laughs.find('span', class_='regular-price')
    product_name_laughs = soup_laughs.find('div', class_='product-name').text.strip()
    price_laughs = float(price_span.text.strip()[3:])

    # Finding the inline script containing the JSON data
    inline_script = soup_glomark.find('script', {'type': 'application/ld+json'})

    # Extracting the name & price
    json_data = json.loads(inline_script.string)
    product_name_glomark = json_data['name']
    price_glomark = float(json_data['offers'][0]['price'])

    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')

 # Test with the given example URLs 
laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html' 
glomark_coconut = 'https://glomark.lk/coconut/p/11624' 
compare_prices(laughs_coconut, glomark_coconut) 