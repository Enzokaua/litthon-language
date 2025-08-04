# Litthon - A linguagem de programação simplista

> Litthon, a linguagem de programação simplista. Esse projeto visa fixar os conhecimentos sobre ANTLR4 e interpretadores, criando uma linguagem com as funções básicas. Essa é a segunda linguagem criada para essa finalidade, centralizando os conhecimentos captados da StupidScript, módulo 3 do repositório de interpretadores.

## 💻 Pré-requisitos

Para executar este projeto, certifique-se de ter as seguintes ferramentas configuradas no seu ambiente:

- **Python 3.0.0** ou superior;
- **Antlr 4.0** ou superior;
- Editor de texto de sua escolha;


### 🚀 Estrutura gramatical

Os tokens reservados da linguagem, consistem em:
```
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
```

### 🛠️ Tecnologias Utilizadas

- **Antlr4**: Linguagem de programação principal do projeto;
- **Python**: Ferramenta de build e gerenciamento de dependências;

## 🛠️ Execução

1. Clone este repositório:
   
```bash
   git clone https://github.com/enzokaua/litthon-language
```
