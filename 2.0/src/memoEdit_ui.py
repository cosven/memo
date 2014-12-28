# -*- coding:utf8 -*-

# =============================================================================
#      FileName: memoEdit_ui.py
#          Desc: memo编辑器UI
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-28 21:53:18
#       History:
# =============================================================================

from PyQt4 import QtGui
from common import _fromUtf8


class MemoEdit_Ui(object):
    '''
    @note::
        memo编辑器界面设置
    '''
    def setupUi(self, MemoEdit):
        '''被memoedit调用'''
        MemoEdit.setFixedWidth(400)

        '''初始化组件'''
        self.titleEdit = QtGui.QLineEdit()
        self.timeEdit = QtGui.QDateTimeEdit()
        self.contentEdit = QtGui.QTextEdit()
        self.okBtn = QtGui.QPushButton(_fromUtf8("确定"))
        self.layout = QtGui.QVBoxLayout()

        '''设置组件大小属性'''
        self.layout.setMargin(0)
        self.layout.setSpacing(0)

        ''' 设置stylesheet'''
        '''设置布局'''
        self.layout.addWidget(self.titleEdit)
        self.layout.addWidget(self.timeEdit)
        self.layout.addWidget(self.contentEdit)
        self.layout.addWidget(self.okBtn)

        self.setLayout(self.layout)
