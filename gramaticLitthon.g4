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
      | add_  #AddArray
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
    | COMMENTTOKEN #COMMENTTOKEN
    ;

systemIn_:SYSTEMINTOKEN VARREGEX;
systemOut_:SYSTEMOUTTOKEN expressions*;
add_: VARREGEX ARRADDINDEXTOKEN expressions ARRTOKENRIGHTTOKEN ;
remove_: VARREGEX ARRREMOVEDINDEXTOKEN expressions ARRTOKENRIGHTTOKEN;
while_:WHILETOKEN expressions LBTOKEN instructions RBTOKEN;
condition_:CONDITIONTOKEN expressions LBTOKEN instructions RBTOKEN (ELSECONDITIONTOKEN LBTOKEN instructions RBTOKEN);
assume: VARREGEX ASSIGNTOKEN expressions;
invoke: PROCEDURESREGEX idExpr (expressions);
idVars: (VARREGEX)*;
idExpr: (expressions)*;
sizing: ARRSIZETOKEN VARREGEX;
find: VARREGEX ARRTOKENLEFTTOKEN expressions ARRTOKENRIGHTTOKEN;
array: VARREGEX ARRTOKENLEFTTOKEN expressions ARRTOKENRIGHTTOKEN;

PROCEDURESREGEX: [A-Z][a-zA-Z0-9_]*;
NUMBERSREGEX: '-'?[0-9]+('.'[0-9]+)?;
NUMINTREGEX: [0-9]+;
VARREGEX: [a-zA-Z][a-zA-Z0-9]+;
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
ARRTOKEN: '<{}>';
ARRTOKENLEFTTOKEN: '<{';
ARRTOKENRIGHTTOKEN: '}>';
ARRREMOVEDINDEXTOKEN: '<{/';
ARRADDINDEXTOKEN: '<{+';

PLUSTOKEN: '{+}';
LESSTOKEN: '{-}';
DIVISIONTOKEN: '{/}';
MULTTOKEN: '{*}';
POTTOKEN: '{^}';

ATTRIBUTIONTOKEN: ':=:';
ASSIGNTOKEN: ':<-:';
COMPARETOKEN: ':==:' | ':!=:' | ':>:' | ':<:' | ':>=:' | ':<=:';

WS : [ \n\t\r]+ -> skip;
COMMENTTOKEN: '<###>' ~[\r\n] -> skip;