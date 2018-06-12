import lxml.html
from bs4 import BeautifulSoup

f = open('RAND_MG120_prettify.html','r',encoding='utf-8').read()
soup = BeautifulSoup(f, "lxml")
p_soup = soup.find_all("p")

with open('out.txt', 'w', encoding='utf-8') as g:
  for n in p_soup:
    print(n, file=g)
