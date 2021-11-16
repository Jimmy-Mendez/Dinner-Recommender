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
from getDinner import makeData
from getCategory import getCategory
from PyQt5.QtCore import Qt

os.chdir("C:/Users/Jmen3/Desktop/Programs/Python/Dinner Recommender/")

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(self.createSlider(), 1, 0)
        grid.addWidget(self.createSlider(), 0, 1)
        self.setLayout(grid)

        self.setWindowTitle("Dinner Recommender")
        self.resize(400, 300)
    def createSlider(self):
        slider = QGroupBox("Slider Example")

        radio1 = QRadioButton("&Radio horizontal slider")

        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(1)

        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(slider)
        vbox.addStretch(1)
        slider.setLayout(vbox)

        return slider
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())

app = QApplication(sys.argv)



###########################################################

adventure = input("Are you feeling adventurous? (1 = yes, 0 = no): ")
distance = input("Max distance (in miles): ")
category = input("Categories?: ")

restaurants = makeData(adventure,distance,category, price)
restaurants_cat = getCategory(restaurants,'Restaurant', 'Vicinity')
print(restaurants_cat.head())

