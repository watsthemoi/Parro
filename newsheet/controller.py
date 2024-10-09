import customtkinter as ctk
from tkinter import filedialog, messagebox
from newsheet.models import NewSheetModel
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

class NewSheetController:
    def __init__(self, root):
        self.models = NewSheetModel()
        self.note_events = []

    def add_audio_file(self):
        # Open file dialog to select an audio file
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
            model_output, midi_data, note_events = predict(file)
            self.note_events.extend(note_events)  # Store note events
            self.models.store_note_events(note_events)    
            return note_events
        except Exception as e:
            raise e       
