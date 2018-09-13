import requests

from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page.content)

soup = BeautifulSoup(page.content, 'html.parser')

print (soup.prettify)

print("")

print(list(soup.children))


print("")

print([type(item) for item in list(soup.children)])

html = list(soup.children)[2]

print("")

print(html)

print("")
print(list(html.children))

body = list(html.children)[3]

print("")
print(list(body.children))

p = list(body.children)[1]

print("")
print(p.get_text())
