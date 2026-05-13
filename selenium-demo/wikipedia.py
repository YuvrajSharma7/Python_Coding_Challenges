from selenium import webdriver
from selenium.webdriver.common.by import By

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
title = driver.title
article_count=driver.find_element(by=By.XPATH,value = '//*[@id="articlecount"]/ul/li[2]/a[1]')
search=driver.find_element(by=By.NAME,value="search")
community_link = driver.find_element(By.LINK_TEXT, 'Community portal')

print(community_link.click())
#//*[@id="articlecount"]/ul/li[2]/a[1]

driver.close()

