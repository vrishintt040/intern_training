url="https://www.ycombinator.com/companies"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

service = Service("D:/tesseract intern/chromedriver.exe")

options = Options()
options.add_argument('--headless')  
options.add_argument('--disable-gpu')  
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
time.sleep(3)


#scroll to the bottom 
last_height=driver.execute_script("return document.body.scrollHeight")
x=1
while x!=0: # USE TRUE FOR INFINITE SCROLLING
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    x-=1
    if new_height == last_height:
        break
    last_height = new_height



#get company urls

from bs4 import BeautifulSoup

soup = BeautifulSoup(driver.page_source, 'html.parser')
cards = soup.find_all("a", class_="_company_i9oky_355")

company_links = ["https://www.ycombinator.com" + card['href'] for card in cards]

driver.quit()

# Get DATA

import requests
data={}

for link in company_links:
    time.sleep(1)
   

    req=requests.get(link)
    soup = BeautifulSoup(req.content, 'html.parser')
    company_name=soup.find("h1", class_="text-3xl font-bold")
    company_name=company_name.text.strip() if company_name else "N/A"
    description=soup.find("div", class_="text-xl")
    description=description.text.strip() if description else "N/A"
    tags_div = soup.find("div", class_="align-center flex flex-row flex-wrap gap-x-2 gap-y-2")
    tags = []
    if tags_div:
        for tag in tags_div.find_all("a"):
            span = tag.find("span")
            if span:
                tags.append(span.text.strip())
            else:
                tags.append(tag.get_text(strip=True))

    website_link = soup.find("a",class_="mb-2 whitespace-nowrap md:mb-0").get("href")

    founded = None
    for div in soup.find_all("div", class_="flex flex-row justify-between"):
        spans = div.find_all("span")
        if spans and spans[0].text.strip() == "Founded:":
            founded = spans[1].text.strip()
            break

    linkedin_link = None
    for a in soup.find_all("a", href=True):
        if "linkedin.com/company" in a["href"]:
            linkedin_link = a["href"]
            break  


    email = None
    for a in soup.find_all("a", href=True):
        if a["href"].startswith("mailto:"):
            email = a["href"].replace("mailto:", "")
            break

    founders = []
    for founder_card in soup.find_all("div", class_="ycdc-card-new"):
        name_div = founder_card.find("div", class_="text-xl font-bold")
        if name_div:
            founders.append(name_div.text.strip())

    data[company_name]={
        "description": description,
        "tags": tags,
        "website_link": website_link,
        "founded": founded,
        "linkedin_link": linkedin_link,
        "email": email,
        "founders": founders
    }

print(data)

with open("Company_data.txt", "a", encoding="utf-8") as file:
    file.write(str(data) + "\n")


