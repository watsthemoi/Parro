
import os
from music21 import *


# Parse the MIDI file with music21
scorexml = converter.parse("recording.musicxml")

# Set the path to the bundled MuseScore
project_dir = os.path.dirname(os.path.abspath("TranscriptApp/"))
muse_path_win = r"bin\MuseScore 4\bin\MuseScore4.exe"
name, ext = os.path.splitext("recording.musicxml")

# Set the environment and user settings explicitly
            
us = environment.UserSettings()
us['musicxmlPath'] = os.path.join(project_dir, muse_path_win)
us['musescoreDirectPNGPath'] = os.path.join(project_dir, muse_path_win)
us['musicxmlPath']

def add_bar(xml):
    try:
        for part in xml.parts:
            new_measure = stream.Measure()
            new_measure.number = len(part.getElementsByClass(stream.Measure)) + 1  # Sequential measure number
            part.append(new_measure)
        xml.write('musicxml', 'modified_file.musicxml')
    except Exception as e:
        print(f"Error while writing MusicXML: {e}")

def remove_bar(xml):
    """In this example, the new bar (3) will be removed"""  
    try:
        for part in xml.parts:
            measure_delete = part.measure(2)
            if measure_delete:
                part.remove(measure_delete)
        xml.write('musicxml', 'mod_file2.musicxml')
    except Exception as e:
        print(f"Error while writing MusicXML: {e}")   

def add_note(xml):
    try:
        for part in xml.parts:
            chosen = part.measure(-1) # Notice: measures is not the same as measure. This denotes final bar
            if chosen:
                chosen.append(note.Note('A4', quarterLength=1.0))          
        xml.write('musicxml', 'mod_file2a.musicxml')        
    except Exception as e:
        print(f"Error while writing MusicXML: {e}")        

def remove_note(xml):
    try:
        for part in xml.parts:
            chosen = part.measure(1) 
            if chosen:
                for n in chosen.notes:
                    if n.name == 'F':
                        chosen.remove(n)
                        break     
        xml.write('musicxml', 'mod_file2ar.musicxml')             
    except Exception as e:
        print(f"Error while writing MusicXML: {e}")  

add_bar(scorexml)
score2 = converter.parse('modified_file.musicxml')
remove_bar(score2)    
score3 = converter.parse('mod_file2.musicxml')
add_note(score3)
score4 = converter.parse('mod_file2a.musicxml')
remove_note(score4)