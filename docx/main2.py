import docx

# checking each type (bold, italic, underlined)
doc = docx.Document("test.docx")
tot_runs = len(doc.paragraphs[0].runs)

cont = 0
while cont < tot_runs:
    print(doc.paragraphs[0].runs[cont].text)
    cont += 1
