import pyttsx3
import PyPDF2
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-1].id)
pdf_file=input("Enter a file name : ")
file_page=int(input("Type from which page do you want to listen "))
with open(pdf_file,'rb') as pdfObj:
    pdfReader=PyPDF2.PdfFileReader(pdfObj)
    numpages=pdfReader.numPages
    for n in range(file_page,numpages):
        page=pdfReader.getPage(n)
        text=page.extractText()
        engine.say(text)
        engine.runAndWait()