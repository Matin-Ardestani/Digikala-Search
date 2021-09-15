# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import urllib.request

class Ui_SearchWindow(object):

    #==================================Designer codes=====================================
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 476)
        MainWindow.setStyleSheet("background: #F4F4F4; border-radius: 15px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(465, 15, 25, 25))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("background: none;")
        self.btn_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/matin/Desktop/Digikala-Search/img/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QtCore.QSize(18, 18))
        self.btn_close.setObjectName("btn_close")
        self.btn_min = QtWidgets.QPushButton(self.centralwidget)
        self.btn_min.setGeometry(QtCore.QRect(435, 15, 25, 25))
        self.btn_min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_min.setStyleSheet("background: none;")
        self.btn_min.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/matin/Desktop/Digikala-Search/img/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_min.setIcon(icon1)
        self.btn_min.setIconSize(QtCore.QSize(18, 18))
        self.btn_min.setObjectName("btn_min")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 421, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #030107;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(60, 60, 430, 40))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(9)
        self.search.setFont(font)
        self.search.setStyleSheet("background-color: #DCDCDC; border-radius: 5px; color: #030107;")
        self.search.setObjectName("search")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(10, 60, 40, 40))
        self.search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_btn.setStyleSheet("background-color: #DCDCDC; border-radius: 5px;")
        self.search_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/matin/Desktop/Digikala-Search/img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon2)
        self.search_btn.setIconSize(QtCore.QSize(25, 25))
        self.search_btn.setObjectName("search_btn")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 110, 340, 360))
        self.frame_2.setStyleSheet("background-color: #DCDCDC; border-radius: 5px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setStyleSheet("QScrollBar {\n"
"    background: #cfcfcf;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 322, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(360, 110, 130, 360))
        self.frame.setStyleSheet("background-color: #DCDCDC; border-radius: 5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.most_related = QtWidgets.QPushButton(self.frame)
        self.most_related.setGeometry(QtCore.QRect(20, 20, 90, 30))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        self.most_related.setFont(font)
        self.most_related.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.most_related.setStyleSheet("background-color: #886BC0; border-radius: 5px; color: #030107;")
        self.most_related.setObjectName("most_related")
        self.most_sale = QtWidgets.QPushButton(self.frame)
        self.most_sale.setGeometry(QtCore.QRect(20, 70, 90, 30))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        self.most_sale.setFont(font)
        self.most_sale.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.most_sale.setStyleSheet("background-color: #C8B6EC; border-radius: 5px; color: #030107;")
        self.most_sale.setObjectName("most_sale")
        self.most_expensive = QtWidgets.QPushButton(self.frame)
        self.most_expensive.setGeometry(QtCore.QRect(20, 170, 90, 30))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        self.most_expensive.setFont(font)
        self.most_expensive.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.most_expensive.setStyleSheet("background-color: #C8B6EC; border-radius: 5px; color: #030107;")
        self.most_expensive.setObjectName("most_expensive")
        self.most_cheap = QtWidgets.QPushButton(self.frame)
        self.most_cheap.setGeometry(QtCore.QRect(20, 120, 90, 30))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        self.most_cheap.setFont(font)
        self.most_cheap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.most_cheap.setStyleSheet("background-color: #C8B6EC; border-radius: 5px; color: #030107;")
        self.most_cheap.setObjectName("most_cheap")
        self.most_new = QtWidgets.QPushButton(self.frame)
        self.most_new.setGeometry(QtCore.QRect(20, 220, 90, 30))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        self.most_new.setFont(font)
        self.most_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.most_new.setStyleSheet("background-color: #C8B6EC; border-radius: 5px; color: #030107;")
        self.most_new.setObjectName("most_new")
        self.former = QtWidgets.QPushButton(self.frame)
        self.former.setGeometry(QtCore.QRect(80, 320, 30, 30))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        self.former.setFont(font)
        self.former.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.former.setStyleSheet("background-color: #C8B6EC; border-radius: 5px;")
        self.former.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/matin/Desktop/Digikala-Search/img/right-row.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.former.setIcon(icon3)
        self.former.setIconSize(QtCore.QSize(25, 25))
        self.former.setObjectName("former")
        self.next = QtWidgets.QPushButton(self.frame)
        self.next.setGeometry(QtCore.QRect(20, 320, 30, 30))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        self.next.setFont(font)
        self.next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next.setStyleSheet("background-color: #C8B6EC; border-radius: 5px;")
        self.next.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/home/matin/Desktop/Digikala-Search/img/left-row.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon4)
        self.next.setIconSize(QtCore.QSize(25, 25))
        self.next.setObjectName("next")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close)
        self.btn_min.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #=======================================My codes=========================
        # call searching methode
        self.search.setFocus(True)
        self.search_btn.clicked.connect(lambda: self.searching('relate'))
        self.search.returnPressed.connect(lambda: self.searching('relate'))

        self.most_expensive.clicked.connect(lambda: self.searching('expensive'))
        self.most_cheap.clicked.connect(lambda: self.searching('cheap'))
        self.most_new.clicked.connect(lambda: self.searching('new'))
        self.most_related.clicked.connect(lambda: self.searching('relate'))
        self.most_sale.clicked.connect(lambda: self.searching('sale'))

        self.category = 'relate'

        # call chage page methode
        self.former.setEnabled(False)
        self.next.hide()
        self.former.hide()
        self.next.clicked.connect(lambda: self.searching('next'))
        self.former.clicked.connect(lambda: self.searching('former'))
        self.page_counter = 1

        self.search_counter = 0



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "جستوجوگر دیجیکالا"))
        self.search.setPlaceholderText(_translate("MainWindow", "جستجو در دیجیکالا..."))
        self.most_related.setText(_translate("MainWindow", "مرتبط ترین"))
        self.most_sale.setText(_translate("MainWindow", "پرفروش ترین"))
        self.most_expensive.setText(_translate("MainWindow", "گران ترین"))
        self.most_cheap.setText(_translate("MainWindow", "ارزان ترین"))
        self.most_new.setText(_translate("MainWindow", "جدید ترین"))


    #====================================My Functions==============================
    def searching(self , btn):

        self.search_counter += 1 # for delete last products

        if self.search_counter > 1:
            self.deleteItems()

        # Add product to the show list
        def addItem(title , image_url , price):
            self.product = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.product.sizePolicy().hasHeightForWidth())
            self.product.setSizePolicy(sizePolicy)
            self.product.setMinimumSize(QtCore.QSize(0, 120))
            self.product.setStyleSheet("background-color: #fff;")
            self.product.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.product.setFrameShadow(QtWidgets.QFrame.Raised)
            self.product.setObjectName("product")
            self.product_photo = QtWidgets.QLabel(self.product)
            self.product_photo.setGeometry(QtCore.QRect(10, 10, 101, 101))
            self.product_photo.setText("")

            data = urllib.request.urlopen(image_url).read()
            self.pic = QtGui.QPixmap()
            self.pic.loadFromData(data)

            self.product_photo.setPixmap(self.pic)
            self.product_photo.setScaledContents(True)
            self.product_photo.setObjectName("product_photo")
            self.product_title = QtWidgets.QLabel(self.product)
            self.product_title.setGeometry(QtCore.QRect(107, 19, 175, 31))
            font = QtGui.QFont()
            font.setFamily("B Nazanin")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            self.product_title.setFont(font)
            self.product_title.setStyleSheet("color: #010107;")
            self.product_title.setWordWrap(True)
            self.product_title.setObjectName("product_title")
            self.product_price = QtWidgets.QLabel(self.product)
            self.product_price.setGeometry(QtCore.QRect(140, 75, 141, 20))
            font = QtGui.QFont()
            font.setFamily("B Nazanin")
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.product_price.setFont(font)
            self.product_price.setStyleSheet("color: #010107;")
            self.product_price.setWordWrap(True)
            self.product_price.setObjectName("product_price")
            self.verticalLayout_2.addWidget(self.product)
            self.product_title.setText(title)
            self.product_price.setText(price)
            self.product_title.setText(title)
            self.product_price.setText(price)


        # create url and set buttons color
        if btn == 'relate':
            url = 'https://www.digikala.com/search/?q=%s' % self.search.text()
            self.most_related.setStyleSheet('background-color: #886BC0; border-radius: 5px; color: #030107;')
            self.most_new.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_cheap.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_expensive.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_sale.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.category = 'relate'
            self.page_counter = 1
            self.next.setEnabled(True)

        elif btn == 'expensive':
            url = 'https://www.digikala.com/search/?q=%s&sortby=21' % self.search.text()
            self.most_expensive.setStyleSheet('background-color: #886BC0; border-radius: 5px; color: #030107;')
            self.most_new.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_cheap.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_related.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_sale.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.category = 'expensive'
            self.page_counter = 1
            self.next.setEnabled(False)
            self.former.setEnabled(False)

        elif btn == 'cheap':
            url = 'https://www.digikala.com/search/?q=%s&sortby=20' % self.search.text()
            self.most_cheap.setStyleSheet('background-color: #886BC0; border-radius: 5px; color: #030107;')
            self.most_new.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_related.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_expensive.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_sale.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.category = 'cheap'
            self.page_counter = 1
            self.next.setEnabled(False)
            self.former.setEnabled(False)

        elif btn == 'new':
            url = 'https://www.digikala.com/search/?q=%s&sortby=1' % self.search.text()
            self.most_new.setStyleSheet('background-color: #886BC0; border-radius: 5px; color: #030107;')
            self.most_related.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_cheap.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_expensive.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_sale.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.category = 'new'
            self.page_counter = 1
            self.next.setEnabled(False)
            self.former.setEnabled(False)
        
        elif btn == 'sale':
            url = 'https://www.digikala.com/search/?q=%s&sortby=7' % self.search.text()
            self.most_sale.setStyleSheet('background-color: #886BC0; border-radius: 5px; color: #030107;')
            self.most_related.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_cheap.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_expensive.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.most_new.setStyleSheet('background-color: #C8B6EC; border-radius: 5px; color: #030107;')
            self.category = 'sale'
            self.page_counter = 1
            self.next.setEnabled(False)
            self.former.setEnabled(False)

        elif btn == 'next':
            if self.page_counter <= 4:
                url = 'https://www.digikala.com/search/?q=%s&pageno=%s&sortby=22' % (self.search.text() , (self.page_counter + 1))
                self.page_counter += 1
                self.former.setEnabled(True)
                if self.page_counter == 4:
                    self.next.setEnabled(False)

        elif btn == 'former':
            if self.page_counter >= 1:
                url = 'https://www.digikala.com/search/?q=%s&pageno=%s&sortby=22' % (self.search.text() , (self.page_counter - 1))
                self.page_counter -= 1
                self.next.setEnabled(True)
                if self.page_counter == 1:
                    self.former.setEnabled(False)


        # show change pages buttons
        self.next.show()
        self.former.show()

        # main request
        req = requests.get(url)
        soup = BeautifulSoup(req.text , 'html.parser')


        # Getting titles -> returns "titles" list
        titles_container = soup.find_all('div' , attrs={'class':'c-product-box__content--row'})
        titles_container = list(titles_container)
        self.titles = []
        for tit in titles_container:
            titles_soup = BeautifulSoup(str(tit) , 'html.parser')
            title = (titles_soup.find('a' , attrs={'class':'js-product-url'}))
            title = (str(title.text)).strip()
            self.titles.append(title)
        

        # Getting images urls -> returns "images_urls" list
        images_container = soup.find_all('a' , attrs={'class':'c-product-box__img c-promotion-box__image js-url js-product-item js-product-url'})
        images_container = list(images_container)
        self.images_urls = []
        for image in images_container:
            image_soup = BeautifulSoup(str(image) , 'html.parser')
            image = image_soup.find('img')
            image = image['src']
            self.images_urls.append(image)


        # Getting prices -> returns prices
        price_container = soup.find_all('div' , attrs={'class':'c-product-box'})
        price_container = list(price_container)

        self.prices = []


        for price in price_container:
            price_soup = BeautifulSoup(str(price) , 'html.parser')
            the_price = price_soup.find('div' , attrs={'class':'c-price__value-wrapper'})

            if the_price != None:
                this = (str(the_price.text)).strip()
                this = this.replace(' ' , '')
                this = this.replace('\n' , ' ')
                self.prices.append(this)
            else:
                self.prices.append('ناموجود')

        
        if (len(self.prices)) > 36:
            diff = abs((len(self.prices)) - 36)

            for this in range(0 , diff):
                self.prices.pop(0)

        if len(self.prices) < len(self.titles):
            difference = (len(self.titles)) - (len(self.prices))
            for i in range(0 , difference):
                self.prices.append('ناموجود')

        # add items
        counter = -1
        for this in self.titles:
            counter += 1
            addItem(self.titles[counter] , self.images_urls[counter] , self.prices[counter])



    # delete all items for new search
    def deleteItems(self):
        self.titles = []
        self.images_urls = []
        self.prices = []
        self.scrollArea.setParent(None)
        self.scrollArea.deleteLater()

        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setStyleSheet("QScrollBar { background: #c2c2c2;\n}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 433, 363))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
