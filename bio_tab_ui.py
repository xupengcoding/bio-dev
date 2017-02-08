# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bio_tab_ui.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import bio_widget
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ImgShowWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.ImgShowWidget.setAutoFillBackground(True)
        self.ImgShowWidget.setObjectName("ImgShowWidget")
        self.tab_input_image1 = QtWidgets.QWidget()
        self.tab_input_image1.setObjectName("tab_input_image1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_input_image1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        #self.label_input_image1 = QtWidgets.QLabel(self.tab_input_image1)
        #self.label_input_image1 = bio_widget.ImageArea(self.tab_input_image1)
        #self.label_input_image1.setAutoFillBackground(True)
        #self.label_input_image1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        #self.label_input_image1.setObjectName("label_input_image1")
        self.image1_canvas = bio_widget.MyMplCanvas()
        self.image1_toolbar = NavigationToolbar(self.image1_canvas, self)
        self.verticalLayout.addWidget(self.image1_toolbar)
        self.verticalLayout.addWidget(self.image1_canvas)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.ImgShowWidget.addTab(self.tab_input_image1, "")
        self.tab_input_image2 = QtWidgets.QWidget()
        self.tab_input_image2.setObjectName("tab_input_image2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_input_image2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #self.label_input_image2 = QtWidgets.QLabel(self.tab_input_image2)
        #self.label_input_image2.setAutoFillBackground(True)
        #self.label_input_image2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        #self.label_input_image2.setObjectName("label_input_image2")
        #self.verticalLayout_2.addWidget(self.label_input_image2)
        self.image2_canvas = bio_widget.MyMplCanvas()
        self.image2_toolbar = NavigationToolbar(self.image2_canvas, self)
        self.verticalLayout_2.addWidget(self.image2_toolbar)
        self.verticalLayout_2.addWidget(self.image2_canvas)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.ImgShowWidget.addTab(self.tab_input_image2, "")
        self.tab_ration_image = QtWidgets.QWidget()
        self.tab_ration_image.setObjectName("tab_ration_image")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_ration_image)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        #self.label_ration_image = QtWidgets.QLabel(self.tab_ration_image)
        #self.label_ration_image.setAutoFillBackground(True)
        #self.label_ration_image.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        #self.label_ration_image.setObjectName("label_ration_image")
        #self.verticalLayout_4.addWidget(self.label_ration_image)
        self.ratio_image_canvas = bio_widget.MyMplCanvas()
        self.ratio_image_toolbar = NavigationToolbar(self.ratio_image_canvas, self)
        self.verticalLayout_4.addWidget(self.ratio_image_toolbar)
        self.verticalLayout_4.addWidget(self.ratio_image_canvas)        
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.ImgShowWidget.addTab(self.tab_ration_image, "")
        self.tab_fitted_image = QtWidgets.QWidget()
        self.tab_fitted_image.setObjectName("tab_fitted_image")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_fitted_image)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        #self.label_fitted_image = QtWidgets.QLabel(self.tab_fitted_image)
        #self.label_fitted_image.setAutoFillBackground(True)
        #self.label_fitted_image.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        #self.label_fitted_image.setObjectName("label_fitted_image")
        #self.verticalLayout_3.addWidget(self.label_fitted_image)
        self.fitted_image_canvas = bio_widget.MyMplCanvas()
        self.fitted_image_toolbar = NavigationToolbar(self.fitted_image_canvas, self)
        self.verticalLayout_3.addWidget(self.fitted_image_toolbar)
        self.verticalLayout_3.addWidget(self.fitted_image_canvas)
        
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.ImgShowWidget.addTab(self.tab_fitted_image, "")
        self.horizontalLayout.addWidget(self.ImgShowWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionFitting_param = QtWidgets.QAction(MainWindow)
        self.actionFitting_param.setObjectName("actionFitting_param")
        self.actionCalc = QtWidgets.QAction(MainWindow)
        self.actionCalc.setObjectName("actionCalc")
        self.actionPooling = QtWidgets.QAction(MainWindow)
        self.actionPooling.setObjectName("actionPooling")
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionFitting_param)
        self.menuMenu.addAction(self.actionCalc)
        self.menuMenu.addAction(self.actionPooling)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.ImgShowWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.label_input_image1.setText(_translate("MainWindow", "Input_image_1"))
        self.ImgShowWidget.setTabText(self.ImgShowWidget.indexOf(self.tab_input_image1), _translate("MainWindow", "Input Image 1"))
        #self.label_input_image2.setText(_translate("MainWindow", "Input_image_2"))
        self.ImgShowWidget.setTabText(self.ImgShowWidget.indexOf(self.tab_input_image2), _translate("MainWindow", "Input Image 2"))
        #self.label_ration_image.setText(_translate("MainWindow", "Ratio_Image"))
        self.ImgShowWidget.setTabText(self.ImgShowWidget.indexOf(self.tab_ration_image), _translate("MainWindow", "Ratio Image"))
        #self.label_fitted_image.setText(_translate("MainWindow", "Fitted Image"))
        self.ImgShowWidget.setTabText(self.ImgShowWidget.indexOf(self.tab_fitted_image), _translate("MainWindow", "Fitted Image"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionFitting_param.setText(_translate("MainWindow", "Fitting Func Config"))
        self.actionCalc.setText(_translate("MainWindow", "Calc"))
        self.actionPooling.setText(_translate("MainWindow", "Pooling"))
