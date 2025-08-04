from gramaticLitthonParser import gramaticLitthonParser
from gramaticLitthonVisitor import gramaticLitthonVisitor
from ExceptionMainClass import MainException

class LitthonLogic(gramaticLitthonVisitor):

    def __init__(self, entryProcediments = 'MainClass', entryParams = []):
        self.entryProcediments = entryProcediments
        self.entryParams = entryParams
        self.procs = {}
        self.stack = []
        self.myvars = {}

    def __proc__(self, name, paramsValue):
        if len(self.procs[name])!= len(paramsValue):
            raise MainException('Error procedure: ' + self.message)

    def visitRoot(self, ctx: gramaticLitthonParser.RootContext):
        for child in ctx.getChildren():
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
            return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))
        return None

    def visitSubtraction(self, ctx: gramaticLitthonParser.SubtractionContext):
        if ctx.LESSTOKEN():
            return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))
        return None

    def visitMore(self, ctx: gramaticLitthonParser.MoreContext):
        if ctx.PLUSTOKEN():
            if isinstance(self.visit(ctx.expr(0)), int) and isinstance(self.visit(ctx.expr(1)), int):
                return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))
            if isinstance(self.visit(ctx.expr(0)), str) and isinstance(self.visit(ctx.expr(1)), str):
                return str(self.visit(ctx.expr(0))) + str(self.visit(ctx.expr(1)))
        return None

    def visitMultiplication(self, ctx: gramaticLitthonParser.MultiplicationContext):
        if ctx.MULTTOKEN():
            return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))
        return None

    def visitCOMMENTTOKEN(self, ctx: gramaticLitthonParser.COMMENTTOKENContext):
        return None

    def visitBoolean(self, ctx: gramaticLitthonParser.BooleanContext):
        return ctx.BOOLTOKEN().getText() == '<TRUE>'

    def visitNumber(self, ctx: gramaticLitthonParser.NumberContext):
        return int(ctx.NUMBERSREGEX().getText())

    def visitFind(self, ctx: gramaticLitthonParser.FindContext):
        return self.myvars.get(ctx.VARREGEX().getText(), [])[self.visit(ctx.expressions())]

    def visitSizing(self, ctx: gramaticLitthonParser.SizingContext):
        return len(self.myvars.get(ctx.VARREGEX().getText(), []))

    def visitIdExpr(self, ctx: gramaticLitthonParser.IdExprContext):
        return [self.visit(e) for e in ctx.expressions()]

    def visitIdVars(self, ctx: gramaticLitthonParser.IdVarsContext):
        return [v.getText() for v in ctx.VARREGEX()]

    def visitSystemInConsole(self, ctx:gramaticLitthonParser.SystemIn_Context):
        self.myvars[ctx.VARREGEX().getText()] = input(f'{ctx.VARREGEX().getText()} : ')
        return ctx.VARREGEX().getText()

    def visitCompare(self, ctx: gramaticLitthonParser.CompareContext):
        if ctx.COMPARETOKEN().getText() == ':==:': return self.visit(ctx.expressions(0)) == self.visit(ctx.expressions(1))
        if ctx.COMPARETOKEN().getText() == ':!=:': return self.visit(ctx.expressions(0)) != self.visit(ctx.expressions(1))
        if ctx.COMPARETOKEN().getText() == ':>:': return self.visit(ctx.expressions(0)) > self.visit(ctx.expressions(1))
        if ctx.COMPARETOKEN().getText() == ':<:': return self.visit(ctx.expressions(0)) < self.visit(ctx.expressions(1))
        if ctx.COMPARETOKEN().getText() == ':>=:': return self.visit(ctx.expressions(0)) >= self.visit(ctx.expressions(1))
        if ctx.COMPARETOKEN().getText() == ':<=:': return self.visit(ctx.expressions(0)) <= self.visit(ctx.expressions(1))
        return None

    def visitSizeValue(self, ctx: gramaticLitthonParser.SizeValueContext):
        return self.visitSizing(ctx)

    def visitFindInArray(self, ctx: gramaticLitthonParser.FindInArrayContext):
        return self.visitFind(ctx)

    def visitArrayType(self, ctx: gramaticLitthonParser.ArrayTypeContext):
        return self.visitArray(ctx)

    def visitPotence(self, ctx: gramaticLitthonParser.PotenceContext):
        return self.visit(ctx.expressions(0)) ** self.visit(ctx.expressions(1))

    def visitBlockCommand(self, ctx: gramaticLitthonParser.BlockCommandContext):
        return self.visit(ctx.expressions())

    def visitString(self, ctx: gramaticLitthonParser.StringContext):
        return ctx.STRINGREGEX().getText().strip('"')

    def visitVar(self, ctx: gramaticLitthonParser.VarContext):
        return self.myvars.get(ctx.VARREGEX().getText())

    def visitRemoveArray(self, ctx: gramaticLitthonParser.RemoveArrayContext):
        if ctx.VARREGEX().getText() in self.myvars and len(self.myvars[ctx.VARREGEX().getText()]) > self.visit(ctx.expressions()):
            self.myvars[ctx.VARREGEX().getText()].pop(self.visit(ctx.expressions()))

    def visitAddArray(self, ctx: gramaticLitthonParser.AddArrayContext):
        if ctx.VARREGEX().getText() not in self.myvars:
            self.myvars[ctx.VARREGEX().getText()] = []
        self.myvars[ctx.VARREGEX().getText()].insert(self.visit(ctx.expressions()), None)

    def visitTypeArray(self, ctx: gramaticLitthonParser.TypeArrayContext):
        if ctx.VARREGEX().getText() not in self.myvars:
            self.myvars[ctx.VARREGEX().getText()] = []
        arr = self.myvars[ctx.VARREGEX().getText()]
        if len(arr) <= self.visit(ctx.expressions()):
            arr.extend([None] * (self.visit(ctx.expressions()) - len(arr) + 1))
        return arr

    def visitAssumeAtributtion(self, ctx: gramaticLitthonParser.AssumeAtributtionContext):
        self.myvars[ctx.VARREGEX().getText()] = self.visit(ctx.assume())
        if isinstance(self.visit(ctx.assume()), int):
            return int(self.visit(ctx.assume()))
        else:
            return self.visit(ctx.expr())

    def visitSystemOutConsole(self, ctx: gramaticLitthonParser.SystemOutConsoleContext):
        return self.visit(ctx.systemOut_())

    def visitSistemInConsole(self, ctx: gramaticLitthonParser.SystemInConsoleContext):
        self.myvars[ctx.VARREGEX().getText()] = input(f'{ctx.VARREGEX().getText()}:')
        return input(f'{ctx.VARREGEX().getText()}:')

    def visitWhile(self, ctx: gramaticLitthonParser.WhileContext):
        while self.visit(ctx.expressions()):
            self.visit(ctx.instructions())
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
        self.procs[ctx.PROCEDURESREGEX().getText()] = (self.visit(ctx.idVars()), ctx.instructions())

    def visitInvokeProperty(self, ctx: gramaticLitthonParser.InvokePropertyContext):
        if ctx.PROCEDURESREGEX().getText() not in self.procs:
            raise MainException(f'Procedure {ctx.PROCEDURESREGEX().getText()} not defined.')
        formal_params, body = self.procs[ctx.PROCEDURESREGEX().getText()]

        if len(formal_params) != len(self.visit(ctx.idExpr())):
            raise MainException('Error procedure: wrong number of params.')

        old_vars = self.myvars.copy()
        for f, a in zip(formal_params, self.visit(ctx.idExpr())):
            self.myvars[f] = a

        result = self.visit(body)
        self.myvars = old_vars
        return result