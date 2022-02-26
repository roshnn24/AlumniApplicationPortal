import mysql.connector as sqltor
from tabulate import tabulate


def alumni():  # to view all the users
    mycon1 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
    cur1 = mycon1.cursor()
    st1 = f"SELECT * FROM userlogin"
    cur1.execute(st1)
    data1 = cur1.fetchall()
    l = list()
    for i in data1:
        a, b = i
        l.append([a, b])
    table = tabulate(l, headers=['Username', 'Password'], tablefmt='orgtbl')
    print(table)
    mycon1.close()


def data():  # to view all the alumni and their data
    mycon1 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
    cur1 = mycon1.cursor()
    st1 = f"SELECT * FROM alumni1"
    cur1.execute(st1)
    data1 = cur1.fetchall()
    l = list()
    for i in data1:
        a, b, c, d, e, f, g = i
        l.append([a, b, c, d, e, f, g])
    table = tabulate(l, headers=['Name', 'DOB','Year Graduated', 'Email', 'Blood Group', 'Address', 'Employment Status'], tablefmt='orgtbl')
    print(table)
    mycon1.close()
