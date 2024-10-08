from PyQt6.QtWidgets import QMainWindow, QMenu, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QMessageBox, QFileDialog
from PyQt6.QtGui import QAction, QIcon
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import pandas as pd

from pymysql.constants.FIELD_TYPE import VARCHAR

from MainUI import Ui_MainWindow
import pymysql
from UpdateKhachHangDialog import UpdateKhachHangDialog


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Tiem Nail Negav')

        # Giau Widget Menu
        self.icon_only_widget.setHidden(True)

        # Giau thanh dropdown
        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finances_dropdown.setHidden(True)
        # Chuyen trang khi bam
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.institution_1.clicked.connect(self.switch_to_institution_page)
        self.institution_2.clicked.connect(self.switch_to_institution_page)

        self.student_info.clicked.connect(self.switch_to_studentInfo_page)
        self.student_payments.clicked.connect(self.switch_to_studentPayments_page)
        self.student_transactions.clicked.connect(self.switch_to_studentTransactions_page)

        self.teacher_info.clicked.connect(self.switch_to_teacherInfo_page)
        self.teacher_salaries.clicked.connect(self.switch_to_teacherSalaries_page)
        self.teacher_transactions.clicked.connect(self.switch_to_teacherTransactions_page)

        self.budgets.clicked.connect(self.switch_to_budgetsInfo_page)
        self.expenses.clicked.connect(self.switch_to_expensesInfo_page)
        self.business_overview.clicked.connect(self.switch_to_businessOverview_page)

        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)

        self.students_1.clicked.connect(self.students_context_menu)
        self.teachers_1.clicked.connect(self.teachers_context_menu)
        self.finances_1.clicked.connect(self.finances_context_menu)

        #Ket noi db
        self.create_connection()

        # Tao bang khach hang
        self.create_customer_table()

        # Load thong tin vao QTable
        self.load_customers_info()
        self.select_model.currentIndexChanged.connect(self.reload_customertable_info)
        self.select_gender.currentIndexChanged.connect(self.reload_customertable_info)
        self.search_student.textChanged.connect(self.search_customer)

        # Dieu chinh kich thuoc bang
        self.customerInfo_table.setColumnWidth(0, 110)
        self.customerInfo_table.setColumnWidth(1, 70)
        self.customerInfo_table.setColumnWidth(2, 60)
        self.customerInfo_table.setColumnWidth(3, 70)
        self.customerInfo_table.setColumnWidth(4, 70)
        self.customerInfo_table.setColumnWidth(5, 50)
        self.customerInfo_table.setColumnWidth(6, 70)
        self.customerInfo_table.setColumnWidth(7, 80)
        self.customerInfo_table.setColumnWidth(8, 80)
        self.customerInfo_table.setColumnWidth(9, 140)

        # Xuat Excel
        self.excelExport_btn.clicked.connect(self.export_to_excel_customerTable)

        # Xuat PDF
        self.pdfExport_btn.clicked.connect(self.export_to_pdf_customerTable)

        # Mo va them khach hang dialog
        self.addCustomer_btn.clicked.connect(self.open_addCustomer_dialog)

    # Chuyen trang
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_institution_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_studentInfo_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_studentPayments_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_studentTransactions_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_teacherInfo_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_teacherSalaries_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_teacherTransactions_page(self):
        self.stackedWidget.setCurrentIndex(7)

    def switch_to_budgetsInfo_page(self):
        self.stackedWidget.setCurrentIndex(8)

    def switch_to_expensesInfo_page(self):
        self.stackedWidget.setCurrentIndex(9)

    def switch_to_businessOverview_page(self):
        self.stackedWidget.setCurrentIndex(10)

    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(11)

    # Xem noi dung cac muc
    def students_context_menu(self):
        self.show_custom_context_menu(self.students_1,
                                      ['Customer Information', 'Customer Payments', 'Customer Transactions'])

    def teachers_context_menu(self):
        self.show_custom_context_menu(self.teachers_1, ['Staff Information', 'Staff Salaries', 'Staff Transactions'])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.finances_1, ['Budgets', 'Expenses', 'Business Overview'])

    def show_custom_context_menu(self, button, menu_items):

        menu = QMenu(self)

        menu.setStyleSheet('''
                                QMenu{
                                background-color: black;
                                color: white;
                                }

                                QMenu:selected{
                                background-color: white;
                                color: #12B298;
                                }

                                ''')
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):

        text = self.sender().text()

        if text == 'Customer Information':
            self.switch_to_studentInfo_page()
        elif text == 'Customer Payments':
            self.switch_to_studentPayments_page()
        elif text == 'Customer Transactions':
            self.switch_to_studentTransactions_page()
        elif text == 'Staff Information':
            self.switch_to_teacherInfo_page()
        elif text == 'Staff Salaries':
            self.switch_to_teacherSalaries_page()
        elif text == 'Staff Transactions':
            self.switch_to_teacherTransactions_page()
        elif text == 'Budgets':
            self.switch_to_budgetsInfo_page()
        elif text == 'Expenses':
            self.switch_to_expensesInfo_page()
        elif text == 'Business Overview':
            self.switch_to_businessOverview_page()

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

    # Tao bang khach hang:
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
                email TEXT
        )"""
        cursor = self.mydb.cursor()
        cursor.execute(create_customer_table_query)

        self.mydb.commit()
        self.mydb.close()

    # Mo cua so them khach hang
    def open_addCustomer_dialog(self):
        from KhachHangDialog import Ui_KhachHangDialog
        addCustomer_dialog = Ui_KhachHangDialog(self)
        result = addCustomer_dialog.exec()
        self.reload_customertable_info()

    def reload_customertable_info(self):
        self.load_customers_info()

    # Tai thong tin vao QTable
    def load_customers_info(self):
        # Clear existing data in the table
        self.customerInfo_table.setRowCount(0)

        # Loc du lieu dua tren model va gioi tinh
        selected_model = self.select_model.currentText()
        selected_gender = self.select_gender.currentText()
        data = self.get_data_from_table(selected_model, selected_gender)

        for row_index, row_data in enumerate(data):
            self.customerInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.customerInfo_table.setItem(row_index, col_index, item)

                double_button_widget = DoubleButtonWidgetCustomer(row_index, row_data, self)

                self.customerInfo_table.setCellWidget(row_index, 9, double_button_widget)
                self.customerInfo_table.setRowHeight(row_index, 50)

    # Xuat Excel
    def export_to_excel_customerTable(self):
        data = []

        self.headers = [self.customerInfo_table.horizontalHeaderItem(col).text() for col in
                        range(self.customerInfo_table.columnCount())]

        for row in range(self.customerInfo_table.rowCount()):
            row_data = [self.customerInfo_table.item(row, col).text() if self.customerInfo_table.item(row,
                                                                                                                  col) is not None else ""
                        for col in range(self.customerInfo_table.columnCount())]
            data.append(row_data)

        df = pd.DataFrame(data, columns=self.headers)

        df_filtered = df.iloc[:, :-1]

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save Excel File", "", "Excel Files (*.xlsx);;All Files (*)")
        if file_path:
            df_filtered.to_excel(file_path, index=False)
            print(f"Table exported to {file_path}")

    # Xuat PDF
    def export_to_pdf_customerTable(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save PDF File", "", "PDF Files (*.pdf);;All Files (*)")

        if file_path:
            pdf_document = SimpleDocTemplate(file_path, pagesize=letter)

            n = self.customerInfo_table.columnCount()

            headers = [self.customerInfo_table.horizontalHeaderItem(col).text() for col in range(n - 1)]

            data = [headers]

            for row in range(self.customerInfo_table.rowCount()):
                row_data = [
                    self.customerInfo_table.item(row, col).text() if self.customerInfo_table.item(row,col) is not None else "" for col in range(n - 1)
                ]
                data.append(row_data)

            pdf_table = Table(data)

            style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 8),
                ('FONTSIZE', (1, 1), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])

            pdf_table.setStyle(style)
            pdf_document.build([pdf_table])
            print(f"Table exported to {file_path}")

    def get_data_from_table(self, nails_filter, gender_filter):
        cursor = self.create_connection().cursor()
        query = f"""SELECT names, customer_id, gender, nails, birthday, age, address, phone_number, email FROM customer_table WHERE
                ('{nails_filter}' = 'SELECT MODEL' OR nails = '{nails_filter}') AND
                ('{gender_filter}' = 'SELECT GENDER' or gender = '{gender_filter}')"""

        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def search_customer(self):
        self.customerInfo_table.setRowCount(0)
        search_query = self.search_student.text()
        cursor = self.create_connection().cursor()
        sql_query = f"""SELECT names, customer_id, gender, nails, birthday, age, address, phone_number, email FROM customer_table WHERE
                                names LIKE '%{search_query}%'"""
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row_index, row_data in enumerate(results):
            self.customerInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.customerInfo_table.setItem(row_index, col_index, item)

                double_button_widget = DoubleButtonWidgetCustomer(row_index, row_data, self)

                self.customerInfo_table.setCellWidget(row_index, 9, double_button_widget)
                self.customerInfo_table.setRowHeight(row_index, 50)


class DoubleButtonWidgetCustomer(QWidget):
    def __init__(self, row_index, row_data, sideBar):
        super().__init__()

        self.row_index = row_index
        self.row_data = row_data
        self.sideBar = sideBar

        self.customer_name = self.row_data[0]
        self.customer_id = self.row_data[1]

        layout = QHBoxLayout(self)

        self.edit_button = QPushButton("", self)
        self.edit_button.setStyleSheet("background-color: blue;")
        self.edit_button.setFixedSize(61, 31)
        self.edit_button.clicked.connect(self.edit_clicked)

        self.delete_button = QPushButton("", self)
        self.delete_button.setStyleSheet("background-color: red;")
        self.delete_button.setFixedSize(61, 31)
        self.delete_button.clicked.connect(self.delete_clicked)

        icon = QIcon(":/edit.png")
        self.edit_button.setIcon(icon)

        icon2 = QIcon(":/delete.png")
        self.delete_button.setIcon(icon2)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

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

    def edit_clicked(self):
        #Hien thi bang du lieu Update
        self.update_dialog=UpdateKhachHangDialog(self.row_index, self.row_data)

        #Reload lai QTable
        self.update_dialog.data_updated.connect(self.sideBar.reload_customertable_info)
        self.update_dialog.exec()

    def delete_clicked(self):
        cursor = self.create_connection().cursor

        #Xac thuc yeu cau nguoi dung
        message=QMessageBox.question(
            self,'Confirmation',
            'Are you sure you want to delete '+ self.customer_name + '?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if message==QMessageBox.StandardButton.Yes:
            delete_query='DELETE FROM customer_table WHERE customer_id=%s'
            cursor = self.mydb.cursor()
            cursor.execute(delete_query,(self.customer_id))
            self.mydb.commit()
            self.mydb.close()
            self.sideBar.reload_customertable_info()




