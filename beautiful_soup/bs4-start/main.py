from bs4 import BeautifulSoup


with open("website.html") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p) # prints 1st <p> tag
print(soup.p['class'])
print(soup.a) # prints 1st <a> tag
print(soup.a['href']) # prints 1st <a> tag's href attribute
print(soup.find_all('a')) # prints list of all <a> tags

for link in soup.find_all('a'):
    print(link.get('href'))

# Accessing using CSS selectors

for heading in soup.select('.heading'): #returns list of all elements with class 'heading'
    print(heading.get_text())

for heading in soup.select('p em strong'): #returns list of all elements which are inside <p><em><strong>----</strong></em></p>
    print(heading.get_text())

for heading in soup.select('p em strong a'): #returns list of all elements which are inside <p><em><strong><a>----</a></strong></em></p>
    print(heading.get('href'))
