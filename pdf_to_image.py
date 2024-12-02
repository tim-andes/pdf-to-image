from PIL import Image
import pdf2image
import os

def convert_pdf_to_images(pdf_file, output_dir):
    # Convert PDF to images
    pages = pdf2image.convert_from_path(pdf_file)

    # Save each page as an image
    for i, page in enumerate(pages):
        output_file_name = f"page_{i+1}.jpg"
        page.save(output_dir + '/' + output_file_name)

# Usage
pdf_file = "C:\\Users\\Tim\\Documents\\code\\pdf-to-image\\DOC_0000015418.pdf"
output_dir = "C:\\Users\\Tim\\Documents\\code\\pdf-to-image"

convert_pdf_to_images(pdf_file, output_dir)

if __name__ == "__main__":
    convert_pdf_to_images(pdf_file, output_dir)