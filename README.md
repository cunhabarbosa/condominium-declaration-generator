# Condominium Declaration Generator

Generate condominium declaration documents in DOCX and PDF format from a Word template.

This tool replaces placeholders in a `.docx` file, preserves the original formatting as much as possible, and can optionally export the result to PDF with metadata.

## Features

- Generate `.docx` files from a Word template
- Generate `.pdf` files from the generated `.docx`
- Add PDF metadata
- Fill placeholders automatically
- Convert dates to Portuguese text
- Convert money values to Portuguese text
- Generate output filenames in the format:
  - `YYYY-MM-DD - 1AP2.docx`
  - `YYYY-MM-DD - 1AP2.pdf`

## Project structure

```text
condominium-declaration-generator/
├─ main.py
├─ README.md
├─ requirements.txt
├─ config.example.json
├─ config.json          <-- local file, not committed
├─ template.docx        <-- not included in the repository
├─ src/
│  ├─ config_loader.py
│  ├─ date_utils.py
│  ├─ docx_generator.py
│  ├─ file_utils.py
│  ├─ fraction_utils.py
│  ├─ money_utils.py
│  └─ pdf_utils.py
└─ output/
```

## Requirements
- Python 3.10+
- Microsoft Word installed (required by docx2pdf on Windows)

```bash
pip install -r requirements.txt
```

## Configuration

Copy config.example.json to config.json and update the values.

