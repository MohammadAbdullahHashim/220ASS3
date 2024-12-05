import tkinter as tk
from tkinter import messagebox, ttk

# Dummy data storage for customers
customers = {}

# Functions
def add_customer():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        customers[name] = email
        messagebox.showinfo("Success", "Customer added successfully!")
        update_customer_table()
        clear_form()
    else:
        messagebox.showerror("Error", "Name and Email are required!")

def delete_customer():
    selected = customer_table.selection()
    if selected:
        for item in selected:
            name = customer_table.item(item)['values'][0]
            del customers[name]
        update_customer_table()
        messagebox.showinfo("Success", "Customer deleted successfully!")
    else:
        messagebox.showerror("Error", "Select a customer to delete!")

def update_customer_table():
    customer_table.delete(*customer_table.get_children())
    for name, email in customers.items():
        customer_table.insert("", "end", values=(name, email))

def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Account Management")

# Form
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Customer", command=add_customer)
add_button.grid(row=2, column=0, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Customer", command=delete_customer)
delete_button.grid(row=2, column=1, padx=10, pady=5)

# Customer Table
customer_table = ttk.Treeview(root, columns=("Name", "Email"), show="headings")
customer_table.heading("Name", text="Name")
customer_table.heading("Email", text="Email")
customer_table.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()


# Ticket Purchasing GUI

import tkinter as tk
from tkinter import ttk, messagebox

# Dummy data for tickets
tickets = [
    {"type": "Single Day", "price": 275, "features": "Valid for one day"},
    {"type": "Multi Day", "price": 480, "features": "Valid for two days"},
    {"type": "VIP Pass", "price": 550, "features": "Reserved seating and fast access"}
]

# Cart
cart = []

# Functions
def add_to_cart(ticket):
    cart.append(ticket)
    update_cart()

def update_cart():
    cart_list.delete(0, tk.END)
    for ticket in cart:
        cart_list.insert(tk.END, f"{ticket['type']} - {ticket['price']} AED")

def checkout():
    if not cart:
        messagebox.showerror("Error", "Your cart is empty!")
    else:
        total = sum(ticket['price'] for ticket in cart)
        messagebox.showinfo("Checkout", f"Total Price: {total} AED\nThank you for your purchase!")
        cart.clear()
        update_cart()

# GUI
root = tk.Tk()
root.title("Ticket Purchasing Interface")

# Ticket Options
tk.Label(root, text="Available Tickets").grid(row=0, column=0, padx=10, pady=5)
ticket_table = ttk.Treeview(root, columns=("Type", "Price", "Features"), show="headings")
ticket_table.heading("Type", text="Type")
ticket_table.heading("Price", text="Price (AED)")
ticket_table.heading("Features", text="Features")
ticket_table.grid(row=1, column=0, padx=10, pady=5)

# Populate ticket table
for ticket in tickets:
    ticket_table.insert("", "end", values=(ticket["type"], ticket["price"], ticket["features"]))

# Add to Cart Button
add_button = tk.Button(root, text="Add to Cart", command=lambda: add_to_cart(tickets[0]))
add_button.grid(row=2, column=0, padx=10, pady=5)

# Cart
tk.Label(root, text="Your Cart").grid(row=0, column=1, padx=10, pady=5)
cart_list = tk.Listbox(root)
cart_list.grid(row=1, column=1, padx=10, pady=5)

# Checkout Button
checkout_button = tk.Button(root, text="Checkout", command=checkout)
checkout_button.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()

# Admin Dashboard

import tkinter as tk
from tkinter import ttk, messagebox

# Dummy data
sales_data = [
    {"type": "Single Day", "sales": 100},
    {"type": "Multi Day", "sales": 50},
    {"type": "VIP Pass", "sales": 20}
]
discounts = {"Single Day": 0, "Multi Day": 10, "VIP Pass": 5}

# Functions
def update_discounts():
    for ticket in discounts:
        discounts[ticket] = int(discount_entries[ticket].get())
    messagebox.showinfo("Success", "Discounts updated successfully!")

# GUI
root = tk.Tk()
root.title("Admin Dashboard")

# Ticket Sales
tk.Label(root, text="Ticket Sales").grid(row=0, column=0, padx=10, pady=5)
sales_table = ttk.Treeview(root, columns=("Type", "Sales"), show="headings")
sales_table.heading("Type", text="Ticket Type")
sales_table.heading("Sales", text="Tickets Sold")
sales_table.grid(row=1, column=0, padx=10, pady=5)

# Populate sales table
for data in sales_data:
    sales_table.insert("", "end", values=(data["type"], data["sales"]))

# Discounts
tk.Label(root, text="Modify Discounts").grid(row=0, column=1, padx=10, pady=5)
discount_entries = {}
row = 1
for ticket, discount in discounts.items():
    tk.Label(root, text=f"{ticket} Discount:").grid(row=row, column=1, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.insert(0, discount)
    entry.grid(row=row, column=2, padx=10, pady=5)
    discount_entries[ticket] = entry
    row += 1

# Update Discounts Button
update_button = tk.Button(root, text="Update Discounts", command=update_discounts)
update_button.grid(row=row, column=1, columnspan=2, padx=10, pady=5)

root.mainloop()
