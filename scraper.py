#12/7/2022 DC:  I got this from https://www.youtube.com/watch?v=QhD015WUMxE


from bs4 import BeautifulSoup #for scrapintg
import requests  #For http requests
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com")  #Request our target website and store it as a variable
soup = BeautifulSoup(page_to_scrape.text, "html.parser")  #Parse the HTML and store it as a varible too
quotes = soup.findAll("span", attrs={"class":"text"})  #Looks for all the span tags with class attribute 'text'
authors = soup.findAll("small", attrs={"class":"author"})  #Looks for all the small tags with class attribute author

file = open("scraped_quotes.csv", "w")  #create a variable that opens a new CSV file
writer = csv.writer(file) #create another variable that writes to it

writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes,authors):  #The zip function of the for loop is what makes it go quote then author instead of all the quotes then all the authors
    print(quote.text)

