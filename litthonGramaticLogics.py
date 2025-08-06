from gramaticLitthonParser import gramaticLitthonParser
from gramaticLitthonVisitor import gramaticLitthonVisitor
from ExceptionMainClass import MainException


class LitthonLogic(gramaticLitthonVisitor):

    def __init__(self, entryProcediments='MainClass', entryParams=[]):
        self.entryProcediments = entryProcediments
        self.entryParams = entryParams
        self.procs = {}
        self.stack = []
        self.myvars = {}

    def __proc__(self, name, paramsValue):
        if len(self.procs[name]) != len(paramsValue):
            raise MainException('Error procedure: ' + self.message)

    def visitRoot(self, ctx: gramaticLitthonParser.RootContext):
        for child in ctx.getChildren():
            if isinstance(child, gramaticLitthonParser.DefinitionProcedureContext):
                self.visit(child)
        if self.entryProcediments in self.procs:
            formal_params, body = self.procs[self.entryProcediments]
            if len(formal_params) != len(self.entryParams):
                raise MainException("Error on entry parameters.")
            old = self.myvars.copy()
            for f, a in zip(formal_params, self.entryParams):
                self.myvars[f] = a
            result = self.visit(body)
            self.myvars = old
            return result
        return None

    def visitDivision(self, ctx: gramaticLitthonParser.DivisionContext):
        if ctx.DIVISIONTOKEN():
            return self.visit(ctx.expressions(0)) / self.visit(ctx.expressions(1))
        return None

    def visitSubtraction(self, ctx: gramaticLitthonParser.SubtractionContext):
        if ctx.LESSTOKEN():
            return self.visit(ctx.expressions(0)) - self.visit(ctx.expressions(1))
        return None

    def visitMore(self, ctx: gramaticLitthonParser.MoreContext):
        if ctx.PLUSTOKEN():
            left = self.visit(ctx.expressions(0))
            right = self.visit(ctx.expressions(1))
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left + right
            return str(left) + str(right)
        return None

    def visitMultiplication(self, ctx: gramaticLitthonParser.MultiplicationContext):
        if ctx.MULTTOKEN():
            return self.visit(ctx.expressions(0)) * self.visit(ctx.expressions(1))
        return None

    def visitBoolean(self, ctx: gramaticLitthonParser.BooleanContext):
        return ctx.BOOLTOKEN().getText() == '<TRUE>'

    def visitNumber(self, ctx: gramaticLitthonParser.NumberContext):
        if "." in ctx.NUMBERSREGEX().getText():
            return float(ctx.NUMBERSREGEX().getText())
        else:
            return int(ctx.NUMBERSREGEX().getText())

    def visitFindInArray(self, ctx: gramaticLitthonParser.FindInArrayContext):
        var_name = ctx.VARREGEX().getText()
        index = self.visit(ctx.expressions())
        if var_name in self.myvars and isinstance(self.myvars[var_name], list) and index < len(self.myvars[var_name]):
            return self.myvars[var_name][index]
        return None

    def visitSizing(self, ctx: gramaticLitthonParser.SizingContext):
        var_name = ctx.VARREGEX().getText()
        if var_name in self.myvars and isinstance(self.myvars[var_name], list):
            return len(self.myvars[var_name])
        return 0

    def visitIdExpr(self, ctx: gramaticLitthonParser.IdExprContext):
        return [self.visit(e) for e in ctx.expressions()]

    def visitIdVars(self, ctx: gramaticLitthonParser.IdVarsContext):
        return [v.getText() for v in ctx.VARREGEX()]

    def visitSystemInConsole(self, ctx: gramaticLitthonParser.SystemInConsoleContext):
        var_name = ctx.systemIn_().VARREGEX().getText()
        self.myvars[var_name] = input(f'{var_name} : ')
        return self.myvars[var_name]

    def visitCompare(self, ctx: gramaticLitthonParser.CompareContext):
        left = self.visit(ctx.expressions(0))
        right = self.visit(ctx.expressions(1))
        op = ctx.COMPARETOKEN().getText()
        if op == ':==:': return left == right
        if op == ':!=:': return left != right
        if op == ':>:': return left > right
        if op == ':<:': return left < right
        if op == ':>=:': return left >= right
        if op == ':<=:': return left <= right
        return None

    def visitSizeValue(self, ctx: gramaticLitthonParser.SizeValueContext):
        return self.visitSizing(ctx)

    def visitArrayType(self, ctx: gramaticLitthonParser.ArrayTypeContext):
        if ctx.VARREGEX():
            var_name = ctx.VARREGEX().getText()
            if var_name not in self.myvars:
                self.myvars[var_name] = []
            if ctx.expressions():
                index = self.visit(ctx.expressions())
                if index < len(self.myvars[var_name]):
                    return self.myvars[var_name][index]
                return None
            return self.myvars[var_name]
        elif ctx.expressions():
            size = self.visit(ctx.expressions())
            return [None] * size
        return []

    def visitPotence(self, ctx: gramaticLitthonParser.PotenceContext):
        return self.visit(ctx.expressions(0)) ** self.visit(ctx.expressions(1))

    def visitBlockCommand(self, ctx: gramaticLitthonParser.BlockCommandContext):
        return self.visit(ctx.expressions())

    def visitString(self, ctx: gramaticLitthonParser.StringContext):
        return ctx.STRINGREGEX().getText().strip('"')

    def visitVar(self, ctx: gramaticLitthonParser.VarContext):
        return self.myvars.get(ctx.VARREGEX().getText())

    def visitRemoveArray(self, ctx: gramaticLitthonParser.RemoveArrayContext):
        var_name = ctx.VARREGEX().getText()
        index = self.visit(ctx.expressions())
        if var_name in self.myvars and isinstance(self.myvars[var_name], list) and index < len(self.myvars[var_name]):
            return self.myvars[var_name].pop(index)
        return None

    def visitArrayAdd(self, ctx: gramaticLitthonParser.ArrayAddContext):
        var_name = ctx.VARREGEX().getText()
        if var_name not in self.myvars:
            self.myvars[var_name] = []
        index = self.visit(ctx.expressions(0))
        value = None
        if ctx.getChildCount() > 3 and isinstance(ctx.getChild(3), gramaticLitthonParser.ExpressionsContext):
            value = self.visit(ctx.getChild(3))
        while len(self.myvars[var_name]) <= index:
            self.myvars[var_name].append(None)

        self.myvars[var_name][index] = value
        return value

    def visitArrayRemove(self, ctx: gramaticLitthonParser.ArrayRemoveContext):
        var_name = ctx.VARREGEX().getText()
        if var_name in self.myvars and isinstance(self.myvars[var_name], list):
            index = self.visit(ctx.expressions(0))
            if index < len(self.myvars[var_name]):
                return self.myvars[var_name].pop(index)
        return None

    def visitAssumeAtributtion(self, ctx: gramaticLitthonParser.AssumeAtributtionContext):
        var_name = ctx.assume().VARREGEX().getText()
        value = self.visit(ctx.assume().expressions())
        self.myvars[var_name] = value
        return value

    def visitSystemOutConsole(self, ctx: gramaticLitthonParser.SystemOutConsoleContext):
        results = []
        for expr in ctx.systemOut_().expressions():
            result = self.visit(expr)
            results.append(str(result))
        print(' '.join(results))
        return None

    def visitSystemOut_(self, ctx: gramaticLitthonParser.SystemOut_Context):
        return [self.visit(expr) for expr in ctx.expressions()]

    def visitExpressions(self, ctx: gramaticLitthonParser.ExpressionsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return None

    def visitAddToArray(self, ctx: gramaticLitthonParser.AddToArrayContext):
        var_name = ctx.VARREGEX().getText()
        index = self.visit(ctx.expressions(0))
        value = self.visit(ctx.expressions(1)) if ctx.expressions() and len(ctx.expressions()) > 1 else None
        if var_name not in self.myvars:
            self.myvars[var_name] = []
        while len(self.myvars[var_name]) <= index:
            self.myvars[var_name].append(None)
        self.myvars[var_name][index] = value
        return value

    def visitSistemInConsole(self, ctx: gramaticLitthonParser.SystemInConsoleContext):
        var_name = ctx.VARREGEX().getText()
        self.myvars[var_name] = input(f'{var_name}:')
        return self.myvars[var_name]

    def visitWhile(self, ctx: gramaticLitthonParser.WhileContext):
        while self.visit(ctx.while_().expressions()):
            self.visit(ctx.while_().instructions())
        return None

    def visitIfLogic(self, ctx: gramaticLitthonParser.IfLogicContext):
        if self.visit(ctx.condition_().expressions()):
            return self.visit(ctx.condition_().instructions(0))
        elif ctx.condition_().ELSECONDITIONTOKEN():
            return self.visit(ctx.condition_().instructions(1))
        return None

    def visitInstructs(self, ctx: gramaticLitthonParser.InstructsContext):
        for instr in ctx.instruction():
            self.visit(instr)

    def visitDefinitionProcedure(self, ctx: gramaticLitthonParser.DefinitionProcedureContext):
        proc_name = ctx.PROCEDURESREGEX().getText()
        params = []
        if ctx.idVars():
            params = self.visit(ctx.idVars())
        self.procs[proc_name] = (params, ctx.instructions())
        return None

    def visitArrayCreation(self, ctx: gramaticLitthonParser.ArrayCreationContext):
        size = self.visit(ctx.expressions())
        return [None] * size

    def visitInvokeProperty(self, ctx: gramaticLitthonParser.InvokePropertyContext):
        invoke_ctx = ctx.invoke()
        proc_name = invoke_ctx.PROCEDURESREGEX().getText()
        if proc_name not in self.procs:
            raise MainException(f'Procedure {proc_name} not defined.')
        formal_params, body = self.procs[proc_name]
        actual_params = []
        if invoke_ctx.idExpr():
            actual_params = self.visit(invoke_ctx.idExpr())
        if len(formal_params) != len(actual_params):
            raise MainException(
                f'Error in procedure {proc_name}: expected {len(formal_params)} parameters, got {len(actual_params)}')
        old_vars = self.myvars.copy()
        for param_name, param_value in zip(formal_params, actual_params):
            self.myvars[param_name] = param_value
        result = self.visit(body)
        self.myvars = old_vars
        return result