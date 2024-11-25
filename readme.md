# PDF to Text Converter

This Python script converts PDF files to plain text files. It provides a graphical user interface (GUI) for selecting PDF files and saves the extracted text as `.txt` files in the same directory as the original PDFs. The script also supports an interactive mode where users can process multiple files consecutively.

## Features
- **GUI File Selection**: Users can select PDF files using a file dialog.
- **Text Extraction**: Extracts text from PDF files and saves it as `.txt`.
- **Interactive Mode**: Prompts users to convert additional files or exit the program.
- **Error Handling**: Handles errors gracefully and logs warnings for unreadable pages.

## Requirements
To run this script, you need the following Python libraries:
- `pdfplumber` - for extracting text from PDFs.
- `tkinter` - for the graphical file selection dialog (pre-installed with Python).

## Installation
1. Clone the repository or download the script.
2. Install the required dependencies using the following command:
   ```bash
   pip install -r requirements.txt
