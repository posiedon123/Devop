import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel

# Initialize the main window
root = tk.Tk()
root.title("Address Book")
root.geometry("500x400")
root.configure(bg="#1c1c1c")  # Dark background

# List to store contacts
contacts = []

# Function to add a contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name:", parent=root)
    phone = simpledialog.askstring("Add Contact", "Enter phone number:", parent=root)
    email = simpledialog.askstring("Add Contact", "Enter email:", parent=root)
    if name and phone and email:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "permanent_address": "",
            "residential_address": ""
        })
        update_contact_list()
        messagebox.showinfo("Success", "Contact added successfully!", parent=root)
    else:
        messagebox.showwarning("Error", "All fields are required!", parent=root)

# Function to view all contacts
def view_contacts():
    if not contacts:
        messagebox.showinfo("Info", "No contacts found.", parent=root)
        return
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(
            tk.END,
            f"{contact['name']} - {contact['phone']} - {contact['email']}"
        )

# Function to search for a contact
def search_contact():
    search_name = simpledialog.askstring("Search Contact", "Enter name to search:", parent=root)
    if search_name:
        found = False
        contact_list.delete(0, tk.END)
        for contact in contacts:
            if search_name.lower() in contact["name"].lower():
                contact_list.insert(
                    tk.END,
                    f"{contact['name']} - {contact['phone']} - {contact['email']}"
                )
                found = True
        if not found:
            messagebox.showinfo("Info", "No matching contacts found.", parent=root)

# Function to delete a contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        update_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!", parent=root)
    else:
        messagebox.showwarning("Error", "No contact selected.", parent=root)

# Function to update the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(
            tk.END,
            f"{contact['name']} - {contact['phone']} - {contact['email']}"
        )

# Function to edit addresses of a selected contact
def edit_address():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Error", "No contact selected.", parent=root)
        return

    index = selected[0]
    contact = contacts[index]

    # Create a new window for address editing
    address_window = Toplevel(root)
    address_window.title("Edit Address")
    address_window.geometry("400x300")
    address_window.configure(bg="#2c2c2c")

    # Permanent Address
    tk.Label(address_window, text="Permanent Address:", bg="#2c2c2c", fg="white").pack(pady=5)
    permanent_address_entry = tk.Entry(address_window, width=40, bg="#3a3a3a", fg="white")
    permanent_address_entry.pack(pady=5)
    permanent_address_entry.insert(0, contact["permanent_address"])

    # Residential Address
    tk.Label(address_window, text="Residential Address:", bg="#2c2c2c", fg="white").pack(pady=5)
    residential_address_entry = tk.Entry(address_window, width=40, bg="#3a3a3a", fg="white")
    residential_address_entry.pack(pady=5)
    residential_address_entry.insert(0, contact["residential_address"])

    # Checkbox to copy permanent address
    def copy_address():
        if same_as_checkbox_var.get():
            residential_address_entry.delete(0, tk.END)
            residential_address_entry.insert(0, permanent_address_entry.get())

    same_as_checkbox_var = tk.BooleanVar()
    same_as_checkbox = tk.Checkbutton(
        address_window,
        text="Same as Permanent Address",
        variable=same_as_checkbox_var,
        command=copy_address,
        bg="#2c2c2c",
        fg="white",
        selectcolor="#3a3a3a"
    )
    same_as_checkbox.pack(pady=5)

    # Save button
    def save_address():
        contact["permanent_address"] = permanent_address_entry.get()
        contact["residential_address"] = residential_address_entry.get()
        messagebox.showinfo("Success", "Address updated successfully!", parent=address_window)
        address_window.destroy()

    save_button = tk.Button(
        address_window,
        text="Save",
        command=save_address,
        bg="#4CAF50",
        fg="white",
        activebackground="#66bb6a",
        relief="flat",
        padx=10,
        pady=5
    )
    save_button.pack(pady=20)

# Function to show the address on double-click
def show_address(event):
    selected = contact_list.curselection()
    if not selected:
        return
    index = selected[0]
    contact = contacts[index]
    address_info = (
        f"Permanent Address:\n{contact['permanent_address'] or 'Not Provided'}\n\n"
        f"Residential Address:\n{contact['residential_address'] or 'Not Provided'}"
    )
    messagebox.showinfo(f"Address for {contact['name']}", address_info, parent=root)

# GUI Elements
# Frame for buttons
button_frame = tk.Frame(root, bg="#1c1c1c")
button_frame.pack(pady=10)

# Button Styles
button_style = {
    "bg": "#3a3a3a",
    "fg": "white",
    "activebackground": "#555555",
    "activeforeground": "white",
    "relief": "flat",
    "padx": 10,
    "pady": 5
}

# Buttons
add_button = tk.Button(button_frame, text="Add Contact", command=add_contact, **button_style)
add_button.grid(row=0, column=0, padx=5)

view_button = tk.Button(button_frame, text="View Contacts", command=view_contacts, **button_style)
view_button.grid(row=0, column=1, padx=5)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contact, **button_style)
search_button.grid(row=0, column=2, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact, **button_style)
delete_button.grid(row=0, column=3, padx=5)

edit_address_button = tk.Button(button_frame, text="Edit Address", command=edit_address, **button_style)
edit_address_button.grid(row=0, column=4, padx=5)

# Listbox to display contacts
contact_list = tk.Listbox(
    root,
    width=50,
    height=10,
    bg="#2c2c2c",
    fg="white",
    selectbackground="#4c4c4c",
    selectforeground="white",
    relief="flat",
    borderwidth=0
)
contact_list.pack(pady=10)

# Bind double-click event to the listbox
contact_list.bind("<Double-Button-1>", show_address)

# Run the application
root.mainloop()
