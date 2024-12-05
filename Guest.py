# Guest Class
class Guest:
    """Represents a guest in the theme park system."""
    def __init__(self, name, email, password):
        self.name = name  # Name of the guest
        self.email = email  # Email address of the guest
        self.password = password  # Password for guest's account
        self.purchase_history = []  # List of purchase orders (Aggregation relationship)
        self.attractions = []  # Many-to-Many relationship with attractions

    # Add an attraction to the guest
    def add_attraction(self, attraction):
        self.attractions.append(attraction)

    # Method to add a purchase order to the guest's history
    def add_purchase_order(self, purchase_order):
        self.purchase_history.append(purchase_order)
