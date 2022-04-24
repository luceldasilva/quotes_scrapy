# Quotes Scraper
Part of Curso de Scrapy ðŸ•·

# Comandos de Windows
cmder u otro emulador de bash
git init
git branch -M main
py -m venv venv
venv\Scripts\activate
## o ponerle alias
alias entorno = venv\Scripts\activate
pip install scrapy autopep8
## por si falta actualizar :v py -m pip install pip --upgrade 
scrapy startproject nombredelproyecto
## creando proyecto
cd nombredelproyecto
## ya haces tu proyecto :v
scrapy crawl nombre_del_name_que_pusiste_en_la_class
## abrir url
scrapy shell "url" 
## si es linux/mac 'comillas simples' 
response.xpath('lo que se pueda :v/text()').get() 
## si queres todos es .getall()
-o name.json o .csv
## para generar un archivo y que guarde ahi si no le pusimos en el archivo que se guarde solo :v 
## para repetir y reescribir todo tipo hacer nuevo
del quotes.json && scrapy crawl quotes -o quotes.json
## esto porque solo pone en la cola si le pones el mismo nombre kkkkk
-a variable=numero
## poner variable a la página