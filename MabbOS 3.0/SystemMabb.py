import os
import platform
import random
import time
import keyboard
import datetime


directory = r"C:\Users\User\Desktop\MabbOS 3.0\files"

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

print("===============================MabbOS===============================")

# print("##      ##  ####  ##    ##       ####   #####\n## #  # ## ##  ## ##    ##      ##  ## ##\n##  ##  ## ###### ####  ####    ##  ##  #####\n##      ## ##  ## ## ## ## ##   ##  ##      ##\n##      ## ##  ## ####  ####     ####   ####")
# print("         Введите help для инструкции")

print("  ___    ___                                ________      ________  \n",
"|   \  /   |     __      _      _         /  ____  \    / _______/  \n",
"| |\ \/ /| |    /  \    | |    | |       |  /    \  |  / /______  \n",
"| | \__/ | |   / /\ \   | |__  | |__     | |      | |  \______  \ \n",
"| |      | |  / ____ \  |    \ |    \    |  \____/  |  ______/  /  \n",
"|_|      |_| /_/    \_\ |____/ |____/     \________/  \________/  \n")

print("                 Введите help для инструкции")

code2 = []
peremennye = {}
libs = {}  

def start(code):
    skip = False
    pc = 0  
    while pc < len(code): # Главный цикл

        if keyboard.is_pressed('esc'):
            return

        line = code[pc]
        line = line.strip()
        parts = line.split()

        if not parts:
            pc += 1
            continue

        if parts[0] == "_ENDIF":
            skip = False
            pc += 1
            continue

        if skip:
            pc += 1
            continue

        # Базовые команды
        try:
            if parts[0] == "//":                            # Комментарии
                pc += 1
                continue
            elif parts[0] == "_PRINT":                      # Вывод переменной или строки
                if parts[1] == "_V":
                    print(peremennye[parts[2]])
                    pc += 1
                    continue   
                else:
                    print(line.replace("_PRINT ", ""))
                    pc += 1
                    continue   

            elif parts[0] == "_VAR":                        # Создание переменной, которая хранит число, текст или пользователя
                if parts[1] == "_NUMBER":
                    if parts[2] == "_RANDOM":
                        peremennye[parts[3]] = random.randint(int(parts[4]), int(parts[5]))
                        pc += 1
                        continue
                    else:
                        peremennye[parts[2]] = int(parts[3])
                        pc += 1
                        continue
                elif parts[1] == "_TEXT":
                    peremennye[parts[2]] = str(parts[3])
                    pc += 1
                    continue
                elif parts[1] == "_INPUT":
                    if parts[2] == "_INT":
                        answer = input(line.replace("_VAR _INPUT _INT", "").replace(parts[3], "").lstrip())
                        peremennye[parts[3]] = int(answer)
                        pc += 1
                        continue
                    else:
                        answer = input(line.replace("_VAR _INPUT", "").replace(parts[2], "").lstrip())
                        peremennye[parts[2]] = answer
                        pc += 1
                        continue
                elif parts[1] == "_DATE":
                    peremennye[parts[2]] = datetime.date.today()
                    pc += 1
                    continue
            
            elif parts[0] == "_EXECUTE":                    # Выполняет программу с указанной строчки
                pc = int(parts[1]) - 1
                continue
            
            elif parts[0] == "_SECOND":                     # Ждет указанное количество секунд
                time.sleep(int(parts[1]))
                pc += 1
                continue
            
            elif parts[0] == "_IF":                         # Если условие выполнено, то выполняется его блок
                arg = parts[1]
                arg2 = parts[3]
                if parts[1] == "_INT":
                    arg = int(parts[2])
                elif parts[3] == "_INT":
                    arg2 = int(parts[4])

                if parts[1] == "_STR":
                    arg = str(parts[2])
                elif parts[3] == "_STR":
                    arg2 = str(parts[4])

                if arg in peremennye:
                    arg = peremennye[parts[1]]
                if arg2 in peremennye:
                    arg2 = peremennye[parts[3]]
                
                condition_met = False
                if parts[2] == "=":
                    condition_met = (arg == arg2)
                elif parts[2] == "<":
                    condition_met = (arg < arg2)
                elif parts[2] == ">":
                    condition_met = (arg > arg2)
                elif parts[2] == "!=":
                    condition_met = (arg != arg2)
                elif parts[2] == "_IN":
                    condition_met = (arg in arg2)
                
                skip = not condition_met
                pc += 1
                continue
            
            elif parts[0] == "_OPERATION":                  # Выполняет операцию с текстом или арифметическую
                if parts[1] == "_LEN":
                    peremennye[parts[2]] = len(peremennye[parts[3]])
                    pc += 1
                    continue   
                elif parts[1] == "_COUNT":
                    count = 0
                    for l in peremennye[parts[2]]:
                        if l == peremennye[parts[4]]:
                            count += 1
                    peremennye[parts[2]] = count
                    pc += 1
                    continue  
                elif parts[1] == "_REPLACE":
                    peremennye[parts[2]] = peremennye[parts[2]].replace(peremennye[parts[3]], peremennye[parts[4]])
                    pc += 1
                    continue   
                elif parts[1] == "_CHANGE":
                    peremennye[parts[2]] = peremennye[parts[3]]
                else:
                    if parts[3] == "+":
                        peremennye[parts[1]] = int(peremennye[parts[2]]) + int(peremennye[parts[4]])
                        pc += 1
                        continue   
                    elif parts[3] == "-":
                        peremennye[parts[1]] = int(peremennye[parts[2]]) - int(peremennye[parts[4]])
                        pc += 1
                        continue 
                    elif parts[3] == "/":
                        peremennye[parts[1]] = int(peremennye[parts[2]]) / int(peremennye[parts[4]])
                        pc += 1
                        continue  
                    elif parts[3] == "*":
                        peremennye[parts[1]] = int(peremennye[parts[2]]) * int(peremennye[parts[4]])
                        pc += 1
                        continue   

            elif parts[0] == "_END":                    # Заканчивает программу
                pc += 1
                break

            elif parts[0] == "_ENDIF":                  # Заканчивает блок _IF
                pc += 1
                continue

            else:
                print(f"Неизвестная команда '{line}'")  # Вывод неизвестной команды
                return
            
        except Exception as e:                          # Вывод ошибки
            print(f"Ошибка в '{line}': {str(e)}")
            return


