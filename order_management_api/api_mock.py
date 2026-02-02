import json
from typing import Dict, Any, List

# Mock backend API functions (replace these with actual API calls)
def check_inventory(product_id: str, quantity: int) -> Dict[str, Any]:
    """
    Mock function to check inventory availability
    In production, this would call /inventory API
    """
    # Simulate API call
    print(f"[API CALL] Checking inventory for product {product_id}, quantity {quantity}")
    
    # Mock response
    return {
        "product_id": product_id,
        "product_name": "Wireless Headphones",
        "available": True,
        "stock_quantity": 50,
        "price": 79.99,
        "quantity_requested": quantity
    }

def process_payment(order_details: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mock function to process payment
    In production, this would call /payment API
    """
    print(f"[API CALL] Processing payment for order: {order_details}")
    
    # Mock response
    return {
        "payment_status": "success",
        "transaction_id": "TXN123456789",
        "amount_charged": order_details["total_amount"],
        "payment_method": "credit_card"
    }

def confirm_order(order_notification: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mock function to confirm order
    In production, this would call your /order/confirmed API
    """
    print(f"[API CALL] Confirming order: {order_notification}")
    
    # Mock response with updated OrderNotification
    return {
        "order_id": "ORD987654321",
        "status": "confirmed",
        "customer_id": order_notification.get("customer_id", "CUST001"),
        "items": order_notification["items"],
        "total_amount": order_notification["total_amount"],
        "payment_info": order_notification["payment_info"],
        "estimated_delivery": "2026-02-05",
        "tracking_number": "TRK456789123",
        "confirmation_timestamp": "2026-01-31T10:30:00Z"
    }