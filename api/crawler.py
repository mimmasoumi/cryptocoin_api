from bs4 import BeautifulSoup
import requests

def coin_detail(coin_name):
    url = 'https://coinmarketcap.com/currencies/%s' % coin_name
    req = requests.get(url)
    print(type(req.status_code))
    if req.status_code == 200:
        url_req = req.text

        soup = BeautifulSoup(url_req, "html.parser")

        coin_tag = soup.find("small", {"class":"nameSymbol"})
        coin_tag = coin_tag.contents[0]

        coin_price = soup.find("div", {"class":"priceValue"})
        coin_price = coin_price.contents[0].text

        return {"name": coin_name, "tag": coin_tag, "price": coin_price}

    else:
        return {"error": "coin not found"}
