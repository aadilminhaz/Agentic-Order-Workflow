"""
E-commerce AI Agent for Order Placement
This agent handles customer order placement by orchestrating backend API calls
"""

import anthropic
import json
from typing import Dict, Any, List
import os
#from agents_config.client import client

#import configured tools configuration
from agents_config.tools_config import tools

#import order-management-client
from order_management_api.order_management_client import confirm_order, process_payment, check_inventory

#Initialise the Anthropic client
client = anthropic.Anthropic()


print('testing order agent')

#map API funtion to tools
tool_functions = {
    "check_inventory" : check_inventory,
    "process_payment": process_payment,
    "confirm_order": confirm_order
}
    

""" Execute appropriate backend function based on the tool name """
def process_tool_call(tool_name: str, tool_input: Dict[str, Any]) -> Any:
    if tool_name in tool_functions:
        return tool_functions[tool_name](**tool_input)
    else:
        raise ValueError(f"Invalid Tool : {tool_name}")



"""Agent loop to process user instructions """
def run_agent(user_message: str, conversation_history: List[Dict] = None) -> str:
    
    if conversation_history is None:
        conversation_history = []
    
    ## Add user message to conversation
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    print(f"\n{'='*60}")
    print(f"USER: {user_message}")
    print(f"{'='*60}\n")

    ## Agent loop - continues until we get a text response (no more tool calls)
    while True:
        #call Claude with tools
        """response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            tools=tools,
            message=conversation_history
        )"""

        print(f"tools*******: {tools}")

        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            tools=tools,
            messages=conversation_history
        )

        print(f"[AGENT] Stop reason: {response.stop_reason}")

        ##Add assitant response to conversation
        conversation_history.append({
            "role": "assistant",
            "content": response.content
        })

        ##Check if tool call is required
        if response.stop_reason == "tool_use":
            ##process all tool calls in the response
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input

                    print(f"\n[TOOL USE] {tool_name}")
                    print(f"[INPUT] {json.dumps(tool_input, indent=2)}")

                    #Execute the tool
                    try:
                        result = process_tool_call(tool_name=tool_name, tool_input=tool_input)
                        print(f"[RESULT] {json.dumps(result, indent=2)}\n")

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(result)
                        })
                    except Exception as e:
                        print(f"[ERROR] {str(e)}\n")
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps({"error": str(e)}),
                            "is_error": True
                        })

            #Add tool results to conversation

            conversation_history.append({
                "role": "user",
                "content": tool_results
            })  
        
        elif response.stop_reason == "end_turn":
            #Extract the final text response
            final_response = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_response += block.text
            
            print(f"\n[AGENT_RESPONSE]\n{final_response}")
            return final_response
        
        else:
            #unexpected stop reason
            break
    
    return "I ecountered an issue processing your request."

def main():
    """
    Demo the agent with an order placement scenario
    """    

    print("\n" + "="*60)
    print("E-COMMERCE AI AGENT - ORDER PLACEMENT DEMO")
    print("="*60)

    #Example use Request
    user_request = "I want to buy 2 units of product PS5 Slim"

    response = run_agent(user_request)

    print("\n"+ "="*60)
    print("DEMO COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()






