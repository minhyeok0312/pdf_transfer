import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF using PyMuPDF
    """
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        text = ""
        
        # Iterate through each page
        for page in doc:
            text += page.get_text()
            
        doc.close()
        return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Example usage
    pdf_path = "sample.pdf"  # Replace with your PDF file path
    if os.path.exists(pdf_path):
        extracted_text = extract_text_from_pdf(pdf_path)
        print("Extracted Text:")
        print(extracted_text)
    else:
        print(f"Error: File {pdf_path} not found") 