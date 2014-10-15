# -*- coding:utf8 -*-
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.initObjects()
        self.setObjects()

        self.activated.connect(self.iconClicked)
    def initObjects(self):
        self.menu = QMenu()
        self.showAction = QAction(u'显示', self, triggered=self.showWidget)
        self.quitAction = QAction(u"退出", self, triggered=self.exitApp)
        self.icon = QIcon('./img/icon.png')

    def setObjects(self):
        self.menu.addAction(self.showAction)
        self.menu.addAction(self.quitAction)
        self.setIcon(self.icon)
        self.setContextMenu(self.menu)

    def iconClicked(self, reason):
        print reason
        if reason==2 or reason==3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
    def exitApp(self):
        self.setVisible(False)
        self.parent().exit()
        qApp.quit()
        sys.exit()
    def showWidget(self):
        self.emit(SIGNAL("showMain"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ti = TrayIcon()
    ti.show()
    sys.exit(app.exec_())
