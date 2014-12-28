#-*- coding:utf8 -*-

# =============================================================================
#      FileName: main.py
#          Desc: 程序主入口
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-27 22:49:53
#       History:
# =============================================================================


import os
import sys

from PyQt4 import QtGui

from window import Window

if __name__ == "__main__":
    os.chdir(sys.path[0])

    app = QtGui.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
