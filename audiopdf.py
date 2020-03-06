import PyPDF2
import pyttsx3


def extract_text(filename):
	"""
	function to extract text from pdf at given filename
	"""
	pdfFileObj = open(filename, "rb")
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	mytext = ""

	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		mytext += pageObj.extractText()

	pdfFileObj.close()

	return mytext


def speak_text(text):
	"""
	function to invoke TTS engine to speak the pdf text
	"""
	engine = pyttsx3.init()
	engine.setProperty('rate', 150)
	engine.setProperty('voice', 'en+m7')
	engine.say(text)
	engine.runAndWait()


if __name__ == "__main__":
	text = extract_text("YourPdf File.pdf") #Enter Your Pdf File
	speak_text(text)