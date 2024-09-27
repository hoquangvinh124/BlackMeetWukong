from PyQt6.QtWidgets import QMainWindow, QMenu
from PyQt6.QtGui import QAction
from pymysql.constants.FIELD_TYPE import VARCHAR

from MainUI import Ui_MainWindow
import pymysql

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('SideBar Menu')

    #Hide Widget Menu
        self.icon_only_widget.setHidden(True)

    #Hide Dropdowns
        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finances_dropdown.setHidden(True)
    #Connect Buttons to switch different pages
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

    #Connect Buttons to respective context menus
        self.students_1.clicked.connect(self.students_context_menu)
        self.teachers_1.clicked.connect(self.teachers_context_menu)
        self.finances_1.clicked.connect(self.finances_context_menu)

    #Connect to db
        self.create_connection()

    #Tao bang khach hang
        self.create_customer_table()

    #Mo va them khach hang dialog
        self.addCustomer_btn.clicked.connect(self.open_addCustomer_dialog)

    #Methods to switch to different pages
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

    #Methods to show context menus
    def students_context_menu(self):
        self.show_custom_context_menu(self.students_1, ['Customer Information','Customer Payments','Customer Transactions'])

    def teachers_context_menu(self):
        self.show_custom_context_menu(self.teachers_1,['Staff Information','Staff Salaries','Staff Transactions'])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.finances_1, ['Budgets','Expenses','Business Overview'])

    def show_custom_context_menu(self, button, menu_items):

        menu = QMenu(self)

        #Set style for the menu
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
        #Add actions to the menu
        for item_text in menu_items:
            action=QAction(item_text,self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        #Show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):

        text=self.sender().text()

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
        #Tao cursor
        cursor = self.mydb.cursor()
        return self.mydb

    #TAO BANG KHACH HANG:

    def create_customer_table(self):
        cursor=self.create_connection().cursor

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
        cursor=self.mydb.cursor()
        cursor.execute(create_customer_table_query)

        #Commit
        self.mydb.commit()
        self.mydb.close()
    #Mo cua so them khach hang
    def open_addCustomer_dialog(self):
        from KhachHangDialog import Ui_KhachHangDialog
        addCustomer_dialog = Ui_KhachHangDialog(self)
        result = addCustomer_dialog.exec()

        if result == Ui_KhachHangDialog.accepted:
            pass






