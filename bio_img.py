import numpy as np
from PIL import Image
import os
import jpype

class ImgProcess:
    def __init__(self):
        self.jvmPath = jpype.getDefaultJVMPath()
        self.jarpath = os.path.join(os.path.abspath('.'), 'loci_tools.jar')
        jpype.startJVM(self.jvmPath, "-ea", "-Djava.class.path=%s" % self.jarpath)
        self.DebugTools = jpype.JClass('loci.common.DebugTools')
        self.DebugTools.enableLogging('INFO')
        self.ChannelFiller = jpype.JClass('loci.formats.ChannelFiller')
        self.ChannelSeparator = jpype.JClass('loci.formats.ChannelSeparator')
        self.FormatTools = jpype.JClass('loci.formats.FormatTools')
        self.DataTools = jpype.JClass('loci.common.DataTools')

    def imread_bip(self, path):
        reader = self.ChannelFiller()
        reader = self.ChannelSeparator(reader)
        reader.setId(path)
        width = reader.getSizeX()
        height = reader.getSizeY()
        pixelType = reader.getPixelType()
        bpp = self.FormatTools.getBytesPerPixel(pixelType)
        fp = self.FormatTools.isFloatingPoint(pixelType)
        little = reader.isLittleEndian()
        sgn = self.FormatTools.isSigned(pixelType)
        print ('%d %d %d'%(width, height, bpp))
        channel = 0
        zplane = 0
        tframe = 0
        #vol = np.zeros((height, width))
        zahler = 0
        #read only one
        index = reader.getIndex(0, 0, 0)
        plane = reader.openBytes(index)
        arr = self.DataTools.makeDataArray2D(plane, bpp, fp, little, height)
        arr1 = np.array(arr).astype(np.double)
        print(arr1.shape)
        return arr1

def averagePooling(step, image):
    '''
    doing a average pooling on a image
    now only integer average pooling
    '''
    image = image.astype(np.double)
    image_shape = image.shape
    #crop
    img_height = image_shape[0]-(image_shape[0]%step)
    img_width = image_shape[1]-(image_shape[1]%step)
    image = image[0:img_height, 0:img_width]
    img_height = int(img_height/step)
    img_width = int(img_width/step)    
    #average pooling
    img_pooled = np.zeros((img_height, img_width))
    for i in range(int(img_height)):
        for j in range(int(img_width)):
            img_pooled[i][j] = np.mean(image[i*step:(i+1)*step, j*step:(j+1)*step])
    return img_pooled

def calcRatioImg(image1, image2):
    '''
    calc tow ratio img
    '''

