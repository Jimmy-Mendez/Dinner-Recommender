import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QCheckBox, QGridLayout, QGroupBox, QMenu, QRadioButton, QVBoxLayout, QSlider)
from PyQt5.QtCore import Qt
from visited import past
from choose import chooseRestaurant

os.chdir("C:/Users/Jmen3/Desktop/Programs/Python/Dinner Recommender/")

# importing libraries
from PyQt5.QtWidgets import *
import sys

inputs = []
results = []

class resultsWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super(resultsWindow, self).__init__()
        layout = QVBoxLayout()
        results.append(chooseRestaurant(inputs[0],inputs[1],inputs[2]))
        self.label = QLabel("The result is: \n" + str(results[-1]) + "\n Press ok if you decide to go here!")
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.storeRestaurant)
        # adding button box to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.buttonBox)
        # setting lay out
        self.setLayout(layout)
    def storeRestaurant(self):
        f = open("visited.py", "w")
        past.append(str(results[-1]))
        f.write("past = ")
        f.write(str(past))
        f.close()
        
# creating a class
# that inherits the QDialog class
class Window(QDialog):

    # constructor
    def __init__(self):
        super(Window, self).__init__()
        # setting window title
        self.setWindowTitle("Python")
        # setting geometry to the window
        self.setGeometry(100, 100, 300, 400)
        # creating a group box
        self.formGroupBox = QGroupBox("Form 1")
        # creating spin box to select age
        self.distance = QSpinBox()
        # creating combo box to select degree
        self.category = QComboBox()
        # adding items to the combo box
        self.category.addItems(["Surprise me!", "Chinese", "Pizza","American","Thai","Indian","Mexican","Cafe","Mediterranean","Diner","Fast Food"])
        # creating a line edit
        self.advLineEdit = QLineEdit()
        # calling the method that create the form
        self.createForm()
        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)
        # addding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)
        # creating a vertical layout
        mainLayout = QVBoxLayout()
        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)
        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)
        # setting lay out
        self.setLayout(mainLayout)
    # get info method called when form is accepted
    def getInfo(self):
        inputs.clear()
        # save the form information
        adventure = format(self.advLineEdit.text())
        category = format(self.category.currentText())
        distance = format(self.distance.text())
        inputs.append(adventure)
        inputs.append(category)
        inputs.append(distance)
        self.show_results()
    def show_results(self):
        self.w = resultsWindow()
        self.w.show()
    # create form method
    def createForm(self):
        # creating a form layout
        layout = QFormLayout()
        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Are you feeling adventurous? (1 = yes, 0 = no):"), self.advLineEdit)
        # for degree and adding combo box
        layout.addRow(QLabel("Enter a category"), self.category)
        # for age and adding spin box
        layout.addRow(QLabel("Max distance willing to travel (in miles)"), self.distance)
        # setting layout
        self.formGroupBox.setLayout(layout)

        
# main method
if __name__ == '__main__':
    # create pyqt5 app
    app = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    # showing the window
    window.show()
    # start the app
    sys.exit(app.exec())



app = QApplication(sys.argv)




