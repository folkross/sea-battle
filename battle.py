
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication



Form, Window = uic.loadUiType("tracker.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def exit_game():
	exit()

form.pushButton_3.clicked.connect(exit_game)




app.exec_()



