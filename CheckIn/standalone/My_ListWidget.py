# -*- coding: utf-8 -*-
import os
import sys
from PySide.QtCore import *
from PySide.QtGui import *


class DropArea(QListWidget):
    def __init__(self, parent=None):
        super(DropArea, self).__init__(parent)
        self.setAcceptDrops(True)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            if event.mimeData().urls() !=[]:
                event.accept()
            else:
                event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            if event.mimeData().urls() !=[]:
                event.accept()
            else:
                event.ignore()

    def dropEvent(self, event):
        super(DropArea, self).dropEvent(event)
        mimeData = event.mimeData()
        if mimeData.hasUrls():
            path = []
            for url in mimeData.urls():
                path.append(url.toLocalFile())
            self.my_add_path(path)

    def my_add_path(self, paths):
        # 1. 获得已存在路径
        current_paths = []
        for i in range(self.count()):
            current_paths.append(self.item(i).text())

        # 2. 加入新路径
        for path in paths:
            abs_path = os.path.abspath(path)
            if abs_path not in current_paths:
                # 2.1 判断是文件还是文件夹
                if os.path.isdir(abs_path):
                    list = GetFileList(abs_path, [])
                    for file in list:
                        if file not in current_paths:
                            self.addItem(QListWidgetItem(file))
                elif os.path.isfile(abs_path):
                    self.addItem(QListWidgetItem(abs_path))

def GetFileList(dir, fileList):
    """遍历文件夹"""
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList