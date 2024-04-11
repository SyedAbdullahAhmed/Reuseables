from fpdf import FPDF
from docx import Document

def convert_docx_to_pdf(docx_file, pdf_file):
    """
    Convert a Word document (.docx) to a PDF file.

    Parameters:
        docx_file (str): Path to the input Word document.
        pdf_file (str): Path to save the output PDF file.
    """
    # Open the Word document
    doc = Document(docx_file)
    
    # Create PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add a page
    pdf.add_page()

    # Set font for text (you can use other fonts that support Unicode characters)
    pdf.set_font("Arial", size=12)

    # Loop through each paragraph in the Word document and add it to the PDF
    for para in doc.paragraphs:
        # Convert the text to Unicode (UTF-8) before adding it to the PDF
        text = para.text.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(200, 10, txt=text, ln=True)

    # Save the PDF to a file
    pdf.output(pdf_file)
    print("Converted...")

# Example usage
convert_docx_to_pdf("Prompt Engineering.docx", "Prompt Engineering.pdf")
convert_docx_to_pdf("Google Search.docx", "Google Search.pdf")