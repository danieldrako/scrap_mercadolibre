from turtle import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time 
driver = webdriver.Chrome("./chromedriver")
url= 'https://www.mercadolibre.com.mx/'

driver.get(url)
search_bar = driver.find_element(By.CLASS_NAME, "nav-search-input") #* Seleccionar barra de busqueda por nombre de clase
search_bar.clear()
search_bar.send_keys('iphone12') #* Busqueda del texto 
search_bar.send_keys(Keys.RETURN) #* Tecla enter 


title_products = driver.find_elements(By.XPATH, '//h2[@class="ui-search-item__title shops__item-title"]') #* los titulos de los productos
title_products = [ title.text for title in title_products ]

price_products = driver.find_elements(By.XPATH, "//li[@class = 'ui-search-layout__item shops__layout-item']//div[@class='ui-search-result__content-wrapper shops__result-content-wrapper']//div[@class='ui-search-result__content-columns shops__content-columns']//div[@class='ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left']/div[1]/div[1]/div[1]/div[1]/span[1]/span[2]/span[2]")
price_products = [ price.text for price in  price_products ]

links_products = driver.find_elements(By.XPATH, "//div[@class='ui-search-item__group ui-search-item__group--title shops__items-group']//a[1]")
links_products = [ link.get_attribute('href') for link in  links_products ]

data_products = {
    "name_products":title_products,
    "price_products":price_products,
    "link_products":links_products
}
df = pd.DataFrame(data_products)

df.to_csv("Productos.csv")

time.sleep(5)
driver.close()


