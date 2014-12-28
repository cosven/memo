# -*- coding:utf8 -*-

# =============================================================================
#      FileName: memoWidget_ui.py
#          Desc: 每个memo布局
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-28 15:19:29
#       History:
# =============================================================================

from PyQt4 import QtGui

import setting
from common import _fromUtf8


class MemoWidget_Ui(object):
    '''
    @note::
        memo布局设置
        memo大小设置
    '''
    def setupUi(self, MemoWidget):
        '''被memo调用'''
        MemoWidget.setFixedWidth(400)

        '''初始化组件'''
        self.layout = QtGui.QHBoxLayout()
        self.leftRedPix = QtGui.QPixmap(setting.leftRedImgPath)
        self.leftLabel = QtGui.QLabel()

        self.centerLayout = QtGui.QVBoxLayout()
        self.centerWidget = QtGui.QWidget()
        self.scrollArea = QtGui.QScrollArea()
        self.titleLabel = QtGui.QLabel(_fromUtf8("便签提醒标题"))
        self.timeLabel = QtGui.QLabel(_fromUtf8("截止日期: 2014-12-28 10:35 星期一"))
        self.contentLabel = QtGui.QLabel(_fromUtf8('''\
            我和小伙伴去游山玩水，聊天扯淡，灵隐寺 \
            西湖，大半个杭州都被我们玩完了 \
            我和小伙伴去游山玩水，聊天扯淡，灵隐寺, \
            我和小伙伴去游山玩水，聊天扯淡，灵隐寺 \
            西湖，大半个杭州都被我们玩完了 \
            我和小伙伴去游山玩水，聊天扯淡，灵隐寺, \
            '''))

        self.rightWidget = QtGui.QWidget()
        self.rightLayout = QtGui.QVBoxLayout()
        self.topButton = QtGui.QPushButton()     # checkable

        '''设置组件大小属性'''
        self.layout.setMargin(0)
        self.layout.setSpacing(0)
        self.centerLayout.setMargin(0)
        self.centerLayout.setSpacing(2)
        self.rightLayout.setMargin(0)
        self.rightLayout.setSpacing(2)

        self.leftLabel.setPixmap(self.leftRedPix)
        self.centerWidget.setFixedWidth(300)
        self.centerWidget.setFixedWidth(300)
        self.centerWidget.setMaximumHeight(142)
        self.titleLabel.setFixedHeight(33)
        self.timeLabel.setFixedHeight(22)
        self.rightWidget.setFixedWidth(82)
        self.topButton.setFixedSize(45, 84)

        self.topButton.setCheckable(True)
        # 设置stylesheet
        labelStyleSheet = '''
            QWidget{
                background-color: #FFFFFF;
            }
            QLabel{
                background-color: #FFFFFF;
                color: #000000;
            }
            QPushButton{
                background-color: #FFFFFF;
                background-image: url(%s);
                outline: none;
                border: 0px;
            }
            QPushButton:checked{
                background-image: url(%s)
            }
            QScrollArea{
                border: 0px;
            }
            QScrollBar{
                width: 5px;
                background-color: #993333;
                border: 0px solid white;
            }
            QScrollBar::handle{
                border: 0px solid white;
            }
            QScrollBar::add-line{
                border: 0px solid white;
            }
            QScrollBar::sub-line{
                border: 0px solid white;
            }
        ''' % (setting.topNoImgPath, setting.topYesImgPath)
        self.rightWidget.setStyleSheet(labelStyleSheet)
        self.centerWidget.setStyleSheet(labelStyleSheet)

        '''设置布局'''
        # 设置中间部分的布局

        self.centerLayout.addWidget(self.titleLabel)
        self.centerLayout.addWidget(self.timeLabel)
        self.centerLayout.addWidget(self.scrollArea)
        self.centerLayout.addStretch(1)
        self.centerWidget.setLayout(self.centerLayout)
        # 设置右边部分布局
        self.rightLayout.addWidget(self.topButton)
        self.rightLayout.addStretch(2)
        self.rightWidget.setLayout(self.rightLayout)
        # 设置主布局
        self.layout.addWidget(self.leftLabel)
        self.layout.addWidget(self.centerWidget)
        self.layout.addWidget(self.rightWidget)

        self.setLayout(self.layout)

if __name__ == "__main__":
    pass
