#-*- coding:utf8 -*-

# =============================================================================
#      FileName: memoEdit.py
#          Desc: memo编辑器
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-28 21:50:14
#       History:
# =============================================================================

from PyQt4 import QtGui, QtCore

from memoEdit_ui import MemoEdit_Ui


class MemoEdit(QtGui.QWidget, MemoEdit_Ui):
    '''
    @note::
        简单memo编辑器
    '''
    def __init__(self):
        super(MemoEdit, self).__init__()

        self.setupUi(self)
        self.initObject()
        self.setObjects()

        self.okBtn.clicked.connect(self.ok)

    def initObject(self):
        self.datetimeFormat = "yyyy-MM-dd dddd hh:mm ap"
        pass

    def setObjects(self):
        '''
        @note::
            datetime = QtCore.QDateTime.fromString(
                "2014-12-28 Sunday 12:00 am", self.datetimeFormat)
        '''
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        pass

    def ok(self):
        '''
        @note::
            编辑完成
        '''
        # data = {}
        title = self.titleEdit.text()
        time = self.timeEdit.dateTime().toString(self.datetimeFormat)
        content = self.contentEdit.document().toPlainText()
        print title, time, content
        self.close()


if __name__ == "__main__":
    import os
    import sys

    os.chdir(sys.path[0])

    app = QtGui.QApplication(sys.argv)
    w = MemoEdit()
    w.show()
    sys.exit(app.exec_())
