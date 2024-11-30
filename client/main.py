from ui.auth import AuthWindow
from ui.menu import App

def main():
    # main frame create
    def on_login_success():
        app = App()
        app.mainloop()

    # auth create
    auth_window = AuthWindow(on_login_success)
    auth_window.mainloop()

if __name__ == "__main__":
    main()
