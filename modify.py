import mysql.connector as sqltor
import mysql.connector.errors
thecon = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
thecur = thecon.cursor()
cur = thecon.cursor()


def update():
    try:
        person = input('Enter name of alumni: ')
        column = input('Enter the column to updated: ')
        new = input('Enter new data to be inserted: ')
        stmt = f"UPDATE alumni1 SET {column}='{new}' WHERE Name='{person}'"
        thecur.execute(stmt)
        thecon.commit()
        print('Data Updated Successfully\n')
    except mysql.connector.errors.DataError:
        print("Invalid input!! Please try again \n\n")
        update()