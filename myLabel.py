# -*- coding:utf8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class FocusEdit(QTextEdit):
    def __init__(self, parent=None):
        super(FocusEdit, self).__init__(parent)

    def focusInEvent(self, event):
        print "edit"
        self.emit(SIGNAL("Editing"))

    def focusOutEvent(self, event):
        if event.reason() == 4: # popup focus
            event.ignore()
        else:
            self.emit(SIGNAL("EditFinish"))

class NoteLabel(QWidget):
    def __init__(self, string=None, parent=None):
        super(NoteLabel, self).__init__(parent)
        self.initObjects()
        self.setObjects(string)
        self.setMySizePolicy()
        self.setStyle()
        self.setEffects()

        self.okBtn.clicked.connect(self.ok)
        self.connect(self.textEdit, SIGNAL("EditFinish"), self.ok)
        self.connect(self.textEdit, SIGNAL("Editing"), self.editing)

    def initObjects(self):
        self.palette = QPalette()
        self.layout = QHBoxLayout()
        self.label = QLabel()
        self.timeLabel = QLabel()
        self.textEdit = FocusEdit()
        self.okBtn = QPushButton(u'确定')

        pix = QPixmap(16, 16)
        pix.fill(Qt.black)
        self.actionTextColor = QAction(QIcon(pix), "&Color", self, \
                triggered=self.textColor)
        self.actionTextFont = QAction(QIcon('./img/font.png'), "&Font", self, \
                triggered=self.textFont)

    def setObjects(self, string):
        if string:
                self.label.setText(string)
        else:
            self.label.setText(u'主人，点击我可以进行编辑')

        self.setPalette(self.palette)
        self.setLabelDefaultFont()
        self.label.setMargin(5)
        self.label.setPalette(self.palette)
        self.label.setWordWrap(True)

        string = QTime.currentTime().toString(Qt.TextDate)
        self.timeLabel.setText(string)
        self.timeLabel.setMargin(10)
        self.timeLabel.setPalette(self.palette)
        self.timeLabel.setWordWrap(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.timeLabel)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.okBtn)
        self.textEdit.hide()
        self.okBtn.hide()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

    def setMySizePolicy(self):
        self.setMaximumWidth(400)
        self.setMinimumWidth(400)
        self.label.setMaximumWidth(300)
        self.label.setMinimumWidth(300)
        self.timeLabel.setMaximumWidth(80)
        self.timeLabel.setMinimumWidth(80)
        self.textEdit.setMaximumHeight(40)
        self.okBtn.setMaximumHeight(40)
        self.okBtn.setMinimumWidth(40)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def setLabelDefaultFont(self):
        font = QFont()
        font.setFamily('Microsoft YaHei')
        font.setPointSize(10)
        self.label.setFont(font)
        self.timeLabel.setFont(font)

    def setStyle(self):
        label = '''
            QLabel{
                border-radius: 4px;
                background-color: #CCCCCC;
                }
            QLabel:Hover{
                border: 2px solid #DDDDDD;
                }
        '''
        edit = '''
            QTextEdit{
                border-top-left-radius: 4px;
                border-bottom-left-radius: 4px;
                background-color: #CCCCCC;
                selection-color: #CCCCCC;
                selection-background-color: #222222;
                color: black;
                }
        '''
        btn = '''
           QPushButton{
                color: #003300;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
                background-color: #CCCC99;
                font-size: 15px;
                font-family: '';
                }
            QPushButton:Hover{
                background-color: #009966;
                color: white;
                }
        '''
        self.textEdit.setStyleSheet(edit)
        self.okBtn.setStyleSheet(btn)
        self.label.setStyleSheet(label)
        self.timeLabel.setStyleSheet(label)

    def setEffects(self):
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.7)
        self.setGraphicsEffect(self.opacity)

    def changeEffects(self):
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.9)
        self.setGraphicsEffect(self.opacity)

    def contextMenuEvent(self, event):
        self.menu = QMenu()
        self.menu.addAction(self.actionTextFont)
        self.menu.addAction(self.actionTextColor)

        self.menu.move(self.cursor().pos())
        self.menu.show()

    def textColor(self):
        currentColor = self.palette.color(QPalette.WindowText)
        color = QColorDialog.getColor(currentColor, self)

        if not color.isValid():
            return
        else:
            self.palette.setColor(self.label.foregroundRole(), color)
            pix = QPixmap(16, 16)
            pix.fill(color)
            self.actionTextColor.setIcon(QIcon(pix))
            self.label.setPalette(self.palette)

    def textFont(self):
        currentFont = self.label.font()
        font = QFontDialog.getFont(currentFont, self)
        if font[1]:
            self.label.setFont(font[0])
            self.timeLabel.setFont(font[0])
            self.actionTextFont.setFont(font[0])

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.hide()
            self.timeLabel.hide()
            self.textEdit.show()
            self.textEdit.setFocus()
            self.textEdit.setText(self.label.text())
            self.okBtn.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        pw = self.parentWidget() # 获取父widget，也就是本程序中的主widget
        widget1 = pw.getTrashRect() # 获取主widget 的 垃圾箱widget（函数名没有改过来）
        flag = self.isCollide(widget1, self) # 检测两个widget的碰撞
        if flag:
            self.emit(SIGNAL('collideTrash'), True) # 碰撞就发射collideTrash信号
        else:
            self.emit(SIGNAL('collideTrash'), False)
        # 以下代码用于进行widget的拖拽
        if QMouseEvent.buttons() == Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.dragPos)
            QMouseEvent.accept()

        if QMouseEvent.buttons() == Qt.RightButton:
            QMouseEvent.ignore()

    def mouseReleaseEvent(self, QMouseEvent):
        # 拖拽动作完成之后检测是否碰撞以确定该widget是否被删除
        pw = self.parentWidget()
        widget1 = pw.getTrashRect()
        flag = self.isCollide(widget1, self)
        if flag:
            print "yes"
            self.emit(SIGNAL('collideTrash'), False)
            self.hide()
            self.destroy()
        else:
            self.emit(SIGNAL('collideTrash'), False)
            self.hide()
            self.show()

    def enterEvent(self, event):
        self.changeEffects()
        pass

    def leaveEvent(self, event):
        self.setEffects()
        pass

    def setText(self, string):
        self.label.setText(string)

    def ok(self):
        text = self.textEdit.document()
        self.label.setText(text.toPlainText())
        self.okBtn.hide()
        self.textEdit.hide()
        self.label.show()

        string = QTime.currentTime().toString(Qt.TextDate)
        self.timeLabel.setText(string)
        self.timeLabel.show()
        self.editFinish()

    def editFinish(self):
        self.emit(SIGNAL("EditFinish"))

    def editing(self):
        print "emit editing"
        self.emit(SIGNAL("Editing"))

    def isCollide(self, widget1, widget2):
        dict1 = {}
        dict1['size'] = widget1.size()
        dict1['pos'] = widget1.pos()

        dict2 = {}
        dict2['size'] = widget2.size()
        dict2['pos'] = widget2.pos()

        r1TopRightX = dict1['pos'].x() + dict1['size'].width()
        r1TopRightY = dict1['pos'].y()
        r1BottomLeftX = dict1['pos'].x()
        r1BottomLeftY = dict1['pos'].y() + dict1['size'].height()

        r2TopRightX = dict2['pos'].x() + dict2['size'].width()
        r2TopRightY = dict2['pos'].y()
        r2BottomLeftX = dict2['pos'].x()
        r2BottomLeftY = dict2['pos'].y() + dict2['size'].height()
        if r1TopRightX > r2BottomLeftX and r1TopRightY < r2BottomLeftY \
                and r2TopRightX > r1BottomLeftX and r2TopRightY < r1BottomLeftY:
                    return True
        else:
            return False

    def setLabelNormalStyle(self):
        normal = '''
            QLabel{
                border-radius: 4px;
                background-color: #CCCCCC;
                }
            QLabel:Hover{
                border: 2px solid #DDDDDD;
                }
        '''
        self.label.setStyleSheet(normal)

    def changeLabelStyleToCollide(self):
        hover = '''
            QLabel{
                border-radius: 4px;
                background-color: #009966;
                border: 2px solid #DDDDDD;
                }
        '''
        self.label.setStyleSheet(hover)



