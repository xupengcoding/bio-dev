from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog
import sys
import bio_ui
import bio_img
import bio_tab_ui
import bio_param_ui
import numpy as np
from PIL import Image
import os
import jpype
import matplotlib  
import matplotlib.cm as cm  
import matplotlib.pyplot as plt

class ParamDialog(QDialog, bio_param_ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(ParamDialog, self).__init__(parent)
        self.setupUi(self)
        self.max_pixel = 100000
        self.min_pixel = 0
        self.fit_a = 1
        self.fit_b = 0
        self.textEdit_max_pixel.setPlainText(str(self.max_pixel))
        self.textEdit_min_pixel.setPlainText(str(self.min_pixel))
        self.textEdit_fitparam_a.setPlainText(str(self.fit_a))
        self.textEdit_fitparam_b.setPlainText(str(self.fit_b))
        #self.buttonBox.clicked.connect(self.buttonOK)
        self.buttonBox.accepted.connect(self.buttonOK)
        self.buttonBox.rejected.connect(self.buttonCancel)
    def buttonOK(self):
        #if button == QtWidgets.QDialogButtonBox.Cancel:
            #print (button)
        self.max_pixel = int(self.textEdit_max_pixel.toPlainText())
        self.min_pixel = int(self.textEdit_min_pixel.toPlainText())
        self.fit_a = int(self.textEdit_fitparam_a.toPlainText())
        self.fit_b = int(self.textEdit_fitparam_b.toPlainText())
        #self.done(self)
        #print(self.textEdit_fitparam_a.toPlainText())
    def buttonCancel(self):
        self.textEdit_max_pixel.setPlainText(str(self.max_pixel))
        self.textEdit_min_pixel.setPlainText(str(self.min_pixel))
        self.textEdit_fitparam_a.setPlainText(str(self.fit_a))
        self.textEdit_fitparam_b.setPlainText(str(self.fit_b))

class MainWindow(QMainWindow, bio_tab_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.label_input_image1.setPixmap(QPixmap("test.jpg"))
        self.input_image1_path = ""
        self.input_image1_type = ""
        self.input_image2_path = ""
        self.input_image2_type = ""
        #ndarray to store image, all grayscale
        self.input_image1 = np.zeros((0))
        self.input_image2 = np.zeros((0))
        self.ratio_image = np.zeros((0))
        self.fitted_image = np.zeros((0))
        self.cropped_ratio_image = np.zeros((0))
        self.fitted_image = np.zeros((0))
        #parames
        #self.max_pixel = 255
        #self.min_pixel = 0
        #self.fit_a = 1
        #self.fit_b = 0
        self.pooling_ratio = 2
        self.tmp_input_image1_path = "tmp_input_img1.png"
        self.tmp_input_image2_path = "tmp_input_img2.png"
        self.tmp_ration_image_path = "tmp_ration_img.png"
        self.tmp_fitted_image_path = "tmp_fitted_img.png"
        self.param_dialog = ParamDialog()
        #init imgprocess
        self.img_process = bio_img.ImgProcess()
        #bind signals
        self.actionOpen.triggered.connect(self.Open)
        self.actionFitting_param.triggered.connect(self.paramSet)
        self.actionPooling.triggered.connect(self.imgPooling)
        self.actionCalc.triggered.connect(self.CalcFittedImage)
        #self.tab_curIdx = self.ImgShowWidget.currentIndex()
        self.ImgShowWidget.tabBarClicked.connect(self.tabBarClicked)

    def tabBarClicked(self, index):
        #print(index)
        if index == 2:
            if self.input_image1.shape[0] and self.input_image2.shape[0]:
                #calc ratio image
                self.ratio_image = self.input_image1 / self.input_image2
                #draw it
                self.ratio_image_canvas.axes.imshow(self.ratio_image, cmap=matplotlib.cm.gray)
                self.ratio_image_canvas.draw()
                return

    def paramSet(self):
        """
        param
        """
        self.param_dialog.show()

    def imgPooling(self):
        if self.input_image1.shape[0] or self.input_image2.shape[0] == "":#the comparison is a warming
            return
        input_image1 = bio_img.averagePooling(self.pooling_ratio, self.input_image1)
        input_image2 = bio_img.averagePooling(self.pooling_ratio, self.input_image2)
        pil_img1 = Image.fromarray(input_image1)
        pil_img2 = Image.fromarray(input_image2)
        pil_img1 = pil_img1.convert('L')
        pil_img2 = pil_img2.convert('L')
        #save to tmp
        pil_img1.save(self.tmp_input_image1_path, "png")
        pil_img2.save(self.tmp_input_image2_path, "png")
        #set pixmap
        self.label_input_image1.setPixmap(QPixmap(self.tmp_input_image1_path))
        self.label_input_image2.setPixmap(QPixmap(self.tmp_input_image2_path))
        self.label_input_image1.update()
        self.label_input_image2.update()

    def Open(self):
        """
        dialog for openning files
        """
        #filename filter using ";;" to separate
        file_name, file_type = QFileDialog.getOpenFileName(
            self, "Select a file", "/", "bip (*.bip);;jpg (*.jpg);;png (*.png)")
        print(file_name, file_type)
        if self.ImgShowWidget.currentIndex() == 0:
            #print("open input_img1")
            self.input_image1_path = file_name
            self.input_image1_type = file_type
            if self.input_image1_type == 'bip (*.bip)':
                #print("open bip")
                self.input_image1 = self.img_process.imread_bip(self.input_image1_path)
                self.image1_canvas.axes.imshow(self.input_image1, cmap=matplotlib.cm.gray)
                self.image1_canvas.draw()
        elif self.ImgShowWidget.currentIndex() == 1:
            #print("open input_img1")
            self.input_image2_path = file_name
            self.input_image2_type = file_type
            if self.input_image2_type == 'bip (*.bip)':
                #print("open bip")
                self.input_image2 = self.img_process.imread_bip(self.input_image2_path)
                self.image2_canvas.axes.imshow(self.input_image2, cmap=matplotlib.cm.gray)
                self.image2_canvas.draw()
    def CalcFittedImage(self):
        '''
        calc the fitted image
        y = a*ratio + b
        '''
        ratio_xbound = self.ratio_image_canvas.axes.get_xbound()
        ratio_ybound = self.ratio_image_canvas.axes.get_ybound()
        #print(ratio_xbound)
        #print(ratio_ybound)
        #clip to the siae
        ratio_shape = self.ratio_image.shape
        crop_x = np.clip(ratio_xbound, 0, int(ratio_shape[1])).astype(np.int)
        crop_y = np.clip(ratio_ybound, 0, int(ratio_shape[0])).astype(np.int)
        self.cropped_ratio_image = self.ratio_image[crop_y[0]:crop_y[1], crop_x[0]:crop_x[1]]
        self.fitted_image = (self.cropped_ratio_image-self.param_dialog.fit_b)/self.param_dialog.fit_a
        print("%f %f"%(np.min(self.fitted_image), np.max(self.fitted_image)))
        #fit image use must find > 0
        #region = np.where(self.fitted_image>0)
        #region_y = [np.min(region[0]), np.max(region[0])]
        #region_x = [np.min(region[1]), np.max(region[1])] 
        #self.fitted_image = self.fitted_image[region_y[0]:region_y[1]+1, region_x[0]:region_x[1]+1]
        self.fitted_image = np.clip(self.fitted_image, 
                                    self.param_dialog.min_pixel, self.param_dialog.max_pixel)
        self.fitted_image_canvas.axes.imshow(self.fitted_image, cmap=matplotlib.cm.jet)
        self.fitted_image_canvas.draw()
        #self.cropped_ratio_image = self.
        '''
        if self.ImgShowWidget.currentIndex() == 0:
            self.input_image1_path = file_name
            self.input_image1 = Image.open(self.input_image1_path)
            self.input_image1 = self.input_image1.convert('L')
            self.input_image1.save(self.tmp_input_image1_path, "png")
            self.input_image1 = np.array(self.input_image1)
            self.label_input_image1.setPixmap(QPixmap(self.tmp_input_image1_path))
            self.label_input_image1.update()
        elif self.ImgShowWidget.currentIndex() == 1:
            self.input_image2_path = file_name
            self.input_image2 = Image.open(self.input_image2_path)
            self.input_image2 = self.input_image2.convert('L')
            self.input_image2.save(self.tmp_input_image2_path, "png")
            self.input_image2 = np.array(self.input_image2)
            #self.input_image1 = cv2.cvtColor(self.input_image1, cv2.COLOR_RGB2GRAY)
            #cv2.imwrite(self.tmp_input_image1_path)
            self.label_input_image2.setPixmap(QPixmap(self.tmp_input_image2_path))
            self.label_input_image2.update()
        '''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

