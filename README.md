#  CloudArchitect DSL

**CloudArchitect** is a specialized Domain-Specific Language (DSL) designed to revolutionize how cloud infrastructure is architected. Unlike traditional configuration files (YAML/JSON) which are flat and verbose, CloudArchitect uses a **graph-based topology** approach to define systems.

It allows architects to treat components as **Nodes** and communication paths as **Links**, while enforcing strict security and architectural policies *before* any code is generated.

---

## Table of Contents
- [Why CloudArchitect?](#-why-cloudarchitect)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Language Reference](#-language-reference)
    - [Topology & Targets](#1-topology--targets)
    - [Networks (Nesting)](#2-networks-nesting--inheritance)
    - [Nodes (Components)](#3-nodes-supported-types)
    - [Links (Traffic)](#4-links-connections)
    - [Policies (Security)](#5-policies-security-guardrails)
- [Installation](#-installation)
- [Usage](#-usage)
- [Examples](#-examples)
    - [Basic Web Stack](#basic-web-stack)
    - [Advanced Microservices](#advanced-microservices-with-nesting)
- [Compiler Pipeline](#-compiler-pipeline-technical)

---

## Why CloudArchitect?

Defining a modern microservices system usually involves writing hundreds of lines of `docker-compose.yml` or HCL (Terraform). These files are:
1.  **Hard to Visualize:** It's difficult to see the "big picture" of who talks to whom.
2.  **Error-Prone:** It's easy to accidentally expose a private database to the public internet.
3.  **Repetitive:** You repeat the same configurations (networks, logging, environment) for every service.

**CloudArchitect solves this by:**
* **Abstraction:** Write less, generate more.
* **Security-First:** Policies like "No DB in Public Network" are checked at compile time.
* **Visual Logic:** The code structure mirrors the actual system diagram.

---

## Key Features

* **Hierarchical Scoping:** Networks can be nested infinitely (e.g., `Cloud -> Region -> VPC -> Subnet`). Inner networks inherit properties (like `region` or `environment`) from their parents.
* **Policy Enforcement Engine:** A built-in semantic analyzer that acts as a "linter on steroids". It validates architectural invariants (e.g., "All generic links must use HTTPS").
* **Smart Inference:** The compiler fills in the blanks. If you link via `proto = postgres`, it automatically infers `port = 5432` unless specified otherwise.
* **Target Agnostic:** Currently compiles to **Docker Compose**, but built on an intermediate representation (IR) that supports future backends like **Terraform** or **Kubernetes Manifests**.

---

## Project Architecture

The project follows a classic multi-pass compiler design pattern:

```text
CloudArchitect/
├── gen/                             # ANTLR4 Generated Code
│   ├── CloudArchitectLexer.py       # Tokenizer
│   ├── CloudArchitectParser.py      # Grammar Rules
│   └── CloudArchitectVisitor.py     # AST Traversal
├── src/                             # Core Logic
│   ├── main.py                      # CLI Entrypoint
│   ├── semantic_analyzer.py         # Scope Resolution & Policy Check
│   ├── ir_generator.py              # Intermediate Representation Builder
│   └── codegen/                     # Backend Drivers
│       └── docker_compose.py        # YAML Generator
├── examples/                        # Reference Architectures
│   └── secure_bank.ca               # Full complex example
├── CloudArchitect.g4                # The EBNF Grammar File
└── requirements.txt                 # Dependencies
```

---

## Language Reference

### 1. Topology & Targets
Every file must define a `topology`. The `target` block tells the compiler what output to generate.

```javascript
topology PaymentSystem {
    target docker_compose {
        version = "3.8"
        output_path = "./dist/docker-compose.yml"
    }
}
```

### 2. Networks (Nesting & Inheritance)
Networks are containers. They define the "scope".
* **Property Inheritance:** If `public = false` is set on a parent network, all children inherit it.
* **Override:** A child node can explicitly override a parent property.

```javascript
network dmz {
    public = true
    region = "us-east-1"

    network api_gateway_layer {
        // Inherits public=true, region="us-east-1"
    }
}
```

### 3. Nodes (Supported Types)
Nodes are the actual running services.

| Node Type | Description | Key Properties |
| :--- | :--- | :--- |
| **`server`** | General purpose app/web server | `image`, `ports`, `replicas`, `env`, `command` |
| **`db`** | Database instance | `image`, `volume`, `user`, `password` |
| **`cache`** | In-memory cache (Redis/Memcached) | `image`, `memory_limit` |
| **`gateway`** | Load balancer or proxy | `image`, `routes` |

**Example:**
```javascript
node auth_service {
    type = server
    image = "my-auth:v1.2"
    replicas = 2
    env = {
        JWT_SECRET = "super_secret"
    }
}
```

### 4. Links (Connections)
Links represent directional traffic flow. They are crucial for generating firewall rules or `depends_on` chains.

**Syntax:** `link <source> -> <target> { options }`

| Property | Description | Default (Inferred) |
| :--- | :--- | :--- |
| `proto` | Protocol (http, tcp, grpc) | `tcp` |
| `port` | Destination Port | Inferred from proto (e.g. http->80) |

**Example:**
```javascript
link frontend -> backend {
    proto = https
    port = 443
}
```

### 5. Policies (Security Guardrails)
Policies are boolean logic statements run against the AST.
* **Keywords:** `deny`, `allow`
* **Selectors:** `node.type`, `network.public`, `link.proto`

**Example:**
```javascript
policy Hardening {
    // Rule 1: Databases must NEVER be in a public network
    deny node.type == "db" in network.public

    // Rule 2: No unencrypted HTTP in the secure zone
    deny link.proto == "http" in network.secure_zone
}
```

---

## Installation

### Prerequisites
* **Python 3.8+**
* **Java 11+** (Only required if you want to regenerate the grammar using ANTLR)

### Setup
1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/CloudArchitect.git](https://github.com/your-username/CloudArchitect.git)
    cd CloudArchitect
    ```

2.  Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  *(Optional)* Regenerate Parsers:
    If you edit `CloudArchitect.g4`:
    ```bash
    antlr4 -Dlanguage=Python3 -visitor CloudArchitect.g4 -o gen/
    ```

---

## Usage

Run the compiler from the source directory:

```bash
python src/main.py [options]
```

| Argument | Description | Default |
| :--- | :--- | :--- |
| `-i, --input` | Path to the `.ca` source file | **Required** |
| `-o, --output` | Path for the generated file | `docker-compose.yml` |
| `--dry-run` | Only run validation/policies, do not generate code | `False` |
| `--verbose` | Print detailed parsing logs | `False` |

**Example:**
```bash
python src/main.py -i examples/secure_bank.ca --verbose
```

---

## Examples

### Basic Web Stack
A simple 2-tier application with a web server and a database.

```javascript
topology SimpleApp {
    target docker_compose { version = "3.8" }

    network app_net {
        public = true
        
        node web {
            type = server
            image = "nginx:latest"
            ports = [80]
        }

        node db {
            type = db
            image = "postgres:14"
        }

        link web -> db { proto = tcp }
    }
}
```

### Advanced Microservices (with Nesting)
Demonstrates scope isolation and policies.

```javascript
topology FinTechSystem {
    policy Security {
        deny node.type == "db" in network.public
    }

    // Public Facing Zone
    network public_dmz {
        public = true
        node load_balancer {
            type = gateway
            image = "traefik:v2"
            ports = [80, 443]
        }
    }

    // Private Secure Zone
    network private_vpc {
        public = false
        
        node core_api {
            type = server
            image = "api:stable"
        }

        node ledger_db {
            type = db
            image = "postgres:alpine"
        }

        // Cross-network linking
        link public_dmz.load_balancer -> core_api {
            proto = http
        }
        
        link core_api -> ledger_db {
            proto = postgres // Implicit port 5432
        }
    }
}
```

---

## Compiler Pipeline (Technical)

For developers interested in how it works:

1.  **Lexing (Tokenization):** The `CloudArchitectLexer` breaks the input string into tokens (KEYWORDS, IDs, SYMBOLS).
2.  **Parsing (AST Construction):** The `CloudArchitectParser` builds a hierarchical tree based on the Grammar.
3.  **Semantic Analysis (The "Brain"):**
    * Walks the AST using the Visitor pattern.
    * Builds a **Symbol Table** to handle scopes (Nesting).
    * Resolves references (`public_dmz.load_balancer`).
    * Executes Policy Logic against the graph nodes.
4.  **IR Generation:** Converts the validated AST into a simplified JSON dictionary (Intermediate Representation).
5.  **Code Generation:** Maps the IR dictionary to the final YAML structure for Docker Compose.
