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

        self.BTN_NEWCOMP = CTkButton(master=self.OPTIONSFRAME, text="New Composition", fg_color=("#212121", "#212121"), 
                                     text_color=("#ffffff", "#ffffff"), anchor="w", width=180, 
                                     image=CTkImage(Image.open(r"assets/Assets/baseline_music_note_(255, 255, 255)_18dp_1x.png"), 
                                     size=(18, 18)), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), 
                                     font=CTkFont(size=15, family="Courier New"), command=self.show_sheet)
        self.BTN_NEWCOMP.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.BTN_NEWRECORDING = CTkButton(master=self.OPTIONSFRAME, text="New Recording", fg_color=("#212121", "#212121"), text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_mic_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"), command= self.show_record)
        self.BTN_NEWRECORDING.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.LB_HZLINE = CTkLabel(master=self.OPTIONSFRAME, text="-----------------------------------------------------------------------------------", anchor="s", justify="center", height=0, text_color=("gray14", "#808080"), font=CTkFont(size=9))
        self.LB_HZLINE.pack(pady=(22,0))

        self.LB_RECORDINGS = CTkLabel(master=self.OPTIONSFRAME, text="Recordings", height=25, fg_color=("#212121", "#212121"), bg_color=("#212121", "gray13"), text_color=("#ffffff", "#ffffff"), font=CTkFont(family="Courier New", size=16, weight="bold"))
        self.LB_RECORDINGS.pack(padx=(15, 0), pady=(20, 0), anchor="w")
        self.BTN_RESUMERECORDING = CTkButton(master=self.OPTIONSFRAME, text="Edit Recording", fg_color=("#212121", "#212121"), text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_tune_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_RESUMERECORDING.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.LB_HZLINE = CTkLabel(master=self.OPTIONSFRAME, text="-----------------------------------------------------------------------------------", anchor="s", justify="center", height=0, text_color=("gray14", "#808080"), font=CTkFont(size=9))
        self.LB_HZLINE.pack(pady=(22,0))

        self.LB_COMPOSITIONS = CTkLabel(master=self.OPTIONSFRAME, text="Compositions", height=25, fg_color=("#212121", "#212121"), bg_color=("#212121", "gray13"), text_color=("#ffffff", "#ffffff"), font=CTkFont(size=16, family="Courier New", weight="bold"))
        self.LB_COMPOSITIONS.pack(padx=(15, 0), pady=(20, 0), anchor="w")
        self.BTN_RESUMECOMPOSITION = CTkButton(master=self.OPTIONSFRAME, text="Edit Composition", 
                                               fg_color=("#212121", "#212121"), text_color=("#ffffff", "#ffffff"), 
                                               anchor="w", width=180, 
                                               image=CTkImage(Image.open(r"assets/Assets/baseline_edit_(255, 255, 255)_18dp_1x.png"), 
                                               size=(18, 18)), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), 
                                               font=CTkFont(size=15, family="Courier New"))
        self.BTN_RESUMECOMPOSITION.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.MAINFRAME = CTkFrame(master=self, width=590, height=514, bg_color=("gray92", "#3e3e3e"), fg_color=("gray90", "#3e3e3e"))
        self.MAINFRAME.pack_propagate(False)
        self.MAINFRAME.pack(fill="both", expand=True)

        self.LB_RECENTS = CTkLabel(master=self.MAINFRAME, text="Recently Viewed", height=54, text_color=("#ffffff", "#ffffff"), width=271, fg_color="transparent", bg_color="transparent", font=CTkFont(family="Courier New", size=25))
        self.LB_RECENTS.pack(pady=(20, 0))

        self.FILESFRAME = CTkFrame(master=self.MAINFRAME, fg_color="transparent", bg_color="transparent", width=500, height=155)
        self.FILESFRAME.pack_propagate(False)
        self.FILESFRAME.pack(pady=(0, 0), side="top")

        self.FILEFRAME1 = CTkFrame(master=self.FILESFRAME, width=150, height=150, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME1.pack_propagate(False)
        self.FILEFRAME1.pack(padx=(5, 0), side="left")
        self.BTN_VIEW = CTkButton(master=self.FILEFRAME1, text="Open", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14))
        self.BTN_VIEW.pack(side="bottom")

        self.FILEFRAME2 = CTkFrame(master=self.FILESFRAME, width=150, height=150, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME2.pack_propagate(False)
        self.FILEFRAME2.pack(pady=(0, 0), padx=(20, 0), side="left")
        self.BTN_VIEW = CTkButton(master=self.FILEFRAME2, text="Open", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14))
        self.BTN_VIEW.pack(side="bottom")

        self.FILEFRAME3 = CTkFrame(master=self.FILESFRAME, width=150, height=150, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME3.pack_propagate(False)
        self.FILEFRAME3.pack(pady=(0, 0), padx=(20, 0), side="left")
        self.BTN_VIEW = CTkButton(master=self.FILEFRAME3, text="Open", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14))
        self.BTN_VIEW.pack(side="bottom")

        self.FILESFRAME2 = CTkFrame(master=self.MAINFRAME, fg_color="transparent", bg_color="transparent", width=500, height=275)
        self.FILESFRAME2.pack_propagate(False)
        self.FILESFRAME2.pack(pady=(0, 0), side="bottom")

        self.FILEFRAME4 = CTkFrame(master=self.FILESFRAME2, width=150, height=150, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME4.pack_propagate(False)
        self.FILEFRAME4.pack(padx=(5, 0), side="left")
        self.BTN_VIEW = CTkButton(master=self.FILEFRAME4, text="Open", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14))
        self.BTN_VIEW.pack(side="bottom")

        self.FILEFRAME5 = CTkFrame(master=self.FILESFRAME2, width=150, height=150, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME5.pack_propagate(False)
        self.FILEFRAME5.pack(pady=(0, 0), padx=(20, 0), side="left")
        self.BTN_VIEW = CTkButton(master=self.FILEFRAME5, text="Open", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14))
        self.BTN_VIEW.pack(side="bottom")

        self.FILEFRAME6 = CTkFrame(master=self.FILESFRAME2, width=150, height=150, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME6.pack_propagate(False)
        self.FILEFRAME6.pack(pady=(0, 0), padx=(20, 0), side="left")
        self.BTN_VIEW = CTkButton(master=self.FILEFRAME6, text="Open", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14))
        self.BTN_VIEW.pack(side="bottom")

    def show_record(self):
        # Change to recording view
        self.master.show_newrecord()

    def show_sheet(self):
        # Change to composition view
        self.master.show_newsheet()        
