import fitz
def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text.
    """
    text = ""
    try:
        print("Running PDF text extraction...")
        with fitz.open(pdf_path) as pdf_document:
            for page in pdf_document:
                text += page.get_text()
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
    return text