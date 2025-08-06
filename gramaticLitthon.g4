grammar gramaticLitthon;

root: defaultProcediments* EOF;

defaultProcediments: PROCEDURESREGEX idVars LBTOKEN instructions RBTOKEN #DefinitionProcedure
      ;

instructions: instruction* #Instructs
      ;

instruction: condition_ #IfLogic
      | while_ #While
      | systemIn_ #SystemInConsole
      | systemOut_ #SystemOutConsole
      | assume #AssumeAtributtion
      | invoke #InvokeProperty
      | array #TypeArray
      | add_ #AddArray
      | remove_ #RemoveArray
      ;

expressions: <assoc=right> expressions POTTOKEN expressions #Potence
    | expressions MULTTOKEN expressions #Multiplication
    | expressions DIVISIONTOKEN expressions #Division
    | expressions LESSTOKEN expressions #Subtraction
    | expressions PLUSTOKEN expressions #More
    | expressions COMPARETOKEN expressions #Compare
    | VARREGEX #Var
    | BOOLTOKEN #Boolean
    | NUMBERSREGEX #Number
    | STRINGREGEX #String
    | array #ArrayType
    | sizing #SizeValue
    | find #FindInArray
    | LBTOKEN expressions RBTOKEN #BlockCommand
    ;

systemIn_: SYSTEMINTOKEN VARREGEX;
systemOut_: SYSTEMOUTTOKEN expressions*;
array:
    VARREGEX ARRTOKENLEFTTOKEN expressions ARRTOKENRIGHTTOKEN #ArrayAccess
    | ARRTOKENLEFTTOKEN expressions ARRTOKENRIGHTTOKEN #ArrayCreation
    | VARREGEX ARRADDINDEXTOKEN expressions ARRTOKENRIGHTTOKEN #ArrayAdd
    | VARREGEX ARRREMOVEDINDEXTOKEN expressions ARRTOKENRIGHTTOKEN #ArrayRemove;
add_: VARREGEX ARRADDINDEXTOKEN expressions ARRTOKENRIGHTTOKEN #AddToArray;
remove_: VARREGEX ARRREMOVEDINDEXTOKEN expressions ARRTOKENRIGHTTOKEN #RemoveFromArray;
while_: WHILETOKEN expressions LBTOKEN instructions RBTOKEN;
condition_: CONDITIONTOKEN expressions LBTOKEN instructions RBTOKEN (ELSECONDITIONTOKEN LBTOKEN instructions RBTOKEN)?;
assume: VARREGEX ASSIGNTOKEN expressions;
invoke: PROCEDURESREGEX idExpr;
idVars: (VARREGEX)*;
idExpr: (expressions)*;
sizing: ARRSIZETOKEN VARREGEX;
find: VARREGEX ARRTOKENLEFTTOKEN expressions ARRTOKENRIGHTTOKEN;

PROCEDURESREGEX: [A-Z][a-zA-Z0-9_]*;
NUMBERSREGEX: '-'?[0-9]+('.'[0-9]+)?;
VARREGEX: [a-zA-Z][a-zA-Z0-9]*;
STRINGREGEX: '"' ('\\' . | ~('\\' | '"'))* '"';

SYSTEMOUTTOKEN: '<L:O:G:L:O:G>';
CONDITIONTOKEN: '<C:A:S:E:>';
ELSECONDITIONTOKEN: '<E:L:S:E>';
WHILETOKEN: '<W:H:I:L:S:T>';
ARRSIZETOKEN: '{L:E:N:G:H:T>/';
BOOLTOKEN: '<TRUE>' | '<FALSE>';

SYSTEMINTOKEN: '<?>';
LBTOKEN: '<{>';
RBTOKEN: '<}>';
ARRTOKENLEFTTOKEN: '<{';
ARRTOKENRIGHTTOKEN: '}>';
ARRREMOVEDINDEXTOKEN: '<{/';
ARRADDINDEXTOKEN: '<{+';

PLUSTOKEN: '{+}';
LESSTOKEN: '{-}';
DIVISIONTOKEN: '{/}';
MULTTOKEN: '{*}';
POTTOKEN: '{^}';

ASSIGNTOKEN: ':<-:';
COMPARETOKEN: ':==:' | ':!=:' | ':>:' | ':<:' | ':>=:' | ':<=:';

COMMENTTOKEN: '<###>' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;