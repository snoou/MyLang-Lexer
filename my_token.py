from enum import Enum, auto
from dataclasses import dataclass
from typing import Union


class TokenType(Enum):

    DIM = auto()
    READONLY = auto()
    AS = auto()
    CHAR = auto()
    INTEGER = auto()
    BOOLEAN = auto()
    DOUBLE = auto()
    REAL = auto()
    DO = auto()
    WHILE = auto()
    LOOP = auto()
    FOR = auto()
    NEXT = auto()
    TO = auto()
    RETURN = auto()
    READ = auto()
    PRINT = auto()
    STRING = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    ENDIF = auto()
    END = auto()
    FUNCTOIN = auto()
    MAIN = auto()
    PUBLIC = auto()
    SUB = auto()
    BYREF = auto()
    BYVAL = auto()
    MOD = auto()

    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    POWER = auto()
    ASSIGN = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    LESS = auto()
    GREATER = auto()
    LESS_EQUAL = auto()
    GREATER_EQUAL = auto()

    LPAREN = auto()
    RPAREN = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    LBRACE = auto()
    RBRACE = auto()
    SEMICOLON = auto()
    COMMA = auto()
    COLON = auto()
    DOT = auto()
    QUOTE = auto()

    IDENTIFIER = auto()
    NUM_LITERAL = auto()
    STRING_LITERAL = auto()

    EOF = auto()
    ERROR = auto()


@dataclass
class Token:
    token_type: TokenType
    lexeme: str
    line: int
    column: int
    value: Union[int, float, str, None] = None

    def __repr__(self):
        if self.value is not None:
            return f"Token({self.token_type.name}, '{self.lexeme}', {self.line}, {self.column}, {self.value})"
        return f"Token({self.token_type.name}, '{self.lexeme}', {self.line}, {self.column})"
