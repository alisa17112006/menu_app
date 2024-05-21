import sqlite3

connect = sqlite3.connect("employee.db")

cursor = connect.cursor()

def add_employee():
    id_em = int(input("Введите id сотрудника => "))
    fio = input("Введите fio сотрудника => ")
    role = input("Введите role сотрудника => ")

    cursor.execute(
        '''
        insert into employee (id, fio, role)
        values (?, ?, ?)
        ''', (id_em, fio, role)
    )

def show():
    cursor.execute('select * from employee')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_em():
    id_del = int(input("Введите id для удаления => "))
    cursor.execute('delete from employee where id = ?', id_del)

while True:
    choice = int(input('Выберите пункт меню:\n1. ПРосмотр всех сотрудников\n2. Добавить сотрудника\n3. Удалить сотрудника\n0. Выход из программы \n=> '))
    if choice == 1:
        show()
    elif choice == 2:
        add_employee()
        connect.commit()
    elif choice == 3:
        delete_em()
        connect.commit()
    elif choice == 0:
        break
    else:
        print("Ошибка ввода")
    cursor.close()
    connect.close()