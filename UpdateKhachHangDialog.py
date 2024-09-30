# Form implementation generated from reading ui file 'C:\Users\ACER\PycharmProjects\BlackMeetWukong\UpdateKhachHangDialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import pymysql
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QMessageBox
from random import randint
from datetime import datetime


class UpdateKhachHangDialog(QDialog):
    def __init__(self, row_index, row_data):
        super().__init__()

        #store the row_index and row_data as ínstance variables
        self.row_index=row_index
        self.row_data=row_data

        self.student_info = self.select_student()[0]

        self.student_name_info = self.student_info[0]
        self.student_id_info = self.student_info[1]
        self.student_gender_info = self.student_info[2]
        self.student_model_info = self.student_info[3]
        self.student_birthday_info = self.student_info[4]
        self.student_age_info = self.student_info[5]
        self.student_address_info = self.student_info[6]
        self.student_phone_info = self.student_info[7]
        self.student_email_info = self.student_info[8]

        self.resize(548, 584)
        self.setStyleSheet(u"QDialog{\n"
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
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.update_name_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.update_name_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.update_name_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.update_name_lineEdit.setObjectName("update_name_lineEdit")
        self.verticalLayout.addWidget(self.update_name_lineEdit)
        self.verticalLayout_17.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_15 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_14.addWidget(self.label_15)
        self.update_gender_comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(7)
        font.setBold(False)
        self.update_gender_comboBox.setFont(font)
        self.update_gender_comboBox.setObjectName("update_gender_comboBox")
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.addItem("")
        self.verticalLayout_14.addWidget(self.update_gender_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_14)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_16 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("\n"
"color: rgb(0, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_16.addWidget(self.label_16)
        self.update_nm_comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(7)
        font.setBold(False)
        self.update_nm_comboBox.setFont(font)
        self.update_nm_comboBox.setObjectName("update_nm_comboBox")
        self.update_nm_comboBox.addItem("")
        self.update_nm_comboBox.addItem("")
        self.update_nm_comboBox.addItem("")
        self.verticalLayout_16.addWidget(self.update_nm_comboBox)
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
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_15.addWidget(self.label_17)
        self.update_dob_dateEdit = QtWidgets.QDateEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(7)
        font.setBold(False)
        self.update_dob_dateEdit.setFont(font)
        self.update_dob_dateEdit.setObjectName("update_dob_dateEdit")
        self.verticalLayout_15.addWidget(self.update_dob_dateEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.verticalLayout_17.addLayout(self.horizontalLayout)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_12 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.update_address_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.update_address_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.update_address_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.update_address_lineEdit.setObjectName("update_address_lineEdit")
        self.verticalLayout_11.addWidget(self.update_address_lineEdit)
        self.verticalLayout_17.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_13 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_12.addWidget(self.label_13)
        self.update_phone_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.update_phone_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.update_phone_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.update_phone_lineEdit.setObjectName("update_phone_lineEdit")
        self.verticalLayout_12.addWidget(self.update_phone_lineEdit)
        self.verticalLayout_17.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_14 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_13.addWidget(self.label_14)
        self.update_email_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.update_email_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.update_email_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.update_email_lineEdit.setObjectName("update_email_lineEdit")
        self.verticalLayout_13.addWidget(self.update_email_lineEdit)
        self.verticalLayout_17.addLayout(self.verticalLayout_13)
        self.layoutWidget1 = QtWidgets.QWidget(self)
        self.layoutWidget1.setGeometry(QtCore.QRect(300, 510, 231, 43))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.updatepushButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.updatepushButton.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.updatepushButton.setFont(font)
        self.updatepushButton.setStyleSheet("QPushButton{\n"
"    background-color: #34D481;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"\n"
"}")
        self.updatepushButton.setObjectName("updatepushButton")
        self.horizontalLayout_2.addWidget(self.updatepushButton)
        self.updatecancelpushButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.updatecancelpushButton.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.updatecancelpushButton.setFont(font)
        self.updatecancelpushButton.setStyleSheet("QPushButton{\n"
"    background-color: #585858;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"\n"
"}")
        self.updatecancelpushButton.setObjectName("updatecancelpushButton")
        self.horizontalLayout_2.addWidget(self.updatecancelpushButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("UpdateKhachHangDialog", "Update Khach Hang Dialog"))
        self.setWindowIcon(QIcon(":/Icons/logo.png"))
        self.label.setText(_translate("UpdateKhachHangDialog", "<html><head/><body><p align=\"center\">Update Customer Information</p></body></html>"))
        self.label_2.setText(_translate("UpdateKhachHangDialog", "Full Name"))
        self.label_15.setText(_translate("UpdateKhachHangDialog", "<html><head/><body><p>Gender</p></body></html>"))
        self.update_gender_comboBox.setItemText(0, _translate("UpdateKhachHangDialog", "Male"))
        self.update_gender_comboBox.setItemText(1, _translate("UpdateKhachHangDialog", "Female"))
        self.update_gender_comboBox.setItemText(2, _translate("UpdateKhachHangDialog", "Others"))
        self.label_16.setText(_translate("UpdateKhachHangDialog", "<html><head/><body><p>Nail Models</p></body></html>"))
        self.update_nm_comboBox.setItemText(0, _translate("UpdateKhachHangDialog", "Nam"))
        self.update_nm_comboBox.setItemText(1, _translate("UpdateKhachHangDialog", "Nữ"))
        self.update_nm_comboBox.setItemText(2, _translate("UpdateKhachHangDialog", "Khác"))
        self.label_17.setText(_translate("UpdateKhachHangDialog", "<html><head/><body><p>Date Of Birth</p></body></html>"))
        self.label_12.setText(_translate("UpdateKhachHangDialog", "Address"))
        self.label_13.setText(_translate("UpdateKhachHangDialog", "Phone Number"))
        self.label_14.setText(_translate("UpdateKhachHangDialog", "Email"))
        self.updatepushButton.setText(_translate("UpdateKhachHangDialog", "Update"))
        self.updatecancelpushButton.setText(_translate("UpdateKhachHangDialog", "Cancel"))
    # RetranlateUi

        #For the Date from the MySQL Database, first convert the string to a Qdate before displaying in QDateEdit
        date_object=QDate.fromString(self.student_birthday_info, "yyyy-MM-dd" )

        self.update_name_lineEdit.setText(str(self.student_name_info))
        self.update_gender_comboBox.setCurrentText(str(self.student_gender_info))
        self.update_nm_comboBox.setCurrentText(str(self.student_model_info))
        self.update_dob_dateEdit.setDate(date_object)
        self.update_address_lineEdit.setText(str(self.student_address_info))
        self.update_phone_lineEdit.setText(str(self.student_phone_info))
        self.update_email_lineEdit.setText(str(self.student_email_info))

        #Store initial gender of the QComboBoxx
        self.lastIndex=self.update_gender_comboBox.currentText()

        self.updatepushButton.clicked.connect(self.update_data)



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

    def select_student(self):

            self.cursor = self.create_connection().cursor()

            #get customer variables from the tuple
            self.student_name=self.row_data[0]
            self.student_id = self.row_data[1]

            params=[
                    self.student_name,
                    self.student_id
            ]

            select_query=f"SELECT * FROM students_table WHERE name=%s AND student_id=%s"

            self.cursor.execute(select_query, params)

            records=self.cursor.fetchall()

            self.mydb.commit()
            self.mydb.close()
            return records

    def  update_data(self):

            try:
                connection = self.create_connection()

                if connection is None:
                        return
                cursor=connection.cursor()

                #Assuming birthday is a QDateObject
                birth_date=self.update_dob_dateEdit.date()

                birthday=self.handleDataChange()
                age=self.calculate_age(birth_date)

                #Check if the gender has changed. create a new customer id
                current_student_id=self.on_gender_changed(self.update_gender_comboBox.currentText())

                params=(
                        self.update_name_lineEdit.text(),
                        current_student_id,
                        self.update_gender_comboBox.currentText(),
                        self.update_nm_comboBox.currentText(),
                        birthday,
                        age,
                        self.update_address_lineEdit.text(),
                        self.update_email_lineEdit.text(),
                        self.update_phone_lineEdit.text(),
                        self.student_id_info
                )

                print(params)

                update_query=f'UPDATE students_table SET names=%s, student_id=%s, gender=%s, model=%s, birthday=%s, age=%s, address=%s, phone_number=%s, email=%s WHERE student_id=%s'

                cursor.execute(update_query, params)
                connection.commit()
                self.show_updated_message()
                cursor.close()
                connection.close()
                self.close()

            except pymysql.connection.Error as err:
                    print(f'Error: {err}')


    def handleDataChange(self):
            # Chuyen doi ngay theo format
            selected_date = self.update_dob_dateEdit.date()
            self.date_string = selected_date.toString('yyyy-MM-dd')

            return self.date_string

    def calculate_age(self, birth_date):
            current_date = datetime.now().date()
            birth_datetime = datetime(birth_date.year(), birth_date.month(), birth_date.day()).date()
            age = current_date.year - birth_datetime.year
            if (current_date.month, current_date.day) < (birth_datetime.month, birth_datetime.day):
                    age -= 1
            return age
    def on_gender_changed(self, index):

            if index !=self.lastIndex:
                    gender_item=self.update_gender_comboBox.currentText()
                    new_student_id=self.generate_customerId(gender_item)

                    return new_student_id
            else:
                    return self.student_id_info

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

    def show_updated_message(self):
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Success")
            msg_box.setText(self.student_name_info + " information updated successfully")
            msg_box.exec()