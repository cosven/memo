# -*- coding:utf8 -*-

from PyQt4 import QtGui, QtCore

from common import _fromUtf8
import setting


class ImgSpacer(QtGui.QLabel):
    '''
    @note::
        memo之间的空格
    '''
    def __init__(self):
        super(ImgSpacer, self).__init__()

        self.pix = QtGui.QPixmap(setting.spacerOneImgPath)
        self.setPixmap(self.pix)


class Window_Ui(object):
    '''
    @note::
        主界面的布局设置
    '''
    def setupUi(self, Window):
        '''被主窗口调用'''
        Window.setWindowTitle(_fromUtf8("便签"))
        Window.setMinimumWidth(400)
        Window.setMaximumWidth(400)

        '''初始化组件'''
        self.layout = QtGui.QVBoxLayout()
        self.topLabelPix = QtGui.QPixmap(setting.topLabelImgPath)
        self.topLabel = QtGui.QLabel()

        '''设置组件属性'''
        self.layout.setMargin(0)
        self.layout.setSpacing(0)
        self.topLabel.setPixmap(self.topLabelPix)

        '''设置布局'''
        self.layout.addWidget(self.topLabel)

        self.setLayout(self.layout)

if __name__ == "__main__":
    pass
