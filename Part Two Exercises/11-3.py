import PyPDF2
import os
import string
import re

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
    
    for s in lines[3:-1]:
        for word in re.split(" |--|-",s):
            # if "--" in word:    
            #     for w in word.split("--"):
            #         t = w.strip(string.punctuation).lower()
            #         if t not in dictionary:
            #             dictionary[t] = 1
            #         else:
            #             dictionary[t] += 1
            # else:
            t = word.strip(string.punctuation).lower()
            if t.isdecimal() or not t.isalnum():
                continue
            if t not in dictionary:
                dictionary[t] = 1
            else:
                dictionary[t] += 1



source = "freq.txt"
print(os.path.dirname(os.path.abspath(__file__)))
try:
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)
    handle = open(path+"/"+source, "wt")
    for keys in dictionary:
        handle.write(str(keys) + " : " + str(dictionary[keys]))
        handle.write("\n")

except:
    print("Wrong!")
    exit