from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from AlWebSpider.AlWebSpiderUI import Ui_Form
import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))

class MoveWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MoveWidget, self).__init__()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

class AlWebSpider(MoveWidget, Ui_Form):
    def __init__(self):
        super(AlWebSpider, self).__init__()
        self.setWindowIcon(QIcon(os.path.join(cwd+'\\UI\\icons', 'alwebspider.png')))
        self.setupUi(self)
        self.showMaximized()
        self.tabWidget.tabBarDoubleClicked.connect(self.tabDoubleClickOpen)
        self.tabWidget.currentChanged.connect(self.currentTabChange)
        self.tabWidget.tabCloseRequested.connect(self.closeCurrentTab)
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_2.clicked.connect(self.winShowMaximized)
        self.pushButton_3.clicked.connect(sys.exit)
        self.pushButton_4.clicked.connect(lambda: self.tabWidget.currentWidget().back())
        self.pushButton_5.clicked.connect(lambda: self.tabWidget.currentWidget().forward())
        self.pushButton_6.clicked.connect(lambda: self.tabWidget.currentWidget().reload())
        self.pushButton_7.clicked.connect(self.navigateHome)
        self.lineEdit.returnPressed.connect(self.navigateToUrl)
        self.pushButton_8.clicked.connect(lambda: self.tabWidget.currentWidget().stop())
        self.addNewTab(QUrl('http://www.google.com'), 'Homepage')

    def addNewTab(self, qUrl = None, label ="Blank"):
        if qUrl is None:
            qUrl = QUrl('http://www.google.com')
        webEngineView = QWebEngineView()
        webEngineView.setUrl(qUrl)
        index = self.tabWidget.addTab(webEngineView, label)
        self.tabWidget.setCurrentIndex(index)
        webEngineView.urlChanged.connect(lambda qUrl, webEngineView = webEngineView: self.updateUrlBar(qUrl, webEngineView))
        webEngineView.loadFinished.connect(lambda _, index = index, webEngineView = webEngineView: self.tabWidget.setTabText(index, webEngineView.page().title()))

    def tabDoubleClickOpen(self, index):
        if index == -1:
            self.addNewTab()

    def currentTabChange(self, index):
        qUrl = self.tabWidget.currentWidget().url()
        self.updateUrlBar(qUrl, self.tabWidget.currentWidget())
        self.updateTitle(self.tabWidget.currentWidget())

    def closeCurrentTab(self, index):
        if self.tabWidget.count() >= 2:
            self.tabWidget.removeTab(index)

    def updateTitle(self, browser):
        if browser != self.tabWidget.currentWidget():
            return
        title = self.tabWidget.currentWidget().page().title()
        if title != '':
            self.setWindowTitle("% s - ALWEBSPIDER" % title)
        else:
            self.setWindowTitle("ALWEBSPIDER")

    def navigateHome(self):
        self.tabWidget.currentWidget().setUrl(QUrl("http://www.google.com"))

    def navigateToUrl(self):
        qUrl = QUrl(self.lineEdit.text())
        if qUrl.scheme() == "":
            qUrl.setScheme("http")
        self.tabWidget.currentWidget().setUrl(qUrl)

    def updateUrlBar(self, qUrl, browser = None):
        if browser != self.tabWidget.currentWidget():
            return
        self.lineEdit.setText(qUrl.toString())
        self.lineEdit.setCursorPosition(0)

    def winShowMaximized(self):
        if self.pushButton_2.isChecked():
            self.widget.setStyleSheet("QWidget#widget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(20,20,20,255), stop:0.706215 rgba(20,20,20,255), stop:0.711864 rgba(45,45,46,255), stop:1 rgba(45,45,45,255));border:4px solid rgb(45,45,45);}")
            self.showMaximized()
        else:
            self.widget.setStyleSheet("QWidget#widget{border:4px solid rgb(45,45,45);}")
            self.showNormal()  

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = AlWebSpider()
    form.show()
    sys.exit(app.exec_())