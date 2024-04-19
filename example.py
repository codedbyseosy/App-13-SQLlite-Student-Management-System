from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
import os
from datetime import datetime
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'path/to/qt/plugins/platforms'

# This child class inherits from the 'QWidget' class
class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__() # super is a func that returns the parent of the class that is being called
                            # the sec init is the one from the parent class that is being called
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout() # instantiating the class 'QGridLayout'

        # Create widgets
        name_label = QLabel("Name:") # label, # instance #1 of the class 'QLabel'
        self.name_line_edit = QLineEdit() # text box

        date_birth_label = QLabel("Date of Birth MM/DD/YYYY:") # label, # label, # instance #2 of the class 'QLabel'
        self.date_birth_line_edit = QLineEdit() # text box

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("") # label, # instance #3 of the class 'QLabel'

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)

        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_birth_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")

app = QApplication(sys.argv)
age_calculator = AgeCalculator() # instantiating the class 'AgeCalculator'
age_calculator.show()
sys.exit(app.exec())

#pip3 install opencv-python==4.9.0.80
#conda create -n myenv python=3.12.2