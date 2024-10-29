class NewSheetModel:
    def __init__(self):
        self.audio_infile = None
        self.audio_outfile = None
        self.note_events = []

        self.xml = None

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
    
    def store_score_parse(self, xml):
        """Store the xml file of the parsed midi"""
        self.score = xml

    def re_score_parse(self):
        """Returns the xml file of the parsed midi"""
        return self.score()    