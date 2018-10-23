from bs4 import BeautifulSoup
import urllib2
import re
import xlsxwriter

# specify url of main page to scrape
drink_url = 'https://www.thespruceeats.com/a-to-z-cocktail-recipes-3962886'

# get html into page
page = urllib2.urlopen(drink_url)

# parse html and store in soup
soup = BeautifulSoup(page, 'html.parser')

# create excel workbook and worksheet
workbook = xlsxwriter.Workbook('drinks.xlsx')
worksheet = workbook.add_worksheet()

# each div contains a few recipes plus some extra data we don't need.
divs = soup.findAll("div", id=re.compile("mntl-sc-block_.*"))

# in each div, the unordered list contains all the drink links
row = 0
for div in divs:
    ul = div.find('ul') # each ul contains a set of drinks
    if ul: # ul error check
        for li in ul.findAll('li'): # each li is a drink
            a = li.find('a')
            if a: # a error check
                worksheet.write(row, 0, a.text)
                worksheet.write(row, 1, a.get('href'))
                row = row + 1

workbook.close()
