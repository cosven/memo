#-*- coding:utf8 -*-

# =============================================================================
#      FileName: fonts.py
#          Desc: 加入自定义字体
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-28 19:23:48
#       History:
# =============================================================================

from PyQt4.QtGui import QFont, QFontDatabase

from logger import log


class Font():
    '''
    @note::
        添加字体类
    '''
    def __init__(self, font_path):
        self.__font = QFont()
        self.font_path = font_path

    def addFont(self):
        '''
        @note::
            成功或者失败
        '''
        font_path = self.font_path
        fontId = QFontDatabase.addApplicationFont(font_path)
        if(fontId != -1):
            fontInfoList = QFontDatabase.applicationFontFamilies(fontId)
            fontFamily = fontInfoList[0]
            self.__font.setFamily(fontFamily)
            log.info("添加字体成功")
            return True
        else:
            log.warning("添加字体失败")
            return False

    def getFont(self):
        self.addFont()
        return self.__font
