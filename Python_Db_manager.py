# Database Manager
import sqlite3
con=sqlite3.connect("DB_Manager.db")
cur=con.cursor()
def tbl(): # Create a Table
    cur.execute(''' CREATE TABLE shop(customer_id,customer_name,city,Phone_no)''')
    con.commit()
    return app()
def data():
    cur.execute(''' INSERT INTO shop VALUES (1,'raghul','coimbature',9876504321),(2,'prakash','chennai',9638502741),(3,'selva','chennai',8529063741),(4,'pream','coimbature',7418520963) ''')
    con.commit()
    return app()
def srtid(): # to sort by id
    for row in cur.execute(''' SELECT * FROM shop ORDER BY customer_id DESC '''):
        print(row)
    return app()
def lstcust(): # to list Customer names
    print('Specific customer is Selected ...')
    for row in cur.execute(''' SELECT * FROM shop WHERE customer_name='pream'  '''):
        print(row)
    return app()
def lstcusbycity():
    print('customer fron Chennai')
    for row in cur.execute(''' SELECT customer_name FROM shop WHERE city='chennai'  '''):
        print(row)
    return app()
def rmcust():
    print('customer is Deleted')
    cur.execute(''' DELETE FROM shop WHERE customer_name='pream'  ''')
    con.commit()
    for i in cur.execute(''' SELECT * FROM shop '''):
        print(i)
    return app()
def lst():
    cur.execute(''' SELECT * FROM shop ''')
    for row in cur:
        print(row)
    return app()
def app():
    print('''
            Press 1 = Create Table
            Press 2 = Add Data
            Press 3 = Sort data By Id
            Press 4 = List Customer by Chennai
            Press 5 = List the Specific Customer
            Press 6 = Remove Specific Customer
            Press 7 = List All Customers
            Press 0 = Exit''')
    op=int(input("Select the Option : "))
    if(op==1):
        return tbl()
    elif(op==2):
        return data()
    elif(op==3):
        return srtid()
    elif(op==4):
        return lstcusbycity()
    elif(op==5):
        return lstcust()
    elif(op==6):
        return rmcust()
    elif(op==7):
        return lst()
    elif(op==0):
        con.close()
        print("Bye have a Good Day")
        return exit
    else:
        print("Retry..")
        return app()
app()
