import basic_pitch
from basic_pitch.inference import predict
from basic_pitch.note_creation import model_output_to_notes
from basic_pitch import ICASSP_2022_MODEL_PATH
from tkinter import PhotoImage, messagebox
from customtkinter import *
import customtkinter as ctk
from newsheet.controller import NewSheetController
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
        self.note_events = []   

        self.MFRM = CTkFrame(master=self, width=225, fg_color=("#212121", "#212121"), 
                             bg_color=("#212121", "#212121"))
        self.MFRM.pack()

        self.BTN_ADD = CTkButton(master=self.MFRM, text="Add Audio", text_color=("#ffffff", "#ffffff"), 
                                  width=180, 
                                  image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), 
                                  size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"),
                                  command=self.add_audio_file)
        self.BTN_ADD.pack(padx=(10, 0), pady=(10, 0))   

        # Add a placeholder to display the score (PNG)
        self.score_display = CTkLabel(self.MFRM, text="Score will appear here")
        self.score_display.pack(padx=(10, 0), pady=(20, 0))

        self.BTN_EDIT = CTkButton(master=self.MFRM, text="Edit", text_color=("#ffffff", "#ffffff"), 
                                  width=180, fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), 
                                  hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"),
                                  command=self.edit_mode)
        self.BTN_EDIT.pack(padx=(10, 0), pady=(15, 0))   

        # Entry bar and confirmation button. Hidden until edit is pressed.
        self.highlight_bar = CTkEntry(master=self.MFRM)
        self.highlight_bar.pack_forget()
        self.BAR_CONFIRM = CTkButton(master=self.MFRM, text="Confirm", command=self.highlight)
        self.BAR_CONFIRM.pack_forget()

        # Measure information display frame
        self.display_info = CTkFrame(master=self.MFRM)
        self.display_info.pack_forget()
        self.clef_lb = CTkLabel(master=self.display_info, text="Clef: ")
        self.clef_lb.pack(pady=5)
        self.ts_lb = CTkLabel(master=self.display_info, text="Time Signature: ")
        self.ts_lb.pack(pady=5)
        self.ks_lb = CTkLabel(master=self.display_info, text="Key: ")
        self.ks_lb.pack(pady=5)
        self.notes_lb = CTkLabel(master=self.display_info, text="Notes: ")
        self.notes_lb.pack(pady=5) 

    def add_audio_file(self):
        """Add File Function to Controller"""
        self.controller.add_audio_file()
        
    def edit_mode(self):
        """Prompts user for measure that they want to edit. 
           After choice, it highlights the measure (shows elements of it as labels)."""
        self.highlight_bar.pack(pady=5)
        self.BAR_CONFIRM.pack(pady=5)

    def highlight(self):
        """Calls controller function to find and highlight measure, and return bar information."""
        self.highlight_bar.pack_forget()
        self.BAR_CONFIRM.pack_forget()

        c, ts, ks, n = self.controller.highlight(self.highlight_bar.get().strip().upper()) 

        # Configure labels with information
        if c:
            self.clef_lb.configure(text=f"Clef: {c}")
            self.clef_lb.pack(pady=5)
        if ts:
            self.ts_lb.configure(text=f"Time Signature: {ts}")
            self.ts_lb.pack(pady=5)
        if ks:
            self.ks_lb.configure(text=f"Key Signature: {ks}")
            self.ks_lb.pack(pady=5)  
        if n:    
            self.notes_lb.configure(text=f"Notes: {n}")
            self.notes_lb.pack(pady=5)

        self.display_info.pack(pady=5)