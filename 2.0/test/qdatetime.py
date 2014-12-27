#-*- coding: utf8 -*-

# from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDate

date = QDate.currentDate()
print date.toString("yyyy-MM-dd")
