from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def search_amazon(product):
    driver = webdriver.Chrome("./chromedriver")
    driver.maximize_window()
    driver.get("https://www.amazon.fr/")
    time.sleep(3) # open a new chrome page
    driver.find_element_by_name("accept").click()
    time.sleep(3)
    search_bar = driver.find_element_by_name("field-keywords")
    time.sleep(3)#
    search_bar.send_keys(product)
    time.sleep(3)
    search_bar.send_keys(Keys.RETURN) # click enter
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div/div/div[2]/h2/a/span").click()
    except:
        driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div[23]/div/span/div/div/div[2]/h2/a").click()
    time.sleep(3)
    driver.find_element_by_id("add-to-cart-button").click()
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="attachSiNoCoverage"]/span/input').click()
        driver.close()
    except:
        pass
