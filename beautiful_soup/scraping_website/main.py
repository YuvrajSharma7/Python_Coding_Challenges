from bs4 import BeautifulSoup
import requests

html= requests.get('https://news.ycombinator.com/').text

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.select('.titleline a'))
titles=soup.find_all('span', class_='titleline')
scores=soup.find_all('span', class_='score')
print(len(titles))
title_texts=[]
for a in titles:
    title_texts.append(a.find('a').get_text())
title_links=[item.find('a').get("href") for item in titles]
score=[int(item.string.split(" ")[0]) for item in scores]
max_score=max(score)
print(max_score)
index=score.index(max_score)
print(f"Title: {title_texts[index]}, Link: {title_links[index]}, Score: {max_score}")