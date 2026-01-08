grammar CloudArchitect;

// --- Parser Rules (The Structure) ---

// Entry point
program: topology* EOF;

// The main container
topology: 'topology' ID '{' statement* '}';

// Statements allowed inside scopes
statement
    : networkDecl
    | nodeDecl
    | linkDecl
    | policyDecl
    | targetDecl
    ;

// Recursive Network Definition
networkDecl: 'network' ID '{' (property | statement)* '}';

// Node Definition
nodeDecl: 'node' ID '{' property* '}';

// Links: Source -> Destination
linkDecl: 'link' qualifiedName '->' qualifiedName '{' property* '}';

// --- IMPROVED POLICY SECTION ---
policyDecl: 'policy' ID '{' policyRule* '}';

policyRule
    : severity STRING '{'           // e.g. deny "Rule Name" {
          selectorClause?           // e.g. from node where ...
          checkClause               // e.g. ensure ...
          messageClause?            // e.g. message "..."
      '}'
    ;

selectorClause: 'from' validId ('where' expr)?; // Scopes the check
checkClause: 'ensure' expr;                     // The logic test
messageClause: 'message' STRING;                // Custom error text

severity: 'deny' | 'warn';
// ------------------------------

// Target Definition
targetDecl: 'target' ID '{' property* '}';

// Properties: key = value
property: validId '=' expr;

// Expressions for values
expr
    : literal
    | list
    | object
    | qualifiedName
    | expr binaryOp expr
    | '(' expr ')'         // Added parentheses support for logic grouping
    ;

literal
    : STRING
    | INT
    | BOOL
    ;

list: '[' (expr (',' expr)*)? ']';
object: '{' (property)* '}';

// Qualified Name: Handles "dot notation"
qualifiedName: validId ('.' validId)*;

// Helper to allow keywords as identifiers (e.g., node.type)
validId
    : ID
    | NODE | NETWORK | LINK | POLICY | TARGET
    | DENY | WARN | FROM | WHERE | ENSURE | MESSAGE
    ;

binaryOp: '==' | '!=' | '>' | '<' | '>=' | '<=' | '&&' | '||' | IN;

// --- Lexer Rules (The Tokens) ---

// Keywords
TOPOLOGY: 'topology';
NETWORK: 'network';
NODE: 'node';
LINK: 'link';
POLICY: 'policy';
TARGET: 'target';

// Policy Keywords
DENY: 'deny';
WARN: 'warn';
FROM: 'from';
WHERE: 'where';
ENSURE: 'ensure';
MESSAGE: 'message';
IN: 'in';

// Data Types
BOOL: 'true' | 'false';

// Identifiers
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

// Literals
INT: [0-9]+;
STRING: '"' .*? '"';

// Symbols
LBRACE: '{'; RBRACE: '}';
LBRACKET: '['; RBRACKET: ']';
LPAREN: '('; RPAREN: ')';
EQUALS: '=';
ARROW: '->';
DOT: '.';
COMMA: ',';

// Operators
EQ: '=='; NEQ: '!=';
GT: '>'; LT: '<'; GTE: '>='; LTE: '<=';
AND: '&&'; OR: '||';

// Skip whitespace/comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;