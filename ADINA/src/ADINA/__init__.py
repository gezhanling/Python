import sys
import os

from PyQt4 import QtGui, QtCore, uic
from __builtin__ import file
qtCreatorFile = "D:\ADINA.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.CalculateTax)
        self.volt_seek.clicked.connect(self.file_dialog)
        self.go_to_exe.clicked.connect(self.GoToExe)

    def CalculateTax(self):
        velocity = str(self.price_box.toPlainText())
        f = open("D:\C-example05f.in","r")
        f.seek(9536,1)
        global first
        first = str(f.read(7))
        if self.Judge() == 1:
            with open("D:\C-example05f.in","r") as f:
                lines = f.readlines()
            with open("D:\C-example05f.in","w") as f_w:
                for line in lines:
                    if first in line:
                        line = line.replace(first,velocity)
                    f_w.write(line)
                global prior
                prior = velocity
        else:
            with open("D:\C-example05f.in","r") as f:
                lines = f.readlines()
            with open("D:\C-example05f.in","w") as f_w:
                for line in lines:
                    if prior in line:
                        line = line.replace(prior,velocity)
                    f_w.write(line)
        prior = velocity    
                                
    def GoToExe(self):
        os.system(r'"D:\adina.bat"')
        
    def file_dialog(self):
        voltFile = open("D:\\voltInput.txt","r")
        i = 5
        while voltFile.tell()<58:
            voltFile.seek(i,1)
            voltL = voltFile.read(5)
            i = 7
            f = open("D:\WanZheng.in","r")
            f.seek(7819,0)
            volt = f.read(5)
            with open("D:\WanZheng.in","r") as f:
                lines = f.readlines()
            with open("D:\WanZheng.in","w") as f_w:
                for line in lines:
                    if volt in line:
                        line = line.replace(volt,voltL)
                    f_w.write(line)
                    #add the .bat
        
            
            
            
        #file_name = QtGui.QFileDialog.getOpenFileName(self,"open file dialog","C:\Users\zhanling_ge\Desktop","Txt files(*.txt)") 
        #with open(file_name,"r") as f:
            #my_txt = f.read()
            #self.textEdit.setPlainText(my_txt)
        
    def Judge(self):
        with open("D:\C-example05f.in","r") as f:
            lines = f.readlines()    
            for line in lines:
                if first in line:
                    return 1
             
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())