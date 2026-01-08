# Generated from U:/University/Projects/CloudArchitect/CloudArchitect.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CloudArchitectParser import CloudArchitectParser
else:
    from CloudArchitectParser import CloudArchitectParser

# This class defines a complete listener for a parse tree produced by CloudArchitectParser.
class CloudArchitectListener(ParseTreeListener):

    # Enter a parse tree produced by CloudArchitectParser#program.
    def enterProgram(self, ctx:CloudArchitectParser.ProgramContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#program.
    def exitProgram(self, ctx:CloudArchitectParser.ProgramContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#topology.
    def enterTopology(self, ctx:CloudArchitectParser.TopologyContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#topology.
    def exitTopology(self, ctx:CloudArchitectParser.TopologyContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#statement.
    def enterStatement(self, ctx:CloudArchitectParser.StatementContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#statement.
    def exitStatement(self, ctx:CloudArchitectParser.StatementContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#networkDecl.
    def enterNetworkDecl(self, ctx:CloudArchitectParser.NetworkDeclContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#networkDecl.
    def exitNetworkDecl(self, ctx:CloudArchitectParser.NetworkDeclContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#nodeDecl.
    def enterNodeDecl(self, ctx:CloudArchitectParser.NodeDeclContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#nodeDecl.
    def exitNodeDecl(self, ctx:CloudArchitectParser.NodeDeclContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#linkDecl.
    def enterLinkDecl(self, ctx:CloudArchitectParser.LinkDeclContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#linkDecl.
    def exitLinkDecl(self, ctx:CloudArchitectParser.LinkDeclContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#policyDecl.
    def enterPolicyDecl(self, ctx:CloudArchitectParser.PolicyDeclContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#policyDecl.
    def exitPolicyDecl(self, ctx:CloudArchitectParser.PolicyDeclContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#policyRule.
    def enterPolicyRule(self, ctx:CloudArchitectParser.PolicyRuleContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#policyRule.
    def exitPolicyRule(self, ctx:CloudArchitectParser.PolicyRuleContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#selectorClause.
    def enterSelectorClause(self, ctx:CloudArchitectParser.SelectorClauseContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#selectorClause.
    def exitSelectorClause(self, ctx:CloudArchitectParser.SelectorClauseContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#checkClause.
    def enterCheckClause(self, ctx:CloudArchitectParser.CheckClauseContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#checkClause.
    def exitCheckClause(self, ctx:CloudArchitectParser.CheckClauseContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#messageClause.
    def enterMessageClause(self, ctx:CloudArchitectParser.MessageClauseContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#messageClause.
    def exitMessageClause(self, ctx:CloudArchitectParser.MessageClauseContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#severity.
    def enterSeverity(self, ctx:CloudArchitectParser.SeverityContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#severity.
    def exitSeverity(self, ctx:CloudArchitectParser.SeverityContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#targetDecl.
    def enterTargetDecl(self, ctx:CloudArchitectParser.TargetDeclContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#targetDecl.
    def exitTargetDecl(self, ctx:CloudArchitectParser.TargetDeclContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#property.
    def enterProperty(self, ctx:CloudArchitectParser.PropertyContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#property.
    def exitProperty(self, ctx:CloudArchitectParser.PropertyContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#expr.
    def enterExpr(self, ctx:CloudArchitectParser.ExprContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#expr.
    def exitExpr(self, ctx:CloudArchitectParser.ExprContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#literal.
    def enterLiteral(self, ctx:CloudArchitectParser.LiteralContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#literal.
    def exitLiteral(self, ctx:CloudArchitectParser.LiteralContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#list.
    def enterList(self, ctx:CloudArchitectParser.ListContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#list.
    def exitList(self, ctx:CloudArchitectParser.ListContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#object.
    def enterObject(self, ctx:CloudArchitectParser.ObjectContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#object.
    def exitObject(self, ctx:CloudArchitectParser.ObjectContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#qualifiedName.
    def enterQualifiedName(self, ctx:CloudArchitectParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#qualifiedName.
    def exitQualifiedName(self, ctx:CloudArchitectParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#validId.
    def enterValidId(self, ctx:CloudArchitectParser.ValidIdContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#validId.
    def exitValidId(self, ctx:CloudArchitectParser.ValidIdContext):
        pass


    # Enter a parse tree produced by CloudArchitectParser#binaryOp.
    def enterBinaryOp(self, ctx:CloudArchitectParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by CloudArchitectParser#binaryOp.
    def exitBinaryOp(self, ctx:CloudArchitectParser.BinaryOpContext):
        pass



del CloudArchitectParser