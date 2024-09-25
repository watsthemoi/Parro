import customtkinter as ctk
from models import Model
from views import NewSheetView

class Controller(ctk.CTk):
    def __init__(self):
        super().__init__()
 
        self.views = NewSheetView(self)
        self.views.encommand(self.views.enable)
        
    def enable(self):
        self.enable()

    # def run(self):
    #     self.root.mainloop()    

    # def addf(self):
        # finsert = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg;*.flac;*.acc")])

    #    if 
    #        self.newsheet.views.enable()