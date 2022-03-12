import smtplib

m = str()


def user():
    global m
    admis = input("Enter your admission number: ")
    n = input("Enter your name: ")
    m = input("Enter email: ")
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('alumni.management.sys@gmail.com', 'Jesus@25')

        subject = f'New User'
        body=f'User with adm no.{admis} and name {n} has requested for registration.Login to grant or decline request.'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('alumni.management.sys@gmail.com', 'roshauninfant@gmail.com', msg)
        print('Registration request sent to admin\n\n')


def confirm():
    e = input('Enter receiver mail address: ')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('alumni.management.sys@gmail.com', 'Jesus@25')

        subject = f'New User'
        body = f'You have been granted access to alumni application'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('alumni.management.sys@gmail.com', e, msg)

