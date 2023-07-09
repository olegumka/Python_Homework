from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    print(name, surname, phone, adress)
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n' 
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n' 
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n')
        print(f'Данные успешно добавлены в {var} csv-файл :)')
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')
        print(f'Данные успешно добавлены в {var} csv-файл :)')

    else: print('Ошибка ввода - нужно ввести цифру 1 или 2')


def print_data():
    print_var = int(input('В каком виде выводить данные: 1 - столбец, 2 - строка?: '))
    if print_var == 1:
        print('1 csv-файл:')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            data_list = list() # в этот список будет складываться итоговый результат
            j = 0
            for i in range(len(data)):
                if data[i] == '\n':
                    data_list.append(''.join(data[j:i]))
                    j = i
            print(''.join(data_list))
    elif print_var == 2:
        print('2 csv-файл:')
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            print(''.join(data))

    else: print('Ошибка ввода - нужно ввести цифру 1 или 2')


def delete_data():
    delete_var = int(input('В каком файле хотите удалить данные?: '))
    if delete_var == 1:
        print('Удаление данных из 1го csv-файл:')
        lines = []
        # Сначала надо прочесть файл, чтобы в список line[] загнать данные с файла:
        with open('data_first_variant.csv', 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            file.seek(0) # Возвращаем курсор в начало файла
            del_line = int(input('Введите номер той строки, которую хотите удалить: '))
        # А теперь пошел процесс удаления:
            lines.pop(del_line - 1)
            file.writelines(lines)
        print(lines)

    elif delete_var == 2:
        print('Удаление данных из 2го csv-файл:')
        lines = []
        with open('data_second_variant.csv', 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            file.seek(0)  # Возвращаем курсор в начало файла
            del_line = int(input('Введите номер той строки, которую хотите удалить: '))
            lines.pop(del_line - 1)
            file.writelines(lines)
        print(lines)
