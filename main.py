# File: main.py
import sys
from PySide6 import QtWidgets
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6 import QtCore, QtGui, QtWidgets

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QWidget)
import datetime
from datetime import datetime
from info import *
from backend import *


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "design.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    table = QtWidgets.QTableView()
    model = TableModel(View())
    window.tableView.setModel(model)
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    #del by id
    #window.pushButton.clicked.connect(lambda: deleteitem(window.lineEdit.text()))
    #insert data
    window.pushButton_2.clicked.connect(lambda: insert(window.lineEdit_3.text(),window.lineEdit_4.text(),window.lineEdit_2.text(),window.lineEdit_5.text(),datetime.today().strftime('%Y-%m-%d')))
    #show data
    window.pushButton_3.clicked.connect(lambda: window.tableView.setModel(TableModel(View())))
    sys.exit(app.exec())