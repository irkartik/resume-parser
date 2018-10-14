from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import os
from django.conf import settings

# def convertPDFToText(path):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     codec = 'utf-8'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#     fp = file(path, 'rb')
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos=set()
#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         interpreter.process_page(page)
#     fp.close()
#     device.close()
#     string = retstr.getvalue()
#     retstr.close()
#     return string

def convertPDFToText(path):
    import textract
    # path= os.path.join(settings.BASE_DIR, path)
    # path = os.path.abspath(path)
    # print(path)
    text = textract.process(path)
    return text


def convertRtfToText(path):
	import textract
	text = textract.process(path)
	return text

def convertDocxToText(path):
	import textract
	text = textract.process(path)
	return text


def convertRtfToText(path):
	import textract
	text = textract.process(path)
	return text

def convertDocxToText(path):
	import textract
	text = textract.process(path)
	return text