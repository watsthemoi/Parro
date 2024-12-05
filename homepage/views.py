from customtkinter import *
from PIL import Image
class HomePageView(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master=master

        set_default_color_theme("dark-blue")
        self.OPTIONSFRAME = CTkFrame(master=self, width=225, fg_color=("#212121", "#212121"), bg_color=("#212121", "#212121"))
        self.OPTIONSFRAME.pack_propagate(False)
        self.OPTIONSFRAME.pack(fill="y", side="left")

        self.LB_TITLE = CTkLabel(master=self.OPTIONSFRAME, text="PARRO", height=25, fg_color=("#212121", "#212121"), bg_color=("#212121", "#212121"), text_color=("#ffffff", "#ffffff"), font=CTkFont(size=35, family="Courier New", weight="bold", overstrike=False))
        self.LB_TITLE.pack(padx=(5, 0), pady=(20, 20))

        self.LB_CREATE = CTkLabel(master=self.OPTIONSFRAME, text="Create", height=25, fg_color=("#212121", "#212121"), bg_color=("#212121", "gray13"), text_color=("#ffffff", "#ffffff"), font=CTkFont(family="Courier New", size=16, weight="bold"))
        self.LB_CREATE.pack(padx=(15, 0), pady=(10, 0), anchor="w")

        self.BTN_NEWCOMP = CTkButton(master=self.OPTIONSFRAME, text="New Composition", fg_color=("#212121", "#212121"), text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_music_note_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"), command= self.show_sheet)
        self.BTN_NEWCOMP.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.BTN_NEWRECORDING = CTkButton(master=self.OPTIONSFRAME, text="New Recording", fg_color=("#212121", "#212121"), text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_mic_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"), command= self.show_record)
        self.BTN_NEWRECORDING.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.MAINFRAME = CTkFrame(master=self, width=590, height=514, bg_color=("gray92", "#3e3e3e"), fg_color=("gray90", "#3e3e3e"))
        self.MAINFRAME.pack_propagate(False)
        self.MAINFRAME.pack(fill="both", expand=True)

    def show_record(self):
        # Change to recording view
        self.master.show_newrecord()

    def show_sheet(self):
        # Change to composition view
        self.master.show_newsheet()    
