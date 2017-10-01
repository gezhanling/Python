import sys
import os
import shutil

from PyQt4 import QtGui, QtCore, uic
from __builtin__ import file
qtCreatorFile = "D:\ADINA_again\ADINA.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.ChangeV)
        self.volt_seek.clicked.connect(self.YaDian)
        self.go_to_exe.clicked.connect(self.GoToExe)

    def ChangeV(self):
        velocity = str(self.price_box.toPlainText())
        f = open("D:\C-example05f.in","r")
        f.seek(9536,0)
        first = str(f.read(7))
        with open("D:\C-example05f.in","r") as f:
            lines = f.readlines()
        with open("D:\C-example05f.in","w") as f_w:
            for line in lines:
                line = line.replace(first,velocity)
                f_w.write(line)
        f.close()
        f_w.close()                        
    def GoToExe(self):
        os.system(r'"D:\adina.bat"')
        
    def YaDian(self):
        voltFile = open("D:\\ADINA_again\\v1.10_3u.txt","r")
        i = 241
        while voltFile.tell()<38668:
            voltFile.seek(i,1)
            time = voltFile.read(11)
            voltFile.seek(4,1)
            disL = voltFile.read(12)
            i=5
            basePath = 'D:\\ADINA_again\\'
            timePath = basePath + time
            if not os.path.exists(timePath):
                os.mkdir(timePath)
            f = open("D:\\ADINA_again\\WanZheng.in","r")
            f.seek(7818,0)
            dis = f.read(12)
            with open("D:\\ADINA_again\\WanZheng.in","r") as f:
                lines = f.readlines()
            with open("D:\\ADINA_again\\WanZheng.in","w") as f_w:
                for line in lines:
                    if dis in line:
                        line = line.replace(dis,disL)
                    f_w.write(line)                    
                    os.system(r'"D:\\ADINA_again\\VOLT.bat"')
                    a = open('D:\\ADINA_again\\listVoltage.txt')
                    lines = a.readlines()
                    lists = []
                    new = []
                    for line in lines:
                        lists.append(line.split())
                    m = lists[119:170]
                    for i in m:
                        for j in i:
                            new.append(j)
                    new = new[1::2]
                    if new[0]<0:
                        maxV = min(new)
                    else:
                        maxV = max(new)
                    f=open('D:\\ADINA_again\\max.txt','a')
                    f.write(time+'    '+maxV)
                    f.write('\n')
                    f.close()  
                    shutil.move("D:\\ADINA_again\\yunTu.jpg","D:\\ADINA_again\\"+time+"\\") 
                    shutil.move("D:\\ADINA_again\\voltage.jpg","D:\\ADINA_again\\"+time+"\\")
                    shutil.move("D:\\ADINA_again\\listVoltage.txt","D:\\ADINA_again\\"+time+"\\")                     
                      
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())