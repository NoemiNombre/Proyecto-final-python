#me confundi un poco en este codigo :(
#importo las librerias 
import requests
from bs4 import BeautifulSoup
import pandas as pd 

#obetener conteinido de la pag
def fetch_page(url):
    response =requests.get(url)
    if response.status_code == 200:
        return response.content
    
    else:
        raise Exception(f"failed to fetch page: {url}")
    
    
#analiso el producto   
def parse_product(product):
    
    name_item = product.find("h5",class_="ps-product__title").text.strip()
    price = product.find("span",class_="ps-product__price sale").text.strip() 
    
    return{  
        "Name":name_item,
        "Price":price
    }
#funcion principal del scrapper
def scraper(url):
    page_content = fetch_page(url)
    soup = BeautifulSoup(page_content, "html.parser")
    products= soup.find_all("div",class_="ps-product ps-product--standard")
    
    #aqui se almacenan los datos
    products_data= []
    
    for product in products:
        product_info = parse_product(product)
        products_data.append(product_info)
        
     
    return pd.DataFrame(products_data)
    
    
def procesar_datos(productos):
    # product['price'] = product['price'].replace(r'[\$,]', '', regex=True).astype(float)
    
    # return product['price']
  processed_data = []
  for nombre, precio in productos:
    #convertir en flotante
      precio = float(precio.replace("$",""))
      processed_data.append({"Name": nombre, "Precio": precio})
    
  
    
    
#obetenr todos los productos de todas las paginas
def obtener_datos_todas_pags(base_url):
  products_data =[]
  page =1
  while True:
    url = f"{base_url}?pagenumber={page}"
    new_productos = scraper(url)
    if not new_productos:
        break

    products_data.extend(new_productos)
    page +=1
    break
  return products_data

def escribir_datos_en_archivo(datos, archivo):
  with open(archivo, "w", encoding="utf-8") as f:
    for linea in datos:
      f.write(linea + "\n")

def guardar_datos_en_csv(datos,archivo):
  df = pd.DataFrame(datos)
  df.to_csv(archivo,index=True, encoding="utf-8")
  return df
#funcion que realiza estadisticas de precios
def estadisticas_precios(df):
  print(f"Precio promedio: £{df['Precio'].mean():.2f}")
  print(f"Precio maximo: £{df['Precio'].max():.2f}")
  print(f"Precio minimo: £{df['Precio'].min():.2f}")

    
 
    
#pagina de donde se scrappea 
base_url = "https://farmaciascruzazul.ec/vitaminas-y-suplementos?pagenumber=1"    


#ejecutar funciones
productos = obtener_datos_todas_pags(base_url)
datos_procesados = procesar_datos(productos)
# datos_procesados = procesar_datos(productos)
# escribir_datos_en_archivo(datos_procesados, "productos.txt")

df = guardar_datos_en_csv(datos_procesados,"productos2.csv")
estadisticas_precios(df)

    
#guardar en csv


print("informacion guardada en .csv")
    






