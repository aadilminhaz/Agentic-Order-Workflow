# E-commerce AI Agent - Order Placement Implementation

## Overview

This is a working prototype of an AI agent that handles e-commerce order placement by orchestrating your backend APIs. The agent uses Claude's function calling capability to execute a multi-step workflow: checking inventory, processing payment, and confirming orders.

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

### 3. **State Management**
`OrderState` class tracks the order throughout the conversation:
- Items in cart
- Inventory check status
- Payment status
- Order confirmation details

## Files

### `ecommerce_agent.py`
Basic implementation showing the core agent loop and function calling.

**Key features:**
- Simple agent loop with tool execution
- Mock API functions (replace with real API calls)
- Demonstrates the complete order placement flow

### `ecommerce_agent_enhanced.py`
Production-ready implementation with advanced features.

**Key features:**
- State management across conversation
- Interactive CLI mode
- Better error handling
- Structured logging
- Conversation history management

## How to Run

### Prerequisites
```bash
pip install anthropic --break-system-packages
```

Set your Anthropic API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### Basic Demo
```bash
python ecommerce_agent.py
```

This runs an automated demo showing:
- User requests 2 wireless headphones
- Agent checks inventory
- Agent processes payment
- Agent confirms order
- User receives order confirmation

### Enhanced Interactive Mode
```bash
python ecommerce_agent_enhanced.py interactive
```

This launches an interactive CLI where you can:
- Have natural conversations with the agent
- Place multiple orders
- Reset and start fresh
- See real-time API calls

### Enhanced Automated Demo
```bash
python ecommerce_agent_enhanced.py
```

## Example Conversation Flow

**User:** "I want to buy 2 units of product WH-2024"

**Agent Internal Process:**
1. Calls `check_inventory("WH-2024", 2)`
   - API returns: Available, $79.99 each, $159.98 total
2. Calls `process_payment({"customer_id": "CUST001", "items": [...], "total_amount": 159.98})`
   - API returns: Payment successful, transaction ID
3. Calls `confirm_order({...order details...})`
   - API returns: Order ID, tracking number, estimated delivery

**Agent Response:**
"Great! I've successfully placed your order for 2 Wireless Headphones. Your order details:
- Order ID: ORD20260131103000
- Total: $159.98
- Tracking: TRK20260131103000
- Estimated delivery: February 5, 2026

You'll receive a confirmation email shortly!"

## Integrating with Your Real APIs

Replace the mock functions with actual API calls:

```python
def check_inventory(product_id: str, quantity: int) -> Dict[str, Any]:
    import requests
    
    response = requests.get(
        f"https://your-api.com/inventory",
        params={"product_id": product_id, "quantity": quantity},
        headers={"Authorization": f"Bearer {YOUR_API_KEY}"}
    )
    
    return response.json()
```

Do the same for `process_payment()` and `confirm_order()`.

## Function Calling Explained

When the agent needs to call a function, it returns a response with `stop_reason="tool_use"` containing:

```json
{
  "type": "tool_use",
  "id": "toolu_123",
  "name": "check_inventory",
  "input": {
    "product_id": "WH-2024",
    "quantity": 2
  }
}
```

Your code then:
1. Extracts the tool name and input
2. Calls your actual backend API
3. Returns the result to the agent
4. Agent continues the workflow

## Adding More Stages

To add order tracking and returns (stages 2 & 3), follow the same pattern:

### 1. Define new tools:
```python
{
    "name": "get_order_status",
    "description": "Retrieves current order status and tracking information",
    "input_schema": {
        "type": "object",
        "properties": {
            "order_id": {"type": "string"}
        }
    }
}
```

### 2. Implement the function:
```python
def get_order_status(order_id: str) -> Dict[str, Any]:
    # Call your /order/tracking API
    return {...}
```

### 3. Add to tool_functions mapping:
```python
tool_functions = {
    "check_inventory": check_inventory,
    "process_payment": process_payment,
    "confirm_order": confirm_order,
    "get_order_status": get_order_status,  # New
}
```

The agent will automatically understand when to use these new tools based on user queries!

## Key Insights

### Why This Works Well:
1. **Natural Language Interface**: Customers don't need to learn specific commands
2. **Intelligent Orchestration**: Agent decides the right sequence of API calls
3. **Context Awareness**: Maintains conversation state across multiple turns
4. **Error Handling**: Agent can handle API failures gracefully
5. **Extensible**: Easy to add new stages/APIs as you expand

### What Makes It Production-Ready:
- Proper error handling at each API call
- State management for multi-turn conversations
- Logging for debugging and monitoring
- Clear separation between agent logic and business logic
- Easy to swap mock functions with real API calls

## Next Steps

1. **Replace mock APIs** with your actual backend endpoints
2. **Add authentication** for secure API access
3. **Implement proper error handling** for network failures, timeouts, etc.
4. **Add database storage** for conversation history and order state
5. **Build a web interface** (React/Next.js) instead of CLI
6. **Add order tracking and returns** (stages 2 & 3)
7. **Implement proactive notifications** using webhooks
8. **Add analytics** to track agent performance

## Questions?

This implementation demonstrates the core pattern. Once you understand this, extending to tracking and returns is straightforward - just add new tool definitions and API integrations following the same pattern!
