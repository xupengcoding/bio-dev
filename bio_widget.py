from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MyMplCanvas(FigureCanvas):
    """
    an widget for matplotlib canvas
    """
    def __init__(self,parent=None, image_arr=None, dpi=100):
        #fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        
        self.axes.hold(False)

        #self.compute_initial_figure()
        
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        #self.mpl_connect('button_press_event', self.onclick)
        
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass
    
    def onclick(self, event):
        pass
        if event.xdata:
            print (self.axes.get_xbound())
            #print('x=%d, y=%d, xdata=%f, ydata=%f' %(event.x, event.y, event.xdata, event.ydata))         


class ImageArea(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(ImageArea, self).__init__(parent)
        self.img_path = ''
        self.pen = QtGui.QPen(QtCore.Qt.blue)
        self.brush = QtGui.QBrush()
        self.refresh = True
        self.rect = [-1, -1, -1, -1] # select rect
        self.width = 0 # image width
        self.height = 0 # image height
        self.dims = 0 # image dims rgb or gray
        #set pen color
    
    def mousePressEvent(self, e):
        self.refresh = True
        #self.refresh = False
        pos = e.pos()
        #print ('Press x:%d y:%d'%(pos.x(), pos.y()))
        self.rect[0] = pos.x()
        self.rect[1] = pos.y()
        self.update()
    
    def mouseReleaseEvent(self, e):
        self.refresh = False
        pos = e.pos()
        #print ('Release x:%d y:%d'%(pos.x(), pos.y()))
        self.rect[2] = pos.x()
        self.rect[3] = pos.y()
        self.update()
    
    def paintEvent(self, QPaintEvent):
        """
        re-implement paintevent
        """
        #print ('paint event')
        super(ImageArea, self).paintEvent(QPaintEvent)
        p = QtGui.QPainter(self)
        p.setPen(self.pen)
        #p.setBrush(self.brush)

        rect = QtCore.QRect(self.rect[0], self.rect[1],
                            self.rect[2]-self.rect[0]+1,
                            self.rect[3]-self.rect[1]+1)
        #rect0 = QtCore.QRect(0, 0, 1, 1)
        if self.refresh:
            #print ('refresh')
            return
        #p.setBrush(QtGui.QBrush(QtGui.QPixmap("test.jpg")))
        p.drawRect(rect)
