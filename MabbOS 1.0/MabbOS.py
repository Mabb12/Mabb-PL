import os
import platform
import random
import time
import winsound

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

print("##      ##  ####  ##    ##       ####   #####\n## #  # ## ##  ## ##    ##      ##  ## ##\n##  ##  ## ###### ####  ####    ##  ##  #####\n##      ## ##  ## ## ## ## ##   ##  ##      ##\n##      ## ##  ## ####  ####     ####   ####")
print("\n   Введите help для вывода всех команд")

directory = r"C:\Users\User\Desktop\mabbOS"

files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

while 1:
    consol = input("")

    if consol == "show files":
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        print(files)

    if consol == "file":
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        print(files)
        file = input("Выберете файл\n")
        for i in files:
            if i == file:
                print("Файл найден")
                file_move = input("Что сделать с файлом? Читать, изменить, удалить\n")
                if file_move == "Читать":
                    with open(file, "r") as file:
                        content = file.read()
                        print(content)
                if file_move == "изменить":
                    with open(file, "w") as file:
                        write = input("Введите то, на что хотите изменить файл\n")
                        file.write(write)
                if file_move == "удалить":
                    path = directory + f'\{file}'
                    if file == 'MabbOS.py':
                        print("Нельзя удалить системный файл")
                        print("Чтобы не допустить удаления системных файлов, компьютер будет выключен")
                        exit()
                    os.remove(path)
                    print(f"Файл {file} успешно удален.")

    if consol == "create file":
        name = input("Название нового файла\n")
        with open(f"{name}", "x"):
            print(f"Файл {name} создан")

    if consol == "clear":
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    if consol == "calc":
        number1 = float(input("Введите первую цифру\n"))
        sign = input("Введите ариф. знак\n")
        number2 = float(input("Введите вторую цифру\n"))
        if sign == "+":
            print(number1 + number2)
        if sign == "-":
            print(number1 - number2)
        if sign == "/":
            print(number1 / number2)
        if sign == "*":
            print(number1 * number2)

    if consol == "off":
        exit()

    if consol == "binary":
        text = input("Напишите текст, который вы хотите перевести в двоичный\n")
        binary = ' '.join(format(ord(i), '08b') for i in text) 
        print(binary)

    if consol == "text":
        binary2 = input("Введите бинарный код, который вы хотите перевести в текст\n")
        binary_values = binary2.split()
        text2 = ''.join(chr(int(binary_value, 2)) for binary_value in binary_values)
        print(text2)

    if consol == "guess":
        print("Вы должны угадать число от 0 до 100")
        number3 = int(random.randint(0, 100))
        win = 1
        counter = 0
        while win == 1:
            number4 = int(input())
            counter += 1
            if number4 > number3:
                print("Больше загаданного числа")
            elif number4 < number3:
                print("Меньше загаданного числа")
            elif number4 == number3:
                print(f"Вы угадали за {counter} попыток")
                win += 1
    
    if consol == "tic-tac toe":
        tic1 = '###'
        tic2 = '###'
        tic3 = '###'
        win2 = 1
        move = 'x'
        player = input('За кого будете играть? х, o\n')

        def check_win(tic1, tic2, tic3):
            if tic1[0] == tic1[1] == tic1[2] != '#':
                return tic1[0]
            if tic2[0] == tic2[1] == tic2[2] != '#':
                return tic2[0]
            if tic3[0] == tic3[1] == tic3[2] != '#':
                return tic3[0]
            
            if tic1[0] == tic2[0] == tic3[0] != '#':
                return tic1[0]
            if tic1[1] == tic2[1] == tic3[1] != '#':
                return tic1[1]
            if tic1[2] == tic2[2] == tic3[2] != '#':
                return tic1[2]
            
            if tic1[0] == tic2[1] == tic3[2] != '#':
                return tic1[0]
            if tic1[2] == tic2[1] == tic3[0] != '#':
                return tic1[2]
            
            return None

        while win2 == 1:
            print(f'{tic1}\n{tic2}\n{tic3}')
            tic_tac = int(input(f"Введите какую клетку изменить на {player} (1-9)\n"))

            if 1 <= tic_tac <= 3:
                if tic1[tic_tac - 1] != '#':
                    print("Эта клетка уже занята! Выберите другую.")
                    continue
                tic1 = tic1[:tic_tac - 1] + player + tic1[tic_tac:]
            elif 4 <= tic_tac <= 6:
                if tic2[tic_tac - 4] != '#':
                    print("Эта клетка уже занята! Выберите другую.")
                    continue
                tic2 = tic2[:tic_tac - 4] + player + tic2[tic_tac - 3:]
            elif 7 <= tic_tac <= 9:
                if tic3[tic_tac - 7] != '#':
                    print("Эта клетка уже занята! Выберите другую.")
                    continue
                tic3 = tic3[:tic_tac - 7] + player + tic3[tic_tac - 6:]
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")
                continue

            winner = check_win(tic1, tic2, tic3)
            if winner:
                print(f'{tic1}\n{tic2}\n{tic3}')
                if winner == player:
                    print(f"Поздравляю! Игрок {player} выиграл!")
                else:
                    print(f"Игрок {player} проиграл!")
                win = 0
                break


            player = 'x' if player == 'o' else 'o'

    if consol == "rock paper scissors":
        choices = ["камень", "ножницы", "бумага"]
        while 1:
            user_choice = input("Выбери: камень, ножницы или бумага (или 'выход' для завершения): ").lower()
            if user_choice == "выход":
                break
            if user_choice not in choices:
                print("Неверный выбор!")
                continue

            computer_choice = random.choice(choices)
            print(f"Компьютер выбрал: {computer_choice}")

            if user_choice == computer_choice:
                print("Ничья!")
            elif (user_choice == "камень" and computer_choice == "ножницы") or \
                (user_choice == "ножницы" and computer_choice == "бумага") or \
                (user_choice == "бумага" and computer_choice == "камень"):
                print("Ты выиграл!")
            else:
                print("Ты проиграл!")

    if consol == "math simulator":
        complexity = input("Введите сложность легкий, сложный\n")
        def generate_question():
            if complexity == "легкий":
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
                operator = random.choice(["+", "-", "*"])
                question = f"{num1} {operator} {num2}"
                answer = eval(question)
                return question, answer
            if complexity == "сложный":
                num1 = random.randint(1, 1000)
                num2 = random.randint(1, 1000)
                operator = random.choice(["+", "-", "*"])
                question = f"{num1} {operator} {num2}"
                answer = eval(question)
                return question, answer

        score = 0

        for _ in range(5):
            question, answer = generate_question()
            user_answer = int(input(f"Сколько будет {question}? "))
            if user_answer == answer:
                print("Правильно!")
                score += 1
            else:
                print("Неправильно!")

        print(f"Твой результат: {score} из 5")
    
    if consol == "gallows":
        words = ['Август', 'Алмаз', 'Алфавит', 'Апрель', 'Арбуз', 'Аристократ', 'Атласный', 'Банан', 'Барабан', 'Батон', 'Берлога', 'Бодаться', 'Болото', 'Борьба', 'Босиком', 'Ботинки', 'Ботинок', 'Брелок', 'Будто', 'Быстро', 'Василёк', 'Вдова', 'Вдруг', 'Великий', 'Веретено', 'Весна', 'Веснушка', 'Возврат', 'Воробей', 'Ворона', 'Ворох', 'Воскресенье', 'Всего', 'Выбор', 'Выгода', 'Высоко', 'Герань', 'Главарь', 'Глобус', 'Год', 'Гнать', 'Город', 'Госпиталь', 'Государыня', 'Гроза', 'Девочка', 'Девять', 'Дерево', 'Диковинный', 'Дремать', 'Друг', 'Европа', 'Ежевика', 'Ёж', 'Жар-птица', 'Женитьба', 'Живой', 'Жилет', 'Забор', 'Загадка', 'Задача', 'Закон', 'Закорючка', 'Замок', 'Запад', 'Заря', 'Зашёл', 'Звонишь', 'Звонят', 'Зеркало', 'Зима', 'Зола', 'Изюм', 'Иней', 'Иногда', 'Ирис', 'Искусно', 'Истина', 'Кабина', 'Какао', 'Каланча', 'Калина', 'Камыш', 'Канарейка', 'Капель', 'Капитан', 'Капот', 'Капуста', 'Карандаш', 'Карман', 'Картон', 'Кастрюля', 'Каток', 'Кафе', 'Кипит', 'Классный', 'Клеить', 'Ковёр', 'Ковшик', 'Колдун', 'Колено', 'Колея', 'Колокольчик', 'Конструктор', 'Контрольная', 'Конфорка', 'Коньки', 'Копейка', 'Копыто', 'Копытце', 'Корабли', 'Королева', 'Косатка', 'Который', 'Кофе', 'Красная площадь', 'Красота', 'Креветка', 'Кремль', 'Крокодил', 'Кроссовки', 'Ландыш', 'Ластик', 'Ласточка', 'Лаять', 'Лепесток', 'Либо', 'Ливень', 'Лимон', 'Линия', 'Лисица', 'Лопата', 'Льёт', 'Лягушка', 'Макароны', 'Мальчик', 'Мармелад', 'Мебель', 'Медведица', 'Мелькает', 'Месяц', 'Метр', 'Мистика', 'Молодой', 'Молоко', 'Монета', 'Морковь', 'Мороженое', 'Москва', 'Мочалка', 'Мужчина', 'Муравей', 'Мыло', 'Мясник', 'Навсегда', 'Надолго', 'Наоборот', 'Например', 'Насос', 'Нашёл', 'Небеса', 'Неделя', 'Незабудка', 'Несколько', 'Ноябрь', 'Облако', 'Обложка', 'Обман', 'Обратно', 'Овраг', 'Овчарка', 'Одуванчик', 'Озорной', 'Опять', 'Орешник', 'Осина', 'Основа', 'Особый', 'Ответ', 'Отец', 'Охота', 'Очень', 'Пальто', 'Песенка', 'Петух', 'Пирог', 'Поднос', 'Полёт', 'Полог', 'Поляна', 'Посуда', 'Потеха', 'Поэт', 'Ребята', 'Рисунок', 'Ронять', 'Россия', 'Рукавицы', 'Сентябрь', 'Синица', 'Собака', 'Согласие', 'Солнце', 'Сорока', 'Съёмка', 'Такой', 'Тарелка', 'Телёнок', 'Томат', 'Тоска', 'Узел', 'Упражнение', 'Учебник', 'Учитель', 'Учительница', 'Февраль', 'Фломастер', 'Хозяин', 'Холод', 'Холодный', 'Хотеть', 'Цинга', 'Цирк', 'Чаепитие', 'Человек', 'Через', 'Черёмуха', 'Черника', 'Чеснок', 'Чирикает', 'Что', 'Чучело', 'Чуять', 'Шалун', 'Шёл', 'Шёлк', 'Щегол', 'Щенок', 'Электричка', 'Яйцо', 'Якорь', 'Ястреб', 'Ящерица']
        word = random.choice(words)
        guessed = "_" * len(word)
        word = list(word)
        guessed = list(guessed)
        attempts = 6

        while attempts > 0 and "_" in guessed:
            print(" ".join(guessed))
            letter = input("Введи букву: ").lower()
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        guessed[i] = letter
            else:
                attempts -= 1
                print(f"Неверно! Осталось попыток: {attempts}")

        if "_" not in guessed:
            print("Поздравляю! Ты угадал слово: ", "".join(guessed))
        else:
            print("Ты проиграл! Загаданное слово было: ", "".join(word))

    if consol == "sudoku":
        def print_board(board):
            for i in range(9):
                for j in range(9):
                    if j == 8:
                        print(board[i][j])
                    else:
                        print(board[i][j], end=" ")

        def check_valid(board, row, col, num):
            for x in range(9):
                if board[row][x] == num:
                    return False
            
            for x in range(9):
                if board[x][col] == num:
                    return False
            
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[i + start_row][j + start_col] == num:
                        return False
            
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0: 
                        for num in range(1, 10):
                            if check_valid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = 0 
                        return False
            return True

        def sudoku():
            board = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
            
            print_board(board)
            
            while True:
                user_input = input("\nВведите строку, столбец и цифру (например, 1 1 5) или 'выход' для выхода: ").strip().lower()
                
                if user_input == 'выход':
                    break
                
                try:
                    row, col, num = map(int, user_input.split())
                    row -= 1  
                    col -= 1

                    if board[row][col] != 0:
                        print("Эта клетка уже заполнена!")
                    elif check_valid(board, row, col, num):
                        board[row][col] = num
                        print("\nОтлично! Обновлённое поле:")
                        print_board(board)
                    else:
                        print("Неверный ход! Попробуйте снова.")
                except (ValueError, IndexError):
                    print("Неверный ввод. Введите строку, столбец и цифру от 1 до 9.")
                
                if all(board[i][j] != 0 for i in range(9) for j in range(9)) and solve(board):
                    print("\nВы победили!")
                    break

        if __name__ == "__main__":
            sudoku()
    
    if consol == "game of life":
        def print_board(board):
            os.system('cls' if os.name == 'nt' else 'clear')
            for row in board:
                print(' '.join(['X' if cell else '.' for cell in row]))

        def next_generation(board):
            new_board = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    alive_neighbors = 0
                    for x in range(i-1, i+2):
                        for y in range(j-1, j+2):
                            if (x >= 0 and x < len(board) and y >= 0 and y < len(board[0])) and (x != i or y != j):
                                if board[x][y]:
                                    alive_neighbors += 1
                    if board[i][j]:
                        if alive_neighbors < 2 or alive_neighbors > 3:
                            new_board[i][j] = False
                        else:
                            new_board[i][j] = True
                    else:
                        if alive_neighbors == 3:
                            new_board[i][j] = True
            return new_board

        def randomize_board(board, alive_percentage=20):
            total_cells = len(board) * len(board[0])
            alive_cells = int(total_cells * alive_percentage / 100)
            for _ in range(alive_cells):
                x = random.randint(0, len(board) - 1)
                y = random.randint(0, len(board[0]) - 1)
                board[x][y] = True
            return board

        def game_of_life():
            print("Введите размеры карты (например, 100 100): ")
            try:
                rows, cols = map(int, input().split())
                if rows < 1 or cols < 1:
                    print("Размеры карты должны быть положительными числами.")
                    return
            except ValueError:
                print("Неверный формат! Используйте два целых числа.")
                return
            
            board = [[False for _ in range(cols)] for _ in range(rows)]

            random_choice = input("Хотите ли вы случайно заполнить карту живыми клетками? (да/нет): ").strip().lower()
            if random_choice == 'да':
                board = randomize_board(board)
            
            print("Добро пожаловать в игру 'Жизнь'!")
            print("Для выхода введите 'выход'.")
            print("Для добавления клетки введите 'add X Y', где X и Y - координаты.")
            print("Для удаления клетки введите 'remove X Y', где X и Y - координаты.")
            
            while True:
                print_board(board)
                user_input = input("\nНажмите 'Enter' для следующего поколения, 'выход' для выхода или команду 'add'/'remove': ").strip().lower()

                if user_input == 'выход':
                    break
                
                if user_input.startswith('add'):
                    try:
                        _, x, y = user_input.split()
                        x, y = int(x), int(y)
                        if 0 <= x < len(board) and 0 <= y < len(board[0]):
                            board[x][y] = True
                            print(f"Живая клетка добавлена на координаты ({x}, {y}).")
                        else:
                            print("Неверные координаты!")
                    except ValueError:
                        print("Неверный формат команды! Используйте 'add X Y'.")
                
                elif user_input.startswith('remove'):
                    try:
                        _, x, y = user_input.split()
                        x, y = int(x), int(y)
                        if 0 <= x < len(board) and 0 <= y < len(board[0]):
                            board[x][y] = False
                            print(f"Живая клетка удалена с координат ({x}, {y}).")
                        else:
                            print("Неверные координаты!")
                    except ValueError:
                        print("Неверный формат команды! Используйте 'remove X Y'.")
                
                else:
                    try:
                        board = next_generation(board)
                        time.sleep(1)
                    except ValueError:
                        print("Неверный ввод. Попробуйте снова.")

        def main():
            game_of_life()

        if __name__ == "__main__":
            main()

    if consol == "wave":
        counter2 = 0
        wave = [
        """
            -      
        """,
        """
           ---     
        """,
        """
          -----    
        """,
        """
           ---     
        """,
        """
            -      
        """,
        ]

        while counter2 <= 50:
            for frame in wave:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print(frame)
                time.sleep(0.0001)
                counter2 += 1
    
    if consol == "animation":
        def clear_screen():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        def animate_file(file_name, frame_delay=0.5):
            file_path = os.path.join(directory, file_name)

            try:
                if not os.path.exists(file_path):
                    print(f"Файл '{file_name}' не найден в директории '{directory}'.")
                    return

                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                if not lines:
                    print(f"Файл '{file_name}' пустой")
                    return

                for line in lines:
                    clear_screen()
                    print(line.strip()) 
                    time.sleep(frame_delay)

            except Exception as e:
                print(f"Произошла ошибка {e}")

        if __name__ == "__main__":
            file_name = input("Введите название файла\n")
            frame_delay = float(input("Введите задержку между кадрами (в секундах)\n"))
            animate_file(file_name, frame_delay)

    if consol == "music":
        notes = {
            '1': 262,  # До
            '2': 294,  # Ре
            '3': 330,  # Ми
            '4': 349,  # Фа
            '5': 392,  # Соль
            '6': 440,  # Ля
            '7': 494,  # Си
        }

        delays = {
            '-': 0.5,   
            ' ': 1.0,   
            ',': 1.5,   
            '.': 2.0,  
        }

        def play_sound(frequency, duration=500):
            winsound.Beep(frequency, duration)

        def process_file(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                for char in content:
                    if char in notes:
                        print(f"Играем ноту: {char} ({notes[char]} Гц)")
                        play_sound(notes[char])
                    elif char in delays:
                        delay = delays[char]
                        print(f"Задержка: {delay} секунд")
                        time.sleep(delay)
                    else:
                        print(f"Неизвестный символ {char}")

            except FileNotFoundError:
                print(f"Файл '{file_path}' не найден")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        if __name__ == "__main__":
            file_name = input("Введите имя файла\n")

            file_path = os.path.join(directory, file_name)

            process_file(file_path)

    if consol == "help":
        print(" Список всех команд:\n-off - выключить компьютер\n-calc - для вычислений\n-clear - очищает консоль\n-create file - создает новый файл\n-file - позволяет изменять или читать файлы\n-show files - показывает все файлы\n-binary - переводит текст в бинарный код\n-text - переводит с бинарного кода в текст\n-guess - игра, где нужно угадать число\n-tic-tac toe - игра крестики-нолики на двоих\n-rock paper scissors - камень, ножницы, бумага\n-math simulator - математический тренажер, где твоя задача - решать примеры\n-gallows - виселица, где есть двести слов\n-sudoku - судоку\n-game of life - игра в жизнь\n-animation - позволяет анимировать файл. Введите wave для встроенной анимации\n-music - позволяет играть музыку, записанную в файл")