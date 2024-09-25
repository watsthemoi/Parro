import customtkinter as ctk
from tkinter import filedialog, messagebox
from models import Model
from views import NewSheetView

class Controller(ctk.CTk):
    def __init__(self, master):
        super().__init__()
 
        self.views = NewSheetView(master)
        self.models = Model()

        self.views.askforfile = self.load

    def load(self): # Opens file and stores contents
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            try:
                self.models.load_file_data(file)
                self.views.display(self.models.data)
                self.views.enable() # Enables buttons after success
            except Exception as e:
                messagebox.showerror("Error",f"Failed to load file: {e}")          

    # Opens User-Chosen File and Stores it in Frame

    # def run(self):
    #     self.root.mainloop()    

    # def addf(self):
        # finsert = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg;*.flac;*.acc")])

    #    if 
    #        self.newsheet.views.enable()