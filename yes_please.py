
# ===== Внутренний функционал модуля =====

def yesPlease(my_str):
    for letter in my_str:
        bits = bin(ord(letter))[2:]
        my_list = bits.zfill(16)
        while len(my_list) > 0:
            current_part = my_list[:4]
            my_list = my_list[4:]
            if current_part[0] == '1':
                letter_one = "а" # русская
            else:
                letter_one = "a" # английская
            if current_part[1] == '1':
                letter_two = "о" # русская
            else:
                letter_two = "o" # английская
            if current_part[2] == '1':
                letter_three = "а" # русская
            else:
                letter_three = "a" # английская
            if current_part[3] == '1':
                letter_four = "а" # русская
            else:
                letter_four = "a" # английская
            daPozaluista = "Д" + letter_one +", п" + letter_two + "ж" + letter_three + "луйст" + letter_four + ". "
            yield daPozaluista


def toNormalStr(my_str):
    str16 = []
    for letter in my_str:
        if letter in ['a', 'а', 'o', 'о']:
            if letter == 'а' or letter == 'о':
                str16.append(1)
            else:
                str16.append(0)
        if len(str16) == 16:
            yield chr(int(''.join([str(num) for num in str16]), 2))
            str16 = []






# ===== Внешний интерфейс модуля =====

# TODO:
#  - Доделать и проверить функционал работу генераторов для конвертации строки в дапожалуйста и наоборот
#  - Запилить интерфейс :D
#   - Для отображения процесса будем использовать модуль из 4 букв, название которого я не помню
#   - Внутреннюю кухню модуля делаем приватной (загуглить про это, потом объяснить тоше что делает символ _ в начале функции)
#  - Заебашить Unit-тесты
#  - Залить проект на гитхаб (потихоньку собираем портфолию ахаха)
#                                                                                                                 <3  <3

def encrypt_string_to_string(input_string: str) -> str:
    """
    Шифрует исходную строку
    :param input_string: исходная строка
    :return: зашифрованная строка
    """
    s = input_string
    result = ""
    for element in yesPlease(s):
        result += element
    return result

def encrypt_string_to_file(input_string: str, output_file_name: str, show_process: bool = False) -> bool:
    """
    Шифрует исходную строку в файл
    :param input_string: исходная строка
    :param filename: имя файла
    :param show_process: флаг отображения процесса (я подскажу как)
    :return: успешно ли произошло сохранение файла
    """
    raise NotImplementedError()

def decrypt_file_to_string(input_file_name: str, show_process: bool = False) -> str:
    """
    Расшифровывает файл
    :param input_file_name: имя файла, который нужно расшифровать
    :param show_process: флаг отображения процесса
    :return: исходная строка
    """
    raise NotImplementedError()

def decrypt_file_to_file(input_file_name: str, output_file_name: str, show_process: bool = False) -> bool:
    """
    Конвертирует зашифрованный файл в незашифрованный
    :param input_file_name: входной зашифрованный файл
    :param output_file_name: выходной файл с исходными данными
    :param show_process: флаг отображения процесса
    :return: успешен ли результат конвертации
    """
    raise NotImplementedError()

def decrypt_string_to_string(input_string: str) -> str:
    """
    Расшифровывает строку
    :param input_string: зашифрованная строка
    :return: исходная строка
    """
    s = input_string
    result = ""
    for element in toNormalStr(s):
        result += element
    return result
