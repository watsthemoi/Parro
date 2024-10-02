class NewSheetModel:
    def __init__(self):
        self.audio_infile = None
        self.audio_outfile = None
        self.note_events = []

    def store_infile(self, file):
        """Store the selected file's path in the model."""
        self.audio_infile = file

    def store_outfile(self, file):
        """Store the resulting MIDI of the processing"""
        self.audio_outfile = file

    def store_note_events(self, note_events):
        """Store note events"""
        self.note_events = note_events

    def get_infile(self):
        """Retrieve the stored input file"""
        return self.audio_infile
    
    def get_outfile(self):
        """Retrieve the resulting MIDI file"""
        return self.audio_outfile
    
