from PyQt5 import QtWidgets
import Database as dbs
import user as ts
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QCalendarWidget
class Example(QWidget):
    def __init__(self,Parent=None):
        super(Example,self).__init__(Parent)
        self.setGeometry(QRect(500,350,500,100))
        self.flag=0
        self.setStyleSheet('background-color:pink')
        self.textName=QLineEdit(self)
        self.textName.setStatusTip('Enter The LoginID')
        self.textPass=QLineEdit(self)
        self.textPass.setStatusTip('Enter the Password')
        self.buttonLogin=QPushButton('Login',self)
        self.buttonLogin.setShortcut('Enter')
        cancel=QPushButton('Cancel')
        cancel.setShortcut('Esc')
        cancel.setStyleSheet('background-color:#ff0080')
        cancel.clicked.connect(self.textName.clear)
        cancel.clicked.connect(self.textPass.clear)
        self.setWindowIcon(QIcon('stock Icon.png'))
        self.textPass.setEchoMode(QLineEdit.Password)
        self.buttonLogin.setStyleSheet('background-color:gold')
        layout=QFormLayout(self)
        self.setWindowTitle('Welcome to SNS & Co')

        layout.addRow('Login ID:',self.textName.setStyleSheet('color:green'))
        layout.addWidget(self.textName)
        layout.addRow('Password:',self.textPass.setStyleSheet('color:blue'))
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(cancel)
        self.buttonLogin.clicked.connect(self.handleLogin)
    def handleLogin(self):
        global cx
        cx = ts.login_check(self.textName.text(),self.textPass.text())
        if ((cx == 0) or (cx == 1)):
            self.flag=1
            self.close()
            self.showindow()
        else:
            QtWidgets.QMessageBox.warning(self,'Error','Invalid User or Password')
    def showindow(self):
        self.fr=Frame()
        if (self.flag==1):
            self.fr.show()

class Frame(QMainWindow):
    def __init__(self):
        super(Frame, self).__init__()
        self.setWindowTitle('SNS & Co')
        self.setWindowIcon(QIcon('stock Icon.png'))
        self.showMaximized()
        self.initUI()
    def initUI(self):
        self.st=stackedExample()
        self.relogin = Example()
        exitAct=QAction(QIcon('exit.jpg'),'Logout and Exit(Alt+F4)',self)
        exitAct.setShortcut('Alt+F4')
        exitAct.setStatusTip('Logout & Exit')
        exitAct.triggered.connect(self.close)
        try:
            exitAct.triggered.connect(self.relogin.close)
        except:
            pass
        logout=QAction(QIcon('login.jpg'),'Logout and login(Ctrl+l)',self)
        logout.setShortcut('Ctrl+l')
        logout.setStatusTip('Logout And Return to login page')
        logout.triggered.connect(self.returnpage)
        self.statusBar()
        toolbar = self.addToolBar('Exit')
        toolbar.setStyleSheet('background-color:#bf00ff')
        toolbar.addAction(exitAct)
        toolbar.addAction(logout)
        self.setCentralWidget(self.st)
        self.show()
    def returnpage(self):
        self.close()
        self.relogin.show()


