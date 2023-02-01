import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://www.techtudo.com.br/noticias/2017/10/confira-a-lista-completa-de-carros-para-need-for-speed"
               "-payback.ghtml")
bs_object = BeautifulSoup(html, "html.parser")
table = bs_object.find("table")
rows = table.findAll("tr")
file_csv = open("cars.csv", "w", newline="", encoding="utf-8")

for row in rows:
    columns_website = row.findAll("td")
    list_for = []
    for column in columns_website:
        list_for.append(column.text)

    writer = csv.writer(file_csv, delimiter=";")
    writer.writerow(list_for)

file_csv.close()
