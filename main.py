import json

data = {"Curso": "Python Web Scraping",
             "Secao": "12",
             "Nome Secao": "Lendo documentos",
             "Numero da Aula": "05",
             "Descricao da Aula": "Arquivos JSON"}

data_json = json.dumps(data)
print(data_json)

with open("exemplo01.json", "w") as arq:
    arq.write(json.dumps(data))
    