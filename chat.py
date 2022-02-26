import mysql.connector as sqltor
from tabulate import tabulate


def cht():
    mycon1 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
    cur1 = mycon1.cursor()
    name = input("Enter your Name: ")
    msg = input('Enter message: ')
    st = "INSERT INTO msg VALUES ('{}', '{}')".format(name, msg)
    cur1.execute(st)
    mycon1.commit()
    print('Message sent successfully\n')


def notify():
    mycon1 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
    cur2 = mycon1.cursor()
    st = "SELECT * FROM msg"
    cur2.execute(st)
    data = cur2.fetchall()
    l = list()
    for i in data:
        a, b = i
        l.append([a, b])
    table = tabulate(l, headers=['Name', 'Message'], tablefmt='orgtbl')
    print(table)
    print()
