from my_token import Token, TokenType
from utils import is_keyword, is_letter_or_underscore, is_digit, is_whitespace_char

class Lexer:
    def __init__(self, input_text: str):
        self.input = list(input_text)
        self.position = 0
        self.read_position = 0
        self.ch = "\0"
        self.line = 1
        self.column = 0
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = "\0"
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1
        self.column += 1

    def peek_char(self):
        if self.read_position >= len(self.input):
            return "\0"
        return self.input[self.read_position]

    def skip_whitespace(self):
        while is_whitespace_char(self.ch):
            if self.ch == "\n":
                self.line += 1
                self.column = 0
            self.read_char()

    def read_number(self):
        start_pos = self.position
        start_col = self.column
        while is_digit(self.ch):
            self.read_char()
        lexeme = "".join(self.input[start_pos : self.position])
        return Token(TokenType.NUM_LITERAL, lexeme, self.line, start_col, int(lexeme))

    def read_string(self):
        start_col = self.column
        self.read_char()
        start_pos = self.position
        while self.ch != '"' and self.ch != "\0":
            self.read_char()

        if self.ch == "\0":
            return Token(
                TokenType.ERROR, "", self.line, start_col, "Unterminated string"
            )

        lexeme = "".join(self.input[start_pos : self.position])
        self.read_char()
        return Token(
            TokenType.STRING_LITERAL, f'"{lexeme}"', self.line, start_col, lexeme
        )

    def read_identifier(self):
        start_pos = self.position
        start_col = self.column
        while is_letter_or_underscore(self.ch) or is_digit(self.ch):
            self.read_char()
        lexeme = "".join(self.input[start_pos : self.position])
        if is_keyword(lexeme):
            return Token(TokenType[lexeme.upper()], lexeme, self.line, start_col)
        return Token(TokenType.IDENTIFIER, lexeme, self.line, start_col)

    def next_token(self):
        self.skip_whitespace()
        tok_col = self.column

        if self.ch == "\0":
            return Token(TokenType.EOF, "", self.line, tok_col)

        if self.ch == '"':
            return self.read_string()

        if is_digit(self.ch):
            return self.read_number()

        if is_letter_or_underscore(self.ch):
            return self.read_identifier()

        if self.ch in ["+", "-", "*", "/", "^"]:
            mapping = {
                "+": TokenType.PLUS,
                "-": TokenType.MINUS,
                "*": TokenType.MULTIPLY,
                "/": TokenType.DIVIDE,
                "^": TokenType.POWER,
            }
            tok = Token(mapping[self.ch], self.ch, self.line, tok_col)
            self.read_char()
            return tok

        if self.ch in ["<", ">", "="]:
            cur = self.ch
            if cur == "<" and self.peek_char() == ">":
                self.read_char()
                self.read_char()
                return Token(TokenType.NOT_EQUAL, "<>", self.line, tok_col)
            elif self.peek_char() == "=":
                self.read_char()
                lexeme = cur + "="
                type_map = {
                    "<=": TokenType.LESS_EQUAL,
                    ">=": TokenType.GREATER_EQUAL,
                    "=": TokenType.EQUAL,
                }
                self.read_char()
                return Token(
                    type_map.get(lexeme, TokenType.EQUAL), lexeme, self.line, tok_col
                )
            else:
                type_map = {
                    "<": TokenType.LESS,
                    ">": TokenType.GREATER,
                    "=": TokenType.EQUAL,
                }
                self.read_char()
                return Token(type_map[cur], cur, self.line, tok_col)

        single_char = {
            "(": TokenType.LPAREN,
            ")": TokenType.RPAREN,
            "[": TokenType.LBRACKET,
            "]": TokenType.RBRACKET,
            "{": TokenType.LBRACE,
            "}": TokenType.RBRACE,
            ",": TokenType.COMMA,
            ";": TokenType.SEMICOLON,
            ":": TokenType.COLON,
            ".": TokenType.DOT,
        }

        if self.ch in single_char:
            tok = Token(single_char[self.ch], self.ch, self.line, tok_col)
            self.read_char()
            return tok

        tok = Token(
            TokenType.ERROR,
            self.ch,
            self.line,
            tok_col,
            f"Unexpected character '{self.ch}'",
        )
        self.read_char()
        return tok

    def tokenize(self):
        tokens = []
        while True:
            token = self.next_token()
            tokens.append(token)
            if token.token_type == TokenType.EOF:
                break
        return tokens
