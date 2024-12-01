import customtkinter
from handler.upload_file import choose_file, upload_file

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("OpenBox")

        # set the position
        self.geometry(f'400x200')

        # file path variable
        self.file_path = None

        # upload button
        self.upload_button = customtkinter.CTkButton(
            self, text="Choose File", command=lambda: choose_file(self)
        )
        self.upload_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        # submit button
        self.submit_button = customtkinter.CTkButton(
            self, text="Upload", command=lambda: upload_file(self), state="disabled"
        )
        self.submit_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        # display chosen file
        self.file_label = customtkinter.CTkLabel(self, text="No file chosen", anchor="w")
        self.file_label.grid(row=2, column=0, padx=20, pady=10, sticky="w", columnspan=2)
