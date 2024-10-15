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

        self.MFRM = CTkFrame(master=self, width=225, fg_color=("#212121", "#212121"), bg_color=("#212121", "#212121"))
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

    def add_audio_file(self):
        """Add File Function"""
        self.controller.add_audio_file()
        #if note_events is not None:
            #self.update_note_events_display(note_events)

    #def update_note_events_display(self, note_events):
        #"""Update the display with note events"""
        #self.score_display.delete("1.0", "end")  # Clear previous content
        #for index, item in enumerate(note_events):
            #self.score_display.insert("end", f"{index + 1}: {item}\n")  # Show note events in textbox              

#    def midi_to_note_octave(self, midi_pitch):
#        # List of note names in an octave (C, C#, D, D#, E, F, F#, G, G#, A, A#, B)
#        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
#
#        # Determine the note and the octave
#        note = note_names[midi_pitch % 12]  # Use modulo 12 to get the note within an octave
#        octave = (midi_pitch // 12) - 1     # MIDI pitch 60 is C4 (middle C), hence subtracting 1
#
#        return note, octave
#
#    # Function to sort note_events by start time and end time
#    def sort_note_events(self, note_events):
#        # Sort by start_time (event[0]), and if necessary by end_time (event[1])
#        return sorted(note_events, key=lambda event: (event[0], event[1]))
#
#    # Example usage after running predict()
#
#    # Provide the path to your input audio file (.wav)
#    audio_file_path = (r"C:\Users\newcr\Documents\baspit\Audio\FLKeysTest3.wav")  # Replace with your actual file path
#
#    # Run the prediction function to get model_output, midi_data, and note_events
#    model_output, midi_data, note_events = predict(audio_file_path)
#
#    print(note_events)

#    # Sort the note events
#    sorted_note_events = sort_note_events(note_events)
#
#    # Now you can print the sorted events
#    for event in sorted_note_events:
#        start_time, end_time, midi_pitch, velocity, _ = event
#        print(f"Start: {start_time:.3f}, End: {end_time:.3f}, Pitch: {midi_pitch}, Velocity: {velocity}")
#
#    for event in sorted_note_events:
#        midi_pitch = event[2]  # Extract the midi_pitch from each event
#        note, octave = midi_to_note_octave(midi_pitch)
#        print(f"MIDI Pitch: {midi_pitch} -> Note: {note}{octave}")