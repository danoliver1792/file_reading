import docx


def read_docx(file_docx):
    """ reading DOCX with function """
    try:
        doc = docx.Document(file_docx)
        text = []

        for p in doc.paragraphs:
            text.append(p.text)

        return "\n".join(text)
    except Exception as error:
        return "Error: ", error
