# Admin Class
class Admin:
    """Represents an admin in the theme park system."""
    def __init__(self, username, password):
        self.username = username  # Username for the admin
        self.password = password  # Password for the admin

    # Method for admin to manage tickets
    def manage_ticket(self, ticket):
        print(f"Admin {self.username} is managing ticket: {ticket.ticket_id}")
