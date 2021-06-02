from bs4 import BeautifulSoup
file = open('index.html', 'r', encoding='utf-8')
data = file.read()
file.close()

soup = BeautifulSoup(data, 'lxml')

# for tag in soup.head.recursiveChildGenerator():
#     print(tag)

reviews = soup.findAll('div', attrs={'class':'reviews'})

for review in reviews:
    name = review.find('div', attrs={'class':'name'}).text
    comment = review.find('div', attrs={'class':'comment'}).text
    print(name, comment, sep=': ')

# print(soup.ul)