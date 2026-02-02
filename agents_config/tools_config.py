tools = [
    {
        "name": "check_inventory",
        "description": "Check if product is available",
        "input_schema": {
            "type": "object",
            "properties": {
                "product_id": {
                    "type": "string",
                    "description": "Product unique identifier"
                },
                "quantity": {
                    "type": "integer",
                    "description": "Quantity requested"
                }
            },
            "required": ["product_id", "quantity"]
        }
    },
    {
        "name": "process_payment",
        "description": "Process payment for the order",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_details": {
                    "type": "object",
                    "description": "Complete order notification with customer, items, and payment information"
                }
            },
            "required": ["order_details"]
        }
    },
    {
        "name": "confirm_order",
        "description": "Confirms the order and generates order ID, tracking number, and estimated delivery date",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_notification": {
                    "type": "object",
                    "description": "Complete order notification with customer, items, and payment information"
                }
            },
            "required": ["order_notification"]
        }
    }
]