while True:
    consol = input("\n>>>")
    if consol == "help":
        print("""
 ____________________________________
|clear        -      очистить консоль|
|show files   -    показать все файлы|
|start file   -     начать файл .mabb|
|off          -   выключить компьютер|
|info         -       информация о ОС|
|зажать esc   -   завершить программу|
|Если у вас программа просит ввести  |
|строку, то нужно зажать enter + esc |
|____________________________________|
""")
    elif consol == "show files":
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        print(files)
    elif consol == "start file":
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        name = input("Название файла ")
        code2.clear()
        peremennye.clear()
        print(f"==============================={name}===============================")
        if name in files:
            with open(directory + "\\" + name, "r") as file:
                for line2 in file:
                    code2.append(line2)
            start(code2)
        else:
            print(f"Файл {name} не найден")
        count = len(name) + 62
        print("=" * count)
    elif consol == "clear":
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')    
        print("===============================MabbOS===============================")
    elif consol == "off":
        exit()
    elif consol == "info":
        print("""              
 ____________________________________
|Эта ОС создана Маббом. В этой ОС    |
|все программы написаны на моем      |
|собственном языке программирования  |
|mabb, чтобы не писать другие файлы  |
|на assembly. На ассембли написан    |
|лишь один файл SystemMabb, а все    |
|другие на mabb. (Это симуляция      |
|MabbOS на python)                   |
|____________________________________|
""")