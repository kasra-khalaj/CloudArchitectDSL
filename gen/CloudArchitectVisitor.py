# Generated from U:/University/Projects/CloudArchitect/CloudArchitect.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CloudArchitectParser import CloudArchitectParser
else:
    from CloudArchitectParser import CloudArchitectParser

# This class defines a complete generic visitor for a parse tree produced by CloudArchitectParser.

class CloudArchitectVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CloudArchitectParser#program.
    def visitProgram(self, ctx:CloudArchitectParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#topology.
    def visitTopology(self, ctx:CloudArchitectParser.TopologyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#statement.
    def visitStatement(self, ctx:CloudArchitectParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#networkDecl.
    def visitNetworkDecl(self, ctx:CloudArchitectParser.NetworkDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#nodeDecl.
    def visitNodeDecl(self, ctx:CloudArchitectParser.NodeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#linkDecl.
    def visitLinkDecl(self, ctx:CloudArchitectParser.LinkDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#policyDecl.
    def visitPolicyDecl(self, ctx:CloudArchitectParser.PolicyDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#policyRule.
    def visitPolicyRule(self, ctx:CloudArchitectParser.PolicyRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#selectorClause.
    def visitSelectorClause(self, ctx:CloudArchitectParser.SelectorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#checkClause.
    def visitCheckClause(self, ctx:CloudArchitectParser.CheckClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#messageClause.
    def visitMessageClause(self, ctx:CloudArchitectParser.MessageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#severity.
    def visitSeverity(self, ctx:CloudArchitectParser.SeverityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#targetDecl.
    def visitTargetDecl(self, ctx:CloudArchitectParser.TargetDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#property.
    def visitProperty(self, ctx:CloudArchitectParser.PropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#expr.
    def visitExpr(self, ctx:CloudArchitectParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#literal.
    def visitLiteral(self, ctx:CloudArchitectParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#list.
    def visitList(self, ctx:CloudArchitectParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#object.
    def visitObject(self, ctx:CloudArchitectParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#qualifiedName.
    def visitQualifiedName(self, ctx:CloudArchitectParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#validId.
    def visitValidId(self, ctx:CloudArchitectParser.ValidIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CloudArchitectParser#binaryOp.
    def visitBinaryOp(self, ctx:CloudArchitectParser.BinaryOpContext):
        return self.visitChildren(ctx)



del CloudArchitectParser