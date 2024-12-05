# Base class: Ticket
class Ticket:
    """Represents a general ticket in the theme park system."""
    def __init__(self, ticket_id, price, ticket_type, validity, discount, limitations):
        self.ticket_id = ticket_id  # Unique ID for the ticket
        self.price = price  # Price of the ticket
        self.ticket_type = ticket_type  # Type of ticket (e.g., Single Day, Multi-Day)
        self.validity = validity  # Validity period or conditions for the ticket
        self.discount = discount  # Discount rate for the ticket
        self.limitations = limitations  # Limitations or restrictions for the ticket
        self.attractions = []  # Many-to-Many relationship with attractions

    # Add an attraction to the ticket
    def add_attraction(self, attraction):
        self.attractions.append(attraction)

# Subclasses of Ticket
class SingleDayTicket(Ticket):
    """Represents a single-day ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, date):
        super().__init__(ticket_id, price, "Single Day", validity, discount, limitations)
        self.date = date  # The specific date the ticket is valid for

class MultiDayTicket(Ticket):
    """Represents a multi-day ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, start_date, end_date):
        super().__init__(ticket_id, price, "Multi Day", validity, discount, limitations)
        self.start_date = start_date  # Start date of the ticket validity
        self.end_date = end_date  # End date of the ticket validity

class AnnualMembership(Ticket):
    """Represents an annual membership ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, renewal_date):
        super().__init__(ticket_id, price, "Annual Membership", validity, discount, limitations)
        self.renewal_date = renewal_date  # Renewal date for the membership

class ChildTicket(Ticket):
    """Represents a child ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, age_limit):
        super().__init__(ticket_id, price, "Child", validity, discount, limitations)
        self.age_limit = age_limit  # Age limit for the child ticket

class GroupTicket(Ticket):
    """Represents a group ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, min_group_size):
        super().__init__(ticket_id, price, "Group", validity, discount, limitations)
        self.min_group_size = min_group_size  # Minimum group size required for this ticket

class VIPExperiencePass(Ticket):
    """Represents a VIP experience ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, additional_benefits):
        super().__init__(ticket_id, price, "VIP", validity, discount, limitations)
        self.additional_benefits = additional_benefits  # Additional benefits included in the VIP pass

# Class to represent park attractions
class Attraction:
    """Represents an attraction in the theme park."""
    def __init__(self, attraction_id, name, capacity, schedule):
        self.attraction_id = attraction_id  # Unique ID for the attraction
        self.name = name  # Name of the attraction
        self.capacity = capacity  # Maximum capacity of the attraction
        self.schedule = schedule  # Operating schedule of the attraction
        self.guests = []  # Many-to-Many relationship with guests
        self.tickets = []  # Many-to-Many relationship with tickets

    # Add a guest to the attraction
    def add_guest(self, guest):
        self.guests.append(guest)

    # Add a ticket to the attraction
    def add_ticket(self, ticket):
        self.tickets.append(ticket)

# Class to represent purchase orders (Composition with Ticket)
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

# Class to represent guests (Aggregation with PurchaseOrder)
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

# Class to represent administrators
class Admin:
    """Represents an admin in the theme park system."""
    def __init__(self, username, password):
        self.username = username  # Username for the admin
        self.password = password  # Password for the admin

    # Method for admin to manage tickets
    def manage_ticket(self, ticket):
        print(f"Admin {self.username} is managing ticket: {ticket.ticket_id}")



if __name__ == "__main__":
    # Create attractions
    roller_coaster = Attraction("A001", "Roller Coaster", 50, "9 AM - 6 PM")
    ferris_wheel = Attraction("A002", "Ferris Wheel", 30, "10 AM - 8 PM")

    # Create tickets and link to attractions
    vip_ticket = VIPExperiencePass("T006", 550.0, "Valid for one day", 0.0, "Limited availability", "Reserved seating")
    vip_ticket.add_attraction(roller_coaster)
    vip_ticket.add_attraction(ferris_wheel)

    # Link attractions to the ticket
    roller_coaster.add_ticket(vip_ticket)
    ferris_wheel.add_ticket(vip_ticket)

    # Create a guest and link to attractions
    guest = Guest("Mohammad Abdulrahman", "mohammad.Abdulrahman@zu.com", "MohdABD@123")
    guest.add_attraction(roller_coaster)
    guest.add_attraction(ferris_wheel)

    # Link guests to attractions
    roller_coaster.add_guest(guest)
    ferris_wheel.add_guest(guest)

    # Print details to verify relationships
    print(f"Guest {guest.name} is visiting the following attractions:")
    for attraction in guest.attractions:
        print(f" - {attraction.name}")

    print(f"The following tickets are valid for {roller_coaster.name}:")
    for ticket in roller_coaster.tickets:
        print(f" - Ticket ID: {ticket.ticket_id}, Type: {ticket.ticket_type}")

    print(f"The following guests visited {ferris_wheel.name}:")
    for guest in ferris_wheel.guests:
        print(f" - Guest Name: {guest.name}")
