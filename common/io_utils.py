# common/io_utils.py
# Helpers for PDF/text IO. Uses pdfplumber as a lightweight PDF parser.

import pdfplumber

def extract_text_from_pdf_filelike(file_like) -> str:
    if file_like is None:
        return ''
    try:
        # file_like should be a BytesIO / Streamlit UploadedFile
        file_like.seek(0)
    except Exception:
        pass
    try:
        with pdfplumber.open(file_like) as pdf:
            pages = [p.extract_text() or '' for p in pdf.pages]
        return '\n\n'.join(pages).strip()
    except Exception as e:
        raise
