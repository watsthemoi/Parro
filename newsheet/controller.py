import customtkinter as ctk
from tkinter import filedialog, messagebox
from models import NewSheetModel
from views import NewSheetView

class NewSheetController:
    def __init__(self, root):
        self.views = NewSheetView(root)
        self.models = NewSheetModel()

        # Bind the Add button
        self.views.BTN_ADD.configure(command=self.add_audio_file)

    def add_audio_file(self):
        # Open file dialog to select an audio file
        file_path = filedialog.askopenfilename(
            title="Select an Audio File",
            filetypes=(("Audio Files", "*.mp3;*.wav"), ("All Files", "*.*"))
        )

        if file_path:
            # Store the file in the model
            self.models.store_file(file_path)

            # Enable the Play and Edit buttons
            self.views.enable_buttons()
            #self.views.BTN_PLAY.configure(state="normal")
            #self.views.BTN_EDIT.configure(state="normal")
