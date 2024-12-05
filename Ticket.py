# Base Ticket Class
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

# SingleDayTicket Subclass
class SingleDayTicket(Ticket):
    """Represents a single-day ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, date):
        super().__init__(ticket_id, price, "Single Day", validity, discount, limitations)
        self.date = date  # The specific date the ticket is valid for


# MultiDayTicket Subclass
class MultiDayTicket(Ticket):
    """Represents a multi-day ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, start_date, end_date):
        super().__init__(ticket_id, price, "Multi Day", validity, discount, limitations)
        self.start_date = start_date  # Start date of the ticket validity
        self.end_date = end_date  # End date of the ticket validity


# AnnualMembership Subclass
class AnnualMembership(Ticket):
    """Represents an annual membership ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, renewal_date):
        super().__init__(ticket_id, price, "Annual Membership", validity, discount, limitations)
        self.renewal_date = renewal_date  # Renewal date for the membership


# ChildTicket Subclass
class ChildTicket(Ticket):
    """Represents a child ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, age_limit):
        super().__init__(ticket_id, price, "Child", validity, discount, limitations)
        self.age_limit = age_limit  # Age limit for the child ticket


# GroupTicket Subclass
class GroupTicket(Ticket):
    """Represents a group ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, min_group_size):
        super().__init__(ticket_id, price, "Group", validity, discount, limitations)
        self.min_group_size = min_group_size  # Minimum group size required for this ticket


# VIPExperiencePass Subclass
class VIPExperiencePass(Ticket):
    """Represents a VIP experience ticket in the theme park system."""
    def __init__(self, ticket_id, price, validity, discount, limitations, additional_benefits):
        super().__init__(ticket_id, price, "VIP", validity, discount, limitations)
        self.additional_benefits = additional_benefits  # Additional benefits included in the VIP pass
