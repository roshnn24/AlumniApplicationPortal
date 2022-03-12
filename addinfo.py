import mysql.connector as sqltor
from mysql.connector import IntegrityError

mycon1 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
cur1 = mycon1.cursor()
cur2 = mycon1.cursor()
cur3 = mycon1.cursor()


def adduser():
    try:
        name = input("Enter Alumni Name: ")
        admno = int(input('Enter admission no: '))
        password = input("Enter Password: ")
        st = "INSERT INTO userlogin VALUES('{}', '{}')".format(name, password)
        st1 = "INSERT INTO alumni1 (Name) VALUES('{}')".format(name)
        st2 = "INSERT INTO admno VALUES('{}', {})".format(name, admno)
        cur1.execute(st)
        cur2.execute(st1)
        cur3.execute(st2)
        mycon1.commit()
        mycon1.close()

        print("User Successfully Added\n")
    except IntegrityError:
        print('Username already exists. Please enter a unique username\n')
        adduser()
