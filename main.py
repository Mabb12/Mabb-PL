import lexer
import interpreter

if __name__ == "__main__":
    code = """
// pon
"""

    tokenizer = lexer.Token()
    interpreter = interpreter.Interpreter()
    interpreter.run(tokenizer.token(code))

