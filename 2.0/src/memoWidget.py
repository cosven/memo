#-*- coding:utf8 -*-

# =============================================================================
#      FileName: memoWidget.py
#          Desc: 每个memo窗口功能实现
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-28 15:22:30
#       History:
# =============================================================================

from PyQt4 import QtGui, QtCore

from memoWidget_ui import MemoWidget_Ui
from memoEdit import MemoEdit
from fonts import Font
from logger import log
import setting


class MemoWidget(QtGui.QWidget, MemoWidget_Ui):
    '''主窗口类功能实现'''
    def __init__(self):
        super(MemoWidget, self).__init__()

        self.setupUi(self)
        self.initObjects()
        self.setObjects()

    def initObjects(self):
        pass

    def setObjects(self):
        '''
        @note::
            设置几个label的一些属性
        '''
        self.setMemoFont()
        self.setMemoTypeset()
        self.titleLabel.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByMouse)
        self.timeLabel.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByMouse)
        self.contentLabel.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByMouse)
        self.scrollArea.setWidgetResizable(True)

    def setMemoTypeset(self):
        '''
        @note::
            设置memo标题等的排版
        '''
        self.titleLabel.setIndent(14)
        self.titleLabel.setMargin(0)
        self.contentLabel.setMargin(0)
        self.timeLabel.setIndent(14)
        self.contentLabel.setIndent(14)
        self.contentLabel.setScaledContents(True)
        self.contentLabel.setWordWrap(True)
        self.scrollArea.setWidget(self.contentLabel)

    def setMemoFont(self):
        '''
        @note::
            系统设定字体
            当字体不存在时，程序可以正常运行，但是界面可能奇怪
        @attention::
            可能出现警告
        '''
        self.fontTitle = Font(setting.MSYAHEI).getFont()  # 自己写的字体类
        self.fontContent = Font(setting.MSYAHEI).getFont()
        self.fontTime = Font(setting.UBUNTUMONO).getFont()

        self.fontTitle.setPointSize(17)
        self.titleLabel.setFont(self.fontTitle)
        self.contentLabel.setFont(self.fontContent)
        self.timeLabel.setFont(self.fontTime)

    def mouseDoubleClickEvent(self, event):
        '''
        @note::
            先设置objectName(获取)
        '''
        log.info("mouse double click")
        if event.button() == QtCore.Qt.LeftButton:
            log.info("left")
            self.memoedit = MemoEdit()
            self.memoedit.show()


if __name__ == "__main__":
    import os
    import sys

    os.chdir(sys.path[0])

    app = QtGui.QApplication(sys.argv)
    w = MemoWidget()
    w.show()
    sys.exit(app.exec_())
