import docx

# saving the contents of the DOCX file to a text file
doc = docx.Document("test.docx")

for a in doc.paragraphs:
    with open("test.txt", "a") as arq:
        arq.write(a.text)
        