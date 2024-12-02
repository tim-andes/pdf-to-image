from PIL import Image
import pdf2image
import os
import tkinter as tk
from tkinter import filedialog

def convert_pdf_to_images(pdf_file, output_dir):
    # Convert PDF to images
    pages = pdf2image.convert_from_path(pdf_file)

    # Save each page as an image
    for i, page in enumerate(pages):
        output_file_name = f"page_{i+1}.jpg"
        page.save(output_dir + '/' + output_file_name)

def select_pdf():
    pdf_file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    output_dir = os.getcwd()
    # Or, pass it to your PDF processing function:
    convert_pdf_to_images(pdf_file_path, output_dir)


if __name__ == "__main__":
    select_pdf()