import mail
import addinfo
import mysql.connector as sqltor
import modify
import new_user
import search
import view
import chat
import modify
mycon1 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
cur1 = mycon1.cursor()
st1 = f"SELECT * FROM userlogin"
cur1.execute(st1)
data1 = cur1.fetchall()
cur2 = mycon1.cursor()


def admin():
    mycon = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
    cur = mycon.cursor()
    st = f"SELECT * FROM login"
    cur.execute(st)
    data = cur.fetchall()
    while True:
        user1 = input("Enter username: ")
        passw = input("Enter password: ")
        if (user1, passw) in data:
            print("You are logged in as admin\n")
            admin_menu()
        else:
            print('Incorrect details! Please try again')


def admin_menu():
    print(f'''1.Add user
2.Change Password
3.Modify/Search Alumni Data
4.Delete a user
5.Logout
6.View all user
7.Grant registration request
8.View all alumni data
9.View messages''')
    n = int(input('Enter option: '))
    if n == 2:
        mail.admin_reset()
        admin()
    elif n == 1:
        addinfo.adduser()
        admin_menu()
    elif n == 3:
        print('''1.Update alumni details
2.Search alumni database''')
        x = int(input("Enter option: "))
        if x == 1:
            modify.update()
            admin_menu()
        elif x == 2:
            search.parameters()
            admin_menu()
        else:
            print("Incorrect option\n")
    elif n == 5:
        print("You have been logged out.\n")
    elif n == 6:
        view.alumni()
        admin_menu()
    elif n == 7:
        new_user.confirm()
        admin_menu()
    elif n == 8:
        view.data()
        admin_menu()
    elif n == 9:
        chat.notify()
        admin_menu()
    elif n == 4:
        na = input('Enter user name to be deleted: ')
        mycon12 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
        cur12 = mycon12.cursor()
        cur13 = mycon12.cursor()
        st4 = "DELETE FROM userlogin WHERE Name= '{}'".format(na)
        st5 = "DELETE FROM alumni1 WHERE Name= '{}'".format(na)
        cur12.execute(st4)
        cur13.execute(st5)
        mycon12.commit()
        print("User deleted!!")
        admin_menu()

def user():
    global row
    mycon = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
    cur = mycon.cursor()
    st = f"SELECT * FROM userlogin"
    cur.execute(st)
    data = cur.fetchall()
    while True:
        user1 = input("Enter username: ")
        passw = input("Enter password: ")
        cur3 = mycon.cursor()
        st1 = f"SELECT * FROM alumni1 WHERE Name='{user1}'"
        cur3.execute(st1)
        row = cur3.fetchone()
        if (user1, passw) in data:
            print("You are logged in as user\n")
            n, d, y, em, b, a, e = row
            print(f'''Name: {n}
Date of birth: {d}
Year of graduation: {y}
Email: {em}
Blood Group: {b}
Address: {a}
Employment Status: {e}\n\n''')
            user_menu()
        else:
            print('Incorrect details! Please try again')


def user_menu():
    print('''1.Update personal data
2.Change Password
3.Leave message to admin
4.View other alumni''')
    ch = int(input("Enter choice: "))
    if ch == 3:
        chat.cht()
        user_menu()
    elif ch == 2:
        mail.user_reset()
    elif ch == 1:
        modify.u_update()
    elif ch == 4:
        view.data()
