# Generated from gramaticLitthon.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .gramaticLitthonParser import gramaticLitthonParser
else:
    from gramaticLitthonParser import gramaticLitthonParser

# This class defines a complete generic visitor for a parse tree produced by gramaticLitthonParser.

class gramaticLitthonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticLitthonParser#root.
    def visitRoot(self, ctx:gramaticLitthonParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#DefinitionProcedure.
    def visitDefinitionProcedure(self, ctx:gramaticLitthonParser.DefinitionProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#Instructs.
    def visitInstructs(self, ctx:gramaticLitthonParser.InstructsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#IfLogic.
    def visitIfLogic(self, ctx:gramaticLitthonParser.IfLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#While.
    def visitWhile(self, ctx:gramaticLitthonParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#SystemInConsole.
    def visitSystemInConsole(self, ctx:gramaticLitthonParser.SystemInConsoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#SystemOutConsole.
    def visitSystemOutConsole(self, ctx:gramaticLitthonParser.SystemOutConsoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#AssumeAtributtion.
    def visitAssumeAtributtion(self, ctx:gramaticLitthonParser.AssumeAtributtionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#InvokeProperty.
    def visitInvokeProperty(self, ctx:gramaticLitthonParser.InvokePropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#TypeArray.
    def visitTypeArray(self, ctx:gramaticLitthonParser.TypeArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#AddArray.
    def visitAddArray(self, ctx:gramaticLitthonParser.AddArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#RemoveArray.
    def visitRemoveArray(self, ctx:gramaticLitthonParser.RemoveArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#Multiplication.
    def visitMultiplication(self, ctx:gramaticLitthonParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#Var.
    def visitVar(self, ctx:gramaticLitthonParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#COMMENTTOKEN.
    def visitCOMMENTTOKEN(self, ctx:gramaticLitthonParser.COMMENTTOKENContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#String.
    def visitString(self, ctx:gramaticLitthonParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#BlockCommand.
    def visitBlockCommand(self, ctx:gramaticLitthonParser.BlockCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#Potence.
    def visitPotence(self, ctx:gramaticLitthonParser.PotenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#ArrayType.
    def visitArrayType(self, ctx:gramaticLitthonParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#FindInArray.
    def visitFindInArray(self, ctx:gramaticLitthonParser.FindInArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#More.
    def visitMore(self, ctx:gramaticLitthonParser.MoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#Subtraction.
    def visitSubtraction(self, ctx:gramaticLitthonParser.SubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#Number.
    def visitNumber(self, ctx:gramaticLitthonParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#SizeValue.
    def visitSizeValue(self, ctx:gramaticLitthonParser.SizeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#Division.
    def visitDivision(self, ctx:gramaticLitthonParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#Compare.
    def visitCompare(self, ctx:gramaticLitthonParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#Boolean.
    def visitBoolean(self, ctx:gramaticLitthonParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#systemIn_.
    def visitSystemIn_(self, ctx:gramaticLitthonParser.SystemIn_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#systemOut_.
    def visitSystemOut_(self, ctx:gramaticLitthonParser.SystemOut_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#add_.
    def visitAdd_(self, ctx:gramaticLitthonParser.Add_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#remove_.
    def visitRemove_(self, ctx:gramaticLitthonParser.Remove_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#while_.
    def visitWhile_(self, ctx:gramaticLitthonParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#condition_.
    def visitCondition_(self, ctx:gramaticLitthonParser.Condition_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#assume.
    def visitAssume(self, ctx:gramaticLitthonParser.AssumeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#invoke.
    def visitInvoke(self, ctx:gramaticLitthonParser.InvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#idVars.
    def visitIdVars(self, ctx:gramaticLitthonParser.IdVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#idExpr.
    def visitIdExpr(self, ctx:gramaticLitthonParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#sizing.
    def visitSizing(self, ctx:gramaticLitthonParser.SizingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#find.
    def visitFind(self, ctx:gramaticLitthonParser.FindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticLitthonParser#array.
    def visitArray(self, ctx:gramaticLitthonParser.ArrayContext):
        return self.visitChildren(ctx)



del gramaticLitthonParser