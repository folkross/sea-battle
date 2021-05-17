from UI.settings import Ui_MainWindow_settings
from UI.startmenu import Ui_MainWindow_startmenu
from UI.rules import Ui_MainWindow_rules
from UI.readygame import Ui_MainWindow_ready
from UI.gamepvp import Ui_MainWindow_pvp
from UI.win import Ui_MainWindow_win

import sys
from random import randrange
import sqlite3
import re
import pygame
import pygame as pg

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QBasicTimer, QCoreApplication

from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QStackedWidget, QMessageBox, QInputDialog, QTableWidgetItem, QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QSound
from PyQt5 import QtWidgets

def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

COORDS = dict(("ABCDEFGHIJ"[x]+str(y+1), (y, x)) for x in range(10) for y in range(10))
players = []
SCREEN_SIZE = [(800,600), (960, 540), (1280, 720), (1920, 1080), (1000, 700)]





def new_cell_mul():  # Когда ставлю звёздочку в QTableWidget
    cell_mul = QTableWidgetItem("*")
    cell_mul.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    return cell_mul


def new_cell_x():  # Когда ставлю крестик в QTableWidget
    cell_x = QTableWidgetItem("X")
    cell_x.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    return cell_x


def new_cell_dot():  # Когда ставлю точку в QTableWidget
    cell_dot = QTableWidgetItem(".")
    cell_dot.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    return cell_dot


background_image = "1"

pygame.init()
pygame.mixer.music.load("sounds/background.wav")
pygame.mixer.music.play(-1)
background_image = "1"


class StartMenuMain(QMainWindow, Ui_MainWindow_startmenu,Ui_MainWindow_settings):
    """Стартовое меню, где можно переключаться между окнами, а также выйти из игры"""


    def __init__(self, parent=None):
        super(StartMenuMain, self).__init__(parent)
        self.setupUi(self)
        self.LOGOSB = QPixmap("images/logo.svg")  
        self.initUI()
        


        if background_image == "1":
            self.setStyleSheet('.QWidget {border-image: url(images/10321.jpg);}')
        elif background_image == "2":
            self.setStyleSheet('.QWidget {border-image: url(images/4321.jpeg);}')
        elif background_image == "3":
            self.setStyleSheet('.QWidget {border-image: url(images/5455.jpg);}')
        elif background_image == "4":
            self.setStyleSheet('.QWidget {border-image: url(images/124432.jpg);}')


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
        windows.setCurrentIndex(1)

    def to_rules(self):  # Переходит в меню правил
        windows.setCurrentIndex(2)

    def to_start(self):  # Переходит в меню начала игры

        windows.setCurrentIndex(3)


class SettingsMain(QMainWindow, Ui_MainWindow_settings,Ui_MainWindow_startmenu):
    """Меню настроек"""

    
    def background1(self):
        background_image = "1"
        windows.resize(*SCREEN_SIZE[0])

    def background2(self):
        
        windows.resize(*SCREEN_SIZE[1])

    def background3(self):
        background_image = "3"
        windows.resize(*SCREEN_SIZE[4])

    def background4(self):
        background_image = "4"
        windows.resize(*SCREEN_SIZE[3])

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

        self.label.setStyleSheet("background-color: #ffffff")

    


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


