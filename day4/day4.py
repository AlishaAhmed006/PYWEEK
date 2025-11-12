import requests
from bs4 import BeautifulSoup
url="https://tsigmjcet.in/"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
print("first heading")
print(soup.find("h2").text)
print("all headings on the page")
for h in soup.find_all("h2"):
    print(h.text)
for a in soup.find_all("a"):
    print("-",a.get_text(strip=True),":",a.get("href"))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1 — Open Chrome
driver = webdriver.Chrome()

# Step 2 — Load the URL
driver.get("https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops")

# Step 3 — Wait for JS to load
time.sleep(4)

# Step 4 — Extract product names dynamically loaded
titles = driver.find_elements(By.CLASS_NAME, "title")

if titles:
    print(f"Found {len(titles)} products:\n")
    for t in titles:
        print(t.text)
else:
    print("No products found!")

driver.quit()

