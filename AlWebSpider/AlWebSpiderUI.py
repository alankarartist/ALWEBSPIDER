from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1366, 768)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget#widget{\n"
"    background-color:rgb(45,45,45);\n"
"    border:4px solid rgb(45,45,45);\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"    background-color:rgb(20,20,20);\n"
"    font-family:OnePlus Sans Display;\n"
"}\n"
"QPushButton{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgb(144,144,144);\n"
"    font:bold;\n"
"    font-size:25px;\n"
"    font-family:Entypo;\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(142,176,27);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"    color:rgb(91,88,53);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(12, -1, 12, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(15, 15))
        self.label.setMaximumSize(QtCore.QSize(15, 15))
        self.label.setStyleSheet("background-color:rgb(142,176,27);\n"
"border-radius:7px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(15, 15))
        self.label_2.setMaximumSize(QtCore.QSize(15, 15))
        self.label_2.setStyleSheet("background-color:rgb(45,45,45);\n"
"border-radius:7px;\n"
"font-family:OnePlus Sans Display;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(15, 15))
        self.label_3.setMaximumSize(QtCore.QSize(15, 15))
        self.label_3.setStyleSheet("background-color:rgb(142,176,27);\n"
"font-family:OnePlus Sans Display;"
"border:4px solid rgb(45,45,45);\n"
"border-radius:7px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(144,144,144); font-family:OnePlus Sans Display;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_7.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit.setStyleSheet("background-color:rgb(31,31,31);\n"
"font-family:OnePlus Sans Display;"
"border-radius:5px;\n"
"color:rgb(144,144,144);\n"
"padding-left:5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_8.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setStyleSheet("QTabBar::tab:selected{\n"
"     background-color:rgb(20,20,20);\n"
"    color:rgb(144,144,144);\n"
"    font-family:OnePlus Sans Display;"
"}\n"
"QWidget{\n"
"    font-family:OnePlus Sans Display;"
"    background-color:rgb(45,45,45);\n"
"    color:rgb(144,144,144);\n"
"    border:0;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ALWEBSPIDER"))
        self.label_4.setText(_translate("Form", "ALWEBSPIDER"))
        self.pushButton.setText(_translate("Form", "Ö"))
        self.pushButton_2.setText(_translate("Form", "ò"))
        self.pushButton_3.setText(_translate("Form", "X"))
        self.pushButton_4.setText(_translate("Form", "ç"))
        self.pushButton_5.setText(_translate("Form", "ê"))
        self.pushButton_6.setText(_translate("Form", "d"))
        self.pushButton_7.setText(_translate("Form", "ï"))
        self.pushButton_8.setText(_translate("Form", "e"))