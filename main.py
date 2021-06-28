import os

command = ""


def runCommand(command, option, argument, argument2):
    if command == "mkdir":
        os.mkdir(argument)
    if command == "rmdir":
        try:
            os.rmdir(argument)
        except FileNotFoundError:
            print("Не удается найти указанный файл.")
    if command == "del":
        try:
            if option == "/p":
                print(argument + ", Delete (Y/N)?")
                answer = input()
                if answer == 'Y':
                    os.remove(argument)
                else:
                    return
            else:
                os.remove(argument)
        except FileNotFoundError:
            print("Не удается найти указанный файл.")
    if command == "net":
        if argument == "user":

    if command == "cd":
        os.chdir(argument)
    if command == "dir":
        # dir_list = os.scandir()
        # print(dir_list)
        #with os.scandir() as it:
        if option == '/b':
            print("Содержимое папки " + os.getcwd())
            os.system('ls')
            #for entry in it:
             #   if not entry.name.startswith('.'):  # and entry.is_file():

              #      print(entry.name + entry.st_atime)
    if command == "rename":
        try:
            os.rename(argument, argument2)
        except FileNotFoundError:
            print("Не удается найти указанный файл.")
    if command == "help":
        if argument == "mkdir":
            print("""Создание каталога.

MKDIR [диск:]путь
MD [диск:]путь

Изменение команды MKDIR при включении расширенной обработки команд:

Команда MKDIR создает при необходимости все промежуточные каталоги в пути.
Например, если \\a не существует, то:

    mkdir \\a\\b\c\d

приводит к тому же результату, что и:

    mkdir \\a
    chdir \\a
    mkdir b
    chdir b
    mkdir c
    chdir c
    mkdir d

При отключении расширенной обработки команд используется только второй вариант.""")
        if argument == "rmdir":
            print("""Удаление каталога.

RMDIR [/S] [/Q] [диск:]путь
RD [/S] [/Q] [диск:]путь

    /S Удаление дерева каталогов, т. е. не только указанного каталога,
            но и всех содержащихся в нем файлов и подкаталогов.

    /Q Отключение запроса подтверждения при удалении дерева каталогов
            с помощью ключа /S.
            """)
        if argument == "del":
            print("""Удаление одного или нескольких файлов.

DEL [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names
ERASE [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names

  names Список из одного или нескольких файлов или каталогов.
                Для удаления группы файлов можно использовать подстановочные знаки. Если
                указан каталог, будут удалены все файлы в этом
                каталоге.

  /P Запрос подтверждения перед удалением каждого файла.
  /F Принудительное удаление файлов, доступных только для чтения.
  /S Удаление указанных файлов из всех подкаталогов.
  /Q Отключение запроса на подтверждение при удалении файлов
  /A Отбор файлов для удаления по атрибутам
  атрибуты R Файлы, доступные только для чтения S Системные файлы
                H Скрытые файлы A Файлы, готовые для архивирования
                I Файлы с неиндексированным содержимым L Точки повторной обработки
                O Автономные файлы - Префикс "-" имеет значение НЕ

Изменение команд DEL и ERASE при включении расширенной обработки команд:

Результаты вывода для ключа /S принимают обратный характер, то есть выводятся
только имена удаленных файлов, а не файлов, которые не удалось найти.
            """)
        if argument == "exit":
            print("""Завершает программу CMD.EXE (интерпретатор команд) или текущий пакетный
файл-сценарий.

EXIT [/B] [exitCode]

  /B Предписывает завершить текущий пакетный файл-сценарий вместо
              завершения CMD.EXE. Если выполняется вне пакетного
              файла-сценария, то будет завершена программа CMD.EXE

  exitCode Указывает цифровое значение. Если указан ключ /B, определяет
              номер для ERRORLEVEL. В случае завершения работы CMD.EXE,
              устанавливает код завершения процесс с данным номером.
            """)
        if argument == "cd":
            print("""Выводит имя или изменяет текущий каталог.

CHDIR [/D] [диск:][путь]
CHDIR [..]
CD [/D] [диск:][путь]
CD [..]

  .. обозначает переход в родительский каталог.

Команда CD диск: отображает имя текущего каталога указанного диска.
Команда CD без параметров отображает имена текущего диска и каталога.

Параметр /D используется для одновременной смены
текущего диска и каталога.

Изменение команды CHDIR при включении расширенной обработки команд:

Имя текущего каталога в строке вызова преобразуется к тому же регистру
символов, что и для существующих имен на диске. Так, команда CD C:\TEMP
на самом деле сделает текущим каталог C:\Temp, если он существует на диске.

Команда CHDIR перестает рассматривать пробелы как разделители, что позволяет
перейти в подкаталог, имя которого содержит пробелы, не заключая все имя
каталога в кавычки. Например:

    cd \winnt\profiles\\username\programs\start menu

приводит к тому же результату, что и:

    cd "\winnt\profiles\\username\programs\start menu"

При отключении расширенной обработки команд используется только второй вариант.
            """)
        if argument == "dir":
            print("""Вывод списка файлов и подкаталогов в указанном каталоге.

DIR [drive:][path][filename] [/A[[:]attributes]] [/B] [/C] [/D] [/L] [/N]
  [/O[[:]sortorder]] [/P] [/Q] [/R] [/S] [/T[[:]timefield]] [/W] [/X] [/4]

  [drive:][path][filename]
              Диск, каталог или имена файлов для включения в список.

  /A Отображение файлов с указанными атрибутами.
  атрибуты D Каталоги. R Файлы, доступные только для чтения
               H Скрытые файлы A Файлы, готовые для архивирования
               S Системные файлы I Файлы с неиндексированным содержимым
               L Точки повторной обработки O Автономные файлы
               - Префикс "-" имеет значение НЕ
  /B Вывод только имен файлов.
  /C Применение разделителя групп разрядов при выводе размеров файлов.
              Используется по умолчанию. Чтобы отключить применение разделителя групп разрядов, задайте ключ /-C.
  /D Вывод списка в нескольких столбцах с сортировкой по столбцам.
  /L Использовать нижний регистр.
  /N Новый формат длинного списка, имена файлов выводятся в крайнем правом столбце.
  /O Сортировка списка отображаемых файлов.
  sortorder N По имени (по алфавиту) S По размеру (начиная с минимального)
               E По расширению (по алфавиту) D По дате и времени (начиная с самого старого)
               G Начать список с каталогов - Префикс "-" обращает порядок
  /P Пауза после заполнения каждого экрана.
  /Q Вывод сведений о владельце файла.
  /R Отображение альтернативных потоков данных этого файла.
  /S Отображение файлов из указанного каталога и всех его подкаталогов.
00:51

/T Выбор поля времени для сортировки.
  timefield C Создание
              A Последнее использование
              W Последнее изменение
  /W Вывод списка в несколько столбцов.
  /X Отображение коротких имен для файлов, чьи имена не соответствуют стандарту 8.3.
              Формат аналогичен выводу с ключом /N, но короткие
              имена файлов выводятся слева от длинных. Если короткого имени у
              файла нет, вместо него выводятся пробелы.
  /4 Вывод номера года в четырехзначном формате

Стандартный набор ключей можно записать в переменную среды DIRCMD. Для отмены
их действия введите в команде те же ключи с префиксом "-", например: /-W.
            """)
        if argument == ' ':
            print("""Для получения сведений об определенной команде наберите HELP <имя команды>
ASSOC Вывод либо изменение сопоставлений по расширениям имен файлов.
ATTRIB Отображение и изменение атрибутов файлов.
BREAK Включение и выключение режима обработки комбинации клавиш CTRL+C.
BCDEDIT Задает свойства в базе данных загрузки для управления начальной
               загрузкой.
CACLS Отображение и редактирование списков управления доступом (ACL)
               к файлам.
CALL Вызов одного пакетного файла из другого.
CD Вывод имени либо смена текущей папки.
CHCP Вывод либо установка активной кодовой страницы.
CHDIR Вывод имени либо смена текущей папки.
CHKDSK Проверка диска и вывод статистики.
CHKNTFS Отображение или изменение выполнения проверки диска во время
               загрузки.
CLS Очистка экрана.
CMD Запуск еще одного интерпретатора командных строк Windows.
COLOR Установка цветов переднего плана и фона, используемых по умолчанию.
COMP Сравнение содержимого двух файлов или двух наборов файлов.
COMPACT Отображение и изменение сжатия файлов в разделах NTFS.
CONVERT Преобразует тома FAT в NTFS. Вы не можете
               преобразовать текущий диск.
COPY Копирование одного или нескольких файлов в другое место.
DATE Вывод либо установка текущей даты.
DEL Удаление одного или нескольких файлов.
DIR Вывод списка файлов и подпапок из указанной папки.
DISKPART Отображает или настраивает свойства раздела диска.
DOSKEY Редактирует командные строки, повторно вызывает команды Windows и создает
               макросы.
DRIVERQUERY Отображает текущее состояние и свойства драйвера устройства.
ECHO Отображает сообщения и переключает режим отображения команд на экране.
ENDLOCAL Завершает локализацию изменений среды для пакетного файла.
ERASE Удаляет один или несколько файлов.
EXIT Завершает работу программы CMD.EXE (интерпретатора командных строк).
FC Сравнивает два файла или два набора файлов и
               отображает различия между ними.
FIND Ищет текстовую строку в одном или нескольких файлах.
FINDSTR Ищет строки в файлах.
FOR Запускает указанную команду для каждого из файлов в наборе.
FORMAT Форматирует диск для работы с Windows.
FSUTIL Отображает или настраивает свойства файловой системы.
FTYPE Отображает либо изменяет типы файлов, используемые при
               сопоставлении по расширениям имен файлов.
GOTO Направляет интерпретатор команд Windows в отмеченную строку
               пакетной программы.
GPRESULT Отображает информацию о групповой политике для компьютера или пользователя.
GRAFTABL Позволяет Windows отображать расширенный набор символов в
               графическом режиме.
HELP Выводит справочную информацию о командах Windows.
ICACLS Отображает, изменяет, архивирует или восстанавливает
               списки ACL для файлов и каталогов.
IF Выполняет условную обработку в пакетных программах.
LABEL Создает, изменяет или удаляет метки тома для дисков.
MD Создает каталог.
MKDIR Создает каталог.
MKLINK Создает символьные ссылки и жесткие связи
MODE Настраивает системные устройства.
MORE Последовательно отображает данные по частям размером в один экран.
MOVE Перемещает один или несколько файлов из одного каталога
               в другой.
OPENFILES Отображает файлы, открытые для файлового ресурса удаленными пользователями.
PATH Отображает или устанавливает путь поиска исполняемых файлов.
PAUSE Приостанавливает выполнение пакетного файла и выводит сообщение.
POPD Восстанавливает предыдущее значение текущего каталога,
               сохраненное с помощью команды PUSHD.
PRINT Выводит на печать содержимое текстового файла.
PROMPT Изменяет командную строку Windows.
PUSHD Сохраняет текущий каталог, затем изменяет его.
RD Удаляет каталог.
RECOVER Восстанавливает данные, которые можно прочитать, с плохого или поврежденного диска.
REM Записывает комментарии в пакетные файлы или файл CONFIG.SYS.
REN Переименовывает файлы.
RENAME Переименовывает файлы.
REPLACE Заменяет файлы.
RMDIR Удаляет каталог.
ROBOCOPY Улучшенная служебная программа копирования файлов и деревьев папок
SET Показывает, устанавливает или удаляет переменные среды Windows.
SETLOCAL Начинает локализацию изменений среды в пакетном файле.
SC Отображает или настраивает службы (фоновые процессы).
SCHTASKS Выполняет команды и запускает программы на компьютере по расписанию.
SHIFT Изменяет положение заменяемых параметров в пакетных файлах.
SHUTDOWN Позволяет локально или удаленно завершить работу компьютера.
SORT Сортирует ввод.
START Выполняет указанную программу или команду в отдельном окне.
SUBST Связывает путь с именем диска.
SYSTEMINFO Отображает сведения о свойствах и конфигурации определенного компьютера.
TASKLIST Отображает все выполняемые задачи, включая службы.
TASKKILL Прекращение или остановка процесса либо приложения.
TIME Отображает или устанавливает системное время.
TITLE Назначает заголовок окна для сеанса CMD.EXE.
TREE Графически отображает структуру каталогов диска или
          пути.
TYPE Отображает содержимое текстовых файлов.
VER Отображает сведения о версии Windows.
VERIFY Устанавливает режим проверки в Windows правильности записи
               файлов на диск.
VOL Отображает метку и серийный номер тома для диска.
XCOPY Копирует файлы и деревья папок.
WMIC Отображает сведения об инструментарии WMI в интерактивной командной оболочке.

Дополнительные сведения о средствах см. в описании программ командной строки в справке.

            """)
        if argument == "rename":
            print("""Переименование одного или нескольких файлов.

RENAME [диск:][путь]имя_файла1 имя_файла2.
REN [диск:][путь]имя_файла1 имя_файла2.

Обратите внимание, что для конечного файла невозможно указать другой диск или путь.
            """)



def parseCommand(command, option, argument, argument2):
    command = command.lower()
    command = command.split()
    commandFirstWord = command[0]
    while len(command) != 3:
        command.append(' ')
    commandSecWord = command[1]
    commandThWord = command[2]
    command = commandFirstWord
    if commandSecWord[0] == '/':
        option = commandSecWord
        argument = commandThWord
    else:
        argument = commandSecWord
        argument2 = commandThWord
    return command, option, argument, argument2


def main():
    print(
        "Microsoft Windows [Version 10.0.19042.1052](c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.")
    command = ' '
    while command != "exit":
        print(os.getcwd() + ">")
        command = input()
        option, argument, argument2 = ' ', ' ', ' '
        command, option, argument, argument2 = parseCommand(command, option, argument, argument2)
        runCommand(command, option, argument, argument2)


if __name__ == "__main__":
    main()