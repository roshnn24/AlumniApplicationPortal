import smtplib
import mysql.connector as sqltor
from mysql.connector import IntegrityError

def confirm():
    mycon1 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
    cur1 = mycon1.cursor()
    cur2 = mycon1.cursor()
    cur3 = mycon1.cursor()
    try:
            name = input("Enter Alumni Name: ")
            admno = int(input('Enter admission no: '))
            password = input("Enter Password: ")
            email = input("Enter Email of user: ")
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
            confirm()
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()  # establishes connection with the SMTP server
        smtp.starttls()  # data encryption
        smtp.ehlo()

        smtp.login('alumni.management.sys@gmail.com', 'Jesus@25')  # logs in the mail ID with SMTP server

        subject = f'Login Credentials'
        body = '''You have been granted access to alumni application
        Use the credentials given below:
        Username:'{}'
        Password:'{}'''''.format(name, password)

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('alumni.management.sys@gmail.com', email, msg)  # used to send the mail
        print('Confirmation mail sent to user\n\n')
