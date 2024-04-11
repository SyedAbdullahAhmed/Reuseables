from PyPDF2 import PdfReader, PdfWriter

def pdfEncryption(pdf):
	reader = PdfReader(pdf)
	writer = PdfWriter()

	for page in reader.pages:
    	 writer.add_page(page)

	writer.encrypt("pdf")

	with open(f"{pdf[:-4]}.pdf", "wb") as f:
	    writer.write(f)

	print(f"{pdf} Encrypted Successfully!")

pdfEncryption("Prompt Engineering.pdf")
pdfEncryption("Google Search.pdf")

