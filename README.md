# MCP - Model Context Protocol Examples

A comprehensive, hands-on collection of examples covering **Model Context Protocol (MCP)** - from creating your first MCP server to deploying production-ready applications using Docker and cloud-native architectures.

## 📚 Table of Contents

- [What is MCP?](#what-is-mcp)
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Key Features](#key-features)
- [Technologies](#technologies)
- [Quick Start Guide](#quick-start-guide)
- [Running Examples](#running-examples)
- [FAQ](#faq)
- [Resources](#resources)

## 🤖 What is MCP?

**Model Context Protocol (MCP)** is a standardized protocol that enables seamless communication between AI models and external tools/systems. It allows:

- 🔌 **Tool Integration**: Connect AI models to custom tools and services
- 🌐 **Universal Communication**: Standardized way for LLMs to interact with resources
- 🔄 **Multi-Transport Support**: Use stdio, HTTP, or custom transports
- 🛡️ **Type-Safe**: Full type support and validation
- 📡 **Remote Execution**: Execute tools on remote servers

## 📖 Overview

This project covers a progressive journey through MCP development:

```
Beginner  ─→  Intermediate  ─→  Advanced  ─→  Production
   ↓              ↓                 ↓             ↓
 Section 1     Section 2,3       Section 4,5    Section 6
```

## ✅ Prerequisites

- **Python 3.12+** (MCP requires modern Python)
- **Git** for version control
- **Docker** (for Section 6)
- **Basic Python knowledge** (async/await, decorators)
- **API familiarity** (helpful for understanding HTTP transport)
- **Terminal/Command Line** comfort

## 🎯 Getting Started

### 1. Set Up the Repository

```bash
git clone <your-repo-url>
cd MCP
```

### 2. Set Up Python Environment

Using `uv` (recommended - faster than pip):
```bash
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Or using traditional venv:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
uv pip install -r pyproject.toml
# or
pip install -e .
```

The project includes:
- `fastmcp` - FastMCP framework for building MCP servers
- `langchain` - For integration with language models
- `langchain-mcp-adapters` - Bridge between LangChain and MCP
- `mcp` - Official MCP specification implementation
- `agentic-terminal` - Terminal-based MCP tools

### 4. Verify Installation

```bash
python main.py
# Expected output: "Hello from mcp-project!"
```

## 📚 Project Structure

### **Section 1: Creating Your First MCP Server** 🌱
**Directory**: `CH-1_CreateMCP/`

Learn the fundamentals of MCP by building a basic server:

- **1_first_mcpserver_stdio.py**: Build a simple MCP server using stdio transport
  - Basic tool definition with `@mcp.tool()` decorator
  - Fetch and process data patterns
  - Running server locally
  
- **2_python_client.py**: Create a Python client to connect to the MCP server
  - Understand client-server communication
  - Making tool calls programmatically
  
- **3_langchain_client.py**: Integrate MCP with LangChain
  - Use MCP tools with language models
  - Automatic tool discovery and binding

**Key Learnings**:
- FastMCP framework basics
- Stdio transport protocol
- Async function handling
- Tool documentation with docstrings

---

### **Section 2: HTTP Transport & Scalability** 🌐
**Directory**: `CH-2_HTTP_MCP/`

Scale your MCP servers for real-world applications:

- **1_http_mcp.py**: Build an HTTP-based MCP server
  - Streamable HTTP transport
  - Network accessibility
  - Multi-client support
  - Running on port 8050
  
- **2_langchain_client.py**: Connect LangChain to HTTP MCP server
  - Remote server communication
  - HTTP client setup
  - Tool availability over network

**Key Learnings**:
- HTTP transport vs Stdio
- Scalability considerations
- Network security basics
- Multi-client architectures

---

### **Section 3: Integrating 3rd Party MCPs** 🔗
**Directory**: `CH-3_3rdParty_MCPs/`

Leverage community MCP servers in your applications:

- **community_mcp.py**: Use open-source community MCP servers
  - Discovering available MCPs
  - Integration patterns
  - Popular community tools
  
- **tavily_mcp.py**: Integrate Tavily search MCP
  - Real-world API integration
  - Web search capabilities
  - Data enrichment workflows

**Key Learnings**:
- MCP ecosystem exploration
- Third-party tool integration
- Composition and orchestration
- API key management

---

### **Section 4: Publishing to PyPI** 📦
**Directory**: `CH-4_PyPI_MCP/` & `MCP_PYPI/`

Package and distribute your MCP as a Python package:

- **1_test_package.py**: Test your packaged MCP
- **2_client.py**: Use the published package as a client
- **MCP_PYPI/**: Complete package structure
  - `pyproject.toml`: Package configuration
  - `src/agentic_terminal/`: Agentic terminal implementation
    - `tools.py`: Custom tool definitions
    - `main.py`: Entry point

**Key Learnings**:
- Python package structure
- PyPI publishing workflow
- Package versioning and dependency management
- Entry points and CLI tools

---

### **Section 5: MCP Gateway & Orchestration** 🎯
**Directory**: `CH-5_MCP_Gateway/`

Build a unified gateway to manage multiple MCP servers:

- **gateway.py**: Central gateway for orchestrating multiple MCPs
  - Mounting multiple MCP servers
  - Request routing
  - Tool discovery and aggregation
  - Unified interface to many tools
  - Example: integrating duckduckgo-mcp-server

**Key Learnings**:
- Gateway pattern architecture
- MCP composition and mounting
- Load balancing concepts
- Tool proxy implementations

---

### **Section 6: Containerization & Docker** 🐳
**Directory**: `CH-6_MCP_Docker/`

Deploy MCP servers in production using Docker:

- **Dockerfile**: Multi-stage Docker configuration
  - Base image: Python 3.11-slim
  - Pre-installed tools (duckduckgo-mcp-server, agentic_terminal)
  - FastMCP runtime
  
- **requirements.txt**: Python dependencies for container
  
- **app/gateway.py**: Gateway application for containerized deployment

**Key Learnings**:
- Dockerfile best practices
- Multi-stage builds
- Container environment setup
- Production deployment patterns
- Tool availability in containers

---

## 🏗️ Architecture

```
MCP/
│
├── CH-1_CreateMCP/           # Basics: Stdio-based MCP
│   ├── 1_first_mcpserver_stdio.py
│   ├── 2_python_client.py
│   └── 3_langchain_client.py
│
├── CH-2_HTTP_MCP/            # HTTP Transport & Scalability
│   ├── 1_http_mcp.py
│   └── 2_langchain_client.py
│
├── CH-3_3rdParty_MCPs/       # Integration Patterns
│   ├── community_mcp.py
│   └── tavily_mcp.py
│
├── CH-4_PyPI_MCP/            # Packaging
│   ├── 1_test_package.py
│   └── 2_client.py
│
├── CH-5_MCP_Gateway/         # Orchestration
│   └── gateway.py
│
├── CH-6_MCP_Docker/          # Production Deployment
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       └── gateway.py
│
├── MCP_PYPI/                 # PyPI Package Structure
│   ├── pyproject.toml
│   ├── README.md
│   └── src/
│       └── agentic_terminal/
│           ├── __init__.py
│           ├── main.py
│           └── tools.py
│
├── Notes/                    # Reference Notes
│
├── pyproject.toml            # Main project config
├── package.json              # NPM metadata
├── main.py                   # Entry point
└── README.md                 # This file
```

## 💡 Key Features

### Progressive Learning Path
- Start with basics (stdio servers)
- Progress to HTTP scalability
- Learn composition and orchestration
- Deploy with Docker

### Hands-On Examples
- Every concept includes working code
- Multiple integration patterns
- Real-world scenarios (search, processing)

### Production-Ready
- Docker containerization
- Gateway architecture
- Multi-server orchestration
- PyPI packaging

### Community Integration
- Third-party MCP servers
- Popular tools (Tavily, DuckDuckGo)
- Integration patterns
- Extensibility examples

## 🛠️ Technologies

| Technology | Purpose | Version |
|-----------|---------|---------|
| **FastMCP** | MCP framework | 3.2.4+ |
| **Python** | Programming language | 3.12+ |
| **Docker** | Containerization | Latest |
| **LangChain** | LLM framework integration | 1.2.17+ |
| **Async/Await** | Concurrent operations | Built-in Python |
| **HTTP** | Network transport | Standard |
| **Stdio** | Local process communication | Standard |
| **UV** | Package management | Latest |

## 🚀 Quick Start Guide

### Example 1: Run the First MCP Server

```bash
# Navigate to Section 1
cd CH-1_CreateMCP

# Activate your virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Run the MCP server
python 1_first_mcpserver_stdio.py
```

### Example 2: Connect a Python Client

```bash
# In another terminal, with venv activated
cd CH-1_CreateMCP
python 2_python_client.py
```

### Example 3: Use with LangChain

```bash
cd CH-1_CreateMCP
python 3_langchain_client.py
```

### Example 4: HTTP Server

```bash
cd CH-2_HTTP_MCP
python 1_http_mcp.py
# Server runs on http://localhost:8050
```

### Example 5: Gateway Architecture

```bash
cd CH-5_MCP_Gateway
python gateway.py
```

### Example 6: Docker Deployment

```bash
cd CH-6_MCP_Docker
docker build -t mcp-server .
docker run -p 8050:8050 mcp-server
```

## 🏃 Running Examples

### Setup for Examples
1. Install all dependencies: `uv pip install -r pyproject.toml`
2. Ensure Python 3.12+ is active: `python --version`
3. Set any required API keys in environment variables

### Running Individual Examples

Each section can be run independently:

```bash
# Section 1 - Basic Server
cd CH-1_CreateMCP && python 1_first_mcpserver_stdio.py

# Section 2 - HTTP Server  
cd CH-2_HTTP_MCP && python 1_http_mcp.py

# Section 5 - Gateway
cd CH-5_MCP_Gateway && python gateway.py

# Section 6 - Docker
cd CH-6_MCP_Docker && docker build -t mcp . && docker run mcp
```

### Debugging

Enable verbose output for MCP debugging:

```bash
# Set debug environment variable
export MCP_DEBUG=1
python your_mcp_file.py
```

## ❓ FAQ

### Q: Do I need GPU support?
**A**: No, MCP servers run on CPU. GPU is only needed if running large language models locally.

### Q: Can I use MCP with other frameworks besides LangChain?
**A**: Yes! MCP is framework-agnostic. It works with any LLM framework that supports the MCP protocol.

### Q: What's the difference between Stdio and HTTP transport?
**A**: 
- **Stdio**: Local communication, lower latency, single machine
- **HTTP**: Network communication, scalable, accessible remotely

### Q: How do I add my own tools to an MCP server?
**A**: Use the `@mcp.tool()` decorator:
```python
@mcp.tool()
async def my_tool(param: str):
    """Tool description."""
    return {"result": "your result"}
```

### Q: Is MCP production-ready?
**A**: Yes! The project includes Docker containerization and gateway patterns for production deployment.

### Q: How do I integrate external APIs?
**A**: Tools can make HTTP calls internally. See Section 3 for Tavily integration example.

### Q: Can I run multiple MCP servers together?
**A**: Yes! Use the gateway pattern (Section 5) to orchestrate multiple servers.

### Q: What's the purpose of PyPI publishing?
**A**: It allows others to install and use your MCP server as a package: `pip install your-mcp-server`

## 📚 Resources

### Official Documentation
- [MCP Specification](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://fastmcp.ai/)
- [LangChain Integration](https://python.langchain.com/docs/integrations/tools/)

### Learning Path
1. **Beginner**: Read Section 1-2 documentation
2. **Intermediate**: Work through Section 3-4 examples
3. **Advanced**: Study Section 5-6 architecture
4. **Expert**: Extend with your own MCPs

## 🔧 Troubleshooting

### Issue: Python version not compatible
**Solution**: Ensure Python 3.12+ is installed
```bash
python --version  # Should show 3.12.x or higher
```

### Issue: FastMCP import error
**Solution**: Reinstall dependencies
```bash
uv pip install --force-reinstall fastmcp
```

### Issue: Port already in use
**Solution**: Use a different port or kill the process
```bash
# On Windows
netstat -ano | findstr :8050
# On Linux/Mac
lsof -i :8050
```

### Issue: Docker build fails
**Solution**: Clear Docker cache and rebuild
```bash
docker system prune -a
docker build --no-cache -t mcp-server .
```

## 📋 License

All rights reserved by **Ansh Lamba**. This project is based on his original work.

---

**Start your MCP journey today!** 🚀

Begin with [Section 1](./CH-1_CreateMCP) and progress at your own pace.

---

<div align="center">

**Credits: [Ansh Lamba](https://github.com/anshlamba) 🙏 | All rights reserved.**

</div>
