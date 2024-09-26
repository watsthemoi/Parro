from tkinter import PhotoImage
from customtkinter import *
from newsheet.controller import NewSheetController
from newsheet.models import NewSheetModel
from univfuncts import UniversalPageFunctions
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

        self.controller = NewSheetController(self)   
        self.slide_anim = UniversalPageFunctions(self) 

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
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"),
                                  command=self.add_audio_file)
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
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"), 
                                  state="disabled", command=self.show_pbtf)
        self.BTN_PLAY.pack(padx=(10, 0), pady=(10, 0), anchor="w")
        self.BTN_EDIT = CTkButton(master=self.OPTIONSFRAME, text="Edit Composition", text_color=("#ffffff", "#ffffff"), 
                                  anchor="w", width=180, 
                                  image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
                                  size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"),
                                  state="disabled")
        self.BTN_EDIT.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.LB_HZLINE = CTkLabel(master=self.OPTIONSFRAME, 
                                  text="-----------------------------------------------------------------------------------", anchor="s", justify="center", height=0, text_color=("gray14", "#808080"), font=CTkFont(size=9))
        self.LB_HZLINE.pack(pady=(10, 0))

        # Mainframe
        self.MFRM = CTkFrame(master=self, width=590, height=514, bg_color=("gray92", "#3e3e3e"), 
                                  fg_color=("gray90", "#3e3e3e"))
        self.MFRM.pack_propagate(False)
        self.MFRM.pack(fill="both", expand=True)

        # Play Tools Frame; Accessed after Adding Audio and Successfully Producing Composition
        # self.PLAY_FRM = CTkFrame(master=self.MFRM, width=200, height=200, bg_color=("gray92", "#3e3e3e"), 
        #                          fg_color=("gray90", "#3e3e3e"))
        # self.PLAY_FRM.pack_propagate(False)
        # self.PLAY_FRM.pack(fill="both", expand=True)

        self.PLAY_BTN_FRM = CTkFrame(master=self.MFRM, width=200, height=200, bg_color=("gray92", "#3e3e3e"), 
                                    fg_color=("gray90", "#3e3e3e"))
        self.PLAY_BTN_FRM.pack_propagate(False)

        self.BTN_TRI = CTkButton(master=self.PLAY_BTN_FRM, text="PLAY", text_color=("#ffffff", "#ffffff"), 
                                  anchor="w", width=180, 
                                  image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
                                  size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_TRI.pack(padx=(10, 0), pady=(10, 0), anchor="w")
        self.BTN_STOP = CTkButton(master=self.PLAY_BTN_FRM, text="STOP", text_color=("#ffffff", "#ffffff"), 
                                  anchor="w", width=180, 
                                  image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
                                  size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_STOP.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        # Edit Tools Frame; Accessed after Successfully Producing Composition Clicking Edit Composition

        self.EDIT_BTN_FRM = CTkFrame(master=self.MFRM, width=200, height=200, bg_color=("gray92", "#3e3e3e"), 
                                    fg_color=("gray90", "#3e3e3e"))
        self.EDIT_BTN_FRM.place_forget()

        self.BTN_1 = CTkButton(master=self.EDIT_BTN_FRM, text="TEST", text_color=("#ffffff", "#ffffff"), 
                                  anchor="w", width=180, 
                                  image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
                                  size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_1.pack(padx=(10, 0), pady=(10, 0), anchor="w")
        self.BTN_1 = CTkButton(master=self.EDIT_BTN_FRM, text="TEST", text_color=("#ffffff", "#ffffff"), 
                                  anchor="w", width=180, 
                                  image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
                                  size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_1.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        # self.EDIT_FRM = CTkFrame(master=self.MFRM, width=200, height=200, bg_color=("gray92", "#3e3e3e"), 
        #                          fg_color=("gray90", "#3e3e3e"))
        #self.EDIT_FRM.pack_propagate(False)
        #self.EDIT_FRM.pack(fill="both", expand=True)

        #self.BTN_E1 = CTkButton(master=self.EDIT_FRM, text="Edit Composition", text_color=("#ffffff", "#ffffff"), 
        #                          anchor="w", width=180, 
        #                          image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
        #                          size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
        #                          hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        #self.BTN_E1.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        # Composition Frame
        self.COMP_FRM = CTkFrame(master=self.MFRM, width=590, height=514, bg_color=("gray92", "#3e3e3e"), 
                                  fg_color=("gray90", "#3e3e3e"))
        self.COMP_FRM.pack_propagate(False)
        self.COMP_FRM.pack(fill="both", expand=True) 

        self.LB_AUDIO_FILE = CTkLabel(master=self.COMP_FRM, text="No file selected", text_color=("#ffffff", "#ffffff"),
                                       font=CTkFont(size=15, family="Courier New"))
        self.LB_AUDIO_FILE.pack(padx=(10, 0), pady=(10, 0))

    def add_audio_file(self):
        """Add File Function"""
        file = self.controller.add_audio_file()    
        if file:  # Update the label if a file is selected
            self.LB_AUDIO_FILE.configure(text=file.split("/")[-1])  # Get the filename
            self.enable_buttons()  # Enable buttons after selecting a file

    def enable_buttons(self):
        """Enable the Play and Edit buttons."""
        self.BTN_PLAY.configure(state="normal")
        self.BTN_EDIT.configure(state="normal")    

     # Showing and hiding Play Mode
    def show_pbtf(self):
        self.slide_anim.slide(self.PLAY_BTN_FRM, self.COMP_FRM, direction="left")

#    def slide_down(self, position):
#        if position < 0:  # Continue sliding until it reaches y = 0
#            self.PLAY_BTN_FRM.place(y=position)
#            self.COMP_FRM.place(y=position + 100)  # Push COMP_FRM down by the height of PLAY_PAUSE_FRM
#            self.after(10, self.slide_down, position + 5)  # Call again with updated position
#        else:
#            self.PLAY_BTN_FRM.place(y=0)  # Ensure it's placed correctly at the end
#            self.COMP_FRM.place(y=100)  # Correct position of COMP_FRM  
    

    def go_home(self, event=None):
        # Call the controller's method to switch to the home page
        self.master.show_homepage()    