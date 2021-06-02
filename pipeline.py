import os
import cv2
import imutils
# import pytesseract
from pdf2image import convert_from_path

def SavePdfDir2Images(dirName):
    files = os.listdir(dirName)

    for file in files:
        pages = convert_from_path(dirName + '/' + file)
        #count = 1
        for page in pages:
            # page.save('Images' + '/' + file[:-4] + str(count) + '.png')
            page.save('Images' + '/' + file[:-4] + '.png')
            img = cv2.imread('Images' + '/' + file[:-4] + '.png')            
            resizeimg = imutils.resize(img, width=1024)
            cv2.imwrite('Images' + '/' + file[:-4] + '.png', resizeimg)
            #count = count + 1
            
def ExtractLinesDir(dirName):
    os.mkdir('temp31')
    files = os.listdir(dirName)
    
    for file in files:
        ExtractLinesFile(file)
        
def ExtractLinesFile(fileName):
  folderName = r'temp31\\' + fileName[:-4]
  os.mkdir(folderName)

  myfile = cv2.imread(r'Images\\' + fileName)

  count = 1
  print(folderName)
  cv2.imwrite(folderName + '\\' + fileName, myfile)
  for i in range(0,myfile.shape[0],115):
    i = i + 65
    myline = myfile[i:i+115, 0:myfile.shape[1]]
    if count < 10:
        cv2.imwrite(folderName + '\\' + 'line0' + str(count) + '.png', myline)
    else:
        cv2.imwrite(folderName + '\\' + 'line' + str(count) + '.png', myline)
                # imutils.resize(myline, width = 1024))
    count = count + 1
    
  print(folderName)
        
            
# SavePdfDir2Images('Testing')
ExtractLinesDir('Images')