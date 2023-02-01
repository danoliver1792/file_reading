import json
from urllib.request import urlopen

datas = urlopen("http://dados.iffarroupilha.edu.br/api/v1/projetos.json").read()
datas = json.loads(datas)
print(datas)
