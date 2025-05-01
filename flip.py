import requests
import pandas as pd
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 12):
    url = f"https://www.flipkart.com/search?q=under+50000+price+mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page={i}"

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="DOjaWF gdgoEp")
    
    
    names = box.find_all("div", class_="KzDlHZ")
    for name_tag in names:
        name = name_tag.text.strip()  # Remove unnecessary whitespaces
        Product_name.append(name)

    
    prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
    for price_tag in prices:
        price = price_tag.text.strip()
        Prices.append(price)

    
    desc = box.find_all("ul", class_="G4BRas")
    for desc_tag in desc:
        description = desc_tag.text.strip()
        Description.append(description)

   
    review = box.find_all("div", class_="XQDdHH")
    for review_tag in review:
        review_text = review_tag.text.strip()
        Reviews.append(review_text)

# Ensure all lists have the same length by padding with None
max_length = max(len(Product_name), len(Prices), len(Description), len(Reviews))

# Padding shorter lists with None
Product_name.extend([None] * (max_length - len(Product_name)))
Prices.extend([None] * (max_length - len(Prices)))
Description.extend([None] * (max_length - len(Description)))
Reviews.extend([None] * (max_length - len(Reviews)))


df = pd.DataFrame({
    "Product Name": Product_name,
    "Prices": Prices,
    "Description": Description,
    "Reviews": Reviews
})


# print(df)

df.to_csv("C:/Users/admin/Desktop/scaping data/flipkart_data_50000_mobiel.csv")



# flip.py
print("Starting Flipkart Scraper...")
import time
time.sleep(2)
print("Flipkart scraping done!")

# # linkedin.py
# print("Starting LinkedIn Scraper...")
# import time
# time.sleep(2)
# print("LinkedIn scraping done!")

