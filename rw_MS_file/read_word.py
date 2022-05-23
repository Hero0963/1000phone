import docx


def readtxt(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


print(readtxt('a001.docx'))


# ref= https://www.tutorialspoint.com/python_text_processing/python_process_word_document.htm