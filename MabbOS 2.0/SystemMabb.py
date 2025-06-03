import os
import platform
import random
import time

directory = r"C:\Users\User\Desktop\MabbOS 2.0\files"

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

print("##      ##  ####  ##    ##       ####   #####\n## #  # ## ##  ## ##    ##      ##  ## ##\n##  ##  ## ###### ####  ####    ##  ##  #####\n##      ## ##  ## ## ## ## ##   ##  ##      ##\n##      ## ##  ## ####  ####     ####   ####")
print("         Введите help для инструкции")

code2 = []
peremennye = {}

def start(code):
    skip = False
    current_line = 0
    while current_line < len(code):
        line = code[current_line]
        current_line += 1
        parts = line.split()
        if not parts:
            continue
        if skip:
            if parts[0] == "_ENDIF":
                skip = False
            continue
        if parts[0] == "_END":
            break
        elif parts[0] == "_PRINT":
            print(line.replace("_PRINT ", "", 1).strip())
        elif parts[0] == "_PRINT-N":
            var_name = line.replace("_PRINT-N ", "", 1).strip()
            if var_name in peremennye:
                print(peremennye[var_name])
            else:
                print(f"Ошибка: переменная '{var_name}' не найдена.")
        elif parts[0] == "_NUMBER":
            var_name = parts[1]
            if parts[2] == "_RANDOM":
                min_val = int(parts[3])
                max_val = int(parts[4])
                peremennye[var_name] = random.randint(min_val, max_val)
            else:
                peremennye[var_name] = int(parts[2])
        elif parts[0] == "_STRING":
            var_name = parts[1]
            text = line.replace("_STRING ", "", 1).replace(var_name, "", 1).strip()
            peremennye[var_name] = text
        elif parts[0] == "_INPUT":
            var_name = parts[1]
            prompt = " ".join(parts[2:])
            user_input = input(prompt)
            try:
                peremennye[var_name] = int(user_input)
            except ValueError:
                peremennye[var_name] = user_input
        elif parts[0] == "_IF":
            var_name = parts[1]
            operator = parts[2]
            value = parts[3]
            var_value = peremennye.get(var_name)
            if var_value is None:
                print(f"Ошибка: переменная '{var_name}' не найдена.")
                skip = True
                continue
            if value.startswith("int"):
                compare_value = int(value[3:])
            elif value in peremennye:
                compare_value = peremennye[value]
            else:
                compare_value = value
            try:
                var_value = int(var_value)
                compare_value = int(compare_value)
            except ValueError:
                pass
            if operator == "=" and var_value == compare_value:
                pass
            elif operator == "!=" and var_value != compare_value:
                pass
            elif operator == "<" and var_value < compare_value:
                pass
            elif operator == ">" and var_value > compare_value:
                pass
            elif operator == "<=" and var_value <= compare_value:
                pass
            elif operator == ">=" and var_value >= compare_value:
                pass
            else:
                skip = True
        elif parts[0] == "_ENDIF":
            pass
        elif parts[0] == "_BACK":
            current_line = 0
        elif parts[0] == "_OPERATION":
            var_name = parts[1]
            operator = parts[2]
            value1 = parts[3]
            value2 = parts[4]
            if value1 in peremennye:
                val1 = peremennye[value1]
            else:
                val1 = int(value1)
            if value2 in peremennye:
                val2 = peremennye[value2]
            else:
                val2 = int(value2)
            if operator == "+":
                peremennye[var_name] = val1 + val2
            elif operator == "-":
                peremennye[var_name] = val1 - val2
            elif operator == "*":
                peremennye[var_name] = val1 * val2
            elif operator == "/":
                peremennye[var_name] = val1 / val2
            elif operator == "%":
                peremennye[var_name] = val1 % val2
            else:
                print(f"Ошибка: неизвестный оператор '{operator}'.")
        elif parts[0] == "_EXECUTE":
            if len(parts) < 2:
                print("Ошибка: недостаточно аргументов для _EXECUTE")
                continue
            try:
                target_line = int(parts[1])
            except ValueError:
                print(f"Ошибка: неверный номер строки '{parts[1]}'")
                continue
            if target_line < 1 or target_line > len(code):
                print(f"Ошибка: номер строки {target_line} вне диапазона 1-{len(code)}")
                continue
            current_line = target_line - 1
        elif parts[0] == "_SECOND":
            second = int(parts[1].strip())
            time.sleep(second)
        elif parts[0] == "_SECOND-N":
            second2 = int(peremennye[parts[1]])
            time.sleep(second2)
        elif parts[0] == "_FILE":
            if len(parts) < 3:
                print("Ошибка: недостаточно аргументов для _FILE")
                continue
            filename = parts[1]
            operation = parts[2]
            filepath = os.path.join(directory, filename)
            if operation == "_READ":
                if len(parts) < 4:
                    print("Ошибка: недостаточно аргументов для _READ")
                    continue
                var_name = parts[3]
                try:
                    with open(filepath, "r") as file:
                        peremennye[var_name] = file.read()
                except FileNotFoundError:
                    print(f"Ошибка: файл '{filename}' не найден.")
            elif operation == "_WRITE":
                text = " ".join(parts[3:])
                try:
                    with open(filepath, "w") as file:
                        file.write(text)
                except IOError:
                    print(f"Ошибка: не удалось записать в файл '{filename}'.")
            elif operation == "_APPEND":
                text = " ".join(parts[3:])
                try:
                    with open(filepath, "a") as file:
                        file.write(text)
                except IOError:
                    print(f"Ошибка: не удалось добавить текст в файл '{filename}'.")
            elif operation == "_DELETE":
                try:
                    os.remove(filepath)
                except FileNotFoundError:
                    print(f"Ошибка: файл '{filename}' не найден.")
                except IOError:
                    print(f"Ошибка: не удалось удалить файл '{filename}'.")
            else:
                print(f"Ошибка: неизвестная операция '{operation}'.")

        elif parts[0] == "_FILE-N":
            if len(parts) < 3:
                print("Ошибка: недостаточно аргументов для _FILE")
                continue
            filename = peremennye[parts[1]]
            operation = parts[2]
            filepath = os.path.join(directory, filename)
            if operation == "_READ":
                if len(parts) < 4:
                    print("Ошибка: недостаточно аргументов для _READ")
                    continue
                var_name = parts[3]
                try:
                    with open(filepath, "r") as file:
                        peremennye[var_name] = file.read()
                except FileNotFoundError:
                    print(f"Ошибка: файл '{filename}' не найден.")
            elif operation == "_WRITE":
                text = peremennye[parts[3]]
                try:
                    with open(filepath, "w") as file:
                        file.write(text)
                except IOError:
                    print(f"Ошибка: не удалось записать в файл '{filename}'.")
            elif operation == "_APPEND":
                text = peremennye[parts[3]]
                try:
                    with open(filepath, "a") as file:
                        file.write(text)
                except IOError:
                    print(f"Ошибка: не удалось добавить текст в файл '{filename}'.")
            elif operation == "_DELETE":
                try:
                    os.remove(filepath)
                except FileNotFoundError:
                    print(f"Ошибка: файл '{filename}' не найден.")
                except IOError:
                    print(f"Ошибка: не удалось удалить файл '{filename}'.")
            else:
                print(f"Ошибка: неизвестная операция '{operation}'.")


while 1:
    consol = input("\n>>>")
    if consol == "help":
        print("clear - очистить консоль\nshow file - показать все файлы\nstart file - начать файл .mabb\nЭта ОС создана Маббом. В этой ОС все программы написаны на моем собственном языке программирования mabb, чтобы не писать другие файлы на assembly. На ассембли написан лишь один файл SystemMabb, а все другие на mabb. (Это симуляция MabbOS на python)")

    if consol == "show files":
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        print(files)

    if consol == "start file":
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        name = input("Название файла ")
        code2.clear()
        peremennye.clear()
        print("-" * 50)
        if name in files:
            with open(directory + "\\" + name, "r") as file:
                for line2 in file:
                    code2.append(line2)
                start(code2)
        else:
            print(f"Файл {name} не найден")
        print("-" * 50)
    
    if consol == "clear":
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')