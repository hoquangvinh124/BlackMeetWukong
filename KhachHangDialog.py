# Form implementation generated from reading ui file 'D:\ProjectTotNghiep\KhachHangDialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox
import pymysql
from random import randint
from datetime import datetime


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
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
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
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
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
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
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
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
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
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);")
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
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);")
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
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);")
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
        KhachHangDialog.setWindowTitle(_translate("Add", "Add"))
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

    #Them khach hang khi nhan nut
        self.addpushButton.clicked.connect(self.add_customer)
        self.cancelpushButton.clicked.connect(self.close)

    def create_connection(self):
        self.mydb = pymysql.connect(
                host='sql12.freemysqlhosting.net',
                user='sql12733511',
                password='fHsPCCsLww',
                database='sql12733511',
                port=3306
                )
        # Tao cursor
        cursor = self.mydb.cursor()
        return self.mydb

    # TAO BANG KHACH HANG:

    def create_customer_table(self):
        cursor = self.create_connection().cursor

        create_customer_table_query = f"""
        CREATE TABLE IF NOT EXISTS customer_table(
                names TEXT,
                customer_id VARCHAR(15) PRIMARY KEY,
                gender TEXT,
                nails TEXT,
                birthday TEXT,
                age INT,
                address TEXT,
                phone_number VARCHAR(15),
                email VARCHAR(15)
        )"""
        cursor = self.mydb.cursor()
        cursor.execute(create_customer_table_query)

        # Commit
        self.mydb.commit()
        self.mydb.close()

    # THEM KHACH HANG
    def insert_new_customer(self):

        try:
            connection = self.create_connection()
            if connection is None:
                return
            cursor = connection.cursor()

            gender = self.gender_comboBox.currentText()
            customer_id = self.generate_customerId(gender)

            birthday = self.handleDataChange()

            birth_date = self.dob_dateEdit.date()
            age = self.calculate_age(birth_date)

            #Tao ds khach hang
            self.new_customer = [
                self.name_lineEdit.text(),
                customer_id,
                self.gender_comboBox.currentText(),
                self.nm_comboBox.currentText(),
                birthday,
                age,
                self.address_lineEdit.text(),
                self.phone_lineEdit.text(),
                self.email_lineEdit.text()
            ]

            #Them nhieu cot
            insert_customer_query = f""" INSERT INTO customer_table (names, customer_id, gender, nails, birthday, age, address, phone_number, email) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            cursor.execute(insert_customer_query, self.new_customer)
            self.show_inserted_message()
            connection.commit()
            cursor.close()
            connection.close()

        except pymysql.connect.Error as err:
            print(f"Error: {err}")


    def generate_customerId(self,gender):

            cursor = self.create_connection().cursor()

            while True:
                 if gender == "Male":
                        id_start_value = '24' + '/U/M'
                 else:
                        id_start_value = '24' + '/U/F'

                 random_value = self.generate_randomNumber()
                 customer_id = id_start_value + random_value

                #Kiem tra neu so da ton tai trong bang
                 cursor.execute(f'SELECT customer_id FROM customer_table WHERE customer_id = %s', (customer_id,))
                 existing_id = cursor.fetchone()

                 if not existing_id:
                     return customer_id



    def generate_randomNumber(self):

            number = randint(1,1000)
            random_number = f'{number:04d}'
            return random_number

    def handleDataChange(self):
        #Chuyen doi ngay theo format
        selected_date = self.dob_dateEdit.date()
        self.date_string = selected_date.toString('yyyy-MM-dd')

        return self.date_string

    def calculate_age(self, birth_date):
        current_date = datetime.now().date()
        birth_datetime = datetime(birth_date.year(), birth_date.month(), birth_date.day()).date()
        age = current_date.year - birth_datetime.year
        if (current_date.month, current_date.day) < (birth_datetime.month, birth_datetime.day):
            age-=1
        return age

    def show_inserted_message(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Add customer")
        msg_box.setStyleSheet("color: rgb(0, 0, 0);")
        msg_box.setText(self.name_lineEdit.text() + " added into the database")
        msg_box.exec()

    def add_customer(self):
        self.insert_new_customer()
        self.accept()