from pytesseract import pytesseract
from PIL import Image
import pandas as pd

class imageToText:
    def __init__(self):
        pass
    
    def extractText(self):
        path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        custom_config = r'-c tessedit_char_whitelist=totalTOTAL1234567890.: --psm 6'
        pytesseract.tesseract_cmd = path_to_tesseract
        text=list()
        df=pd.read_excel('Filename/filname.xls')
        for i in df['Filename']:
            text.append(pytesseract.image_to_string(Image.open('Images/'+str(i)+'.png')  ,config=custom_config))
        return text
