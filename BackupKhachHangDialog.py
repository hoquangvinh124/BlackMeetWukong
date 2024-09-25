# Form implementation generated from reading ui file 'D:\ProjectTotNghiep\KhachHangDialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Ui_KhachHangDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(548, 584)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setStyleSheet("QDialog{\n"
"    background-color: #F8F8F8;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 1px solid gray;\n"
"    border-radius: 6px;\n"
"    padding-left: 15px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"    border: 1px solid gray;\n"
"    border-radius: 6px;\n"
"    padding-left: 15px;\n"
"    height: 31px;\n"
"}\n"
"\n"
"QComboBox{\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    background-color: black;\n"
"    color: white;\n"
"    height: 35px;\n"
"    padding-left: 15px;\n"
"    font-weight: ;\n"
"    selection-background-color: #2980B9;\n"
"}\n"
"\n"
"")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, 70, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 551, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(52, 212, 129);")
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 521, 392))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.name_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.name_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.verticalLayout.addWidget(self.name_lineEdit)
        self.verticalLayout_17.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_15 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_14.addWidget(self.label_15)
        self.gender_comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.gender_comboBox.setFont(font)
        self.gender_comboBox.setObjectName("gender_comboBox")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.verticalLayout_14.addWidget(self.gender_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_14)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_16 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_16.addWidget(self.label_16)
        self.nm_comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.nm_comboBox.setFont(font)
        self.nm_comboBox.setObjectName("nm_comboBox")
        self.nm_comboBox.addItem("")
        self.nm_comboBox.addItem("")
        self.nm_comboBox.addItem("")
        self.verticalLayout_16.addWidget(self.nm_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_16)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_17 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_15.addWidget(self.label_17)
        self.dob_dateEdit = QtWidgets.QDateEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.dob_dateEdit.setFont(font)
        self.dob_dateEdit.setObjectName("dob_dateEdit")
        self.verticalLayout_15.addWidget(self.dob_dateEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.verticalLayout_17.addLayout(self.horizontalLayout)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_12 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.address_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.address_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.address_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.address_lineEdit.setObjectName("address_lineEdit")
        self.verticalLayout_11.addWidget(self.address_lineEdit)
        self.verticalLayout_17.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_13 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_12.addWidget(self.label_13)
        self.phone_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.phone_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.phone_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.verticalLayout_12.addWidget(self.phone_lineEdit)
        self.verticalLayout_17.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_14 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_13.addWidget(self.label_14)
        self.email_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.email_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.verticalLayout_13.addWidget(self.email_lineEdit)
        self.verticalLayout_17.addLayout(self.verticalLayout_13)
        self.layoutWidget1 = QtWidgets.QWidget(self)
        self.layoutWidget1.setGeometry(QtCore.QRect(300, 510, 231, 43))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addpushButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.addpushButton.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.addpushButton.setFont(font)
        self.addpushButton.setStyleSheet("QPushButton{\n"
"    background-color: #34D481;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"\n"
"}")
        self.addpushButton.setObjectName("addpushButton")
        self.horizontalLayout_2.addWidget(self.addpushButton)
        self.cancelpushButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.cancelpushButton.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.cancelpushButton.setFont(font)
        self.cancelpushButton.setStyleSheet("QPushButton{\n"
"    background-color: #585858;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"\n"
"}")
        self.cancelpushButton.setObjectName("cancelpushButton")
        self.horizontalLayout_2.addWidget(self.cancelpushButton)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, KhachHangDialog):
        _translate = QtCore.QCoreApplication.translate
        KhachHangDialog.setWindowTitle(_translate("Thêm Khách Hàng", "Thêm Khách Hàng"))
        self.label.setText(_translate("KhachHangDialog", "<html><head/><body><p align=\"center\">Add customer</p></body></html>"))
        self.label_2.setText(_translate("KhachHangDialog", "Full Name"))
        self.label_15.setText(_translate("KhachHangDialog", "<html><head/><body><p>Gender</p></body></html>"))
        self.gender_comboBox.setItemText(0, _translate("KhachHangDialog", "Male"))
        self.gender_comboBox.setItemText(1, _translate("KhachHangDialog", "Female"))
        self.gender_comboBox.setItemText(2, _translate("KhachHangDialog", "Others"))
        self.label_16.setText(_translate("KhachHangDialog", "<html><head/><body><p>Nail Models</p></body></html>"))
        self.nm_comboBox.setItemText(0, _translate("KhachHangDialog", "Nam"))
        self.nm_comboBox.setItemText(1, _translate("KhachHangDialog", "Nữ"))
        self.nm_comboBox.setItemText(2, _translate("KhachHangDialog", "Khác"))
        self.label_17.setText(_translate("KhachHangDialog", "<html><head/><body><p>Date Of Birth</p></body></html>"))
        self.label_12.setText(_translate("KhachHangDialog", "Address"))
        self.label_13.setText(_translate("KhachHangDialog", "Phone Number"))
        self.label_14.setText(_translate("KhachHangDialog", "Email"))
        self.addpushButton.setText(_translate("KhachHangDialog", "Add"))
        self.cancelpushButton.setText(_translate("KhachHangDialog", "Cancel"))
