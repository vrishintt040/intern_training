import requests as req
from bs4 import BeautifulSoup
import time
import random

r=req.get("https://www.scrapethissite.com/pages/simple/")
print(r.status_code)
#print(r.text)

soup=BeautifulSoup(r.content,"html.parser")
print(soup.prettify())

print(soup.title.string)
print(soup.find("h1").text.strip())
print(soup.title.string)

country_dict={}

for country in soup.find_all("div",class_="col-md-4 country"):
    country_name=country.find("h3",class_="country-name").text.strip()
    capital = country.find('span', class_='country-capital').text.strip()
    population= country.find('span', class_='country-population').text.strip()
    area= country.find('span', class_='country-area').text.strip()
    country_dict[country_name] = {
        'capital': capital,
        'population': population,
        'area': area
    }

print(country_dict)

r=req.get("https://webscraper.io/test-sites/e-commerce/static/computers/tablets")

soup=BeautifulSoup(r.content,"html.parser")
print(r.status_code)
products = soup.find("div", class_="col-lg-9").find("div", class_="row").find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
title=soup.find("div",class_="col-lg-9").find("h1",class_="page-header").text.strip().split()[-1]

product_dict={}

for product in products:
    price = product.find("h4", class_="price float-end card-title pull-right").span.text.strip()
    title=product.find("a", class_="title").text.strip()
    description=product.find("p", class_="description card-text").text.strip()
    review_count=product.find("p", class_="review-count float-end").text.strip().split()[0]
    rating_tag = product.find("p", attrs={"data-rating": True})
    rating = rating_tag["data-rating"] if rating_tag else None

    if "Tablets" not in product_dict:
        product_dict["Tablets"] = []
    product_dict["Tablets"].append({
        'title': title,
        'price': price,
        'description': description,
        'review_count': review_count,
        'rating': rating
    })

    print(f"Title: {title} Price: {price} Description: {description} Review Count: {review_count} Rating: {rating}")
    print("--------------------------------------------------")

print(product_dict["Tablets"])

#Handle headers and cookies for authenticated scraping.

session=req.Session()

login_page=session.get("https://quotes.toscrape.com/login")
soup=BeautifulSoup(login_page.content,"html.parser")

csrf_token = soup.find("input", {"name": "csrf_token"})["value"]
#print(csrf_token)
payload = {
    "csrf_token": csrf_token,
    "username": "admin",
    "password": "admin"
}

response=session.post("https://quotes.toscrape.com/login", data=payload)

for i in range(1, 6):
    profile_page=session.get(f"https://quotes.toscrape.com/page/{i}",proxies={})
    soup=BeautifulSoup(profile_page.content,"html.parser")

    for quote in soup.find_all("div", class_="quote"):
        quote_text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()

        print(f"Quote: {quote_text} Author: {author} ")
        time.sleep(random.randint(1, 3))

#Transition to Dynamic Web Scraping with Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

service = Service("D:/tesseract intern/chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://webscraper.io/test-sites/e-commerce/more/computers/tablets")
time.sleep(3)

while True:
    try:
        price=driver.find_elements(By.CLASS_NAME, "price")
        title=driver.find_elements(By.CLASS_NAME, "title")
        description=driver.find_elements(By.CLASS_NAME, "card-text")
        review_count=driver.find_elements(By.CLASS_NAME, "review-count")

        for p, t, d, r in zip(price, title, description, review_count):
            print(f"Price: {p.text} Title: {t.text} Description: {d.text} Review Count: {r.text}")

        more_ele = driver.find_element(By.CLASS_NAME, "ecomerce-items-scroll-more")
        if more_ele.is_displayed() and more_ele.is_enabled():
            more_ele.click()
            time.sleep(2)
        else:
            break
    except NoSuchElementException:
        break  


time.sleep(3)

driver.quit()