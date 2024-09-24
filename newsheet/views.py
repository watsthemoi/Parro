from tkinter import PhotoImage
from customtkinter import *
from PIL import Image
import platform

class NewSheetView(CTkFrame):  # Inheriting from CTkFrame instead of CTk
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        set_default_color_theme("dark-blue")
        # Detect OS
        if platform.system() == "Darwin":  # macOS
            cursor_style = "pointinghand"
        else:  # Windows or other OS
            cursor_style = "hand2"

        # Left options frame
        self.OPTIONSFRAME = CTkFrame(master=self, width=225, fg_color=("#212121", "#212121"), bg_color=("#212121", "#212121"))
        self.OPTIONSFRAME.pack_propagate(False)
        self.OPTIONSFRAME.pack(fill="y", side="left")

        self.LB_TITLE = CTkLabel(master=self.OPTIONSFRAME, text="PARRO", height=25, cursor=cursor_style, fg_color=("#212121", "#212121"), bg_color=("#212121", "#212121"), text_color=("#ffffff", "#ffffff"), font=CTkFont(size=35, family="Courier New", weight="bold", overstrike=False))
        self.LB_TITLE.pack(padx=(5, 0), pady=(20, 20))
        self.LB_TITLE.bind("<Button-1>", self.go_home)

        self.LB_FL = CTkLabel(master=self.OPTIONSFRAME, text="File", height=25, text_color=("#ffffff", "#ffffff"), 
                                        font=CTkFont(size=15, family="Courier New", weight="bold"))
        self.LB_FL.pack(padx=(15, 0), pady=(10, 0), anchor="w")

        self.BTN_ADD = CTkButton(master=self.OPTIONSFRAME, text="Add Audio", text_color=("#ffffff", "#ffffff"), 
                                  anchor="w", width=180, 
                                  image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
                                  size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_ADD.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.LB_HZLINE = CTkLabel(master=self.OPTIONSFRAME, 
                                  text="-----------------------------------------------------------------------------------", anchor="s", justify="center", height=0, text_color=("gray14", "#808080"), font=CTkFont(size=9))
        self.LB_HZLINE.pack(pady=(10, 0))

        self.LB_INTER = CTkLabel(master=self.OPTIONSFRAME, text="Interact", height=25, text_color=("#ffffff", "#ffffff"), 
                                        font=CTkFont(size=15, family="Courier New", weight="bold"))
        self.LB_INTER.pack(padx=(15, 0), pady=(10, 0), anchor="w")

        self.BTN_PLAY = CTkButton(master=self.OPTIONSFRAME, text="Play", text_color=("#ffffff", "#ffffff"), 
                                  anchor="w", width=180, 
                                  image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
                                  size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_PLAY.pack(padx=(10, 0), pady=(10, 0), anchor="w")
        self.BTN_EDIT = CTkButton(master=self.OPTIONSFRAME, text="Edit Composition", text_color=("#ffffff", "#ffffff"), 
                                  anchor="w", width=180, 
                                  image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
                                  size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_EDIT.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.LB_HZLINE = CTkLabel(master=self.OPTIONSFRAME, 
                                  text="-----------------------------------------------------------------------------------", anchor="s", justify="center", height=0, text_color=("gray14", "#808080"), font=CTkFont(size=9))
        self.LB_HZLINE.pack(pady=(10, 0))

        # Main frame
        self.MAINFRAME = CTkFrame(master=self, width=590, height=514, bg_color=("gray92", "#3e3e3e"), fg_color=("gray90", "#3e3e3e"))
        self.MAINFRAME.pack_propagate(False)
        self.MAINFRAME.pack(fill="both", expand=True)

    def go_home(self, event=None):
        # Call the controller's method to switch to the home page
        self.master.show_homepage()    