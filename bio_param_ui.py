# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bio_param_ui.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 50, 326, 200))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_max_pixel = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_max_pixel.setObjectName("label_max_pixel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_max_pixel)
        self.textEdit_max_pixel = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_max_pixel.setObjectName("textEdit_max_pixel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_max_pixel)
        self.label_min_pixel = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_min_pixel.setObjectName("label_min_pixel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_min_pixel)
        self.textEdit_min_pixel = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_min_pixel.setObjectName("textEdit_min_pixel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_min_pixel)
        self.label_fitparam_a = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_fitparam_a.setObjectName("label_fitparam_a")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_fitparam_a)
        self.textEdit_fitparam_a = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_fitparam_a.setObjectName("textEdit_fitparam_a")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_fitparam_a)
        self.label_fitparam_b = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_fitparam_b.setObjectName("label_fitparam_b")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_fitparam_b)
        self.textEdit_fitparam_b = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_fitparam_b.setObjectName("textEdit_fitparam_b")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_fitparam_b)

        self.label_compound_threshold = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_compound_threshold.setObjectName("label_compound_threshold")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_compound_threshold)
        self.textEdit_compound_threshold = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_compound_threshold.setObjectName("textEdit_compound_threshold")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit_compound_threshold)

        self.label_cmap_min = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_cmap_min.setObjectName("label_cmap_min")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_cmap_min)
        self.textEdit_cmap_min = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_cmap_min.setObjectName("textEdit_cmap_min")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit_cmap_min)

        self.label_cmap_max = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_cmap_max.setObjectName("label_cmap_max")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_cmap_max)
        self.textEdit_cmap_max = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_cmap_max.setObjectName("textEdit_cmap_max")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textEdit_cmap_max)                

        self.buttonBox.raise_()
        self.formLayoutWidget.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_max_pixel.setText(_translate("Dialog", "max-pixel"))
        self.label_min_pixel.setText(_translate("Dialog", "min-pixel"))
        self.label_fitparam_a.setText(_translate("Dialog", "fitparam-a"))
        self.label_fitparam_b.setText(_translate("Dialog", "fitparam-b"))
        self.label_compound_threshold.setText(_translate("Dialog", "compound-threshold"))
        self.label_cmap_min.setText(_translate("Dialog", "colormap min"))
        self.label_cmap_max.setText(_translate("Dialog", "colormap max"))

