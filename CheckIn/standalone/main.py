# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('gbk')

from PySide.QtCore import *
from PySide.QtGui import *
import UI_QTUI; reload(UI_QTUI)
import subprocess


class Check_In(QMainWindow):
    def __init__(self, parent=None):
        super(Check_In, self).__init__(parent)
        self.ui = UI_QTUI.Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot(str, name="on_listWidget_currentTextChanged")
    def on_listWidget_currentTextChanged(self, text):
        self.ui.lineEdit_local_path.setText(text)

    @Slot(name="on_MQPushButton_Delete_clicked")
    def on_MQPushButton_Delete_clicked(self):
        select_list = []
        for item in self.ui.listWidget.selectedItems():
            row = self.ui.listWidget.row(item)
            select_list.append(row)
        select_list = sorted(select_list, reverse=1)
        for index in select_list:
            self.ui.listWidget.takeItem(index)

    @Slot(name="on_MQPushButton_Open_local_path_clicked")
    def on_MQPushButton_Open_local_path_clicked(self):
        path = self.ui.lineEdit_local_path.text()
        cmd = u'explorer /select, ' + path
        subprocess.Popen(cmd)

    @Slot(name="on_MQPushButton_Open_checkin_path_clicked")
    def on_MQPushButton_Open_checkin_path_clicked(self):
        path = self.ui.lineEdit_checkin.text()
        cmd = u'explorer /select, ' + path
        subprocess.Popen(cmd)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Check_In()
    window.show()
    sys.exit(app.exec_())
