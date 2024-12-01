from ui.auth import AuthWindow
from ui.menu import App
import customtkinter as tk

def main():
    tk.set_appearance_mode("dark")
    # main frame create
    def on_login_success():
        app = App()
        app.grid_rowconfigure(0, weight=1)  # auto resize
        app.grid_columnconfigure(0, weight=1)  # resize
        app.mainloop()

    # auth create
    auth_window = AuthWindow(on_login_success)
    auth_window.resizable(False, False)
    auth_window.grid_rowconfigure(0, weight=1)  # auto resize
    auth_window.grid_columnconfigure(0, weight=1) # resize
    auth_window.mainloop()

if __name__ == "__main__":
    main()
