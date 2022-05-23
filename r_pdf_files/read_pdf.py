import sys
import importlib

importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def read_pdf(path, to_path):
    f = open(path, "rb")

    parser = PDFParser(f)

    pdf_file = PDFDocument()

    parser.set_document(pdf_file)
    pdf_file.set_parser(parser)

    pdf_file.initialize()

    if not pdf_file.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        manger = PDFResourceManager()

        laparams = LAParams()
        device = PDFPageAggregator(manger, laparams=laparams)
        interpreter = PDFPageInterpreter(manger, device)

        for page in pdf_file.get_pages():
            interpreter.process_page(page)

            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(to_path, "a") as f:
                        str = x.get_text()
                        # print(str)
                        f.write(str + "\n")


path = r"D:\PythonProject\first\r_pdf_files\p01.pdf"

to_path = r"D:\PythonProject\first\r_pdf_files\a.txt"

read_pdf(path, to_path)
