class Interpreter:
    def __init__(self):
        self.pc = 0
        self.variables = {}
        self.call_stack = []
        self.len_tokens = 0
        self.tokens = []
        self.labels = {}
        self.operations = ['_TAKE', '_LENGTH', '-', '+', '*', '/', '**']
        self.call = 0

    def _print(self):
        output = []
        self.pc += 1
        while self.pc < self.len_tokens:
            token_type, token_value = self.tokens[self.pc]
            if token_type == 'NEWLINE':
                break
            if token_type == 'ID':
                if token_value in self.variables:
                    var_value = ''.join(self.variables[token_value])
                    output.append(str(var_value))
                else:
                    raise NameError(f"Неизвестная переменная '{token_value}'")
            else:
                output.append(str(token_value))
            self.pc += 1
        print(' '.join(output))
        self.pc += 1

    def _var(self):
        self.pc += 1
        var_type = self.tokens[self.pc][1]
        self.pc += 1
        var_name = self.tokens[self.pc][1]
        self.pc += 1

        if self.tokens[self.pc][0] == 'ASSIGN':
            self.pc += 1

            token_type, token_value = self.tokens[self.pc]
            if var_type == '_TEXT':
                if token_type == 'ID':
                    if token_value in self.variables:
                        value = self.variables[token_value]
                    else:
                        raise NameError(f"Неизвестная переменная '{token_value}'")
                else:
                    value = token_value
                self.pc += 1

            elif var_type == '_NUMBER':
                if token_type == 'ID':
                    if token_value in self.variables:
                        value = int(self.variables[token_value])
                    else:
                        raise NameError(f"Неизвестная переменная '{token_value}'")
                else:
                    if token_value == "-":
                        self.pc += 1
                        token_type, token_value = self.tokens[self.pc]
                        value = -int(token_value)
                    else:
                        value = int(token_value)
                self.pc += 1

            elif var_type == '_INPUT':
                if token_type == 'ID':
                    if token_value in self.variables:
                        question = self.variables[token_value]
                    else:
                        raise NameError(f"Неизвестная переменная '{token_value}'")
                else:
                    question = token_value
                value = input(question)
                self.pc += 1

            elif var_type == "_ARRAY":
                value = []
                while self.pc < self.len_tokens:
                    token_type, token_value = self.tokens[self.pc]
                    if token_type == 'NEWLINE':
                        break
                    elif token_type == 'ID':
                        if token_value in self.variables:
                            value.append(self.variables[token_value])
                        else:
                            raise NameError(f"Неизвестная переменная '{token_value}'")
                    elif token_type in ('NUMBER', 'STRING'):
                        try:
                            value.append(int(token_value))
                        except ValueError:
                            value.append(token_value)
                    self.pc += 1
            else:
                raise SyntaxError(f"Неизвестный тип переменной '{var_type}'")

            self.variables[var_name] = value
            self.pc += 1
        else:
            raise SyntaxError(f"Нет знака присвоения '='")

    def _execute(self):
        self.pc += 1
        token, number = self.tokens[self.pc]
        count = 0
        if token == "ID":
            number = self.variables[number]
        number = int(number) - 2

        self.pc = 0
        while self.pc < self.len_tokens:
            token, word = self.tokens[self.pc]
            if count > number:
                break
            elif token == 'NEWLINE':
                count += 1
            self.pc += 1

    def _operation(self):
        self.pc += 1
        token, variable = self.tokens[self.pc]
        self.pc += 1
        if self.pc < self.len_tokens and self.tokens[self.pc][0] == 'ASSIGN':
            self.pc += 1

        elements = []
        while self.pc < self.len_tokens:
            token_type, token_value = self.tokens[self.pc]
            if token_type == 'NEWLINE':
                break

            if token_type == 'KEYWORD' and token_value == '_LENGTH':
                self.pc += 1
                next_token_type, next_token_value = self.tokens[self.pc]
                if next_token_type == 'ID':
                    if next_token_value in self.variables:
                        value = str(self.variables[next_token_value])
                        elements.append(len(value))
                    else:
                        raise NameError(f"Неизвестная переменная '{next_token_value}'")
                elif next_token_type == 'STRING':
                    elements.append(len(next_token_value))
                else:
                    raise SyntaxError("_LENGTH требует строку или строковую переменную")
                self.pc += 1
                continue

            if token_type == 'ID':
                if token_value in self.variables:
                    value = self.variables[token_value]
                    try:
                        value = int(value)
                    except (ValueError, TypeError):
                        pass
                    elements.append(value)
                else:
                    raise NameError(f"Неизвестная переменная '{token_value}'")
            elif token_type in ('NUMBER', 'STRING'):
                elements.append(token_value)
            elif token_type == 'OP' or token_value in self.operations:
                elements.append(token_value)

            self.pc += 1

        if not elements:
            raise SyntaxError("Неверный формат операции")

        if len(elements) == 1:
            self.variables[variable] = elements[0]
            self.pc += 1
            return

        if len(elements) < 3 or len(elements) % 2 == 0:
            raise SyntaxError("Неверный формат операции")

        result = elements[0]
        for i in range(1, len(elements), 2):
            operation = elements[i]
            next_value = elements[i + 1]

            if operation == "+":
                if isinstance(result, list):
                    if isinstance(next_value, list):
                        result.extend(next_value)
                    else:
                        result.append(next_value)
                else:
                    result += next_value
            elif operation == "-":
                if isinstance(result, list):
                    if isinstance(next_value, list):
                        result = [item for item in result if item not in next_value]
                    else:
                        try:
                            result.remove(next_value)
                        except ValueError:
                            pass
                else:
                    try:
                        result -= next_value
                    except TypeError:
                        result = str(result).replace(str(next_value), "", 1)
            elif operation == "*":
                result *= next_value
            elif operation == "/":
                if isinstance(result, list):
                    if isinstance(next_value, list):
                        result = [item for item in result if item not in next_value]
                    else:
                        try:
                            while next_value in result:
                                result.remove(next_value)
                        except ValueError:
                            pass
                else:
                    try:
                        result /= next_value
                    except TypeError:
                        result = str(result).replace(str(next_value), "")
            elif operation == "_TAKE":
                result = elements[i - 1][next_value]
            elif operation == "**":
                result **= int(next_value)
            else:
                raise SyntaxError(f"Неизвестная операция '{operation}'")

        self.variables[variable] = result
        self.pc += 1

    def _if(self):
        self.pc += 1
        token_type1, arg1 = self.tokens[self.pc]
        left_value = self.variables[arg1] if token_type1 == 'ID' else arg1

        self.pc += 1
        token_type2, compare_op = self.tokens[self.pc]
        self.pc += 1
        token_type3, arg2 = self.tokens[self.pc]
        right_value = self.variables[arg2] if token_type3 == 'ID' else arg2

        if compare_op in ('<', '>'):
            try:
                left_value = float(left_value)
                right_value = float(right_value)
            except ValueError:
                pass

        condition_met = {
            "==": lambda: str(left_value) == str(right_value),
            "!=": lambda: str(left_value) != str(right_value),
            "<": lambda: left_value < right_value,
            ">": lambda: left_value > right_value,
            "_IN": lambda: str(left_value) in str(right_value)
        }.get(compare_op, lambda: False)()

        if not condition_met:
            nesting_level = 1
            while self.pc < self.len_tokens:
                self.pc += 1
                token_type, token_value = self.tokens[self.pc]
                if token_type == 'KEYWORD':
                    if token_value == '_IF':
                        nesting_level += 1
                    elif token_value == '_ENDIF':
                        nesting_level -= 1
                        if nesting_level == 0:
                            break

        self.pc += 1

    def _call(self):
        self.pc += 1
        token, name = self.tokens[self.pc]
        line_pc = self.labels[name]

        self.call = self.pc

        self.pc = line_pc

    def _label(self):
        self.pc += 1
        token, name_label = self.tokens[self.pc]
        self.pc += 1
        self.labels[name_label] = self.pc
        while self.pc < self.len_tokens:
            token, value = self.tokens[self.pc]
            if value == "_ENDLABEL":
                self.pc += 2
                break
            self.pc += 1

    def _endlabel(self):
        self.pc = self.call + 1

    def run(self, tokens: list):
        """Метод для проверки и выполнения команд"""
        self.len_tokens = len(tokens)
        self.tokens = tokens
        while self.pc < self.len_tokens:
            try:
                token_type, token_value = self.tokens[self.pc]

                if token_type == 'NEWLINE':
                    self.pc += 1
                    continue

                elif token_type == 'KEYWORD':
                    if token_value == '_PRINT':  # Команда вывода в консоль
                        self._print()
                        continue
                    elif token_value == '_VAR':  # Команда создания переменной
                        self._var()
                        continue
                    elif token_value == '_EXECUTE':  # Команда для выполнения программы с заданной строки (goto)
                        self._execute()
                        continue
                    elif token_value == '_OPERATION':  # Команда для сложения двух чисел/переменных и записи ответа в указанную переменную
                        self._operation()
                        continue
                    elif token_value == '_END':  # Команда для прекращения выполнения кода
                        break
                    elif token_value == '_IF':  # Команда для проверки, истинно ли условие
                        self._if()
                        continue
                    elif token_value == "_ENDIF": # Конец блока _IF (заглушка)
                        self.pc += 1
                        continue
                    elif token_value == "_LABEL": # Команда для создания метки
                        self._label()
                        continue
                    elif token_value == "_CALL": # Команда для перехода к метке
                        self._call()
                        continue
                    elif token_value == "_ENDLABEL": # Команда для перехода к той строке, где была вызвана его метка
                        self._endlabel()
                        continue
                    else:
                        raise SyntaxError(f"Неизвестная команда '{token_value}'")

                elif token_type == "//":
                    while self.pc < self.len_tokens:
                        token, value = self.tokens[self.pc]
                        if token == "NEWLINE":
                            break
                        self.pc += 1
                    continue

                else:
                    self.pc += 1
                    raise SyntaxError(f"Неизвестная команда '{token_value}'")

            except Exception as e:
                count_line = 0
                for i in tokens:
                    if i[0] == "NEWLINE":
                        count_line += 1
                    if i == self.tokens[self.pc]:
                        break
                print(f"\033[31m{e}. Номер строки: {count_line}\033[0m")
                return