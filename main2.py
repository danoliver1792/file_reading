import json

# reading the JSON file and printing the corresponding one of the keys
with open("exemplo01.json", "r") as arq:
    content = arq.read()
    data_json = json.loads(content)
    print(data_json["Curso"])
