import fitz


def replace_text_in_pdf(input_pdf_path, output_pdf_path, replacements):
    pdf_document = fitz.open(input_pdf_path)
    page = pdf_document.load_page(0)

    point = fitz.Point(175, 105)

    text = "Abbas Rahimzadeh"

    page.insert_text(point, text, fontsize=8, color=(0, 0, 0))

    pdf_document.save(output_pdf_path)


# Example usage


input_pdf_path = "final.pdf"
output_pdf_path = "output.pdf"
replacements = {
    "First name": "Abbas",
    "Gender": "Ali",
    # Add more replacements as needed
}

replace_text_in_pdf(input_pdf_path, output_pdf_path, replacements)
