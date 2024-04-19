from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, \
    QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox
from PyQt6.QtGui import QAction
import sys
import os
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # instantiate the parent class' init method
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add student", self) # 'self' connects 'QAction' to the actual class 'MainWindow'
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self) # 'self' connects 'QAction' to the actual class 'MainWindow'
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table) # different from 'QWidget's' 'setLayout' b/c this is 'QMainWindow'

    def load_data(self):
        connection = sqlite3.connect("database.db") # connect to db
        result = connection.execute("SELECT * FROM students") # extract data from the 'students' table in the db
                                                              # note: a database can have multiple tables
        self.table.setRowCount(0) # prevents new data from being added on top of old data and duplicates each time the code is reloaded
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number) # insert number of rows
            for column_number, data in enumerate(row_data): # insert actual data from each tuple into each row
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data))) # specify the coordinates of the cell in the table
        connection.close()


    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

class InsertDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Insert Student Data") # different from 'QWidget's' 'setLayout' b/c this is 'QDialog'
            self.setFixedWidth(300)
            self.setFixedHeight(300)

            layout = QVBoxLayout()

            # Add student name widget
            self.student_name = QLineEdit()
            self.student_name.setPlaceholderText("Name")
            layout.addWidget(self.student_name)

            # Add combo box of courses
            self.course_name = QComboBox()
            courses = ["Biology", "Math", "Astronomy", "Physics"]
            self.course_name.addItems(courses)
            layout.addWidget(self.course_name)

            # Add mobile widget
            self.mobile_number = QLineEdit()
            self.mobile_number.setPlaceholderText("Mobile number")
            layout.addWidget(self.mobile_number)

            # Add a submit button
            button = QPushButton("Register")
            button.clicked.connect(self.add_student)
            layout.addWidget(button)
            
            self.setLayout(layout)

        def add_student(self):
            name = self.student_name.text()
            course = self.course_name.itemText(self.course_name.currentIndex())
            mobile = self.mobile_number.text()
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor() # since we are inserting into the db we use a cursor object
            cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", 
                           (name, course, mobile)) # students is the name of the table
                                # we are trying to access in the db
            connection.commit()
            connection.commit()
            cursor.close()
            connection.close()
            main_window.load_data()
        
app = QApplication(sys.argv)
main_window = MainWindow() # instantiating the class 'AgeCalculator'
main_window.show()
main_window.load_data()
sys.exit(app.exec())