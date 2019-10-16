




from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("/home/albino/PycharmProjects/laudi/resources/WORK PDF/MG 2201-2205.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)