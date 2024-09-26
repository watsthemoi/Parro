

class NewSheetModel:
    def __init__(self):
        self.audio_file = None
        self.play_mode = False # Page mode after pressing play

    def store_file(self, file):
        """Store the selected file's path in the model."""
        self.audio_file = file

    def get_file(self):
        """Retrieve the stored file's path."""
        return self.audio_file

