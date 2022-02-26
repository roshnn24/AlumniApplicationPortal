import mail
import mysql.connector
import login
conn = mysql.connector.connect(host='localhost', user='root', passwd='1234', database='vnps')
cur2 = conn.cursor()


def change():
    otp = int(input('Enter the OTP sent to admin mail: '))
    while mail.number == otp:
        new = input('Enter new password: ')
        new1 = input('Confirm new password: ')
        if new == new1:
            st = f"UPDATE login SET password='{new}' WHERE Name='roshaun'"
            cur2.execute(st)
            conn.commit()
            conn.close()
            print('Password changed successfully\n\n')
            login.admin()
            break
        else:
            print('Passwords do not match!!. Try again')
            continue
    else:
        print('Incorrect OTP entered!!!')
