import requests
from bs4 import BeautifulSoup
import time

import pandas as pd


url = "https://books.toscrape.com/"

#decorador paa medir tiempo de ejecucion

def medir_tiempo(func):
  def wrapper(*args,**kwargs):
    inicio = time.time()
    resultado = func(*args, **kwargs)
    fin = time.time()
    print(f"Tiempo e ejecucion de {func.__name__}: {fin-inicio:.4f} segundos")
    return resultado
  return wrapper


#funcion para realizar el web scrapping

@medir_tiempo
def obtener_datos_productos(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  productos = []

  #adaptar los selsctores a la estuctura del sitio
  items = soup.select(".product_pod")

  for item in items:
    name_element = item.select_one("h3 a")
    price_element = item.select_one(".price_color")

    #controlar que los elemntos existan antes de enta
    if name_element and price_element:
      name = name_element["title"]
      price = price_element.get_text(strip=True)
      productos.append((name,price))

    if not name_element or not price_element:
      continue

  return productos

#para obtener datos de todas las pagina de la web

@medir_tiempo
def obtener_datos_todas_pags(base_url):
  productos =[]
  page =1
  while True:
    url = f"{base_url}/catalogue/page-{page}.html"
    nuevos_productos = obtener_datos_productos(url)
    if not nuevos_productos:
      break

    productos.extend(nuevos_productos)
    page +=1
  return productos


#funcion para procesar daTOs

@medir_tiempo
def procesar_datos(productos):
  datos_procesados = []
  for nombre, precio in productos:
    #convertir en flotante
    precio = float(precio.replace("£","").replace("Â",""))

    datos_procesados.append({"Producto": nombre, "Precio": precio})

    #control de flujo
    # if len(datos_procesados) >=10:
    #   break

  return datos_procesados

#funcion para escribir los datos en n .txt
@medir_tiempo
def escribir_datos_en_archivo(datos, archivo):
  with open(archivo, "w", encoding="utf-8") as f:
    for linea in datos:
      f.write(linea + "\n")


#guardar datos en un cvs
@medir_tiempo
def guardar_datos_en_csv(datos,archivo):
  df = pd.DataFrame(datos)
  df.to_csv(archivo,index=True, encoding="utf-8")
  return df


#funcion que realiza estadisticas de precios
def estadisticas_precios(df):
  print(f"Precio promedio: £{df['Precio'].mean():.2f}")
  print(f"Precio maximo: £{df['Precio'].max():.2f}")
  print(f"Precio minimo: £{df['Precio'].min():.2f}")

#ejecutar funciones
productos = obtener_datos_todas_pags(url)

datos_procesados = procesar_datos(productos)
# escribir_datos_en_archivo(datos_procesados, "productos.txt")

df = guardar_datos_en_csv(datos_procesados,"productos.csv")
estadisticas_precios(df)


