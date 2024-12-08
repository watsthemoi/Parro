from tkinter import PhotoImage
from customtkinter import *
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import librosa.display
import platform
from newrecord.controller import Recorder

class NewRecordView(CTkFrame):  # Inheriting from CTkFrame instead of CTk
    rec = Recorder(channels=1)
    running = None
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

        self.LB_COMPOSITIONS = CTkLabel(master=self.OPTIONSFRAME, text="File", height=25, text_color=("#ffffff", "#ffffff"), font=CTkFont(size=15, family="Courier New", weight="bold"))
        self.LB_COMPOSITIONS.pack(padx=(15, 0), pady=(10, 0), anchor="w")

        self.BTN_SAVE = CTkButton(master=self.OPTIONSFRAME, text="Save", text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_save_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_SAVE.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.BTN_DELETE = CTkButton(master=self.OPTIONSFRAME, text="Delete", text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_delete_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_DELETE.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.BTN_NEW = CTkButton(master=self.OPTIONSFRAME, text="New", text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_plus_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_NEW.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.LB_HZLINE = CTkLabel(master=self.OPTIONSFRAME, text="-----------------------------------------------------------------------------------", anchor="s", justify="center", height=0, text_color=("gray14", "#808080"), font=CTkFont(size=9))
        self.LB_HZLINE.pack(pady=(10, 0))

        self.LB_SOURCE = CTkLabel(master=self.OPTIONSFRAME, text="Audio Source", height=25, text_color=("#ffffff", "#ffffff"), font=CTkFont(size=15, family="Courier New", weight="bold"))
        self.LB_SOURCE.pack(padx=(15, 0), pady=(20, 0), anchor="w")

        self.BTN_CAS = CTkButton(master=self.OPTIONSFRAME, text="Input Source", text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_source_settings_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_CAS.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        self.LB_HZLINE = CTkLabel(master=self.OPTIONSFRAME, text="-----------------------------------------------------------------------------------", anchor="s", justify="center", height=0, text_color=("gray14", "#808080"), font=CTkFont(size=9))
        self.LB_HZLINE.pack(pady=(10, 0))

        self.LB_COMPOSITIONS = CTkLabel(master=self.OPTIONSFRAME, text="Export", height=25, text_color=("#ffffff", "#ffffff"), font=CTkFont(size=15, family="Courier New", weight="bold"))
        self.LB_COMPOSITIONS.pack(padx=(15, 0), pady=(20, 0), anchor="w")

        self.BTN_CONVERT = CTkButton(master=self.OPTIONSFRAME, text="Create Score", text_color=("#ffffff", "#ffffff"), anchor="w", width=180, image=CTkImage(Image.open(r"assets/Assets/baseline_open_new_(255, 255, 255)_18dp_1x.png"), size=(18, 18)), fg_color=("#212121", "gray13"), bg_color=("#212121", "gray13"), hover_color=("#ff8080", "#ff5e5e"), font=CTkFont(size=15, family="Courier New"))
        self.BTN_CONVERT.pack(padx=(10, 0), pady=(10, 0), anchor="w")

        # Main frame
        self.MAINFRAME = CTkFrame(master=self, width=590, height=514, bg_color=("gray92", "#3e3e3e"), fg_color=("gray90", "#3e3e3e"))
        self.MAINFRAME.pack_propagate(False)
        self.MAINFRAME.pack(fill="both", expand=True)

        self.LB_REC = CTkLabel(master=self.MAINFRAME, text="Recording", height=54, text_color=("#ffffff", "#ffffff"), width=271, fg_color="transparent", bg_color="transparent", font=CTkFont(family="Courier New", size=25))
        self.LB_REC.pack(pady=(20, 0))

        self.FILESFRAME = CTkFrame(master=self.MAINFRAME, fg_color="transparent", bg_color="transparent", width=500, height=100)
        self.FILESFRAME.pack_propagate(False)
        self.FILESFRAME.pack(pady=(0, 0), side="top")

        self.FILEFRAME1 = CTkFrame(master=self.FILESFRAME, width=100, height=100, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME1.pack_propagate(False)
        self.FILEFRAME1.pack(padx=(5, 0), side="left")

        self.BTN_VIEW = CTkButton(master=self.FILEFRAME1, text="Start", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14), command=self.start)
        self.BTN_VIEW.pack(pady=(20, 0), side="top", anchor="e")

        self.FILEFRAME2 = CTkFrame(master=self.FILESFRAME, width=100, height=100, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME2.pack_propagate(False)
        self.FILEFRAME2.pack(padx=(5, 0), side="left")

        self.BTN_VIEW = CTkButton(master=self.FILEFRAME2, text="Stop", fg_color=("#c0c0c0", "#808080"), bg_color="transparent", hover_color=("#808080", "#2a2a2a"), width=100, font=CTkFont(family="Courier New", size=14), command=self.stop)
        self.BTN_VIEW.pack(pady=(20, 0), side="top", anchor="w")

        self.FILEFRAME3 = CTkFrame(master=self.FILESFRAME, width=400, height=70, fg_color="transparent", bg_color="transparent")
        self.FILEFRAME3.pack_propagate(False)
        self.FILEFRAME3.pack(padx=(50, 0))

        self.LB_LEFT = CTkLabel(master=self.FILEFRAME3, text="-30dB")
        self.LB_LEFT.pack(padx=(0,0), side="left", anchor="w")
        self.LB_RIGHT = CTkLabel(master=self.FILEFRAME3, text="+30dB")
        self.LB_RIGHT.pack(padx=(0,0), side="right", anchor="e")
        self.SLDR_GAINCONTROL = CTkSlider(master=self.FILEFRAME3, width=250, from_=-30, to=30, number_of_steps=20, button_color="#ffffff", button_hover_color="#ffffff")
        self.SLDR_GAINCONTROL.set(0)
        self.SLDR_GAINCONTROL.pack(padx=(0, 0), pady=(0,0), side="left")

        self.AUD_FRM = CTkFrame(master=self.MAINFRAME, width=300, height=200, bg_color=("gray92", "#3e3e3e"), fg_color=("gray90", "#3e3e3e"))
        self.AUD_FRM.pack_propagate(False)
        self.AUD_FRM.pack(fill="both")

        # Initialize Matplotlib Figure
        self.fig, self.ax = plt.subplots(figsize=(5, 2))
        self.fig.patch.set_facecolor("#3e3e3e")
        self.ax.set_facecolor("#3e3e3e")
        self.ax.axis('off')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.AUD_FRM)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def go_home(self, event=None):
        # Call the controller's method to switch to the home page
        self.master.show_homepage()

    def start(self):
        global running
        if self.running is None:
            self.running = NewRecordView.rec.open('recording.wav', 'wb')
            self.running.start_recording()
            self.update_waveform()
            
    def stop(self):
        global running
        if self.running is not None:
            self.running.stop_recording()
            self.running.close()
            self.running = None

    def update_waveform(self):
        if self.running is not None:
            # Clear the plot
            self.ax.clear()

            # Set the background color of the plot to match the app
            self.ax.set_facecolor("#3e3e3e")  # Use the desired gray color for background

            # Get the current audio data
            audio_data = self.running.get_audio_data()

            if len(audio_data) > 0:
                # Ensure the audio data is flattened (1D array) before plotting
                flattened_audio = audio_data.flatten()

                # Down Sample the audio to make it look better on the graph
                down_sampled_audio = librosa.resample(flattened_audio, orig_sr=self.rec.rate, target_sr=self.rec.rate // 10)

                # Plot the waveform using librosa with white line for the waveform
                librosa.display.waveshow(down_sampled_audio, sr=self.rec.rate, ax=self.ax, color='white', linewidth=3)

                # Set axis limits to ensure the waveform is visible
                self.ax.set_ylim([-1, 1])  # Adjust this range based on your data scale

            self.ax.axis('off')

            # Redraw the canvas
            self.canvas.draw()

        # Schedule the next update if still running
        self.after(100, self.update_waveform)
