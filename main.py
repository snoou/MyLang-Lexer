import sys
import json
from lexer import Lexer
from my_token import TokenType


def print_pretty(tokens):
    print(f"\n{' TOKENIZATION RESULTS ':-^80}")
    print(f"{'Line':<5} {'Column':<10} {'Type':<25} {'Lexeme'}")
    print("-" * 80)

    for token in tokens:
        if token.token_type == TokenType.EOF:
            break
        print(
            f"{token.line:<5} {token.column:<10} {token.token_type.name:<25} {token.lexeme:<20}"
        )

    print("-" * 80)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, "r") as f:
        source_code = f.read()

    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    print_pretty(tokens)


if __name__ == "__main__":
    main()
