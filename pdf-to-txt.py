import os
import tkinter as tk
from tkinter import filedialog
import pdfplumber

def select_pdfs():
    """
    Opens a GUI dialog for the user to select PDF files.
    Returns the list of selected file paths.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_paths = filedialog.askopenfilenames(
        title="Select PDF files for conversion",
        filetypes=[("PDF Files", "*.pdf")],
    )
    return file_paths

def convert_pdf_to_text(pdf_path):
    """
    Converts a PDF file to plain text and saves it in the same directory as the PDF.
    Args:
        pdf_path (str): Path to the PDF file.
    """
    try:
        print(f"Processing: {pdf_path}")
        # Read the PDF with pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page_number, page in enumerate(pdf.pages, start=1):
                try:
                    text += page.extract_text() or ""
                    print(f" - Extracted text from page {page_number}.")
                except Exception as e:
                    print(f" ! Warning: Could not extract text from page {page_number}: {e}")
        
        # Define the output path
        output_path = os.path.splitext(pdf_path)[0] + ".txt"
        
        # Write the text to a .txt file
        with open(output_path, "w", encoding="utf-8") as text_file:
            text_file.write(text)
        print(f" - Successfully saved text to: {output_path}")
    except Exception as e:
        print(f"Error processing file {pdf_path}: {e}")

def main():
    print("PDF to Text Converter (Interactive)")
    print("====================================")
    
    while True:
        # Select PDF files
        pdf_files = select_pdfs()
        if not pdf_files:
            print("No files selected. Exiting.")
            break
        
        # Process each selected PDF
        for pdf_path in pdf_files:
            convert_pdf_to_text(pdf_path)
        
        # Ask the user if they want to process another file
        while True:
            user_choice = input("Do you want to convert another file? (Y/n): ").strip().lower()
            if user_choice in ['y', 'n', '']:
                break
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        
        if user_choice == 'n':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()
