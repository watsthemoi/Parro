

class NewSheetModel:
    def __init__(self):
        self.audio_file_path = None

    def store_file(self, file_path):
        """Store the selected file's path in the model."""
        self.audio_file_path = file_path

    def get_file(self):
        """Retrieve the stored file's path."""
        return self.audio_file_path

