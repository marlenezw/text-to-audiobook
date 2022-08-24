import PyPDF2, pikepdf,pyttsx3

pdf = pikepdf.open("short-story.pdf") #open and decrypt the pdf 
pdf.save('decrypted-short-story.pdf') #save the decrypted version
pdf_Reader = PyPDF2.PdfFileReader('decrypted-short-story.pdf') #read pdf

speaker = pyttsx3.init() #initiate voice

#iterate through the pages (this will read page 4 to 6)
for num in range(4,6):
    page = pdf_Reader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()