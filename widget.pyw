# -*- coding:utf8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from myLabel import NoteLabel
from myMenu import MainMenu
from trayIcon import TrayIcon


class mainUi(QGraphicsView):
    def __init__(self, parent=None):
        super(mainUi, self).__init__(parent)
        self.initObjects()
        self.setObjects()
        self.setEffects()

        self.connect(self.mainMenu, SIGNAL("add"), self.addNoteLabel)
        self.connect(self.trayIcon, SIGNAL("show"), self.show)

        self.trayIcon.show()

    def initObjects(self):
        self.trayIcon = TrayIcon()
        self.isEditing = False
        self.leftLayout = QVBoxLayout()
        self.centerLayout = QVBoxLayout()
        self.mainMenu = MainMenu()
        self.layout = QHBoxLayout()

    def setObjects(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)
        selfSize = QSize(600, 370)
        deskRect = self.getDeskSize()
        selfPoint = QPoint()
        selfPoint.setX(deskRect.center().x() - selfSize.width()/2)
        selfPoint.setY(deskRect.center().y() - selfSize.height()/2)

        self.setGeometry(QRect(selfPoint, selfSize))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.leftLayout.addWidget(self.mainMenu)
        self.centerLayout.addStretch(1)
        self.layout.addLayout(self.leftLayout)
        self.layout.addSpacing(10)
        self.layout.addLayout(self.centerLayout)
        self.layout.addStretch(1)
        self.setLayout(self.layout)
        self.setWindowIcon(QIcon('./img/icon.png'))
        self.trayIcon.setParent(self)

    def setEffects(self):
        backImg = QPixmap('./img/1.png').scaled(self.size())
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(backImg))
        self.setPalette(palette)


    def addNoteLabel(self):
        label = NoteLabel(u'主人，点击我可以进行编辑哦')
        self.connect(label, SIGNAL("collideTrash"), \
                self.trashHover)
        self.connect(label, SIGNAL("Editing"), self.editing)
        self.connect(label, SIGNAL("EditFinish"), self.editFinish)
        allCount = self.centerLayout.count()
        self.centerLayout.insertWidget(allCount-1, label)

    def getDeskSize(self):
        rect = QApplication.desktop().availableGeometry()
        return rect

    def getTrashRect(self):
        return self.mainMenu.getTrashPosSize()

    def trashHover(self, flag):
        if flag:
            self.mainMenu.changeTrashStyleToHover()
        else:
            self.mainMenu.setTrashStyle()

    def editFinish(self):
        self.isEditing = False

    def editing(self):
        print "receive editing"
        self.isEditing = True

    def myHide(self):
        print self.isEditing
        if self.isEditing:
            pass
        else:
            self.hide()

    def closeEvent(self, event):
        self.hide()
        event.ignore()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = mainUi()
    w.show()
    sys.exit(app.exec_())
