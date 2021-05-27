from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import remover


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 349)
        MainWindow.setMinimumSize(QtCore.QSize(650, 349))
        MainWindow.setMaximumSize(QtCore.QSize(650, 349))
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#24272b;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.path_value = QtWidgets.QLineEdit(self.centralwidget)
        self.path_value.setEnabled(False)
        self.path_value.setGeometry(QtCore.QRect(130, 190, 260, 31))
        self.path_value.setStyleSheet("color:white;")
        self.path_value.setObjectName("path_value")
        self.browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse_btn.setGeometry(QtCore.QRect(400, 190, 100, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.browse_btn.setFont(font)
        self.browse_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.browse_btn.setMouseTracking(False)
        self.browse_btn.setAutoFillBackground(False)
        self.browse_btn.setStyleSheet("    color: #333;\n"
                                      "    border: 2px solid #555;\n"
                                      "    border-radius: 20px;\n"
                                      "    border-style: outset;\n"
                                      "    background: qradialgradient(\n"
                                      "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                      "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                      "        );\n"
                                      "    padding: 5px;\n"
                                      "")
        self.browse_btn.setIconSize(QtCore.QSize(16, 16))
        self.browse_btn.setAutoRepeat(False)
        self.browse_btn.setAutoExclusive(False)
        self.browse_btn.setAutoDefault(False)
        self.browse_btn.setDefault(False)
        self.browse_btn.setFlat(False)
        self.browse_btn.setObjectName("browse_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 611, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#429bf5;\n"
                                 "font:bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 180, 21, 21))
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(260, 250, 131, 41))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.start_btn.setMouseTracking(False)
        self.start_btn.setAutoFillBackground(False)
        self.start_btn.setStyleSheet("    color: #333;\n"
                                     "    border: 2px solid #555;\n"
                                     "    border-radius: 20px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding: 5px;\n"
                                     "")
        self.start_btn.setIconSize(QtCore.QSize(16, 16))
        self.start_btn.setAutoRepeat(False)
        self.start_btn.setAutoExclusive(False)
        self.start_btn.setAutoDefault(False)
        self.start_btn.setDefault(False)
        self.start_btn.setFlat(False)
        self.start_btn.setObjectName("start_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Empty Folder Remover"))
        self.browse_btn.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Empty Folder Remover"))
        self.label_2.setText(_translate("MainWindow", "Path"))
        self.start_btn.setText(_translate("MainWindow", "Start"))

    def browser(self):
        self.file_path = QFileDialog.getExistingDirectory(None, "Select Directory")
        self.path_value.setText(self.file_path)

    def on_browse_click(self):
        self.browse_btn.clicked.connect(self.browser)

    def deleter(self):
        remover.remove(self.file_path)


    def on_run_click(self):
        self.start_btn.clicked.connect(self.deleter)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.on_browse_click()
    ui.on_run_click()
    MainWindow.show()
    sys.exit(app.exec_())
