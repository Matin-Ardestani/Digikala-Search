from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from search import Ui_SearchWindow

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())