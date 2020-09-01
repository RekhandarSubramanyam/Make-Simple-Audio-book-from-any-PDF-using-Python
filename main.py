import pyttsx3
import PyPDF2
from tkinter.filedialog import *
book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()