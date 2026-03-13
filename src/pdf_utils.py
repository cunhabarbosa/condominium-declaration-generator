"""PDF generation and metadata utilities."""

from pathlib import Path
from typing import Dict
from docx2pdf import convert
from pypdf import PdfReader, PdfWriter


def generate_pdf(docx_file: str | Path, pdf_file: str | Path) -> None:
    """Generate a PDF from a DOCX file."""
    convert(input_path=str(docx_file), output_path=str(pdf_file))


def add_pdf_metadata(pdf_file: str | Path, metadata: Dict[str, str], output_pdf_file: str | Path | None = None) -> None:
    """
    Add metadata to a PDF file.

    If output_pdf_file is omitted, the input PDF is overwritten.
    """
    input_path = str(pdf_file)
    output_path = str(output_pdf_file or pdf_file)

    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(metadata)

    with open(output_path, "wb") as file:
        writer.write(file)
