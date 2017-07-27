import requests
from bs4 import BeautifulSoup


# url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# req = requests.get(url)
# soup = BeautifulSoup(req.text, 'lxml')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print("h1: %s" % soup.h1)
# print("h1 string: %s" % soup.h1.string)
# print("h1 class: %s" % soup.h1['class'])
# print("h1 id: %s" % soup.h1['id'])
# print("h1 atributes: %s" % soup.h1.attrs)
# print("all h2")
# for sub_heading in soup.find_all('h2'):
#   print(sub_heading)
# print(soup.p.contents[10])

# #####################

url = 'https://www.bloomberg.com/quote/SPX:IND'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')

name = soup.find('h1', attrs={'class': 'name'}) # Vi class name la duy nhat tren page nay
print('name: %s' % name.text.strip())
price = soup.find('div', attrs={'class': 'price'}) # Vi class price cung duy nhat
print('price: %s' % price.text)