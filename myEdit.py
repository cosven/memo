# -*- coding:utf8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class EditWidget(QLineEdit):
    def __init__(self, parent=None):
        super(EditWidget, self).__init__(parent)
        self.initObject()
        self.setObject()
        self.okBtn.clicked.connect(self.ok)

    def initObject(self):
        self.textEdit = QTextEdit()
        self.okBtn = QPushButton()
        self.layout = QHBoxLayout()

    def setObject(self):
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.okBtn)
        self.setLayout(self.layout)
    
    def ok(self):
        self.hide()
        return self.textEdit.document()