class ReadyMain(QMainWindow, Ui_MainWindow_ready):
    """Меню подготовления к самой игре"""

    def __init__(self, parent=None):             
        super(ReadyMain, self).__init__(parent)
        self.setupUi(self)

        self.map = SeaMap(self.boardMap)
        self.new_count()  # Обновление переменных-счётчиков
        self.new_map()  # Обновление карты
        self.new_images('green')  # Добавления изображений

        self.initUI()

    def initUI(self):
        # Задаю цвет и форму кнопкам
        for w in [self.linkorButton, self.kreyserButton, self.esminecButton, self.torpedButton]:
            w.setStyleSheet("color: white; background-color: #b6afa9;"
                            "border-radius: 10px;")
        self.torpedButton.clicked.connect(self.setShip)
        self.esminecButton.clicked.connect(self.setShip2)
        self.kreyserButton.clicked.connect(self.setShip3)
        self.linkorButton.clicked.connect(self.setShip4)

        self.readyButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                       "border-radius: 10px;")
        self.readyButton.clicked.connect(self.start)


    def new_images(self, who):  # Создание(обновление) изображений
        self.pixmap_linkor = QPixmap(f"images/Linkor_{who}.svg")
        self.pixmap_kreyser = QPixmap(f"images/Kreyser_{who}.svg")
        self.pixmap_esminec = QPixmap(f"images/Esminec_{who}.svg")
        self.pixmap_torped = QPixmap(f"images/Torped_{who}.svg")

        self.pixmap_linkor = self.pixmap_linkor.scaled(259, 110)
        self.pixmap_kreyser = self.pixmap_kreyser.scaled(260, 110)
        self.pixmap_esminec = self.pixmap_esminec.scaled(260, 110)
        self.pixmap_torped = self.pixmap_torped.scaled(260, 110)

        self.linkorImage.setPixmap(self.pixmap_linkor)
        self.kreyserImage.setPixmap(self.pixmap_kreyser)
        self.esminecImage.setPixmap(self.pixmap_esminec)
        self.torpedImage.setPixmap(self.pixmap_torped)

    def new_map(self):  # Метод создаёт(обновляет) карту
        for i in range(self.boardMap.columnCount()):
            for j in range(self.boardMap.rowCount()):
                self.boardMap.setItem(i, j, new_cell_dot())
        self.boardMap.resizeColumnsToContents()
        self.boardMap.resizeRowsToContents()

        self.boardMap.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.boardMap.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def new_db(self, who):  # Занесения данных в базу данных
        self.con = sqlite3.connect("Players.db")
        self.cur = self.con.cursor()
        for i, j in COORDS.items():
            self.cur.execute(f"""UPDATE {who} SET {i[0]} = '{str(self.boardMap.item(*COORDS[i]).text())}'
                         WHERE id={int(i[1:])}""")
        self.con.commit()

    def is_null(self):
        if self.countL == 0:
            self.pixmap_linkor = QPixmap(f"images/Linkor_white.svg")
            self.pixmap_linkor = self.pixmap_linkor.scaled(259, 110)
            self.linkorImage.setPixmap(self.pixmap_linkor)
        if self.countK == 0:
            self.pixmap_kreyser = QPixmap(f"images/Kreyser_white.svg")
            self.pixmap_kreyser = self.pixmap_kreyser.scaled(259, 110)
            self.kreyserImage.setPixmap(self.pixmap_kreyser)
        if self.countE == 0:
            self.pixmap_esminec = QPixmap(f"images/Esminec_white.svg")
            self.pixmap_esminec = self.pixmap_esminec.scaled(259, 110)
            self.esminecImage.setPixmap(self.pixmap_esminec)
        if self.countT == 0:
            self.pixmap_torped = QPixmap(f"images/Torped_white.svg")
            self.pixmap_torped = self.pixmap_torped.scaled(259, 110)
            self.torpedImage.setPixmap(self.pixmap_torped)

    def start(self):
        """Если Игрок1 нажал кнопку,
        то Игрок2 начинает заполнять данные.
        Иначе начинает игру"""
        # Проверка, все ли корабли поставлены
        if any(self.count.values()):
            self.error("Вы не поставили все корабли")
            return
        if self.sender().text() == 'Я  готов':
            self.new_db("Player1")
            players.append(Player('Player1', self.boardMap, self.ships))  # Добавление в список игрока
            players
            self.new_images('red')
            self.readyButton.setText("Я готов")
            self.playerLabel.setText("Игрок 2")
            self.new_count()  # Обновление переменных-счётчиков
            self.new_map()  # Обновление карты



        else:
            self.new_db("Player2")
            players.append(Player('Player2', self.boardMap, self.ships))  # Добавление в список игрока
            windows.setCurrentIndex(4)

    def new_count(self):  # Создание(обновление) переменных-счётчиков
        self.count = { 'L': 1, 'K': 2, 'E': 3, 'T': 4}
        self.ships = { 'L': [], 'K': [], 'E': [], 'T': []}
        for who in "TEKL":
            {'L': self.linkorButton,
             'K': self.kreyserButton,
             'E': self.esminecButton,
             'T': self.torpedButton}[who].setToolTip(f"{self.count[who]} left")

    def coords_is_right(self, new_coords, num, mode='dual'):
        # проверка на правильность введённых координат
        new_coords[0] = new_coords[0].upper()
        new_coords[1] = new_coords[1].upper()
        if mode != 'v':
            return (COORDS[new_coords[1]][0] - COORDS[new_coords[0]][0] == 0 and
                    COORDS[new_coords[1]][1] - COORDS[new_coords[0]][1] == num) or \
                   (COORDS[new_coords[1]][0] - COORDS[new_coords[0]][0] == num and
                    COORDS[new_coords[1]][1] - COORDS[new_coords[0]][1] == 0)
        return (COORDS[new_coords[1]][0] - COORDS[new_coords[0]][0] == num and
                COORDS[new_coords[1]][1] - COORDS[new_coords[0]][1] == 0)

    def check(self, c1, c2, i, num):
        # Проверка, если в координатах есть * или X,
        if num == 1:
            return (str(self.boardMap.item(c1 + i, c2).text()) == "*" or
                    str(self.boardMap.item(c1 + i, c2).text()) == "X")
        return (str(self.boardMap.item(c1, c2 + i).text()) == "*" or
                str(self.boardMap.item(c1, c2 + i).text()) == "X")

    def error(self, text="Недопустимый размер или форма корабля."):  # Вызов ошибки
        QMessageBox.critical(self, 'Ошибка!', text)

    def setShipByType(self, coords, num, who):  # Создание любого корабля на поле
        error = False
        new_coords = coords.split('-')
        if self.coords_is_right(new_coords, num):
            vertical = self.coords_is_right(new_coords, num, 'v')
            c1, c2 = COORDS[new_coords[0]][0], COORDS[new_coords[0]][1]
            for i in range(num + 1):
                if self.check(c1, c2, i, 1 if vertical else 2):
                    self.error("Сюда нельзя поставить корабль")
                    return
            coords_as_num = []
            for i in range(num + 1):
                if not vertical:
                    self.boardMap.setItem(c1, c2 + i, new_cell_x())
                    coords_as_num.append((c1, c2 + i))
                    if i == num:
                        self.map.shoot(c1, c2 + i, "sink")
                else:
                    self.boardMap.setItem(c1 + i, c2, new_cell_x())
                    coords_as_num.append((c1 + i, c2))
                    if i == num:
                        self.map.shoot(c1 + i, c2, 'sink')
            self.count[who] -= 1
            self.ships[who].append([coords_as_num, {'L': 4, 'K': 3, 'E': 2, 'T': 1}[who]])
            {'L': self.linkorButton,
             'K': self.kreyserButton,
             'E': self.esminecButton,
             'T': self.torpedButton}[who].setToolTip(f"{self.count[who]} left")

        else:
            self.error()



    def setShip(self):  # Создание корабля
        items = sorted(["ABCDEFGHIJ"[item.column()]+str(item.row()+1) for item in self.boardMap.selectedItems()], key=natural_key)
        n = len(items)
        if n == 1:
            if self.count[' TEKL'[n]] == 0:
                self.error("Все корабли этого типа поставлены")
                return
            try:
                self.setShipByType(f"{items[0]}-{items[-1]}", n-1, " TEKL"[n])
            except BaseException:
                self.error()
        else:
            self.error()

    def setShip2(self):  # Создание корабля
        items = sorted(["ABCDEFGHIJ"[item.column()]+str(item.row()+1) for item in self.boardMap.selectedItems()], key=natural_key)
        n = len(items)
        if n == 2:
            if self.count[' TEKL'[n]] == 0:
                self.error("Все корабли этого типа поставлены")
                return
            try:
                self.setShipByType(f"{items[0]}-{items[-1]}", n-1, " TEKL"[n])
            except BaseException:
                self.error()
        else:
            self.error()

    def setShip3(self):  # Создание корабля
        items = sorted(["ABCDEFGHIJ"[item.column()]+str(item.row()+1) for item in self.boardMap.selectedItems()], key=natural_key)
        n = len(items)
        if n == 3:
            if self.count[' TEKL'[n]] == 0:
                self.error("Все корабли этого типа поставлены")
                return
            try:
                self.setShipByType(f"{items[0]}-{items[-1]}", n-1, " TEKL"[n])
            except BaseException:
                self.error()
        else:
            self.error()

    def setShip4(self):  # Создание корабля
        items = sorted(["ABCDEFGHIJ"[item.column()]+str(item.row()+1) for item in self.boardMap.selectedItems()], key=natural_key)
        n = len(items)
        if n == 4:
            if self.count[' TEKL'[n]] == 0:
                self.error("Все корабли этого типа поставлены")
                return
            try:
                self.setShipByType(f"{items[0]}-{items[-1]}", n-1, " TEKL"[n])
            except BaseException:
                self.error()
        else:
            self.error()