class stackedExample(QWidget):
    def __init__(self):
        super(stackedExample, self).__init__()
        self.leftlist = QListWidget()
        self.leftlist.setFixedWidth(200)

        if(cx == 1):
            self.leftlist.insertItem(0, 'Add Stock')
        self.leftlist.insertItem(1, 'Manage Stock')
        self.leftlist.insertItem(2, 'View Stock')
        self.leftlist.insertItem(3, 'All Transactions')
        if(cx == 1):
            self.leftlist.insertItem(4, 'Users')

        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()
        self.stack4=QWidget()
        self.stack5=QWidget()

        if(cx==1):
            self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()
        if(cx==1):
            self.stack5UI()

        self.stack=QStackedWidget(self)
        if(cx==1):
            self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.stack.addWidget(self.stack4)
        if(cx==1):
            self.stack.addWidget(self.stack5)


        hbox=QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(10,10,200,200)
        self.leftlist.setStyleSheet('background-color:#17ceeb')
        self.show()

    def display(self,i):
        self.stack.setCurrentIndex(i)

    def stack1UI(self):
        layout=QFormLayout()

        self.ok=QPushButton('Add Stock',self)
        cancel=QPushButton('Cancel',self)
        self.ok.setStyleSheet('background-color:#ff0080')
        cancel.setStyleSheet('background-color:yellow')
        self.stock_name=QLineEdit()
        layout.addRow('Stock Name:',self.stock_name)
        self.stock_name.setStatusTip("Enter the Stock Name to Add(Don't Use Characters in the Stock Name)")
        self.stock_count=QLineEdit()
        layout.addRow('Quantity:',self.stock_count)
        self.stock_count.setStatusTip("Enter the Quantity to Add Otherwise Enter the value '0'")
        self.stock_cost=QLineEdit()
        layout.addRow('Cost of Stock(per Item):',self.stock_cost)
        self.stock_cost.setStatusTip('Enter the Cost of the Item')
        layout.addWidget(self.ok)
        layout.addWidget(cancel)
        self.ok.setShortcut('Enter')
        self.ok.setStatusTip('Add Stock(Enter)')
        self.ok.clicked.connect(self.addingstock)
        cancel.setShortcut('Esc')
        cancel.setStatusTip('Cancel(Esc)')
        cancel.clicked.connect(self.stock_name.clear)
        cancel.clicked.connect(self.stock_count.clear)
        cancel.clicked.connect(self.stock_cost.clear)
        self.stack1.setLayout(layout)

    def addingstock(self):
        try:
            s=dbs.insert_prod(self.stock_name.text(),self.stock_count.text(),self.stock_cost.text())
            if(s==1):
                QtWidgets.QMessageBox.about(self,'Stock','Stock Added')
                self.stock_name.clear()
                self.stock_count.clear()
                self.stock_cost.clear()
            else:
                QtWidgets.QMessageBox.warning(self,'Stock','This Stock is Already Present')
        except:
            QtWidgets.QMessageBox.warning(self,'Stock','Enter the Valid Input')

    def stack2UI(self):
        layout=QHBoxLayout()
        layout.setGeometry(QRect(0,300,1150,500))
        tabs=QTabWidget()
        self.tab1=QWidget()
        self.tab2=QWidget()
        if(cx==1):
            self.tab3=QWidget()
            self.tab4=QWidget()

        tabs.addTab(self.tab1,'Add Quantity')
        tabs.addTab(self.tab2,'Reduce Quantity')
        if(cx==1):
            tabs.addTab(self.tab3,'Delete Stock')
            tabs.addTab(self.tab4,'Cost Change')

        self.tab1UI()
        self.tab2UI()
        if(cx==1):
            self.tab3UI()
            self.tab4UI()

        layout.addWidget(tabs)
        self.stack2.setLayout(layout)

    def tab1UI(self):
        layout=QFormLayout()
        self.ok_add=QPushButton('Add Stock',self)
        cancel=QPushButton('Cancel',self)
        self.ok_add.setStyleSheet('background-color:#ff0080')
        cancel.setStyleSheet('background-color:yellow')
        self.stock_name_add=QLineEdit()
        layout.addRow('Stock Name:',self.stock_name_add)
        self.stock_name_add.setStatusTip('Enter the Stock Name to Add Quantity')

        self.stock_count_add=QLineEdit()
        layout.addRow('Quantity to add:', self.stock_count_add)
        layout.addWidget(self.ok_add)
        self.stock_count_add.setStatusTip('Enter the Number of Stocks to Add')

        layout.addWidget(cancel)
        self.tab1.setLayout(layout)
        self.ok_add.setShortcut('Enter')
        self.ok_add.setStatusTip('Add Stock(Enter)')
        self.ok_add.clicked.connect(self.call_add)
        #self.ok_add.clicked.connect(self.updatestock)
        cancel.setShortcut('Esc')
        cancel.setStatusTip('Cancel(Esc)')
        cancel.clicked.connect(self.stock_name_add.clear)
        cancel.clicked.connect(self.stock_count_add.clear)

    def call_add(self):
            if(self.stock_count_add.text().isnumeric()):
                k=dbs.Updatestock(self.stock_name_add.text(),int(self.stock_count_add.text()),1)
                if(k==1):
                    QtWidgets.QMessageBox.about(self,'Stock','Stock Added')
                    self.stock_count_add.clear()
                else:
                    QtWidgets.QMessageBox.warning(self,'Stock','This Item is not present')
            else:
                QtWidgets.QMessageBox.warning(self,'Stock','Enter the Valid Inputs')

    def tab2UI(self):
        layout = QFormLayout()
        self.ok_red = QPushButton('Reduce Stock', self)
        cancel = QPushButton('Cancel', self)
        self.ok_red.setStyleSheet('background-color:#ff0080')
        cancel.setStyleSheet('background-color:yellow')
        self.stock_name_red = QLineEdit()
        layout.addRow("Stock Name:", self.stock_name_red)
        self.stock_name_red.setStatusTip('Enter the Stock Name to Reduce Quantity')
        self.ok_red.setShortcut('Enter')
        self.ok_red.setStatusTip('Reduce Stock(Enter)')
        self.stock_count_red = QLineEdit()
        self.stock_count_red.setStatusTip('Enter the Number of Stocks to Reduce')
        layout.addRow("Quantity to reduce:", self.stock_count_red)

        layout.addWidget(self.ok_red)
        layout.addWidget(cancel)
        self.tab2.setLayout(layout)
        cancel.setShortcut('Esc')
        cancel.setStatusTip('Cancel(Esc)')
        self.ok_red.clicked.connect(self.call_red)  # need to write function to reduce quantity
        cancel.clicked.connect(self.stock_name_red.clear)
        cancel.clicked.connect(self.stock_count_red.clear)
        #self.ok_red.clicked.connect(self.updatestock)

    def call_red(self):
        try:
            if(self.stock_count_red.text().isnumeric()):
                k=dbs.Updatestock(self.stock_name_red.text(),int(self.stock_count_red.text()),-1)
                if(k==1):
                    QtWidgets.QMessageBox.about(self,'Stock','Stock Reduced')
                    self.stock_count_red.clear()
                elif(k==0):
                    QtWidgets.QMessageBox.warning(self,'Stock','This Item is not present')
                else:
                    QtWidgets.QMessageBox.warning(self,'Stock','They are not have that much amount of stock to Reduce')
            else:
                QtWidgets.QMessageBox.warning(self,'Stock','Enter the valid Inputs')
        except:
            QtWidgets.QMessageBox.warning(self,'Stock','Enter the valid Inputs')

    def tab3UI(self):
        layout = QFormLayout()
        self.ok_del = QPushButton('Delete Stock', self)
        cancel = QPushButton('Cancel', self)
        self.ok_del.setStyleSheet('background-color:#ff0080')
        cancel.setStyleSheet('background-color:yellow')
        self.stock_name_del = QLineEdit()
        self.stock_name_del.setStatusTip('Enter the Name of the Stock to Delete')
        layout.addRow("Stock Name:", self.stock_name_del)
        layout.addWidget(self.ok_del)
        layout.addWidget(cancel)
        self.tab3.setLayout(layout)
        self.ok_del.setShortcut('Enter')
        self.ok_del.setStatusTip('Delete Stock(Enter)')
        cancel.setShortcut('Esc')
        cancel.setStatusTip('Cancel(Esc)')
        self.ok_del.clicked.connect(self.call_del) # need to write function to delete stock
        #self.ok_del.clicked.connect(self.updatestock)
        cancel.clicked.connect(self.stock_name_del.clear)

    def tab4UI(self):
        layout=QFormLayout()
        self.stock_value_change=QLineEdit()
        self.stock_value_change.setStatusTip('Enter the Name of the Stock to Change its Value')
        layout.addRow('Stock Name:',self.stock_value_change)
        self.new_value=QLineEdit()
        self.new_value.setStatusTip('Enter the New value of the Stock')
        layout.addRow('Enter the New Value:',self.new_value)
        srh=QPushButton('Change the Cost')
        cancel=QPushButton('Cancel')
        srh.setStyleSheet('background-color:#ff0080')
        cancel.setStyleSheet('background-color:yellow')
        srh.setShortcut('Enter')
        srh.setStatusTip('Change the Cost(Enter)')
        cancel.setShortcut('Esc')
        cancel.setStatusTip('Cancel(Esc)')
        layout.addWidget(srh)
        layout.addWidget(cancel)
        self.tab4.setLayout(layout)
        srh.clicked.connect(self.change_value)
        cancel.clicked.connect(self.stock_value_change.clear)
        cancel.clicked.connect(self.new_value.clear)

    def change_value(self):
        try:
            if(self.new_value.text().isnumeric() and int(self.new_value.text())>=0):
                k=dbs.Update_value(self.stock_value_change.text(),int(self.new_value.text()))
                if(k==1):
                    QtWidgets.QMessageBox.about(self,'Stock','The value of the Stock is Changed')
                    self.stock_value_change.clear()
                    self.new_value.clear()
                else:
                    QtWidgets.QMessageBox.warning(self,'Stock','This Item is not present')
            else:
                QtWidgets.QMessageBox.warning(self,'Stock','Enter the Valid Input')
        except:
            QtWidgets.QMessageBox.warning(self,'Stock','Enter the Valid Input')

    def call_del(self):
        q=dbs.delete_stock(self.stock_name_del.text())
        if(q!=0):
            QtWidgets.QMessageBox.warning(self,'Stock','This Stock is not available to delete')
        else:
            QtWidgets.QMessageBox.about(self,'Stock','Stock Deleted')
            self.stock_name_del.clear()

    def stack3UI(self):
        layout=QVBoxLayout()
        self.srb=QPushButton()
        self.srb.setText('Get Result..')
        self.srb.setShortcut('Enter')
        self.srb.setStatusTip('Get Result(Enter)')
        self.srb.setStyleSheet('background-color:yellow')
        self.view=QTableWidget()
        self.lbl3=QLabel()
        self.lbl_conf_text=QLabel()
        self.lbl_conf_text.setText('Enter the Stock Name to Search:')
        self.conf_text=QLineEdit()
        self.conf_text.setStatusTip('Enter the Search Keyword')
        cancel=QPushButton()
        cancel.setText('Refresh..')
        cancel.setShortcut('F5')
        cancel.setStatusTip('Refresh(F5)')
        cancel.setStyleSheet('background-color:#ff0080')

        self.view.setColumnCount(3)
        self.view.setColumnWidth(0, 250)
        self.view.setColumnWidth(1, 250)
        self.view.setColumnWidth(2, 200)
        self.view.insertRow(0)
        self.view.setItem(0, 0, QTableWidgetItem('Stock Name'))
        self.view.setItem(0, 1, QTableWidgetItem('Quantity'))
        self.view.setItem(0, 2, QTableWidgetItem('Cost(Per Item)'))

        '''
        self.view.setColumnCount(3)
        self.view.setItem(0,0,QTableWidgetItem('stock name'))
        self.view.setItem(0,1,QTableWidgetItem('Quantity'))
        self.view.setItem(0,2,QTableWidgetItem('Cost(per Item)'))
        '''
        layout.addWidget(self.view)
        layout.addWidget(self.lbl_conf_text)
        layout.addWidget(self.conf_text)
        layout.addWidget(self.srb)
        layout.addWidget(self.lbl3)
        layout.addWidget(cancel)
        cancel.clicked.connect(self.conf_text.clear)
        cancel.clicked.connect(self.show_search)
        self.srb.clicked.connect(self.show_search)
        self.stack3.setLayout(layout)

    def show_search(self):
        if self.view.rowCount()>1:
            for i in range(1,self.view.rowCount()):
                self.view.removeRow(1)

        #x_act=dbs.show_stock
        x = []
        if self.conf_text.text() != '':
            for i in dbs.show_stock():
                a = i
                if self.conf_text.text().lower() in a[0].lower():
                    x.append(a)
        else:
            x=dbs.show_stock()

        if len(x)!=0:
            for i in range(1,len(x)+1):
                self.view.insertRow(i)
                a=list(x[i-1])
                self.view.setItem(i,0,QTableWidgetItem(a[0].replace('_',' ').upper()))
                self.view.setItem(i,1,QTableWidgetItem(str(a[1])))
                self.view.setItem(i,2,QTableWidgetItem(str(a[2])))
            self.lbl3.setText('Viewing Stock Database.')
        else:
            self.lbl3.setText('No Valid Information in Database.')

    def stack4UI(self):
        layout = QVBoxLayout()

        self.trans_button=QPushButton()
        self.trans_button.setText('Get History..')
        self.trans_button.setShortcut('Enter')
        self.trans_button.setStatusTip('Get History(Enter)')
        self.trans_button.setStyleSheet('background-color:yellow')
        self.lbl=QLabel()
        self.lbl_search=QLabel()
        self.lbl_search.setText('Enter the TransactionID:')
        self.search_word=QLineEdit()
        self.search_word.setStatusTip('Enter the Transction ID to Show')
        clear_button=QPushButton()
        clear_button.setText('Refresh..')
        clear_button.setShortcut('F5')
        clear_button.setStatusTip('Refresh(F5)')
        clear_button.setStyleSheet('background-color:#ff0080')

        self.trans=QTableWidget()
        self.trans.setColumnCount(6)
        self.trans.setColumnWidth(0,175)
        self.trans.setColumnWidth(1,300)
        self.trans.setColumnWidth(2,150)
        self.trans.setColumnWidth(3,100)
        self.trans.setColumnWidth(4,100)
        self.trans.setColumnWidth(5,700)
        self.trans.insertRow(0)
        self.trans.setItem(0,0,QTableWidgetItem('TransactionID'))
        self.trans.setItem(0,1,QTableWidgetItem('Stock name'))
        self.trans.setItem(0,2,QTableWidgetItem('Transaction Type'))
        self.trans.setItem(0,3,QTableWidgetItem('Date'))
        self.trans.setItem(0,4,QTableWidgetItem('Time'))
        self.trans.setItem(0,5,QTableWidgetItem('Transaction Specific'))

        layout.addWidget(self.trans)
        layout.addWidget(self.lbl_search)
        layout.addWidget(self.search_word)
        layout.addWidget(self.trans_button)
        layout.addWidget(self.lbl)
        layout.addWidget(clear_button)
        self.trans_button.clicked.connect(self.show_trans_history)
        clear_button.clicked.connect(self.search_word.clear)
        clear_button.clicked.connect(self.show_trans_history)
        self.stack4.setLayout(layout)

    def show_trans_history(self):
        if self.trans.rowCount()>1:
            for i in range(1,self.trans.rowCount()):
                self.trans.removeRow(1)
        x=[]
        if self.search_word.text() != '':
            for i in dbs.show_transaction():
                a = i
                if self.search_word.text() in a[0]:
                    x.append(a)
        else:
            x=dbs.show_transaction()

        if len(x)!=0:
            for i in range(1,len(x)+1):
                self.trans.insertRow(i)
                a=list(x[i-1])
                self.trans.setItem(i,0,QTableWidgetItem(str(a[0])))
                self.trans.setItem(i,1,QTableWidgetItem(str(a[1]).capitalize()))
                self.trans.setItem(i,2,QTableWidgetItem(str(a[2])))
                self.trans.setItem(i,3,QTableWidgetItem(str(a[3])))
                self.trans.setItem(i,4,QTableWidgetItem(str(a[4])))
                self.trans.setItem(i,5,QTableWidgetItem(str(a[5])))
            self.lbl.setText('Viewing Transaction Database')
        else:
            self.lbl.setText('No Valid Information in Transaction Database')

    def stack5UI(self):
        layout = QHBoxLayout()
        layout.setGeometry(QRect(0,300,1150,500))
        tabs=QTabWidget()
        self.tabs1=QWidget()
        self.tabs2=QWidget()
        self.tabs3=QWidget()
        self.tabs4=QWidget()

        tabs.addTab(self.tabs1,'Users List')
        tabs.addTab(self.tabs2,'Add User')
        tabs.addTab(self.tabs3,'Remove User')
        tabs.addTab(self.tabs4,'Change Password')
        
        self.UsersList()
        self.AddUser()
        self.Removeuser()
        self.ChangePassword()
        layout.addWidget(tabs)

        self.stack5.setLayout(layout)

    def UsersList(self):
        layout=QFormLayout()

        srh=QPushButton()
        srh.setText('Get Result..')
        srh.setShortcut('Enter')
        srh.setStatusTip('Get User List(Enter)')
        srh.setStyleSheet('background-color:yellow')

        self.srh=QLineEdit()
        self.srh.setStatusTip('Enter the Login Id to find the User')
        cancel=QPushButton()
        cancel.setStatusTip('Refresh(F5)')
        cancel.setText('Refresh..')
        cancel.setStyleSheet('background-color:#ff0080')

        self.labl=QLabel()
        self.table=QTableWidget()
        self.table.setColumnCount(4)

        layout.addRow('Users List:',self.table)
        #layout.addWidget(self.table)
        layout.addRow('Enter the Login Id:',self.srh)
        layout.addWidget(srh)
        layout.addWidget(self.labl)
        layout.addWidget(cancel)
        self.tabs1.setLayout(layout)
        srh.clicked.connect(self.listing)
        cancel.setShortcut('F5')
        cancel.clicked.connect(self.srh.clear)
        cancel.clicked.connect(self.listing)

    def listing(self):
        self.table.setColumnWidth(0, 300)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.insertRow(0)
        self.table.setItem(0, 0, QTableWidgetItem('Login Id'))
        self.table.setItem(0, 1, QTableWidgetItem('password'))
        self.table.setItem(0, 2, QTableWidgetItem('Name'))
        self.table.setItem(0, 3, QTableWidgetItem('Phone Number'))

        if self.table.rowCount()>1:
            for i in range(1,self.table.rowCount()):
                self.table.removeRow(1)
        x_act=ts.ShowUser()
        #print(x_act)
        x=[]
        if self.srh.text() != '':
            for i in range(0,len(x_act)):
                a = list(x_act[i])
                if self.srh.text().lower() in a[0].lower():
                    x.append(a)
        else:
            x = ts.ShowUser()

        if len(x)!=0:
            for i in range(1,len(x)+1):
                a=list(x[i-1])
                if(a[0]!=None and a[3]!=None and a[2]!=None):
                    self.table.insertRow(i)
                    #a=list(x[i-1])
                    self.table.setItem(i,0,QTableWidgetItem(a[0].replace('_',' ')))
                    self.table.setItem(i,1,QTableWidgetItem(str(a[1])))
                    self.table.setItem(i,2,QTableWidgetItem(str(a[2])))
                    self.table.setItem(i,3,QTableWidgetItem(str(a[3])))
            self.labl.setText('Viewing User Details')
        else:
            self.labl.setText('No Valid User Information')

    def AddUser(self):
        layout = QFormLayout()
        srh=QPushButton('Add User')
        srh.setShortcut('Enter')
        srh.setStatusTip('Add User(enter)')
        srh.setStyleSheet('background-color:gold')
        cancel=QPushButton('Cancel')
        cancel.setShortcut('Esc')
        cancel.setStatusTip('Cancel(Esc)')
        cancel.setStyleSheet('background-color:#ff0080')
        self.Adduser=QLineEdit()
        self.Adduser.setStatusTip("Enter the Login ID(Use only alpha Numeric Characters Don't Use any Special Characters Except '_'")
        layout.addRow('Login ID:',self.Adduser)
        self.passcode=QLineEdit()
        self.passcode.setStatusTip('Enter the Password of your User ID')
        layout.addRow('Password:',self.passcode)
        self.conpasscode=QLineEdit()
        self.conpasscode.setStatusTip('Enter the Same Password to confirm the Password to Save')
        layout.addRow('Confirm Password:',self.conpasscode)
        self.Name=QLineEdit()
        self.Name.setStatusTip('Enter the Name of the User(Use only Alphabets')
        layout.addRow('Name:',self.Name)
        self.phoneno=QLineEdit()
        self.phoneno.setStatusTip('Enter the Phone Number of the User(Use only Numbers)')
        layout.addRow('Phone Number:',self.phoneno)


        layout.addWidget(srh)
        layout.addWidget(cancel)
        self.tabs2.setLayout(layout)
        srh.clicked.connect(self.AddUser1)
        cancel.clicked.connect(self.Adduser.clear)
        cancel.clicked.connect(self.passcode.clear)
        cancel.clicked.connect(self.conpasscode.clear)
        cancel.clicked.connect(self.Name.clear)
        cancel.clicked.connect(self.phoneno.clear)

    def AddUser1(self):
        c1=self.Adduser.text().replace('@','').replace('.','')
        c2=self.passcode.text()!=''
        c3=self.conpasscode.text()!=''
        c4=self.Name.text().isalpha()
        c5=self.phoneno.text().isnumeric()
        t=0
        if(self.passcode.text()==self.conpasscode.text() and c1.isidentifier() and c2 and c3 and c4 and c5):
            t=ts.add_user(self.Adduser.text(),self.passcode.text(),self.Name.text(),self.phoneno.text().replace('_',''))
            if(t==1):
                QtWidgets.QMessageBox.about(self,'User','User Added')
                self.Adduser.clear()
                self.passcode.clear()
                self.conpasscode.clear()
                self.Name.clear()
                self.phoneno.clear()
            else:
                QtWidgets.QMessageBox.warning(self, 'User', 'This User ID is Already Have So Create the Another ID')
        else:
            if c5 and c4 and c3 and c2 and c1.isidentifier():
                QtWidgets.QMessageBox.warning(self,'User','Password and Confirm Password are not Same')
            else:
                QMessageBox.warning(self,'User','Enter the Valid Informations')

    def Removeuser(self):
        layout=QFormLayout()
        self.rmuser=QLineEdit()
        self.rmuser.setStatusTip('Login ID of the User to Remove them')
        layout.addRow('Enter the Login ID to Remove:',self.rmuser)
        cancel=QPushButton('Remove User')
        cancel.setShortcut('Enter')
        cancel.setStatusTip('Remove User(Enter)')
        cancel.setStyleSheet('background-color:gold')
        cancel1=QPushButton('cancel')
        cancel1.setShortcut('Esc')
        cancel1.setStatusTip('Cancel(Esc)')
        cancel1.setStyleSheet('background-color:#ff0080')

        layout.addWidget(cancel)
        cancel.clicked.connect(self.RemoveUser)
        layout.addWidget(cancel1)
        cancel1.clicked.connect(self.rmuser.clear)
        self.tabs3.setLayout(layout)

    def RemoveUser(self):
        t=str(self.rmuser.text())
        ts.remove_user(t)
        QtWidgets.QMessageBox.about(self,'User','User will be Removed')
        self.rmuser.clear()

    def ChangePassword(self):
        layout=QFormLayout()
        self.chguser=QLineEdit()
        self.chguser.setStatusTip('Enter the Login ID to Change the Password')
        layout.addRow('Enter the Login ID:',self.chguser)
        self.newpassword=QLineEdit()
        self.newpassword.setStatusTip('Enter the New Password to save')
        layout.addRow('Enter the New Password:',self.newpassword)
        chgpwd=QPushButton('Change Password')
        chgpwd.setShortcut('Enter')
        chgpwd.setStatusTip('Change Password(Enter)')
        chgpwd.setStyleSheet('background-color:gold')
        cancel=QPushButton('Cancel')
        cancel.setShortcut('Esc')
        cancel.setStatusTip('Cancel(Esc)')
        cancel.setStyleSheet('background-color:#ff0080')

        layout.addWidget(chgpwd)
        layout.addWidget(cancel)
        chgpwd.clicked.connect(self.chngpwd)
        cancel.clicked.connect(self.chguser.clear)
        cancel.clicked.connect(self.newpassword.clear)
        self.tabs4.setLayout(layout)

    def chngpwd(self):
        s=ts.change_password(self.chguser.text(),self.newpassword.text())
        if(s==1):
            QtWidgets.QMessageBox.about(self,'User','Password Changed')
            self.chguser.clear()
            self.newpassword.clear()
        else:
            QtWidgets.QMessageBox.warning(self,'User','User not found. Enter the Correct Login ID')
            self.chguser.clear()
            self.newpassword.clear()

if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    login=Example()
    login.show()
    sys.exit(app.exec_())
