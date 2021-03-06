# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\muham\OneDrive\Desktop\PyqtFinal\untitled4.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
from PyQt5.QtWidgets import QTableWidgetItem

class DorduncuSayfa(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Sale Documents")
        MainWindow.resize(800, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.table_tbl.setGeometry(QtCore.QRect(40, 140, 561, 231))
        self.table_tbl.setObjectName("table_tbl")
        self.table_tbl.clicked.connect(self.table_tbl_clicked)
        self.table_tbl.setColumnCount(0)
        self.table_tbl.setRowCount(0)
        self.text_lbl2 = QtWidgets.QLabel(self.centralwidget)
        self.text_lbl2.setGeometry(QtCore.QRect(60, 90, 81, 20))
        self.text_lbl2.setObjectName("text_lbl2")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(620, 300, 141, 71))
        self.delete_btn.setObjectName("delete_btn")
        self.delete_btn.clicked.connect(self.delete_btn_clicked)
        self.nameOfBook_text = QtWidgets.QLineEdit(self.centralwidget)
        self.nameOfBook_text.setGeometry(QtCore.QRect(410, 50, 111, 20))
        self.nameOfBook_text.setObjectName("nameOfBook_text")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(620, 140, 141, 71))
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add_btn_clicked)
        self.id_text = QtWidgets.QLineEdit(self.centralwidget)
        self.id_text.setGeometry(QtCore.QRect(150, 50, 111, 20))
        self.id_text.setObjectName("id_text")
        self.text_lbl1 = QtWidgets.QLabel(self.centralwidget)
        self.text_lbl1.setGeometry(QtCore.QRect(60, 50, 81, 20))
        self.text_lbl1.setObjectName("text_lbl1")
        self.text_lbl3 = QtWidgets.QLabel(self.centralwidget)
        self.text_lbl3.setGeometry(QtCore.QRect(320, 50, 81, 20))
        self.text_lbl3.setObjectName("text_lbl3")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(620, 220, 141, 71))
        self.update_btn.setObjectName("update_btn")
        self.update_btn.clicked.connect(self.update_btn_clicked)
        self.authorName_text = QtWidgets.QLineEdit(self.centralwidget)
        self.authorName_text.setGeometry(QtCore.QRect(150, 90, 113, 20))
        self.authorName_text.setObjectName("authorName_text")
        self.text_lbl3_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_lbl3_2.setGeometry(QtCore.QRect(320, 90, 81, 20))
        self.text_lbl3_2.setObjectName("text_lbl3_2")
        self.orderStatus_text = QtWidgets.QLineEdit(self.centralwidget)
        self.orderStatus_text.setGeometry(QtCore.QRect(410, 90, 111, 20))
        self.orderStatus_text.setObjectName("orderStatus_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Sale Documents", "Sale Documents"))
        self.text_lbl2.setText(_translate("MainWindow", "AUTHOR NAME"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.text_lbl1.setText(_translate("MainWindow", "SALE ID"))
        self.text_lbl3.setText(_translate("MainWindow", "NAME OF BOOK"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.text_lbl3_2.setText(_translate("MainWindow", "STATUS"))
        self.showList()

    def add_btn_clicked(self):
    
        
        saleID = self.id_text.text()
        author = self.authorName_text.text()
        nameOfBook = self.nameOfBook_text.text()
        saleStatus = self.orderStatus_text.text()
          
       

        try:
            self.dbConnect = sql.connect('mfafinalproject.db')
            self.c = self.dbConnect.cursor()
            self.c.execute("Insert into sale Values(?,?,?,?)", (saleID,author,nameOfBook,saleStatus))
            self.dbConnect.commit()
            self.c.close()
            self.dbConnect.close()
            print("Add Succesful")
            self.showList()
            

        except Exception:
            print('Wrong !!')   

    def showList(self):
        
        self.db = sql.connect('mfafinalproject.db')
        self.table_tbl.clear()  
        self.table_tbl.setColumnCount(4)
        self.table_tbl.setHorizontalHeaderLabels(('saleID','author','nameOfBook',"saleStatus"))   
        self.table_tbl.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        
        cursor = self.db.cursor()
        query = "Select * From sale"
        cursor.execute(query)

        rows = cursor.fetchall()

        self.table_tbl.setRowCount(len(rows))
        
        for rowIndex, rowsInfo in enumerate(rows):
            for columnIndex, columnsInfo in enumerate(rowsInfo):
                self.table_tbl.setItem(rowIndex, columnIndex, QTableWidgetItem(str(columnsInfo)))    

    
    def delete_btn_clicked(self):

        saleID = self.id_text.text()
        try:
            self.dbConnect = sql.connect('mfafinalproject.db')
            self.cursor = self.dbConnect.cursor()
            self.cursor.execute("Delete from sale where saleID = ?", (saleID))
            self.dbConnect.commit()
            self.cursor.close()
            self.dbConnect.close()
            print('Success')
            self.showList()
         

        except Exception:
            print('Wrong !!') 


    def table_tbl_clicked(self):
        self.id_text.setText(self.table_tbl.item(self.table_tbl.currentRow(), 0).text())
        self.authorName_text.setText(self.table_tbl.item(self.table_tbl.currentRow(), 1).text())
        self.nameOfBook_text.setText(self.table_tbl.item(self.table_tbl.currentRow(), 2).text())
        self.orderStatus_text.setText(self.table_tbl.item(self.table_tbl.currentRow(), 3).text())
        
        

    def update_btn_clicked(self):      

        
        saleID = self.id_text.text()
        author = self.authorName_text.text()
        nameOfBook = self.nameOfBook_text.text()
        saleStatus = self.orderStatus_text.text()

        try:
            self.dbConnect = sql.connect('mfafinalproject.db')
            self.cursor = self.dbConnect.cursor()
            self.cursor.execute("Update sale set author = ?, nameOfBook = ?, status = ? where saleID = ?", 
            (author, nameOfBook, saleStatus, saleID))
            self.dbConnect.commit()
            self.cursor.close()
            self.dbConnect.close()
            print('Success')
            self.showList()
            

        except Exception:
            print('Wrong !! ')             


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DorduncuSayfa()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())