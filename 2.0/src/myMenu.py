# -*- coding:utf8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import setting

class EffectLabel(QLabel):
    def __init__(self, parent=None):
        super(EffectLabel, self).__init__(parent)
        self.opacity = QGraphicsOpacityEffect()
        self.setEffects()

    def enterEvent(self, event):
        self.changeEffects()

    def leaveEvent(self, event):
        self.setEffects()

    def setEffects(self):
        self.opacity.setOpacity(0.5)
        self.setGraphicsEffect(self.opacity)

    def changeEffects(self):
        self.opacity.setOpacity(0.9)
        self.setGraphicsEffect(self.opacity)
    
class EffectButton(QPushButton):
    def __init__(self, parent=None):
        super(EffectButton, self).__init__(parent)
        self.opacity = QGraphicsOpacityEffect()
        self.setEffects()
    
    def enterEvent(self, event):
        self.changeEffects()
    
    def leaveEvent(self, event):
        self.setEffects()

    def setEffects(self):
        self.opacity.setOpacity(0.5)
        self.setGraphicsEffect(self.opacity)

    def changeEffects(self):
        self.opacity.setOpacity(0.9)
        self.setGraphicsEffect(self.opacity)

    def mouseMoveEvent(self, event):
        pass

class MainMenu(QWidget):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.initObjects()
        self.setObjects()
        self.setTrashStyle()
        self.setMyStyle()
        self.setMySize()
        pw = self.parentWidget()
        self.addBtn.clicked.connect(self.addBtnClicked)

    def initObjects(self):
        self.trashOpacity = QGraphicsOpacityEffect()
        self.opacity = QGraphicsOpacityEffect()
        self.addBtn = EffectButton()
        self.trashLabel= EffectLabel()
        self.layout = QVBoxLayout()

    def setObjects(self):
        self.layout.addWidget(self.addBtn)
        self.layout.addWidget(self.trashLabel)
        self.layout.addStretch(1)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

    def setMySize(self):
        self.trashLabel.setMaximumSize(48, 48)
        self.trashLabel.setMinimumSize(48, 48)
        self.addBtn.setMaximumSize(48, 48)
        self.addBtn.setMinimumSize(48, 48)
    
    def setMyStyle(self):
        add = '''
            QPushButton{
                border-radius: 4px;
                background-image: url(%s);
                }
            QPushButton:Pressed{
                background-image: url(%s);
                }
        ''' % (setting.ADDICON, setting.ADDICONHOVER)
        self.addBtn.setStyleSheet(add)
        
    def setTrashStyle(self):
        trash = '''
            QLabel{
                border-radius: 4px ;
                background-image: url(%s);
                }
            QLabel:Hover{
                background-image: url(%s);
                }

        ''' % (setting.TRASHICON, setting.TRASHICONHOVER)
        self.trashLabel.setStyleSheet(trash)
        self.trashLabel.setEffects()
    
    def setMySelfStyle(self):
        style = '''
            QWidget{
                background-color: #DDDDDD;
                }
        '''
        self.setStyleSheet(style)

    def getTrashPosSize(self):
        return self.trashLabel
    
    def changeTrashStyleToHover(self):
        trash = '''
            QLabel{
                border-radius: 4px ;
                background-image: url(%s);
                }
        ''' % setting.TRASHICONHOVER
        self.trashLabel.setStyleSheet(trash)
        self.trashLabel.changeEffects()
    
    def addBtnClicked(self):
        self.emit(SIGNAL("add"))
