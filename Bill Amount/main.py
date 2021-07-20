
from PDF_to_image_conversion.pdfToImage import pdfToImage
from Image_to_text_conversion.imgaeToText_conversion import imageToText
import pandas as pd
from Prediction.prediction import Predict
import numpy as np

def main():
    print('Program started')
    pdfToImage('Filename/filname.xls','Dataset/').converion()
    df=pd.read_excel('Filename/filname.xls')
    text=imageToText().extractText()
    amount=Predict(text).make_predictons()
    df['Amount'] = [np.round(x,2) for x in amount]
    df.to_csv('Submission/submission.csv',index=False)

if __name__ == '__main__':
    main()
