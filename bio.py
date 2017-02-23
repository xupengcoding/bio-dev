from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox 
import sys
import bio_ui
import bio_img
import bio_tab_ui
import bio_param_ui
import numpy as np
from PIL import Image
import copy
import os
import jpype
import matplotlib  
import matplotlib.cm as cm  
import matplotlib.pyplot as plt
from scipy import interpolate

class ParamDialog(QDialog, bio_param_ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(ParamDialog, self).__init__(parent)
        self.setupUi(self)
        self.max_pixel = 100000
        self.min_pixel = 0
        self.fit_a = 1.
        self.fit_b = 0.
        self.compound_threshold = 0.
        self.cmap_min = -1.
        self.cmap_max = -1.
        self.textEdit_max_pixel.setPlainText(str(self.max_pixel))
        self.textEdit_min_pixel.setPlainText(str(self.min_pixel))
        self.textEdit_fitparam_a.setPlainText(str(self.fit_a))
        self.textEdit_fitparam_b.setPlainText(str(self.fit_b))
        self.textEdit_compound_threshold.setPlainText(str(self.compound_threshold))
        self.textEdit_cmap_min.setPlainText(str(self.cmap_min))
        self.textEdit_cmap_max.setPlainText(str(self.cmap_max))
        #self.buttonBox.clicked.connect(self.buttonOK)
        self.buttonBox.accepted.connect(self.buttonOK)
        self.buttonBox.rejected.connect(self.buttonCancel)
    def buttonOK(self):
        #if button == QtWidgets.QDialogButtonBox.Cancel:
            #print (button)
        self.max_pixel = int(self.textEdit_max_pixel.toPlainText())
        self.min_pixel = int(self.textEdit_min_pixel.toPlainText())
        self.fit_a = float(self.textEdit_fitparam_a.toPlainText())
        self.fit_b = float(self.textEdit_fitparam_b.toPlainText())
        self.compound_threshold = float(self.textEdit_compound_threshold.toPlainText())
        #self.done(self)
        #print(self.textEdit_fitparam_a.toPlainText())
        self.cmap_min = float(self.textEdit_cmap_min.toPlainText())
        self.cmap_max = float(self.textEdit_cmap_max.toPlainText())
    def buttonCancel(self):
        self.textEdit_max_pixel.setPlainText(str(self.max_pixel))
        self.textEdit_min_pixel.setPlainText(str(self.min_pixel))
        self.textEdit_fitparam_a.setPlainText(str(self.fit_a))
        self.textEdit_fitparam_b.setPlainText(str(self.fit_b))
        self.textEdit_compound_threshold.setPlainText(str(self.compound_threshold))
        self.textEdit_cmap_min.setPlainText(str(self.cmap_min))
        self.textEdit_cmap_max.setPlainText(str(self.cmap_max))

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
        self.input_image1 = np.zeros((0))#image1 is the background image
        self.input_image2 = np.zeros((0))#image2 is the fluorescence
        self.back_image = np.zeros((0))
        self.fluorescence_image = np.zeros((0))
        self.compound_rgb = np.zeros((0))
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
        #self.actionPooling.triggered.connect(self.imgPooling)
        self.actionCalc.triggered.connect(self.CalcFittedImage)
        #self.tab_curIdx = self.ImgShowWidget.currentIndex()
        self.ImgShowWidget.tabBarClicked.connect(self.tabBarClicked)

    def tabBarClicked(self, index):
        #print(index)
        if index == 2:
            if not self.input_image1.shape == self.input_image2.shape:
                reply = QMessageBox.warning(
                    self,"Error", "Please use two images with the same shape to calculate ratio image!", 
                    QMessageBox.Yes | QMessageBox.No)
                return
            if self.input_image1.shape[0] and self.input_image2.shape[0]:
                #calc ratio image
                self.ratio_image = self.input_image1 / self.input_image2
                #draw it
                self.ratio_image_canvas.fig.clear()
                self.ratio_image_canvas.axes = self.ratio_image_canvas.fig.add_subplot(111)
                ratio_img = self.ratio_image_canvas.axes.imshow(self.ratio_image, cmap=matplotlib.cm.jet)
                #self.ratio_image_canvas.fig.c
                self.ratio_image_canvas.fig.colorbar(ratio_img)
                self.ratio_image_canvas.draw()
                return
        if index == 4:
            if self.input_image1.shape[0] and self.input_image2.shape[0]:
                self.CalcFlorescenceImage()

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
        #print(file_name, file_type)
        if self.ImgShowWidget.currentIndex() == 0:
            #print("open input_img1")
            self.input_image1_path = file_name
            self.input_image1_type = file_type
            if self.input_image1_type == 'bip (*.bip)':
                #print("open bip")
                self.input_image1 = self.img_process.imread_bip(self.input_image1_path)
                self.image1_canvas.fig.clear()
                self.image1_canvas.axes = self.image1_canvas.fig.add_subplot(111)
                img1 = self.image1_canvas.axes.imshow(self.input_image1, cmap=matplotlib.cm.gray)
                self.image1_canvas.fig.colorbar(img1)
                self.image1_canvas.draw()
        elif self.ImgShowWidget.currentIndex() == 1:
            #print("open input_img1")
            self.input_image2_path = file_name
            self.input_image2_type = file_type
            if self.input_image2_type == 'bip (*.bip)':
                #print("open bip")
                self.input_image2 = self.img_process.imread_bip(self.input_image2_path)
                self.image2_canvas.fig.clear()
                self.image2_canvas.axes = self.image2_canvas.fig.add_subplot(111)
                img2 = self.image2_canvas.axes.imshow(self.input_image2, cmap=matplotlib.cm.gray)
                self.image2_canvas.fig.colorbar(img2)
                self.image2_canvas.draw()
    def CalcFittedImage(self):
        '''
        calc the fitted image
        y = a*ratio + b
        '''
        if not self.ratio_image.shape[0]:
            reply = QMessageBox.warning(
                self,"Error", "Please generate ratio image before calculating the fitted image!", 
                QMessageBox.Yes | QMessageBox.No)
            return
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
        #print("fitted image range: %f %f"%(np.min(self.fitted_image), np.max(self.fitted_image)))
        self.fitted_image = np.clip(self.fitted_image, 
                                    self.param_dialog.min_pixel, self.param_dialog.max_pixel)
        self.fitted_image_canvas.fig.clear()
        self.fitted_image_canvas.axes = self.fitted_image_canvas.fig.add_subplot(111)
        #if self.param_dialog.cmap_max > self.param_dialog.cmap_min \
            #and self.param_dialog.cmap_min >= 0:
        cmap_min = self.param_dialog.cmap_min
        cmap_max = self.param_dialog.cmap_max
        if cmap_min == -1.:
            cmap_min = np.min(self.fitted_image)
        if cmap_max == -1.:
            cmap_max = np.max(self.fitted_image)
        fitted_img = self.fitted_image_canvas.axes.imshow(
            self.fitted_image, cmap=matplotlib.cm.jet,
            vmin=cmap_min, vmax=cmap_max)
        #else:
            #fitted_img = self.fitted_image_canvas.axes.imshow(self.fitted_image, cm.jet)
        self.fitted_image_canvas.fig.colorbar(fitted_img)
        self.fitted_image_canvas.draw()
    def CalcFlorescenceImage(self):
        '''
        calc florescenceImage(self):
        add a param min_val
        '''
        #resize to bk-image1
        #image1_shape = self.input_image1.shape
        #image2_shape = self.input_image2.shape
        self.back_image = copy.deepcopy(self.input_image1)
        self.fluorescence_image = copy.deepcopy(self.input_image2)
        bk_shape = self.back_image.shape
        fl_shape = self.fluorescence_image.shape
        if bk_shape[0] != fl_shape[0] or bk_shape[1] != fl_shape[1]:
            fl_tmp_img = copy.deepcopy(self.fluorescence_image)
            fl_tmp1_img = np.zeros((fl_shape[0], bk_shape[1]))
            for i in range(fl_shape[0]):
                x = np.linspace(0, 1, fl_shape[1])
                fl_interp1d = interpolate.interp1d(x, fl_tmp_img[i,:], kind='linear')
                x_new = np.linspace(0, 1, bk_shape[1])
                fl_tmp1_img[i,:] = fl_interp1d(x_new)
            fl_tmp_img = copy.deepcopy(fl_tmp1_img)
            fl_tmp1_img = np.zeros((bk_shape[1], bk_shape[0]))
            fl_tmp_img = np.transpose(fl_tmp_img)
            for i in range(bk_shape[1]):
                x = np.linspace(0, 1, fl_shape[0])
                fl_interp1d = interpolate.interp1d(x, fl_tmp_img[i,:], kind='linear')
                x_new = np.linspace(0, 1, bk_shape[0])
                fl_tmp1_img[i,:] = fl_interp1d(x_new)
            fl_tmp1_img = np.transpose(fl_tmp1_img)
            self.fluorescence_image = fl_tmp1_img
        #process bk-img:input_image1
        fl_shape = self.fluorescence_image.shape
        #clip bk-img
        self.back_image = np.clip(self.back_image, 0, np.max(self.back_image))
        self.back_image = self.back_image / np.max(self.back_image)
        self.back_image = self.back_image * 255
        self.back_image = self.back_image + 1
        #process fl_image
        self.fluorescence_image = self.fluorescence_image / np.max(self.fluorescence_image)
        
        #use threshold to filt the fluorescence image
        #print('compound threshold: %f'%self.param_dialog.compound_threshold)
        self.fluorescence_image = np.where(self.fluorescence_image > self.param_dialog.compound_threshold,
                                           self.fluorescence_image, np.zeros(fl_shape))
        self.fluorescence_image = self.fluorescence_image * 255
        self.fluorescence_image = self.fluorescence_image + 1
        #calc rgb
        bk_rgb = np.zeros((bk_shape[0], bk_shape[1], 3))
        fl_rgb = np.zeros((bk_shape[0], bk_shape[1], 3))
        #calc rgb
        gray_cmap = cm.gray
        hot_cmap = cm.hot #the matlab code use hot(256) , I think its both ok
        bk_gray = gray_cmap(self.back_image.astype(np.int))
        #print(np.shape(bk_gray))
        fl_hot = hot_cmap(self.fluorescence_image.astype(np.int))
        for rgb_dim in range(3):
            gray_cmap_rows_for_bk = self.back_image.astype(np.int)
            hot_cmap_rows_for_fl = self.fluorescence_image.astype(np.int)
            bk_rgb[:, :, rgb_dim] = bk_gray[:, :, rgb_dim].reshape(bk_shape)
            fl_rgb[:, :, rgb_dim] = fl_hot[:, :, rgb_dim].reshape(fl_shape)
        #fusion
        opacity = 0.5
        self.compound_rgb = (1-opacity)*bk_rgb+opacity*fl_rgb
        #draw the compound_rgb
        self.fluorescence_image_canvas.fig.clear()
        self.fluorescence_image_canvas.axes = self.fluorescence_image_canvas.fig.add_subplot(111)
        self.fluorescence_image_canvas.axes.imshow(self.compound_rgb)
        self.fluorescence_image_canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

