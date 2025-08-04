from gramaticLitthonLexer import gramaticLitthonLexer
from gramaticLitthonParser import *
from litthonGramaticLogics import LitthonLogic
import sys

def main():
    visitor = LitthonLogic()  # Cria uma única instância
    input_stream = FileStream(sys.argv[1])
    lexer = gramaticLitthonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gramaticLitthonParser(token_stream)
    tree = parser.root()
    visitor.visit(tree)

if __name__ == "__main__":
    main()