# https://omnianalytics.io/2018/08/28/ebay-web-scrape-tutorial/


# <h3 class="s-item__title" role="text">Super Mario Sunshine - Gamecube Nintendo Game</h3>
# <span class="s-item__price">$12.50</span>
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select
import time


#obj = Select()
bold = "\033[1m"
reset = "\033[0;0m"

def webNavigation(url):

    # Source
    # https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08

    # Good video on dropdowns
    # https://www.youtube.com/watch?v=Iiat5mc1Yz8

    # Using Chrome to access Web
    driver = webdriver.Chrome(executable_path='C:\\Users\\corni\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\chromedriver.exe')


    # Open website
    driver.get(url)
    driver.maximize_window()

    #sort_by_lowest_price_button = driver.find_element_by_xpath("//*[@id='w8-w1']/div/div/ul/li[4]/a/span/text()").click()

    #sort_by_lowest_price_button = driver.find_element_by_xpath('//*[@id="w6"]/div[1]/div[2]/div/ul/li[4]/a/h2').click()

    elm = driver.find_element_by_link_text('Buy It Now')
    driver.implicitly_wait(1)
    elm.click()

    elm = driver.find_element_by_link_text('Price + Shipping: lowest first')
    driver.implicitly_wait(1)
    elm.click()



    #sort_by_lowest_price_button = driver.find_element_by_class_name('srp-controls--selected-value') # Sort by lowest prcie



    #driver.click("//*[@id='w8-w1']/div/div/ul/li[4]/a/span/text()= 'Price + Shipping: lowest first'")

    #driver.click('//*[@id="w4-w1_btn"]/div/svg/use')

    return driver

    #//*[@id="w8-w1"]/div/div/ul/li[4]/a/span/svg # svg tag
    #//*[@id="w8-w1"]/div/div/ul/li[4]/a/span/text() # "Price + Shipping: lowest first"

    #buy_it_now_button = driver.find_element_by_name('Buy It Now')


    #<div class="srp-controls--selected-value">Best Match</div>








def make_urls(names):

    # eBay url that can be modified to search for a specific item on eBay
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR11.TRC2.A0.H0.XIp.TRS1&_nkw="

    #List of urls to be created for searches in name_list
    urls = []

    for name in names:
        urls.append(url + name.replace(" ", "+"))

        return urls


def ebay_scrape(urls):

    open("demoFile.txt", "w").close() # Clears the contents of the file before writing in new scrape

    for url in urls:

        res = requests.get(url)

        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')

        name = soup.find("h3", {"class": "s-item__title"}).get_text(separator=u" ")

        try:
            price = soup.find("span", {"class": "s-item__price"}).get_text()


            f = open("demoFile.txt", "a")

            f.write(url)
            print(url)

            f.write("\nITEM NAME: " + name)
            print(bold + "ITEM NAME:  " + reset + name)

            f.write("\nPRICE: " + price + "\n\n")
            print(bold + "PRICE:  " + reset + price + "\n")
        except AttributeError:
            print("NoneType Encountered")







def make_urls(names):
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR11.TRC2.A0.H0.XIp.TRS1&_nkw="
    urls = []

    for name in names:
          urls.append(url + name.replace(" ", "+"))
    return urls


name_list = ["Mario Sunshine Gamecube", "twighlight princess zelda wii"]

# webNavigation(make_urls(name_list))

 # Works to go through list, but second window does not click BuyItNow

for x in name_list:
    driver = webNavigation("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR0.TRC0.A0.H0.TRS5&_nkw=" + x)
    driver.implicitly_wait(2)
#driver = webNavigation("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR0.TRC0.A0.H0.TRS5&_nkw=Mario+Sunshine+Gamecube&_sacat=0")
#driver.click("//*[@id='w4-w1_btn']/div/svg/use")



ebay_scrape(make_urls(name_list))

