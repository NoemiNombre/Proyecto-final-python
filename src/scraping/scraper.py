#importo las librerias 
import requests
from bs4 import BeautifulSoup
import pandas as pd 

#pagina de donde se scrappea 
base_url = "https://www.pharmacys.com.ec/pharmacys/skin-care-days"

#obtenemos conteindo de la pagina 
# def get_info(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.content
#     else:
#         raise Exception(f"Noe se puedo obtener la informacion de: {url}")
 
#  #conseguir productos que voy a scrappear
# def get_product(product):
#     #para encontrar el producto por nombre de la class en HTML
#     title =product.find("",class_="title").text.strip()
#     description = product.find("",class_="description").text.strip()
#     price = product.find("h4",class_="price").text.strip()
#     return{
#         "tittle":title,
#         "description":description,
#         "price":price,
#     }
    
# def scrape(url):
#     page_content = get_info(url)
#     soup = BeautifulSoup(page_content,"html.parser")
#     products= soup.find_all("div",class_="thumbnail")
 
      
# #alguna pagina con paginación y recorrer todas


def get_products(url):
    response =requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    products= []
    
    #agergar los productos con los selsctores de la pag
    items= soup.select(".product")
    for item in items:
        name_element = item.select_one(".product_name")
        price_element= item.select_one(".product_price")
        img_element=item.select_one("a img")
        
         