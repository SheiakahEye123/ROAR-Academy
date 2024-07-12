import PyPDF2
import os

try:
    source = "Sense-and-Sensibility-by-Jane-Austen.pdf"
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)

except:
    exit

pdfReader = PyPDF2.PdfReader(open(path+"/"+source, "rb"))

dictionary = dict()

page_number = len(pdfReader.pages)   # this tells you total pages 

for i in range(page_number):
    page_object = pdfReader.pages[i]    # We just get page 0 as example 
    page_text = page_object.extract_text()   # this is the str type of full page

    lines = page_text.split('\n')
    
    for s in lines[3:]:
        for word in s.split(" "):
            if not word[-1].isalpha

            sheikaheye123


    if i == 0:
        print(lines[3:])


