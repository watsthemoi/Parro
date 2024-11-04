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
            project_dir = os.path.dirname(os.path.abspath("TranscriptApp/"))
            muse_path_win = r"bin\MuseScore 4\bin\MuseScore4.exe"
            muse_path_mac = os.path.join(project_dir, "bin", "musescore", "MuseScore 4.app", "Contents", "MacOS", "mscore")
            name, ext = os.path.splitext(midi_path)

            # Set the environment and user settings explicitly
            # Path depends on OS
            us = environment.UserSettings()
            if platform.system() == "Darwin":  # macOS
                us['musicxmlPath'] = muse_path_mac
                us['musescoreDirectPNGPath'] = muse_path_mac
                us['musicxmlPath'] 
            
            else:  # Windows or other OS
                us['musicxmlPath'] = os.path.join(project_dir, muse_path_win)
                us['musescoreDirectPNGPath'] = os.path.join(project_dir, muse_path_win)
                us['musicxmlPath']

            # Write the file and save it towards the filepath
            score_file_path = os.path.join(project_dir, f"{name}")
            score.write('musicxml.png', fp=score_file_path)

            if os.path.exists(f"{name}-1.png"):
                return self.update_view_with_score(f"{name}-1.png")
            else:
                print("Failed to generate score image.")

        except Exception as e:
            raise e
        
    def add_white_padding(self, image):
        """Add white padding to the top of the image."""
        width, height = image.size

        # Create a new image with a white background
        new_height = height + 20
        padded_image = Image.new('RGB', (width, new_height), (255, 255, 255))  # White background

        # Paste the original image on the new image, shifted down to create top padding
        padded_image.paste(image, (0, 20))

        return padded_image

    def crop_image(self, image, padding=20):
        bg = Image.new(image.mode, image.size, (255, 255, 255))  # White background for comparison
        diff = ImageChops.difference(image, bg)
        bbox = diff.getbbox()  # Find the bounding box of the non-white areas

        if bbox:
            # Add padding to the bounding box
            left, upper, right, lower = bbox
            left = max(left - padding, 0)
            upper = max(upper - padding, 0)
            right = min(right + padding, image.width)
            lower = min(lower + padding, image.height)

            # Crop the image with the padded bounding box
            return image.crop((left, upper, right, lower))

        return image  # Return original image if no white space detected
    
    def scale_image(self, image, max_width, max_height):
        """Scale the image down to fit within max_width and max_height, maintaining aspect ratio."""
        # Get the original dimensions of the image
        width, height = image.size

        # Calculate the aspect ratio
        aspect_ratio = width / height

        # Determine the new width and height while maintaining the aspect ratio
        if width > max_width or height > max_height:
            # Check if the image is wider or taller than the allowed dimensions
            if aspect_ratio > 1:
                # Wider than tall, scale by width
                new_width = max_width
                new_height = int(max_width / aspect_ratio)
            else:
                # Taller than wide, scale by height
                new_height = max_height
                new_width = int(max_height * aspect_ratio)
        else:
            # The image is smaller than the max dimensions, so return it as is
            return image

        # Resize the image while maintaining the aspect ratio
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    def update_view_with_score(self, png_path):
        """Display the rendered score (PDF or PNG) in the view."""
        try:
            image = Image.open(png_path)
            if image:  
                cropped_image = self.crop_image(image)
                padded_image = self.add_white_padding(cropped_image)

                # Scale the image down while maintaining the aspect ratio (e.g., max width and height of 400)
                scaled_image = self.scale_image(padded_image, max_width=800, max_height=800)
                img_tk = ImageTk.PhotoImage(scaled_image)

                self.root.score_display.configure(image=img_tk, text='')  # Update the image in the view
                self.root.score_display.image = img_tk  # Keep a reference to avoid garbage collection

        ### Poppler omitted code:
        #   # For simplicity, convert the PDF's first page to an image using Pillow
            # You need to install 'pdf2image' package for this (pip install pdf2image)
            #from pdf2image import convert_from_path

            #project_dir = os.path.dirname(os.path.abspath("TranscriptApp/"))
            #if platform.system() == "Darwin": 
            #    poppler_path = os.path.join(project_dir, 'bin', 'poppler', '24.04.0_1', 'bin')
            #else:
            #    poppler_path = os.path.join(project_dir, 'bin', 'poppler-24.08.0', 'Library', 'bin')

            #images = convert_from_path(pdf_path, poppler_path=poppler_path)
        
         

        except Exception as e:
            print(f"Error displaying score: {e}")    

