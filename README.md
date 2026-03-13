# Condominium Declaration Generator

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/github/license/cunhabarbosa/condominium-declaration-generator)
![Repo size](https://img.shields.io/github/repo-size/cunhabarbosa/condominium-declaration-generator)
![Last commit](https://img.shields.io/github/last-commit/cunhabarbosa/condominium-declaration-generator)

Generate condominium declaration documents in **DOCX and PDF format** from a Word template.

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


## Motivation

Managing condominium administration often requires generating formal declaration documents for property transactions.

This tool automates the generation of these documents from a Word template, reducing manual work and ensuring consistent formatting.


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

## Quick Start

```bash
git clone https://github.com/cunhabarbosa/condominium-declaration-generator
cd condominium-declaration-generator

pip install -r requirements.txt

cp config.example.json config.json

python main.py
```

Note:
- Adjust the configuration in `config.json` if needed.
- Make sure `template.docx` contains the required placeholders

## Template placeholders

The template file must contain the following placeholders:

```text
{{DATA_EXTENSO}}
{{DATA_CURTA}}
{{FRACAO}}
{{ANDAR}}
{{APART}}
{{DATA_LIQUIDACAO}}
{{VALOR_ANUAL}}
{{VALOR_ANUAL_EXTENSO}}
{{VALOR_MENSAL}}
{{VALOR_MENSAL_EXTENSO}}
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Created by [Antonio Barbosa](https://github.com/cunhabarbosa)