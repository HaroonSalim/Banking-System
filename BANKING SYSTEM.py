import tkinter as tk
from tkinter import ttk, messagebox

class BankingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")

        self.create_login_gui()

    def create_login_gui(self):
        self.login_frame = ttk.Frame(self.root, padding="20")
        self.login_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(self.login_frame, text="Username:").grid(row=0, column=0, pady=10)
        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, pady=10)

        ttk.Label(self.login_frame, text="Password:").grid(row=1, column=0, pady=10)
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=10)

        login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        register_button = ttk.Button(self.login_frame, text="Register", command=self.register)
        register_button.grid(row=3, column=0, columnspan=2, pady=10)

    def create_dashboard_gui(self):
        self.dashboard_frame = ttk.Frame(self.root, padding="20")
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(self.dashboard_frame, text="Welcome to Your Dashboard!").grid(row=0, column=0, columnspan=2, pady=10)

        transfer_button = ttk.Button(self.dashboard_frame, text="Transfer Money", command=self.transfer_money)
        transfer_button.grid(row=1, column=0, pady=10)

        balance_button = ttk.Button(self.dashboard_frame, text="Check Balance", command=self.check_balance)
        balance_button.grid(row=1, column=1, pady=10)

        deposit_button = ttk.Button(self.dashboard_frame, text="Deposit Money", command=self.deposit_money)
        deposit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the user exists in the file
        try:
            with open("user_data.txt", "r") as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(",")
                    if username == stored_username and password == stored_password:
                        self.create_dashboard_gui()
                        return

            messagebox.showerror("Login Error", "Invalid username or password")
        except FileNotFoundError:
            messagebox.showerror("Login Error", "No registered users found")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username already exists
        try:
            with open("user_data.txt", "r") as file:
                for line in file:
                    stored_username, _ = line.strip().split(",")
                    if username == stored_username:
                        messagebox.showerror("Registration Error", "Username already exists")
                        return
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist

        # Register the user
        with open("user_data.txt", "a") as file:
            file.write(f"{username},{password}\n")
            messagebox.showinfo("Registration Successful", "User registered successfully!")

    def transfer_money(self):
        # Add transfer money functionality here
        pass

    def check_balance(self):
        # Add check balance functionality here
        pass

    def deposit_money(self):
        # Add deposit money functionality here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()
