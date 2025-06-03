import lexer
import interpreter

if __name__ == "__main__":
    code = """
// Здесь творец - это ты. Так твори!
"""

    tokenizer = lexer.Token()
    interpreter = interpreter.Interpreter()
    interpreter.run(tokenizer.token(code))

