from tabulate import tabulate

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 9:  # изменено на 9 для завершения работы
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = input('Введите новые данные (Фамилия,Имя,Телефон,Описание): ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 5:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 6:
            last_name = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 7:
            write_txt('phonebook.txt', phone_book)
            print('Справочник сохранен в текстовом формате.')
        elif choice == 8:
            source_file = input('Введите имя исходного файла: ')
            target_file = input('Введите имя файла назначения: ')
            line_number = int(input('Введите номер строки для копирования: '))
            try:
                copy_line(source_file, target_file, line_number)
                print(f'Строка {line_number} скопирована из {source_file} в {target_file}.')
            except FileNotFoundError as e:
                print(f'Ошибка: {e}')

        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить номер абонента\n"
          "6. Удалить абонента\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Копировать данные из одного файла в другой\n"
          "9. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def print_result(phone_book):
    print(tabulate(phone_book, headers="keys", tablefmt="grid"))

def find_by_lastname(phone_book, last_name):
    result = [record for record in phone_book if record['Фамилия'] == last_name]
    return tabulate(result, headers="keys", tablefmt="grid") if result else "Абонент не найден."

def find_by_number(phone_book, number):
    result = [record for record in phone_book if record['Телефон'] == number]
    return tabulate(result, headers="keys", tablefmt="grid") if result else "Абонент не найден."

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return "Номер изменен."
    return "Абонент не найден."

def delete_by_lastname(phone_book, last_name):
    for i, record in enumerate(phone_book):
        if record['Фамилия'] == last_name:
            del phone_book[i]
            return "Абонент удален."
    return "Абонент не найден."

def copy_line(source_file, target_file, line_number):
    with open(source_file, 'r', encoding='utf-8') as src, open(target_file, 'a', encoding='utf-8') as tgt:
        lines = src.readlines()
        if 0 < line_number <= len(lines):
            tgt.write(lines[line_number - 1])
        else:
            print(f"Номер строки {line_number} выходит за пределы файла {source_file}.")

if __name__ == "__main__":
    work_with_phonebook()