import customtkinter as ctk
from tkinter import filedialog, messagebox
from newsheet.models import NewSheetModel

class NewSheetController:
    def __init__(self, root):
        self.models = NewSheetModel()

    def add_audio_file(self):
        # Open file dialog to select an audio file
        file = filedialog.askopenfilename(
            title="Select an Audio File",
            filetypes=(("Audio Files", "*.mp3;*.wav"), ("All Files", "*.*"))
        )

        if file:
            try:
            # Store the file in the model
                self.models.store_file(file)
                return file
            except Exception as e:
                print("File Access Error: ", e)   
        return None
            
            
            
