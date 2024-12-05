# Attraction Class
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
