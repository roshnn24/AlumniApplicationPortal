import mysql.connector as sqltor
import login
import mail
import new_user
from art import *
mycon = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
cur = mycon.cursor()
cur1 = mycon.cursor()
st = f"SELECT * FROM login"
cur.execute(st)
data = cur.fetchall()
st1 = f"SELECT * FROM userlogin"
cur1.execute(st1)
data1 = cur1.fetchall()
tprint('''ALUMNI 
MANAGEMENT 
SYSTEM''')
print("""1.Login as admin
2.Login as user""")
n = int(input('Enter choice(1/2): '))
if n == 1:
    login.admin()
elif n == 2:
    print("""1.Registered Users
2. New User""")
    op = int(input("Enter Option: "))
    if op == 2:
        mail.reg()
    elif op == 1:
        login.user()
else:
    print('Enter a valid option!!')
