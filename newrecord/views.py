from customtkinter import *
from PIL import Image

class NewRecordView(CTkFrame):  # Inheriting from CTkFrame instead of CTk
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.pack(fill="both", expand=True)  # Fill the window and expand to its size
        set_default_color_theme("dark-blue")

        # Left options frame
        self.OPTIONSFRAME = CTkFrame(master=self, fg_color=("#212121", "#212121"), bg_color=("#212121", "#212121"))
        self.OPTIONSFRAME.pack_propagate(False)
        self.OPTIONSFRAME.pack(fill="y", side="left")

        self.LB_TITLE = CTkLabel(master=self.OPTIONSFRAME, text="OPTIONS", height=25, text_color=("#ffffff", "#ffffff"), font=CTkFont(size=35, family="Courier New", weight="bold", overstrike=False))
        self.LB_TITLE.pack(padx=(10, 0), pady=(20, 0))

        self.BTN_SAVE = CTkButton(master=self.OPTIONSFRAME, text="Save", text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_SAVE.pack(padx=(10, 0), pady=(30, 0))

        self.BTN_DELETE = CTkButton(master=self.OPTIONSFRAME, text="Delete", text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_delete_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_DELETE.pack(padx=(10, 0), pady=(10, 0))

        self.LB_HZLINE = CTkLabel(master=self.OPTIONSFRAME, text="-----------------------------------------------------------------------------------", anchor="s", justify="center", height=0, text_color=("gray14", "#808080"), font=CTkFont(size=9))
        self.LB_HZLINE.pack(pady=(22, 0))

        self.LB_COMPOSITIONS = CTkLabel(master=self.OPTIONSFRAME, text="Export", height=25, text_color=("#ffffff", "#ffffff"), font=CTkFont(size=15, family="Courier New", weight="bold"))
        self.LB_COMPOSITIONS.pack(padx=(20, 0), pady=(20, 0), anchor="w")

        self.BTN_CONVERT = CTkButton(master=self.OPTIONSFRAME, text="Create Score", text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_open_new_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_CONVERT.pack(padx=(10, 0), pady=(10, 0))

        # Main frame
        self.MAINFRAME = CTkFrame(master=self, width=590, height=514, bg_color=("gray92", "#3e3e3e"), fg_color=("gray90", "#3e3e3e"))
        self.MAINFRAME.pack_propagate(False)
        self.MAINFRAME.pack(fill="both")

        self.LB_RECENTS = CTkLabel(master=self.MAINFRAME, text="Recording", height=54, text_color=("#ffffff", "#ffffff"), width=271, fg_color="transparent", bg_color="transparent", font=CTkFont(family="Courier New", size=25))
        self.LB_RECENTS.pack(pady=(20, 0))

        self.FILESFRAME = CTkFrame(master=self.MAINFRAME, fg_color="transparent", bg_color="transparent", width=500, height=155)
        self.FILESFRAME.pack_propagate(False)
        self.FILESFRAME.pack(pady=(0, 0), side="top")

        self.FILEFRAME1 = CTkFrame(master=self.FILESFRAME, width=150, height=150, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME1.pack_propagate(False)
        self.FILEFRAME1.pack(padx=(5, 0), side="left")

        self.BTN_VIEW = CTkButton(master=self.FILEFRAME1, text="Start", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14))
        self.BTN_VIEW.pack(side="top")

        self.FILEFRAME2 = CTkFrame(master=self.FILESFRAME, width=150, height=150, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME2.pack_propagate(False)
        self.FILEFRAME2.pack(padx=(5, 0), side="left")

        self.BTN_VIEW = CTkButton(master=self.FILEFRAME2, text="Stop", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14))
        self.BTN_VIEW.pack(side="top")
