import os

def runCommand(command, option, argument):
    if command == "mkdir":  
        if argument[0] == ' ':
            print("Ошибка в синтаксисе команды.")
        else:
            try:
                os.mkdir(argument[0])
            except FileNotFoundError:
                print("Ошибка в синтаксисе команды.")
    elif command == "ipconfig":
        if option == "/all":
            os.system("ifconfig -a")
        else:
            os.system("ifconfig")
    elif command == "exit":
        return
    elif command == "cmd.exe":
        if argument[0] == '<':
            try:
                f = open(argument[1], 'r')
                while True:
                    str = f.readline()
                    if not str:
                        break
                    option = ' '
                    argument = []
                    command, option, argument = parseCommand(str, option, argument)
                    runCommand(command, option, argument)
                f.close()
            except FileNotFoundError:
                print("Не удается найти указанный файл.")

    elif command == "type":
        try:
            os.system("cat " + argument[0])
        except FileNotFoundError:
            print("Не удается найти указанный файл.")
    elif command == "rmdir":  
        try:
            os.rmdir(argument[0])
        except FileNotFoundError:
            print("Не удается найти указанный файл.")
        except OSError:
            print("Папка не пуста.")
    elif command == "del":
        try:
            if option == "/p":
                print(argument[0] + ", Delete (Y/N)?")
                answer = input()
                if answer == 'Y':
                    os.remove(argument[0])
                else:
                    return
            else:
                os.remove(argument[0])
        except FileNotFoundError:
            print("Не удается найти указанный файл.")
        except IsADirectoryError:
            print("Файл является директорией.")

    elif command == "cd":  
        if argument[0] == ' ':
            print(os.getcwd() + ">")
        else:
            try:
                os.chdir(argument[0])
            except FileNotFoundError:
                print("Системе не удается найти указанный путь.")

    elif command == "dir":  
        if option == '/b':
            
            os.system('ls')

    elif command == "rename":
        try:
            os.rename(argument[0], argument[1])
        except FileNotFoundError:
            print("Не удается найти указанный файл.")
    elif command == "help":
        if argument[0] == "mkdir":
            print("""Создает каталог или подкаталог. 
mkdir <path>
<path> 	Указывает имя и расположение нового каталога. """)
        elif argument[0] == "ipconfig":
            print("""Вывод деталей текущего соединения
            mkdir <path>
            <path> 	Указывает имя и расположение нового каталога. """)
        elif argument[0] == "rmdir":
            print("""Удаление каталога.

RMDIR <path>
<path> 	Указывает расположение и имя каталога, который требуется удалить. 

    """)
        elif argument[0] == "del":
            print("""Удаление одного файла.
DEL [/P] names
  name Имя файла.
  /P Запрос подтверждения перед удалением каждого файла.
  """)
        elif argument[0] == "exit":
            print("""Завершает программу CMD.EXE (интерпретатор команд) или текущий пакетный
файл-сценарий.
EXIT  
            """)
        elif argument[0] == "cd":
            print("""Выводит имя или изменяет текущий каталог.
CD [путь]
CD [..]
  .. обозначает переход в родительский каталог.
Команда CD без параметров отображает имена текущего диска и каталога.
""")
        elif argument[0] == "dir":
            print("""Вывод списка файлов и подкаталогов в указанном каталоге.
DIR [path][filename] /B 
  [path][filename]
              Каталог или имена файлов для включения в список.
  /B Вывод только имен файлов.
              """)
        elif argument[0] == ' ':
            print("""Для получения сведений об определенной команде наберите HELP <имя команды>
CD Вывод имени либо смена текущей папки.
CMD.EXE < Запуск командного сценария.
DEL Удаление одного или нескольких файлов.
DIR Вывод списка файлов и подпапок из указанной папки.
EXIT Завершает работу программы CMD.EXE (интерпретатора командных строк).
HELP Выводит справочную информацию о командах Windows.
IPCONFIG Выводит детали текущего соединения.
MKDIR Создает каталог.
RENAME Переименовывает файлы.
RMDIR Удаляет каталог.
TYPE Отображает содержимое текстовых файлов.
Дополнительные сведения о средствах см. в описании программ командной строки в справке.
            """)
        elif argument[0] == "rename":
            print("""Переименование одного или нескольких файлов.

RENAME [путь]имя_файла1 имя_файла2.



            """)  
        elif argument[0] == "type":
            print("""Вывод содержимого одного или нескольких текстовых файлов.

TYPE [путь]имя_файла
                        """)
        else:
            print(""" Данная команда не поддерживается. Воспользуйтесь параметром \"""" + argument[0] + " /?\".")
    else:
        print(command + ": команда не найдена.")

def parseCommand(command, option, argument):
    command = command.lower()
    command = command.split()

    while len(command) < 3:
        command.append(' ')
    for word in command[1:]:
        if word[0] == '/':
            option = word
        else:
            argument.append(word)
    if not argument:
        argument = [" ", " "]
    command = command[0]
    return command, option, argument


def main():
    print(
        "Microsoft Windows [Version 10.0.19042.1052](c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.")

    command = ' '
    while command != "exit":
        print(os.getcwd() + ">")
        str = input()
        option = ' '
        argument = []
        command, option, argument = parseCommand(str, option, argument)
        runCommand(command, option, argument)


if __name__ == "__main__":
    main()
