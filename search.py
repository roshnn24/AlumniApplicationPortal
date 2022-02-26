import mysql.connector as sqltor
from tabulate import tabulate
mycon1 = sqltor.connect(host='localhost', user='root', passwd='1234', database='vnps')
cur1 = mycon1.cursor()


def parameters():
    print('Set search parameters\n')
    print("""1.Search by name
2.Search by Blood group
3.Search by Address
4.Search by Employment Status
5.Return to main menu""")
    n = int(input("Enter option: "))
    if n == 1:
        name = input("Enter name: ")
        st = f"SELECT * FROM alumni1 WHERE Name LIKE '%{name}%'"
        cur1.execute(st)
        data = cur1.fetchall()
        l1 = list()
        for i in data:
            a, b, c, d, e, f, g = i
            l1.append([a, b, c, d, e, f, g])
        table = tabulate(l1, headers=['Name', 'DOB', 'Year Graduated', 'Email', 'Blood Group', 'Address', 'Employment Status'],
                         tablefmt='orgtbl')
        print(table)
        if len(data) == 0:
            print('No data found\n')
        parameters()
    elif n == 2:
        bg = input('Enter blood group: ')
        st1 = f"SELECT * FROM alumni1 WHERE BG LIKE '%{bg}%'"
        cur1.execute(st1)
        data = cur1.fetchall()
        l2 = list()
        for i in data:
            a, b, c, d, e, f, g = i
            l2.append([a, b, c, d, e, f, g])
        table = tabulate(l2, headers=['Name', 'DOB','Year Graduated', 'Email', 'Blood Group', 'Address', 'Employment Status'],
                         tablefmt='orgtbl')
        print(table)
        if len(data) == 0:
            print('No data found\n')
        parameters()
    elif n == 5:
        print("Entering main menu...\n")
    else:
        print("Under development, please try again later")
