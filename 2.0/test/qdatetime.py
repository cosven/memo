#-*- coding: utf8 -*-

if __name__ == "__main__":
    from PyQt4.QtCore import QDate

    date = QDate.currentDate()
    print date.toString("yyyy-MM-dd")
