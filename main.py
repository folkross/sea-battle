from UI.startmenu import Ui_MainWindow_startmenu
from UI.rules import Ui_MainWindow_rules
from UI.settings import Ui_MainWindow_settings

import sys
from random import randrange
import sqlite3

import pygame
import pygame as pg


from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QBasicTimer, QCoreApplication

from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QStackedWidget, QMessageBox, QInputDialog, QTableWidgetItem, QAction
from PyQt5 import QtCore, QtGui, QtMultimedia, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QSound, QSoundEffect 

global background_image
pygame.init()
pygame.mixer.music.load("sounds/background.wav")
pygame.mixer.music.play(-1)
background_image = "1"


class StartMenuMain(QMainWindow, Ui_MainWindow_startmenu):
    """Стартовое меню, где можно переключаться между окнами, а также выйти из игры"""

    def __init__(self, parent=None):
        super(StartMenuMain, self).__init__(parent)
        self.setupUi(self)
        self.LOGOSB = QPixmap("images/logo.svg")  
        
        
        if background_image == "1":
            self.setStyleSheet('.QWidget {border-image: url(images/10321.jpg);}')
        elif background_image == "2":
            self.setStyleSheet('.QWidget {border-image: url(images/4321.jpeg);}')
        elif background_image == "3":
            self.setStyleSheet('.QWidget {border-image: url(images/5455.jpg);}')
        elif background_image == "4":
            self.setStyleSheet('.QWidget {border-image: url(images/124432.jpg);}')

        self.initUI()

    def initUI(self):

        self.label.setPixmap(self.LOGOSB)
        
        



        # Задаю цвет кнопкам
        self.startButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                       "border-radius: 10px;")
        self.rulesButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                       "border-radius: 10px;")
        self.settingsButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                          "border-radius: 10px;")
        self.exitButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                      "border-radius: 10px;")

        self.startButton.clicked.connect(self.to_start)
        self.rulesButton.clicked.connect(self.to_rules)
        self.exitButton.clicked.connect(QCoreApplication.instance().quit)
        self.settingsButton.clicked.connect(self.to_settings)




 


    def to_settings(self):  # Переходит в меню настроек
        windows.setCurrentIndex(2)

    def to_rules(self):  # Переходит в меню правил
        windows.setCurrentIndex(1)

    def to_start(self):  # Переходит в меню начала игры
        windows.setCurrentIndex(0)


class SettingsMain(QMainWindow, Ui_MainWindow_settings):
    """Меню настроек"""

    

    def __init__(self, parent=None):
        super(SettingsMain, self).__init__(parent)
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.volume_level) 
        self.setStyleSheet('.QWidget {border-image: url(images/10321.jpg);}')
        self.initUI()
        


    def volume_level(self): # Регулировка звука
        new_value = str(self.horizontalSlider.value())
        if new_value == "0":
            pygame.mixer.music.pause()
        elif new_value == "1":
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.1)
        elif new_value == "2":
            pygame.mixer.music.set_volume(0.3)
        elif new_value == "3":
            pygame.mixer.music.set_volume(0.6)
        elif new_value == "4":
            pygame.mixer.music.set_volume(0.8)
        elif new_value == "5":
            pygame.mixer.music.set_volume(1)
       
           
    def background1(self):
        background_image = "1"
        self.setStyleSheet('.QWidget {border-image: url(images/10321.jpg);}')

    def background2(self):
        background_image = "2"
        self.setStyleSheet('.QWidget {border-image: url(images/4321.jpeg);}')

    def background3(self):
        background_image = "3"
        self.setStyleSheet('.QWidget {border-image: url(images/5455.jpg);}')

    def background4(self):
        background_image = "4"
        self.setStyleSheet('.QWidget {border-image: url(images/124432.jpg);}')

    


    def initUI(self):
        self.LOGOSB = QPixmap("images/logo.svg")
        self.logoImage.setPixmap(self.LOGOSB)

        # Задаю цвет кнопкам
        self.backButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                      "border-radius: 10px;")


        self.backButton.clicked.connect(self.to_start)

        self.pushButton_3.clicked.connect(self.background1)
        self.pushButton_4.clicked.connect(self.background2)
        self.pushButton.clicked.connect(self.background3)
        self.pushButton_2.clicked.connect(self.background4)



    


    def to_start(self):  # Переход в стартовое меню
        windows.setCurrentIndex(0)





class RulesMain(QMainWindow, Ui_MainWindow_rules):
    """Меню правил"""

    def __init__(self, parent=None):
        super(RulesMain, self).__init__(parent)
        self.setupUi(self)
        self.LOGOSB = QPixmap("images/logo.svg")
        self.setStyleSheet('.QWidget {border-image: url(images/10321.jpg);}')
        self.initUI()

    def initUI(self):
        self.backButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                      "border-radius: 10px;")
        self.backButton.clicked.connect(self.to_start)

        self.logoImage.setPixmap(self.LOGOSB)
        self.label.setText("""Игровое поле — обычно квадрат 10×10 у каждого игрока, на котором размещается флот кораблей. 
            Вертикали обычно нумеруются сверху вниз, а горизонтали помечаются буквами слева направо. 
            При этом используются буквы латинского алфавита от «a» до «j». 

            Размещаются:

            1 корабль — ряд из 4 клеток («четырёхпалубный»)
            2 корабля — ряд из 3 клеток («трёхпалубные»)
            3 корабля — ряд из 2 клеток («двухпалубные»)
            4 корабля — 1 клетка («однопалубные»)""")




  

    def to_start(self):  # Переход в стартовое меню
        windows.setCurrentIndex(0)




if __name__ == '__main__': 
    app = QApplication(sys.argv)

   
    startmenu_window = StartMenuMain()
    rules_window = RulesMain()
    settings_window = SettingsMain()

    windows = QStackedWidget()

    windows.addWidget(startmenu_window)  # 0
    windows.addWidget(rules_window)   # 1
    windows.addWidget(settings_window) # 2

    windows.setWindowTitle("Морской бой")


    windows.show()
    sys.exit(app.exec())
