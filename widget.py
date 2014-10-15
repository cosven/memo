#!/usr/bin/python
# -*- coding:utf8 -*-
import os
import json

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from myLabel import NoteLabel
from myMenu import MainMenu
from trayIcon import TrayIcon
import dataAccess

class mainUi(QWidget):
    def __init__(self, parent=None):
        super(mainUi, self).__init__(parent)

        self.initObjects()
        self.setObjects()
        self.setEffects()
        self.initProgram()

        self.connect(self.mainMenu, SIGNAL("add"), self.addNewNoteLabel)
        self.connect(self.trayIcon, SIGNAL("show"), self.show)
        self.connect(self.timer, SIGNAL("timeout()"), self.deadlineCome)
        self.connect(self.trayIcon, SIGNAL("showMain"), self.myShow)


    def initObjects(self):
        self.timer = QTimer()
        self.firstMemo = {}
        self.trayIcon = TrayIcon()
        self.isEditing = False
        self.leftLayout = QVBoxLayout()
        self.centerLayout = QVBoxLayout()
        self.mainMenu = MainMenu()
        self.layout = QHBoxLayout()

    def setObjects(self):
        self.trayIcon.show()
        # selfSize = QSize(600, 370)
        # deskRect = self.getDeskSize()
        # selfPoint = QPoint()
        # selfPoint.setX(deskRect.center().x() - selfSize.width()/2)
        # selfPoint.setY(deskRect.center().y() - selfSize.height()/2)

        # self.setGeometry(QRect(selfPoint, selfSize))
        # self.setMaximumSize(568,370)
        self.setMinimumWidth(550)
        self.setMaximumWidth(600)
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
        self.setWindowTitle("memo")

    def initLabel(self, date):
        memolist = dataAccess.read(date)
        datetime = QDateTime.currentDateTime()
        date = QDate.currentDate()
        if len(memolist):
            self.firstMemo = memolist[0]
            for each in memolist:
                self.addLabel(each)
            self.setFirstMemo()
            self.deadlineReady()

    def deadlineReady(self):
        '''
        when the deadline is changed or seted, this function should be called;
        it calculate the interval between the deadline and the currenttime;
        '''
        self.timer.stop()
        datetime = QDateTime.currentDateTime()
        interval = QDateTime.fromString(self.firstMemo['deadline']).msecsTo(datetime)
        if interval <= 0:
            self.timer.setInterval(-interval)
            self.timer.start()
        else:
            self.deadlineCome()
            self.timer.stop()
            self.timer.setInterval(600000)
            self.timer.start()

    def initProgram(self):
        date = QDate.currentDate().toString()
        if os.path.exists('log.json'):
            self.initLabel(unicode(date))
            dictdata = {}
            dictdata['last'] = unicode(date)
            jsondata = json.dumps(dictdata)
            f = open('log.json', 'w')
            f.write(jsondata)
            f.close()
        else:
            ' first run the program '
            dictdata = {}
            dictdata['last'] = unicode(date)
            jsondata = json.dumps(dictdata)
            f = open('log.json', 'w')
            f.write(jsondata)
            f.close()

    def setEffects(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        backImg = QPixmap('./img/1.jpg').scaled(self.size())
        self.palette = QPalette()
        self.palette.setBrush(self.backgroundRole(), QBrush(backImg))
        # self.palette.setColor(QPalette.Background, QColor(255,255,255,200))
        self.setPalette(self.palette)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFocusPolicy(Qt.StrongFocus)

    def addLabel(self, data):
        label = NoteLabel(data, self)
        self.connect(label, SIGNAL("collideTrash"), \
                self.trashHover)
        self.connect(label, SIGNAL("Editing"), self.editing)
        self.connect(label, SIGNAL("EditFinish"), self.editFinish)
        self.connect(label, SIGNAL("OneMemoFinish"), self.oneMemoFinish)
        allCount = self.centerLayout.count()
        if allCount == 0:
            self.centerLayout.addWidget(label)
        else:
            self.centerLayout.insertWidget(allCount-1, label)

    def addNewNoteLabel(self):
        date = QDate.currentDate().toString()
        datetime = QDateTime.currentDateTime().toString()
        allCount = self.centerLayout.count()
        content = {
                'id': allCount-1,
                'content': u'主人，双击我可以进行编辑，右键可以进行个性化设置O(∩_∩)O哈！',
                'deadline': unicode(datetime),
                'pid': unicode(date),
                'finished': False,
                }
        label = NoteLabel(content, self)
        self.connect(label, SIGNAL("collideTrash"), \
                self.trashHover)
        self.connect(label, SIGNAL("Editing"), self.editing)
        self.connect(label, SIGNAL("EditFinish"), self.editFinish)
        self.connect(label, SIGNAL("OneMemoFinish"), self.oneMemoFinish)
        self.centerLayout.insertWidget(allCount-1, label)
        self.setFirstMemo()
#        self.deadlineReady()

    def getData(self):
        date = QDate.currentDate().toString()
        memolist = []
        # while self.centerLayout.count():
        for i in range(self.centerLayout.count()):
            item = self.centerLayout.itemAt(i)
            try:
                w = item.widget()
                if w:
                    c = w.getContent()
                    memolist.append(c)
            except Exception, e:
                pass
        data = {}
        data['id'] = unicode(date)
        data['memolist'] = memolist
        return data

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
        self.setFirstMemo()
        self.deadlineReady()
        self.isEditing = False

    def editing(self):
        self.isEditing = True

    def myHide(self):
        if self.isEditing:
            pass
        else:
            self.hide()

    def myShow(self):
        if not self.isVisible():
            self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.pos()
        if self.isEditing:
            self.emit(SIGNAL("EditFinish")) # label will catch this signal and ok 
        event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 以下代码用于进行widget的拖拽
        if QMouseEvent.buttons() == Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.dragPos)
            QMouseEvent.accept()

        if QMouseEvent.buttons() == Qt.RightButton:
            QMouseEvent.ignore()

    def exit(self):
        data = self.getData()
        dataAccess.save(data)
        self.close()

    def closeEvent(self, event):
        data = self.getData()
        dataAccess.save(data)
        self.hide()
        event.ignore()
        self.trayIcon.showMessage(u"提示",
                u'程序已最小化到托盘，点击托盘可以进行操作')

    def compareTime(self, memo1, memo2):
        time1 = QDateTime.fromString(memo1['deadline'])
        time2 = QDateTime.fromString(memo2['deadline'])
        if time1.secsTo(time2) > 0: # time1 < time2
            return memo1
        else:
            return memo2

    def deadlineCome(self):
        self.trayIcon.showMessage(u"最后期限已到", self.firstMemo['content']\
                + '\n\n' + u'10分钟后提醒', 1,
                100)

    def setFirstMemo(self):
        data = self.getData()
        memolist = data['memolist']
        for each in memolist:
            if not each['finished']:
                if not self.firstMemo.has_key('deadline'):
                    self.firstMemo = each
                else:
                    if self.firstMemo['finished']:
                        self.firstMemo = each
                    self.firstMemo = self.compareTime(self.firstMemo, each)
        self.trayIcon.showMessage(u'你现在最先需要完成', \
                self.firstMemo['deadline']+'\n'+self.firstMemo['content'], \
                1, 100)

    def oneMemoFinish(self, string):
        print "memo receive"
        self.trayIcon.showMessage(u'下面任务已完成', string, 1, 1000)
        self.setFirstMemo()
        self.deadlineReady()


class mainWidget(QWidget):
    def __init__(self, parent=None):
        super(mainWidget, self).__init__(parent)
        self.initObjects()
        self.setObjects()

        self.m.show()

    def initObjects(self):
        self.m = mainUi()
        self.layout = QHBoxLayout()
    
    def setObjects(self):
        deskRect = self.getDeskSize()
        selfPoint = QPoint()
        selfPoint.setX(deskRect.center().x() - selfSize.width()/2)
        selfPoint.setY(deskRect.center().y() - selfSize.height()/2)
        self.setGeometry(QRect(selfPoint, selfSize))
        point = QPoint(0,0)
        self.setWindowOpacity(0.5)
        self.layout.addWidget(self.m)
        self.setLayout(self.layout)

    def getDeskSize(self):
        rect = QApplication.desktop().availableGeometry()
        return rect

if __name__ == "__main__":
    import sys
    currentPath = sys.path[0]
    print currentPath
    os.chdir(currentPath)

    app = QApplication(sys.argv)
    w = mainUi()
    w.show()
    sys.exit(app.exec_())
