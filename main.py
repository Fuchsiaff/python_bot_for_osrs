
from pyautogui import *
from PIL import Image
from time import sleep
import random
import threading
from pymsgbox import alert
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QThread
from PyQt5 import QtTest


FAILSAFE = True

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Python bot'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 340
        self.threading = Thread() #yes
        self.threading.start()
        #self.setWindowIcon(QIcon()
        self.willow_log = r'images\willow.png'
        #self.maple_log = r'images\maple_log.png'
        #self.yew_log = None
        #self.magic_log = None

        #self.knife_willows = r'images\knife_willow.png'
        #self.willow_long_bow = r'images\long_bow.png'
        self.backpack_image = r'images\backpack_loadout.png'
        self.python_power = r'images\python_powered.png'
        self.main()  # running the main func

    
    def main(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        
        #creating willow button

        button = QPushButton('Willow longbows',self)
        button.move(0,310)
        button.clicked.connect(self.threading.willow)

        #creating maple button

        button_maple = QPushButton("Maple longbows", self)
        b1 = button_maple.clicked.connect(self.threading.maple)
        print(b1)
        button_maple.move(100,310)

        #creating yew longbow button
        button_yew = QPushButton('Yew longbows', self)
        button_yew.clicked.connect(self.threading.yew)
        button_yew.move(190,0)

        #creating magic longbow button
        button_magic = QPushButton("Magic longbows", self)
        button_magic.clicked.connect(self.threading.magic)
        button_magic.move(290, 0)
        #Creating a new label for our image
        backpack_loadout_label = QLabel(self)
        backpack_image_label = QPixmap(self.backpack_image)
        backpack_loadout_label.setPixmap(backpack_image_label)
        backpack_loadout_label.resize(backpack_image_label.width(), backpack_image_label.height())
        
        
        #Creating the recommendation label and adding text to it

        rec_label= QLabel(self)
        rec_label.move(10, 260)
        rec_label.resize(185,10)
        rec_label.setText("You must use this backpack loadout ^")
        
        #Python power
        python_label = QLabel(self)
        python_label_pixmap = QPixmap(self.python_power)
        python_label.setPixmap(python_label_pixmap)
        python_label.resize(200,160)
        
        python_label.move(260, 180)
        
        self.show()
        
#Creating a new class for threading
class Thread(QThread):
    def __init__(self):
        super().__init__()
        self.willow_log = r'images\willow.png'
        self.maple_log = r'images\maple_log.png'
        self.yew_log = None
        self.magic_log = None
        self.python_power = r'images\python_powered.png'
        self.knife_willows = r'images\knife_willow.png'
        self.willow_long_bow = r'images\long_bow.png'
        self.backpack_image = r'images\backpack_loadout.png'



    def willow(self):
        duration_time = random.uniform(0.80, 1.35)
        #print(duration_time)
        #finding the log
        knife = locateCenterOnScreen(self.knife_willows) 
        log_image = locateCenterOnScreen(self.willow_log)
        if log_image is None or self.knife_willows is None:
            alert('No logs found or knife found', 'Error')
            return "shit"
        else:
            click(log_image, duration=duration_time)
            QtTest.QTest.qWait(1000)
            if knife is None:
                alert('No knife found', 'Error')

            click(knife, duration=0.92)
            QtTest.QTest.qWait(1000)
            long_bow_image = locateCenterOnScreen(self.willow_long_bow)
            click(long_bow_image, duration=duration_time)
            QtTest.QTest.qWait(50000) # It takes approx 50 seconds to fletch the whole in


    def maple(self):
        image = locateCenterOnScreen(self.maple_log)
        if image is None:
            alert('No logs found', 'Error')
        else: 
            click(image, duration=0.92)
            if self.knife_willows is None:
                alert("No knife found", "Error")

    def yew(self):
        pass
    def magic(self):
        pass



if __name__ == '__main__':

    app = QApplication(sys.argv)
    go = main()
    sys.exit(app.exec_())
    
    

