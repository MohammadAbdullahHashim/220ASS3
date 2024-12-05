# PurchaseOrder Class
class PurchaseOrder:
    """Represents a purchase order in the ticketing system."""
    def __init__(self, order_id, total_price, order_date):
        self.order_id = order_id  # Unique ID for the purchase order
        self.total_price = total_price  # Total price for all tickets in the order
        self.order_date = order_date  # Date the order was placed
        self.tickets = []  # List of tickets included in the order (Composition relationship)

    # Method to add a ticket to the purchase order
    def add_ticket(self, ticket):
        self.tickets.append(ticket)
