#importo las librerias 
import requests
from bs4 import BeautifulSoup
import pandas as pd 

#pagina de donde se scrappea 
base_url = "https://www.pharmacys.com.ec/pharmacys/skin-care-days"

#obtenemos conteindo de la pagina 

#alguna pagina con paginación y recorrer todas