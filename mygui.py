import os
from GoogleOcr import extract_text
from PyQt5 import QtCore, QtGui, QtWidgets

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Adhithya\Desktop\julia_economics\skillful-fx-314503-1559df828651.json"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.files = []
        self.fileIdx = 0
        self.filePath = ''
        self.txtFilePath = ''
        self.getTextSafetyFlag = False
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 450)
        # MainWindow.setMaximumSize(QtCore.QSize(1050, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1024, 250))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("default.png"))
        self.label.setObjectName("label")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 255, 1024, 200))
        font = QtGui.QFont()
        font.setFamily("French Script MT")
        font.setPointSize(22)
        self.textEdit.setFont(font)
        self.textEdit.setText("Choose a file for text")
        self.textEdit.setObjectName("textEdit")
        
        self.Load = QtWidgets.QPushButton(self.centralwidget)
        self.Load.setGeometry(QtCore.QRect(160, 400, 75, 25))
        self.Load.setObjectName("Load")
        self.Load.clicked.connect(self.loadFnc)
                
        self.Prev = QtWidgets.QPushButton(self.centralwidget)
        self.Prev.setGeometry(QtCore.QRect(300, 400, 75, 25))
        self.Prev.setObjectName("Prev")
        self.Prev.clicked.connect(self.prevFnc)
        
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(440, 400, 75, 25))
        self.Next.setObjectName("Next")
        self.Next.clicked.connect(self.nextFnc)
        
        self.GetText = QtWidgets.QPushButton(self.centralwidget)
        self.GetText.setGeometry(QtCore.QRect(580, 400, 75, 25))
        self.GetText.setObjectName("GetText")
        self.GetText.clicked.connect(self.getTextFnc)
        
        self.SaveText = QtWidgets.QPushButton(self.centralwidget)
        self.SaveText.setGeometry(QtCore.QRect(720, 400, 75, 25))
        self.SaveText.setObjectName("SaveText")
        self.SaveText.clicked.connect(self.saveTextFnc)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataEnty"))
        self.textEdit.setText("Choose a file for text")
        self.Next.setText(_translate("MainWindow", "Next"))
        self.Prev.setText(_translate("MainWindow", "Prev"))
        self.GetText.setText(_translate("MainWindow", "Get Text"))
        self.SaveText.setText(_translate("MainWindow", "Save text"))
        self.Load.setText(_translate("MainWindow", "Load"))


    def loadFnc(self):
        if self.getTextSafetyFlag:
            self.saveTextFnc()
        
        self.dirName =  QtWidgets.QFileDialog.getExistingDirectory(None, 'Open working directory', os.getcwd(), QtWidgets.QFileDialog.ShowDirsOnly)
        files = os.listdir(self.dirName)
        self.files = [file for file in files if file.find('.png') > -1]
        
        if len(self.files) < 1:
            print('No Image files found')
        else:            
            self.fileIdx = 0
            self.filePath = self.dirName + r'\\' + self.files[self.fileIdx]
            self.label.setPixmap(QtGui.QPixmap(self.filePath))
            
            
        
    def nextFnc(self):
        if self.getTextSafetyFlag:
            self.saveTextFnc()
            
        if self.fileIdx < len(self.files)-1:
            self.fileIdx += 1            
            self.filePath = self.dirName + r'\\' + self.files[self.fileIdx]
            self.label.setPixmap(QtGui.QPixmap(self.filePath))
            self.getTextFnc()
            print(self.filePath)
        
        
    def prevFnc(self):
        if self.getTextSafetyFlag:
            self.saveTextFnc()
            
        if self.fileIdx >= 1 :
            self.fileIdx -= 1
            self.filePath = self.dirName + r'\\' + self.files[self.fileIdx]
            self.label.setPixmap(QtGui.QPixmap(self.filePath))
            self.getTextFnc()
            print(self.filePath)
        
        
        
    def getTextFnc(self):
        if not self.filePath == '':
            self.txtFilePath = self.filePath[:-3] + 'txt'
            self.getTextSafetyFlag = True
            
            if os.path.isfile(self.txtFilePath):
                print ("File exist")
                print('I am in if')
                fid = open(self.txtFilePath,'r')
                text = fid.read()
                self.textEdit.setText(text)
                fid.close()
            else:
                # self.textEdit.setText('OCR text request will be made')
                self.textEdit.setText(extract_text(self.filePath,'result.png'))
            
                
    def saveTextFnc(self):
        if not self.txtFilePath == '':
            print('i am in savetext if')
            print(self.txtFilePath)
            file = open(self.txtFilePath,"w")
            text =  (self.textEdit.toPlainText().encode('ascii', 'ignore')).decode()
            file.write(text)
            file.close()
            self.getTextSafetyFlag = False
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
