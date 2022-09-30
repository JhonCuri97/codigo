#EJEMPLO DE SRACPPING

from bs4 import BeautifulSoup
import requests 

url =requests.get("https://camara-arequipa.org.pe/directorio")
status_code=url.status_code
if status_code==200:
    html=BeautifulSoup(url.text,"html.parser")
    empresas= html.find_all('div',{'class':'card-body'})
    for empresa in empresas:
        nombre = empresa.find_all('h5',{'class':'card-title'})
        print(nombre)
else:
    print("error nro"+ str(status_code))
