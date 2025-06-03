class Token:
    def __init__(self):
        self.keywords = {"_PRINT", "_EXECUTE", "_IF", "_ENDIF", "_VAR", "_NUMBER", "_TEXT", "_INPUT", "_END", "_OPERATION", "_LABEL", "_CALL", "_ENDLABEL", "_LENGTH", "_TAKE", "_ARRAY"}
        self.operations = {"-", "+", "/", "*"}
        self.comparison_op = {"<", ">", "_IN"}
        self.count = 0
        self.tokens = []

    def string(self):
        start = self.count + 1
        end = self.code.find("'", start)
        if end == -1:
            end = self.len_code
        self.tokens.append(('STRING', self.code[start:end]))
        self.count = end + 1

    def number(self):
        start = self.count
        while self.count < self.len_code and self.code[self.count].isdigit():
            self.count += 1
        if start != self.count:
            self.tokens.append(('NUMBER', int(self.code[start:self.count])))

    def assign(self):
        """Метод для добавления присваивания"""
        self.tokens.append(('ASSIGN', self.code[self.count]))
        self.count += 1

    def id(self):
        """Метод для добавления названия переменной"""
        start = self.count
        while self.count < self.len_code and self.code[self.count] != " " and self.code[self.count] != "\n":
            self.count += 1
        identifier = self.code[start:self.count]
        self.tokens.append(('ID', identifier))

    def command(self):
        """Метод для добавления команды или же ключевых слов"""
        start = self.count
        while self.count < self.len_code and self.code[self.count] != " " and self.code[self.count] != "\n":
            self.count += 1
        word = self.code[start:self.count]
        if word in self.keywords:
            self.tokens.append(("KEYWORD", word))
        else:
            self.count = start
            self.id()

    def operation(self):
        """Метод для добавления арифметической операции"""
        self.tokens.append(("OP", self.code[self.count]))
        self.count += 1

    def new_line(self):
        """Метод для добавления новой строки"""
        self.tokens.append(("NEWLINE", "\n"))
        self.count += 1

    def skip_whitespace(self):
        self.count += 1

    def compare(self):
        """Метод для добавления операции сравнения"""
        self.tokens.append(("COMPARE", self.code[self.count]))
        self.count += 1

    def token(self, code: str):
        """Метод для добавления в список токенов токены"""
        self.code = code
        self.len_code = len(self.code)

        while self.count < self.len_code:
            symbol = self.code[self.count]

            if self.count + 1 < self.len_code:
                two_char = self.code[self.count] + self.code[self.count + 1]
                if two_char in ('==', '!='):
                    self.tokens.append(('COMPARE', two_char))
                    self.count += 2
                    continue
                if two_char == '//':
                    self.tokens.append(('//', two_char))
                    self.count += 2
                    continue
                if two_char == '**':
                    self.tokens.append(('OP', two_char))
                    self.count += 2
                    continue

            if symbol == "'":
                self.string()
                continue
            elif symbol == "\n" or symbol == "#":
                self.new_line()
                continue
            elif symbol in self.comparison_op:
                self.tokens.append(('COMPARE', symbol))
                self.count += 1
                continue
            elif symbol == "=":
                self.assign()
                continue
            elif symbol.isdigit():
                self.number()
                continue
            elif symbol == "_" or symbol.isalpha():
                self.command()
                continue
            elif symbol in self.operations:
                self.operation()
                continue
            elif symbol == " ":
                self.skip_whitespace()
                continue
            else:
                self.count += 1

        return self.tokens
