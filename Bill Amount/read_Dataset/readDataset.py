import os
import xlwt


class readData:
    def __init__(self,path):
        self.path=path
        print('In readDataset')
    def readFileAndStoreInExcel(self):
        datas=os.listdir(self.path)
        datas=list(datas)
        a = xlwt.Workbook(encoding='utf-8')
        s = a.add_sheet('filename',cell_overwrite_ok=True)
        s.write(0,0,'Filename')
        row=1
        for x in datas:
            s.write(row,0,x.replace('.pdf',''))
            row=row+1

        print('Filename store in excel')
        a.save('Filename/filname.xls')

