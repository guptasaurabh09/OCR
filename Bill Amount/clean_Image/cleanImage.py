import cv2

from PIL import Image

class cleanImg:
    def __init__(self,imgarr,j):
        self.imgarr=imgarr
        self.j=j
        print('In cleanImg')
    def cleaning(self):
        img = cv2.cvtColor(cv2.bilateralFilter(self.imgarr, 9, 75, 75), cv2.COLOR_BGR2GRAY)  
        thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                cv2.THRESH_BINARY,11,2)
        print('Image name: '+str(self.j)+' is cleaned')
        Image.fromarray(thresh2).save('Images/'+str(self.j)+'.png')
        
        