class PVPMain(QMainWindow, Ui_MainWindow_pvp):
    def __init__(self, parent=None):
        super(PVPMain, self).__init__(parent)
        self.setupUi(self)


        self.turn = "Игрок1"  # Очередь первого игрока

        self.map = []
        self.map.append(SeaMap(self.tableWidget))
        self.map.append(SeaMap(self.tableWidget_2))

        self.new_boards()  # Создание игрового поля

        self.initUI()

    def initUI(self):
        self.tableWidget.cellClicked[int, int].connect(self.course1)
        self.tableWidget_2.cellClicked[int, int].connect(self.course2)


        self.board1Label.setText("Игрок 1")
        self.board2Label.setText("Игрок 2")
        self.board1Label.setStyleSheet("background-color: #B22222")
        self.board2Label.setStyleSheet("background-color: #1E90FF")


        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget_2.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def new_boards(self):
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                self.tableWidget.setItem(i, j, new_cell_dot())
        for i in range(self.tableWidget_2.columnCount()):
            for j in range(self.tableWidget_2.rowCount()):
                self.tableWidget_2.setItem(i, j, new_cell_dot())
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.resizeRowsToContents()

    def change_of_course(self):  # Смена хода
        if self.turn == "Игрок1":
            self.turn = "Игрок2"
            self.board2Label.setStyleSheet("background-color: #B22222")
            self.board1Label.setStyleSheet("background-color: #1E90FF")
            players[0], players[1] = players[1], players[0]
        elif self.turn == "Игрок2":
            self.turn = "Игрок1"
            self.board1Label.setStyleSheet("background-color: #B22222")
            self.board2Label.setStyleSheet("background-color: #1E90FF")
            players[0], players[1] = players[1], players[0]


    def info(self, text="Координаты правильные"):  # Информационное табло
        QMessageBox.information(self, "INFO", text)

    def error(self, text="Вы уже стреляли в эту клетку."):  # Вызов ошибки
        QMessageBox.critical(self, 'Ошибка!', text)

    def check(self):
        if all(players[1].board[i][j] == 0 for i in range(10) for j in range(10)):
            self.info(f"Выиграл {self.turn}!")
            windows.setCurrentIndex(5)
            return

    def course1(self, c1, c2):
        self.course(c1, c2, 1)

    def course2(self, c1, c2):
        self.course(c1, c2, 2)

    def course(self, r, c, num):  # Ход
        if self.turn[-1] == '1' and num == 2 or self.turn[-1] == '2' and num == 1:
            flag = True
            coord = (r, c)
        else:
            flag = False

        if num == 1:
            if str(self.tableWidget.item(r, c).text()) == "*" or str(self.tableWidget.item(r, c).text()) == "X" :
                self.error()
                return
        else:
            if str(self.tableWidget_2.item(r, c).text()) == "*" or str(self.tableWidget_2.item(r, c).text()) == "X" :
                self.error()
                return

        if flag:
            if self.dot_or_notdot((r, c)):
                dead = self.shootAndCheckIfShipIsDead((r, c))
                what = 'sink' if dead else  'hit'
                pl = 1 if self.turn[-1] == '1' else 0
                self.map[pl].shoot(r, c, what)
                players[1].board[r][c] = 0
                self.info("Корабль потоплен!" if dead else "Попадание!")

                self.check()
            else:
                pl = 1 if self.turn[-1] == '1' else 0
                self.map[pl].shoot(r, c, 'miss')
                self.info("Промах!")

                self.change_of_course()
        else:
            QMessageBox.critical(self, "Ошибка!", "Не ваша очередь!")

    def dot_or_notdot(self, coord):  # Проверка попал, не попал
        new_coord = None
        for key, value in COORDS.items():
            if value == coord:
                new_coord = (key, value)
                break
        con = sqlite3.connect("Players.db")
        cur = con.cursor()
        result = cur.execute(
            f"""SELECT {new_coord[0][0]} FROM Player{players[1].who[-1]}
            WHERE id={new_coord[1][0] + 1}""").fetchone()
        if result[0] == "." or result[0] == "*":
            return False
        return True

    def shootAndCheckIfShipIsDead(self, pos):  # Стреляем по кораблю и проверяем, потопил или ранил
        x, y = pos
        if 0 <= x < 10 and 0 <= y < 10:
            if players[1].board[x][y] == 1:
                for who in "TEKL":
                    for ship in players[1].ships[who]:
                        if pos in ship[0]:
                            ship[1] -= 1
                            return ship[1] == 0
        return False



