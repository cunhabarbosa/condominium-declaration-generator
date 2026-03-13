"""Main entry point for the condominium declaration generator."""

from pathlib import Path
from typing import Any, Dict, Tuple

from src.config_loader import load_config
from src.date_utils import generate_date, parse_date
from src.money_utils import format_money
from src.fraction_utils import get_fraction_info
from src.docx_generator import generate_docx
from src.pdf_utils import generate_pdf, add_pdf_metadata
from src.file_utils import validate_file_exists


def generate_filename(date_str: str, floor: str, apartment: str) -> str:
    """
    Generate the output filename in the format:
    YYYY-MM-DD - 5AP4
    """
    date_obj = parse_date(date_str)
    date_iso = date_obj.strftime("%Y-%m-%d")
    return f"{date_iso} - {floor}AP{apartment}"


def build_placeholders(config: Dict[str, Any]) -> Tuple[Dict[str, str], str, str]:
    """Build the placeholder dictionary for the template."""
    fraction, floor, apartment = get_fraction_info(config["fraction"])

    declaration_date_long, declaration_date_short = generate_date(
        config.get("declaration_date")
    )
    settlement_date_long, _ = generate_date(config["settlement_date"])

    annual_value_str, annual_value_text = format_money(config["annual_value"])
    monthly_value_str, monthly_value_text = format_money(config["monthly_value"])

    placeholders = {
        "{{DATA_EXTENSO}}": declaration_date_long,
        "{{DATA_CURTA}}": declaration_date_short,
        "{{FRACAO}}": fraction,
        "{{ANDAR}}": floor,
        "{{APART}}": apartment,
        "{{DATA_LIQUIDACAO}}": settlement_date_long,
        "{{VALOR_ANUAL}}": annual_value_str,
        "{{VALOR_ANUAL_EXTENSO}}": annual_value_text,
        "{{VALOR_MENSAL}}": monthly_value_str,
        "{{VALOR_MENSAL_EXTENSO}}": monthly_value_text,
    }

    return placeholders, floor, apartment


def build_pdf_metadata(config: Dict[str, Any], placeholders: Dict[str, str]) -> Dict[str, str]:
    """Build PDF metadata dictionary."""
    metadata_config = config.get("pdf_metadata", {})

    return {
        "/Title": metadata_config.get("title", "Declaração de encargos do Condomínio"),
        "/Author": metadata_config.get("author", "Condomínio Molares 16"),
        "/Subject": metadata_config.get(
            "subject",
            f"Declaração para efeitos da alienação da fração {placeholders['{{FRACAO}}']}"
        ),
        "/Keywords": metadata_config.get(
            "keywords",
            "condomínio, declaração, alienação, encargos"
        ),
        "/Creator": metadata_config.get("creator", "Python generator"),
        "/Producer": metadata_config.get("producer", "docx2pdf + pypdf"),
    }


def print_placeholders(placeholders: dict[str, str]) -> None:
    """Print placeholders in a readable table format."""

    print("\nPlaceholders used in the document:")
    print("-" * 50)

    max_key = max(len(k) for k in placeholders)

    for key, value in placeholders.items():
        print(f"{key:<{max_key}} : {value}")

    print("-" * 50)


def main() -> None:
    """Main entry point."""

    config_path = validate_file_exists("config.json", "Configuration file")
    config = load_config(config_path)

    placeholders, floor, apartment = build_placeholders(config)

    _, declaration_date_short = generate_date(config.get("declaration_date"))
    filename = generate_filename(declaration_date_short, floor, apartment)

    template_file = validate_file_exists(
        config.get("template_file", "template.docx"),
        "Template file"
    )

    output_dir = Path(config.get("output_dir", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    print_placeholders(placeholders)

    docx_file = output_dir / f"{filename}.docx"
    pdf_file = output_dir / f"{filename}.pdf"

    generate_docx(
        template_file=template_file,
        output_file=docx_file,
        placeholders=placeholders
    )

    if config.get("generate_pdf", True):
        generate_pdf(docx_file=docx_file, pdf_file=pdf_file)
        pdf_metadata = build_pdf_metadata(config, placeholders)
        add_pdf_metadata(pdf_file=pdf_file, metadata=pdf_metadata)

    print(f"Generated DOCX: {docx_file}")
    if config.get("generate_pdf", True):
        print(f"Generated PDF:  {pdf_file}")


if __name__ == "__main__":
    main()