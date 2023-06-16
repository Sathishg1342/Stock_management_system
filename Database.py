import datetime
import mysql.connector
#import test as tst

db = mysql.connector.connect(user='root',host='localhost',password='saths@18',database='stockmanagement')
c = db.cursor()
'''
c.execute("update stock_available set Quantity=%s where Stocks=%s",(50,'Fan'))
db.commit()
'''
'''
c.execute("select * from stock_available")
print(c.column_names)
for i in c:
    print(i)
'''
'''
x=datetime.datetime.now()
print(x.strftime("%d-%m-%Y"),end=' ')
print(x.strftime('%I %M %S %p'))
'''
try:
    c.execute("Create Table stock_available (Stocks varchar(100),Quantity int(10),cost int(10))")
    c.execute("create table transaction_history (TransactionID varchar(30),StockName varchar(50),TransactionType varchar(20),TransDate varchar(15),TransTime varchar(15),TransDetails varchar(300))")
    db.commit()
except Exception:
    pass

def insert_prod(stocks,quantity,cost):
    x=show_stock()
    z=1
    for i in x:
        t=list(i)
        if(str(t[0]).lower()==str(stocks).lower()):
            z=0
            break
    if(z==1):
        sql="insert into stock_available(Stocks,Quantity,cost) values(%s,%s,%s)"
        val=(stocks.capitalize(),int(quantity),int(cost))
        c.execute(sql,val)
        Transactions(str(stocks),'Stock Inserted',str(stocks)+' added with Quantity:'+str(quantity)+' and Cost(Per Unit in Rs.):'+str(cost))
        db.commit()
    return z

def show_stock():
    c.execute("SELECT * FROM stock_available ORDER BY Stocks ")
    zebra=c.fetchall()
    return zebra
def show_transaction():
    c.execute("select * from transaction_history")
    t=c.fetchall()
    return t

def delete_stock(stock):
    x=show_stock()
    z=1
    for i in x:
        t=list(i)
        if(str(t[0]).lower() == stock.lower()):
            sql = "delete from stock_available where Stocks=%s"
            val = (stock.capitalize(),)
            c.execute(sql, val)
            Transactions(str(stock),'Stock Removed',str(stock)+' will be Removed')
            db.commit()
            z=0
            break
    return z
#print(delete_stock('fridge'))

def Updatestock(stock,quantity,update):#It is necessary that update value is 1(add Quantity) or -1(reduce quantity)
    x=show_stock()
    z=0
    for i in x:
        t=list(i)
        if(str(t[0]).lower()==str(stock).lower()):
            z=1
            s=int(t[1])
            break
    else:
        return z
    if(z==1):
        s=s+(quantity*update)
        if(s>=0):
            c.execute("update stock_available set Quantity=%s where Stocks=%s",(s,stock.capitalize()))
            Transactions(str(stock),'Stock Updated','Quantity of '+str(stock)+' Changed from '+str(t[1])+' to '+str(s))
            db.commit()
            return z
        else:
            return -1

#print(Updatestock('fan',50,-1))
def Update_value(stock,cost):
    x=show_stock()
    z=0
    for i in x:
        t=list(i)
        if(str(t[0]).lower()==str(stock).lower()):
            z=1
            break
    else:
        return z
    if(z==1):
        c.execute("update stock_available set cost=%s where Stocks=%s",(int(cost),stock))
        Transactions(str(stock),'Value Changed','Value of the '+str(stock)+' Changed from '+str(t[1])+' to '+str(cost))
        db.commit()
        return(z)
#print(Update_value('iron box',500))
'''
x=datetime.datetime.now()
print(x.strftime("%d-%m-%Y"),end=' ')
print(x.strftime('%I:%M:%S:%p'))
#ff6666
#00ff00
#0000ff
'''
def Transactions(name,type,details):
    nw=datetime.datetime.now()
    tsID=nw.strftime("%Y%m%d%I%M%S")
    tnsdate=nw.strftime("%d-%m-%Y")
    tnstime=nw.strftime("%I:%M:%S")
    sql="insert into transaction_history(TransactionID,StockName,TransactionType,TransDate,TransTime,TransDetails) values (%s,%s,%s,%s,%s,%s)"
    val=(tsID,name,type,tnsdate,tnstime,details)
    c.execute(sql,val)
    db.commit()

#Transactions('dsdsfds','dfdsfdsfds','fdsfdfds')
'''
c.execute("delete from stock_available")
db.commit()
print(show_transaction())
print(show_stock())
'''
'''
sql = "delete from stock_available where Stocks=%s"
            val = (stock.capitalize(),)
            c.execute(sql, val)
e=[]
for q in show_stock():
    print(q)
    e.append(q)
print(type(q))
print(type(e))
print(e)
'''
#print(insert_prod('fan',10,5000))
