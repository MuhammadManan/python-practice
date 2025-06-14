import PyPDF2 # type: ignore
import sys
import os

def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    # Example usage: python main.py file1.pdf file2.pdf file3.pdf output.pdf
    if len(sys.argv) < 4:
        print("Usage: python main.py file1.pdf file2.pdf ... output.pdf")
        sys.exit(1)

    *input_pdfs, output_pdf = sys.argv[1:]
    for pdf in input_pdfs:
        if not os.path.exists(pdf):
            print(f"File not found: {pdf}")
            sys.exit(1)

    merge_pdfs(input_pdfs, output_pdf)
    print(f"Merged PDFs saved as {output_pdf}")