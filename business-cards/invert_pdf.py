from PIL import Image, ImageOps
import fitz  # PyMuPDF
import io

# Open the PDF
pdf_path = "front_foil.pdf"
output_path = "front_color_final.pdf"

# Open the PDF with PyMuPDF
pdf_document = fitz.open(pdf_path)

# Create a new PDF
output_pdf = fitz.open()

# Process each page
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]

    # Render page to an image at high resolution
    mat = fitz.Matrix(300/72, 300/72)  # 300 DPI
    pix = page.get_pixmap(matrix=mat, alpha=False)

    # Convert to PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Invert the image (swap black and white)
    inverted_img = ImageOps.invert(img)

    # Save inverted image to bytes buffer as PNG
    img_buffer = io.BytesIO()
    inverted_img.save(img_buffer, format='PNG')
    img_bytes = img_buffer.getvalue()

    # Create a new page in output PDF with same dimensions
    new_page = output_pdf.new_page(width=page.rect.width, height=page.rect.height)

    # Insert the inverted image
    img_rect = new_page.rect
    new_page.insert_image(img_rect, stream=img_bytes)

# Save the output PDF
output_pdf.save(output_path)
output_pdf.close()
pdf_document.close()

print(f"Inverted PDF saved as {output_path}")
