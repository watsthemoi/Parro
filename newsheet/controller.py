import customtkinter as ctk
from models import Model
from views import NewSheetView

class NewSheetController(ctk.CTk):
    def __init__(self):
        
        self.model = Model()
        self.view = NewSheetView(self.root)

        self.view.encommand(self.enable)
        
    

    # def addf(self):
        # finsert = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg;*.flac;*.acc")])

    #    if 
    #        self.newsheet.views.enable()