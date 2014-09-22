# -*- coding:utf8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class NoDragPushButton(QPushButton):
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            QPushButton.__init__(self)
        if len(args) == 1:
            QPushButton.__init__(self, args[0])
        if len(args) == 2:
           QPushButton.__init__(self, args[0], args[1])
        if len(args) == 3:
            QPushButton.__init__(self, args[0], args[1], args[2])

        self.setEffects()
        self.setMyStyle()
        self.setMySizePolicy()


    def setMyStyle(self):
        style = '''
            QPushButton{
                border-radius: 2px;
                color: #EEEEEE;
                background-color: #CCCC99;
                font-size: 20px;
                font-family: 'Consolas';
                }
            QPushButton:Hover{
                color: black;
                }
        '''
        self.setStyleSheet(style)

    def setMySizePolicy(self):
        self.setMaximumWidth(400)
        self.setMinimumWidth(300)
        self.setMinimumHeight(20)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def mouseMoveEvent(self, QMouseEvent):
        pass
    
    def setEffects(self):
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.7)
        self.setGraphicsEffect(self.opacity)

    def changeEffects(self):
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.8)
        self.setGraphicsEffect(self.opacity)

    def enterEvent(self, event):
        pass
    def leaveEvent(self, event):
        pass
