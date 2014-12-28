#-*- coding:utf8 -*-

# =============================================================================
#      FileName: window.py
#          Desc: 程序主窗口
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-28 15:14:52
#       History:
# =============================================================================

from PyQt4 import QtGui, QtCore

from window_ui import Window_Ui, ImgSpacer
from memoWidget import MemoWidget
import setting


class Window(QtGui.QWidget, Window_Ui):
    '''主窗口类功能实现'''
    def __init__(self):
        super(Window, self).__init__()

        self.setupUi(self)

        self.initObjects()
        self.setObjects()

    def initObjects(self):
        self.memoWidget = MemoWidget()
        self.imgSpacer = ImgSpacer()
        self.windowIcon = QtGui.QIcon(setting.windowIconImgPath)
        pass

    def setObjects(self):
        self.layout.addWidget(self.memoWidget)
        self.layout.addWidget(self.imgSpacer)
        self.setWindowIcon(self.windowIcon)
        # 这句加了之后,命令行运行, 程序不能正常退出
        # self.setWindowFlags(QtCore.Qt.Tool)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


if __name__ == "__main__":
    import os
    import sys

    os.chdir(sys.path[0])

    app = QtGui.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
