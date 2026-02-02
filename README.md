# Agentic-Order-Workflow
Agentic Order workflow : AI-powered e-commerce experience for customers


## Description


## Setup
1. Setup python 3.12 environment
- conda create -n agent_3.12 python=3.12
- conda activate agent_3.12

2. Install requirements
- pip install -r requirements.txt
- setup your & export Anthropic Key in start.sh, else os.environ["ANTHROPIC_API_KEY"] in the client
- sh start.sh


## Architecture

```
User Message
    ↓
AI Agent (Claude)
    ↓
Function Calling → Backend APIs
    ↓            (/inventory, /payment, /order/confirmed)
Tool Results
    ↓
AI Agent (Claude)
    ↓
Natural Language Response
```

## Key Components

### 1. **Tool Definitions** (`tools` array)
Each backend API is defined as a "tool" that the agent can call:
- `check_inventory`: Validates product availability and pricing
- `process_payment`: Processes payment for the order
- `confirm_order`: Generates order confirmation with tracking details

### 2. **Agent Loop**
The agent follows this workflow:
1. Receives user message
2. Analyzes intent and decides which tools to use
3. Calls backend APIs through tool execution
4. Receives API responses
5. Continues until workflow is complete
6. Returns natural language response to user