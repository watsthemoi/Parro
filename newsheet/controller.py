import customtkinter as ctk
from tkinter import filedialog, messagebox
from newsheet.models import NewSheetModel
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import os
import platform
from music21 import converter, environment, lily
import os
import time
import subprocess
from PIL import Image, ImageTk, ImageChops

class NewSheetController:
    def __init__(self, root):
        self.models = NewSheetModel()
        self.note_events = []
        self.file = " "
        midi_file = "midifile.mid"
        self.root = root

    def add_audio_file(self):
        # Open file dialog to select an audio file
        # Detect OS
        if platform.system() == "Darwin":  # macOS
            file = filedialog.askopenfilename(
            title="Select an Audio File"
        )
        else:  # Windows or other OS
            file = filedialog.askopenfilename(
                title="Select an Audio File",
                filetypes=(("Audio Files", "*.mp3;*.wav"), ("All Files", "*.*"))
        )

        if file:
            try:
                # Store the file in the model
                self.models.store_infile(file)
                return self.process_file(file)
            except Exception as e:
                messagebox.showerror("Error", f"File Access Error: {e}")
        return None
            
    def process_file(self, file):
        """Processes file for pitch data with predict()"""
        try:
            model_output, midi_data, note_events = predict(file, ICASSP_2022_MODEL_PATH)
            
            self.note_events.extend(note_events)  # Store note events
            self.models.store_note_events(note_events)    

            file_str = os.path.basename(file)
            name, _ = os.path.splitext(file_str)
            midi_data.write(f'{name}.mid')
            
            time.sleep(1)
            # Generate the score using music21
            self.generate_music21_score(f"{name}.mid")

            return note_events
        except Exception as e:
            raise e                

    def generate_music21_score(self, midi_path):
        """Convert MIDI to music21 score and render as LilyPond"""
        try:
            # Parse the MIDI file with music21
            score = converter.parse(midi_path)

            # Set the path to the bundled LilyPond binary
            # No executable needed in PATH for MacOS
            project_dir = os.path.dirname(os.path.abspath("TranscriptApp/"))

            # Set the environment and user settings explicitly
            us = environment.UserSettings()
            us['musicxmlPath'] = r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe'
            us['musescoreDirectPNGPath'] = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"
            us['musicxmlPath']

            # Save the LilyPond file and specify PNG output
            score_file_path = os.path.join(project_dir)
            score.write('musicxml.png', fp=score_file_path)

        except Exception as e:
            raise e
        