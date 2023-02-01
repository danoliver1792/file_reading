from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
from urllib.request import urlopen


def read_pdf(file_pdf):
    """ function to read PDF file, returning the content in text """
    resources = PDFResourceManager()
    buffer = StringIO()
    layout_params = LAParams()
    disp = TextConverter(resources, buffer, laparams=layout_params)

    process_pdf(resources, disp, file_pdf)
    disp.close()

    content = buffer.getvalue()
    buffer.close()

    return content


# opening local file
filePDF = open("edital.pdf", "rb")
exit_file = read_pdf(filePDF)

print(exit_file)

# opening file on web
filePDF = urlopen("https://s3.novatec.com.br/sumarios/sumario-9788575226926.pdf")

filePDF.close()