class WinMain(QMainWindow, Ui_MainWindow_win):  
    """Меню выиграша"""

    def __init__(self, parent=None):
        super(WinMain, self).__init__(parent)
        self.setupUi(self)
        self.LOGO = QPixmap("images/logo.svg")
        self.initUI()
        self.setStyleSheet('.QWidget {border-image: url(images/4321.jpeg);}')

    def initUI(self):
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton.setStyleSheet("color: white; background-color: #082567;"
                                      "border-radius: 20px;")
        self.label_2.setPixmap(self.LOGO)


class Player:
    def __init__(self, who, map, ships):
        self.who = who
        self.board = []
        self.ships = ships
        for i in range(10):
            self.board.append([])
            for j in range(10):
                self.board[i].append(0)
        for i in range(10):
            for j in range(10):
                if str(map.item(i, j).text()) == 'X':
                    self.board[i][j] = 1


class SeaMap:
    def __init__(self, board):
        self.map = board

    def shoot(self, row, col, result):
        if result == 'miss':
            self.map.setItem(row, col, new_cell_mul())
        elif result == 'hit':
            self.map.setItem(row, col, new_cell_x())
        elif result == 'sink':
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        if str(self.map.item(i, j).text()) == '.':
                            self.map.setItem(i, j, new_cell_mul())
            self.map.setItem(row, col, new_cell_x())
            for j in range(10):
                if str(self.map.item(row, j).text()) == 'X':
                    col = j
                    for i in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= i < 10 and 0 <= u < 10:
                                if str(self.map.item(i, u).text()) == '.':
                                    self.map.setItem(i, u, new_cell_mul())
            for v in range(10):
                if str(self.map.item(v, col).text()) == 'X':
                    row = v
                    for v in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= v < 10 and 0 <= u < 10:
                                if str(self.map.item(v, u).text()) == '.':
                                    self.map.setItem(v, u, new_cell_mul())


if __name__ == '__main__': 
    app = QApplication(sys.argv)

   
    startmenu_window = StartMenuMain()
    settings_window = SettingsMain()
    rules_window = RulesMain()
    ready_window = ReadyMain()
    pvp_window = PVPMain()
    win_window = WinMain()

    windows = QStackedWidget()

    windows.addWidget(startmenu_window)  # 0
    windows.addWidget(settings_window)  # 1
    windows.addWidget(rules_window)  # 2
    windows.addWidget(ready_window)  # 3
    windows.addWidget(pvp_window)  # 4
    windows.addWidget(win_window)  # 5

    windows.setWindowTitle("Морской бой")
    windows.show()
    sys.exit(app.exec())
