from PyPDF2 import PdfReader, PdfWriter

def pdfDecryption(pdf):
	reader = PdfReader(pdf)
	writer = PdfWriter()
	

	if reader.is_encrypted:
   		reader.decrypt("pdf")

	for page in reader.pages:
    	 writer.add_page(page)

	with open(f"{pdf[:-4]}.pdf", "wb") as f:
	    writer.write(f)

	print(f"{pdf} Decrypted Successfully!")

pdfDecryption("Prompt Engineering.pdf")
pdfDecryption("Google Search.pdf")