from gramaticLitthonLexer import gramaticLitthonLexer
from gramaticLitthonParser import *
from litthonGramaticLogics import LitthonLogic
import sys
from antlr4 import *

def main():
    visitor = LitthonLogic()
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    lexer = gramaticLitthonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gramaticLitthonParser(token_stream)
    tree = parser.root()
    visitor.visit(tree)

if __name__ == "__main__":
    main()