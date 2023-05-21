#Quotes to scrap project

# Please make sure you have b4s and requests module installed before run this code
from bs4 import BeautifulSoup
import requests
import csv

scrap_page = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(scrap_page.text, "html.parser")
quotes = soup.findAll("span",attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

file = open("Scrape_quotes.csv","w")
writer = csv.writer(file)
writer.writerow(["QUOTES","AUTHOR"])

for quote, author in zip(quotes,authors):
    print(quote.text," - ",author.text)
    writer.writerow([quote.text,author.text])
file.close()
