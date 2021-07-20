import pandas as pd
from pdf2image import convert_from_path
from clean_Image.cleanImage import cleanImg
import numpy as np
from read_Dataset.readDataset import readData

class pdfToImage:
    def __init__(self,excelPath,dataPath):
        self.excelPath=excelPath
        self.dataPath=dataPath
        readData(self.dataPath).readFileAndStoreInExcel()
        print('In pdfToImage')
    def converion(self):
        
        df=pd.read_excel(self.excelPath)
        for j in df['Filename']:           
            images = convert_from_path(self.dataPath+str(j)+".pdf",poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
            #images[0].save('Images/'+str(j)+'.png', 'PNG')
            cleanImg(np.array(images[0]),j).cleaning()
