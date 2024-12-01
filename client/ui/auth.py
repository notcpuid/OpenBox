import customtkinter

class AuthWindow(customtkinter.CTk):
    def __init__(self, on_login_success):
        super().__init__()

        self.on_login_success = on_login_success

        self.title("Auth")

        # set the position 
        self.geometry(f'600x300')

        # header
        self.title_label = customtkinter.CTkLabel(self, text="OpenBox", font=("Segoe UI", 16))
        self.title_label.grid(row=0, column=0, pady=20)

        # username
        self.login_entry = customtkinter.CTkEntry(self, placeholder_text="Username", font=("Segoe UI", 12))
        self.login_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # pass
        self.password_entry = customtkinter.CTkEntry(self, placeholder_text="Password", font=("Segoe UI", 12), show="*")
        self.password_entry.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # log in button
        self.login_button = customtkinter.CTkButton(self, text="Log in", font=("Segoe UI", 12), command=self.login)
        self.login_button.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        # message
        self.error_label = customtkinter.CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=4, column=0, padx=20, pady=10)

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        if login == "test" and password == "test":
            self.after(100, self.destroy())
            self.on_login_success()
        else:
            self.error_label.configure(text="Wrong username or password", font=("Segoe UI", 12))
