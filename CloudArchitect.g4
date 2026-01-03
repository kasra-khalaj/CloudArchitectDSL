grammar CloudArchitect;

// --- Parser Rules (The Structure) ---

// Entry point: A file can contain multiple topologies
program: topology* EOF;

// The main container
topology: 'topology' ID '{' statement* '}';

// Statements allowed inside a topology or network
statement
    : networkDecl
    | nodeDecl
    | linkDecl
    | policyDecl
    | targetDecl
    ;

// Recursive Network Definition
// Note: 'statement*' allows networks inside networks (nesting)
networkDecl: 'network' ID '{' (property | statement)* '}';

// Node Definition (Leaf component)
nodeDecl: 'node' ID '{' property* '}';

// Links: Source -> Destination
// Uses qualifiedName to allow linking across scopes (e.g., public.lb -> private.api)
linkDecl: 'link' qualifiedName '->' qualifiedName '{' property* '}';

// Policy Definition
policyDecl: 'policy' ID '{' policyRule* '}';
policyRule: 'deny' expr;

// Target Definition (Compiler Output Configuration)
targetDecl: 'target' ID '{' property* '}';

// Properties: key = value
// Using validId allows properties like 'type = ...' where 'type' might become a keyword later
property: validId '=' expr;

// Expressions for values
expr
    : literal
    | list
    | object
    | qualifiedName
    | expr binaryOp expr // For policy logic (==, in)
    ;

literal
    : STRING
    | INT
    | BOOL
    ;

list: '[' (expr (',' expr)*)? ']';
object: '{' (property)* '}';

// Qualified Name: Handles "dot notation" (e.g., network.node.attr)
// Uses validId to allow keywords as parts of names (e.g., node.type)
qualifiedName: validId ('.' validId)*;

// Helper rule to resolve keyword collisions
// This tells the parser: "It's okay if a name looks like a keyword"
validId
    : ID
    | NODE
    | NETWORK
    | LINK
    | POLICY
    | TARGET
    | DENY
    ;

binaryOp: '==' | '!=' | IN;

// --- Lexer Rules (The Tokens) ---

// Keywords
TOPOLOGY: 'topology';
NETWORK: 'network';
NODE: 'node';
LINK: 'link';
POLICY: 'policy';
TARGET: 'target';
DENY: 'deny';
IN: 'in';

// Data Types
BOOL: 'true' | 'false';

// Identifiers (must start with a letter)
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

// Literals
INT: [0-9]+;
STRING: '"' .*? '"';

// Symbols
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
EQUALS: '=';
ARROW: '->';
DOT: '.';
COMMA: ',';
COLON: ':';

// Skip whitespace and comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;