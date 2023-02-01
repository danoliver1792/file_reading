import docx

# reading DOCX content
doc = docx.Document("Hello World.docx")
for a in doc.paragraphs:
    print(a.text)
