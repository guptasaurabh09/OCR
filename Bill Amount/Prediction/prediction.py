import statistics
import re

class Predict:
    def __init__(self,textList):
        self.textList=textList
        
    def make_predictons(self):
        
        k=[]
        for i in self.textList:
            k.append(i.split('\n'))
        for i in k:
            j=0
            while j<len(i):
                result1=re.search(r"subtotal", i[j].lower())
                result2=re.search(r"total", i[j].lower())
                result3=re.search(r"amount", i[j].lower())
                result4=re.search(r"cash", i[j].lower())
                result5=re.search(r"\€", i[j].lower())  
                result6=re.search(r"\$", i[j].lower())
                result7=re.search(r"stay", i[j].lower())
                result8=re.search(r"due", i[j].lower())
                if result1==None and result2==None and result3==None and result4==None and result5==None and result6==None and result7==None and result8 ==None:
                    i.pop(j)
                else:
                    j=j+1
        final=[]
        
        for i in range(len(k)):
            temp=[]
            for j in range(len(k[i])):
                result=re.findall("\d+\.\d+",k[i][j])
                if len(result)>0:
                    temp.append(float(result[0]))
                if len(result)==0:
                    result=re.findall("\d+ \.\d+",k[i][j])
                    if len(result)>0:
                        formatted_result = result[0].replace(' ','').strip()
                        temp.append(float(formatted_result))
                if  re.findall("€",k[i][j]):
                    result_euro=re.findall("\d{0,},\d{0,}",k[i][j])
                    if len(result_euro)>0:
                        formatted_result = result_euro[0].replace(',','').strip()
                        temp.append(float(formatted_result))
                        
            
            if len(temp)==0:
                final.append(0)
            else:
                final.append(max(temp))               
                
        for i in range(len(final)):
            if final[i]==0:
                final[i]=statistics.median(final)
                
        return final
