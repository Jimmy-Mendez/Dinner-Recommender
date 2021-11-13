import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(200, 200, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)
layout = QHBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))
window.setLayout(layout)
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())

#replace commas with '%2C'
#webpage: google.com/search?q=name+vicinity
#class=YhmCb

###########################################################

adventure = input("Are you feeling adventurous? (1 = yes, 0 = no): ")
distance = input("Max distance (in miles): ")
category = input("Categories?: ")
price = input("Price Range?: ")


makeData(adventure,distance,category, price)
