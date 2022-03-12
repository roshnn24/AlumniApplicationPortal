import random
import smtplib
import pass_reset
import mysql.connector as sqltor
# def reset(x):
#     with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#         smtp.ehlo()  # establishes connection with the SMTP server
#         smtp.starttls()  # data encryption
#         smtp.ehlo()
#
#         smtp.login('roshauninfant@gmail.com', 'AsusvivobookS14')
#
#         subject = f'Password Reset'
#         body = f'Your OTP for password reset is {random.randint(1000, 9999)}'
#
#         msg = f'Subject: {subject}\n\n{body}'
#
#         smtp.sendmail('roshauninfant@gmail.com', x, msg)


number = random.randint(1000, 9999)
number1 = random.randint(1000, 9999)


def admin_reset():
    global number
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()  # establishes connection with the SMTP server
        smtp.starttls()  # data encryption
        smtp.ehlo()

        smtp.login('alumni.management.sys@gmail.com', 'Jesus@25')  # logs in the mail ID with SMTP server

        subject = f'Password Reset'
        body = f'Your OTP for password reset is {number}'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('alumni.management.sys@gmail.com', 'roshauninfant@gmail.com', msg)  # used to send the mail
        print('Password reset information sent to admin mail successfully\n\n')
        pass_reset.change()


def user_reset():
    global number1
    name = input('Enter your name: ')
    admno = int(input('Enter your admission no: '))
    mycon1 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
    cur1 = mycon1.cursor()
    st = "SELECT * FROM admno WHERE Name = '{}'".format(name.title())
    cur1.execute(st)
    data = cur1.fetchall()
    for i in data:
        a, b = i
    if admno == b:
        remail = input("Enter your email address: ")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()  # establishes connection with the SMTP server
            smtp.starttls()  # data encryption
            smtp.ehlo()

            smtp.login('alumni.management.sys@gmail.com', 'Jesus@25')  # logs in the mail ID with SMTP server

            subject = f'Password Reset'
            body = f'Your OTP for password reset is {number}'

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail('alumni.management.sys@gmail.com', remail, msg)  # used to send the mail
            print('Password reset information sent to your mail successfully\n\n')
            pass_reset.uchange()
    else:
        print('Incorrect admission no !! Please contact the admin...')