import json
from typing import Dict, Any, List
#from api_mock import check_inventory, confirm_order, process_payment

# Mock backend API functions (replace these with actual API calls)
def check_inventory(product_id: str, quantity: int) -> Dict[str, Any]:
   return check_inventory(product_id=product_id, quantity=quantity)

def process_payment(order_details: Dict[str, Any]) -> Dict[str, Any]:
   return process_payment(order_details=order_details)

def confirm_order(order_notification: Dict[str, Any]) -> Dict[str, Any]:
    return confirm_order(order_notification=order_notification)
    