from UI.startmenu import Ui_MainWindow_startmenu
from UI.rules import Ui_MainWindow_rules


import sys
from random import randrange
import sqlite3

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QBasicTimer, QCoreApplication

from PyQt5.QtWidgets import QApplication, QMainWindow, \
	QStackedWidget, QMessageBox, QInputDialog, QTableWidgetItem, QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QSound



class StartMenuMain(QMainWindow, Ui_MainWindow_startmenu):
	"""Стартовое меню"""

	def __init__(self, parent=None):
		super(StartMenuMain, self).__init__(parent)
		self.setupUi(self)
		self.LOGOSB = QPixmap("images/logo.svg")  # Картинка логотипа игры
		self.gmen = True  
		self.initUI()

	def initUI(self):
		self.label.setPixmap(self.LOGOSB)


		# Задаю цвет кнопкам
		self.startButton.setStyleSheet("color: white; background-color: #082567;"
									   "border-radius: 20px;")
		self.rulesButton.setStyleSheet("color: white; background-color: #082567;"
									   "border-radius: 20px;")
		self.settingsButton.setStyleSheet("color: white; background-color: #082567;"
										  "border-radius: 20px;")
		self.exitButton.setStyleSheet("color: white; background-color: #082567;"
									  "border-radius: 20px;")

		self.startButton.clicked.connect(self.to_start)
		self.rulesButton.clicked.connect(self.to_rules)
		self.exitButton.clicked.connect(QCoreApplication.instance().quit)
		self.settingsButton.clicked.connect(self.to_settings)

   

	def to_settings(self):  # Переходит в меню настроек
		windows.setCurrentIndex(10)

	def to_rules(self):  # Переходит в меню правил
		windows.setCurrentIndex(1)

	def to_start(self):  # Переходит в меню начала игры
		windows.setCurrentIndex(3)




class RulesMain(QMainWindow, Ui_MainWindow_rules):
	"""Меню правил"""

	def __init__(self, parent=None):
		super(RulesMain, self).__init__(parent)
		self.setupUi(self)
		self.LOGOSB = QPixmap("images/logo.svg")
		self.initUI()

	def initUI(self):
		self.backButton.setStyleSheet("color: white; background-color: #082567;"
									  "border-radius: 20px;")
		self.backButton.clicked.connect(self.to_start)

		self.logoImage.setPixmap(self.LOGOSB)
		self.label.setText("""Игровое поле — обычно квадрат 10×10 у каждого игрока, на котором размещается флот кораблей. 
			Вертикали обычно нумеруются сверху вниз, а горизонтали помечаются буквами слева направо. 
			При этом используются буквы латинского алфавита от «a» до «j». 

			Размещаются:

			1 корабль — ряд из 4 клеток («четырёхпалубный»)
			2 корабля — ряд из 3 клеток («трёхпалубные»)
			3 корабля — ряд из 2 клеток («двухпалубные»)
			4 корабля — 1 клетка («однопалубные»)

			При ходе нужно выбрать клетку из территории 10x10 и клетка открывается если в клетке пусто, 
			то ход переходит сопернику, если в клетке появился корабль, то ход продолжается.

			Выигрывает тот кто попопит все 10 кораблей противника раньше.""")






	def to_start(self):  # Переход в стартовое меню
		self.gmen = startmenu_window.gmen
		windows.setCurrentIndex(0)



if __name__ == '__main__': 
	app = QApplication(sys.argv)

   
	startmenu_window = StartMenuMain()
	rules_window = RulesMain()

	windows = QStackedWidget()

	windows.addWidget(startmenu_window)  # 0
	windows.addWidget(rules_window)  # 1


	windows.setWindowTitle("Морской бой")


	windows.show()
	sys.exit(app.exec())
