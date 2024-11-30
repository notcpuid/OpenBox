import customtkinter
import tkinter.filedialog
import requests
import hashlib
import os

def choose_file(self):
    # open file dialog
    file_path = tkinter.filedialog.askopenfilename()
    if file_path:
        self.file_path = file_path
        self.file_label.configure(text="Selected file: " + os.path.basename(file_path), font=("Segoe UI", 12))
        self.submit_button.configure(state="normal")
    else:
        self.file_label.configure(text="No file chosen", font=("Segoe UI", 12))
        self.submit_button.configure(state="disabled")

def upload_file(self):
    if self.file_path:
        try:
            url = "http://127.0.0.1:8080/upload"
            # read file
            with open(self.file_path, "rb") as file:
                file_content = file.read()
                
                # generate md5 hash
                md5_hash = hashlib.md5(file_content).hexdigest()
                print(f"[ openbox ] MD5 Hash: {md5_hash}") 
                
                # send file
                response = requests.post(url, files={"file": (md5_hash, file_content)})
            
            if response.status_code == 200:
                print("[ openbox ] file uploaded successfully")
                print("[ openbox ] " + str(response.json()))  # response
            else:
                print("[ openbox ] file upload failed:", response.text)
        except Exception as e:
            print(f"[ openbox ] an error occurred: {e}")
    else:
        print("[ openbox ] no file path provided")