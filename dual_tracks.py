import muspy
import matplotlib.pyplot as plt
from matplotlib import gridspec

# Load the MIDI file (replace with your file path)
music_data = muspy.read_midi('bach_846.mid')

# Function to segment by measures (same as before)
def segment_measures(music_data, beats_per_measure, measures_per_segment=3):
    ticks_per_beat = music_data.resolution
    ticks_per_measure = beats_per_measure * ticks_per_beat
    ticks_per_segment = ticks_per_measure * measures_per_segment

    segments = []
    start_tick = 0
    max_tick = max(note.time + note.duration for track in music_data.tracks for note in track.notes)
    while start_tick < max_tick:
        segment = muspy.Music(tracks=[], resolution=music_data.resolution, metadata=music_data.metadata)
        for track in music_data.tracks:
            new_track = muspy.Track(program=track.program, is_drum=track.is_drum, name=track.name)
            # Ensure notes spanning across segments are handled properly
            for note in track.notes:
                if start_tick <= note.time < start_tick + ticks_per_segment or \
                   start_tick < note.time + note.duration <= start_tick + ticks_per_segment:
                    new_track.notes.append(note)
            segment.tracks.append(new_track)
        segments.append(segment)
        start_tick += ticks_per_segment

    return segments

# Parameters
beats_per_measure = 2 
measures_per_segment = 10  # 3 measures per segment

# Segment the music data
segments = segment_measures(music_data, beats_per_measure, measures_per_segment)

# Create a figure with gridspec to have two rows per segment
fig = plt.figure(figsize=(20, len(segments)*4))
gs = gridspec.GridSpec(len(segments) * 2, 1)  # 2 rows per segment

# Plot each segment
for i, segment in enumerate(segments):
    #if (len(segment.notes) == 0):
    # Plot bass clef first
    ax_bass = fig.add_subplot(gs[i * 2, 0])
    
    # Plot treble clef second
    ax_treble = fig.add_subplot(gs[i * 2 + 1, 0])

    # Assign tracks[0] to Piano right and tracks[1] to Piano left
    piano_right = segment.tracks[0]  # Piano right is in treble clef
    piano_left = segment.tracks[1]   # Piano left is in bass clef
    piano_left.transpose(12)

    # Plot the notes in their respective clefs
    muspy.show_score(music=muspy.Music(tracks=[piano_left], resolution=segment.resolution, metadata=segment.metadata), 
                     fig=fig, ax=ax_bass, note_spacing=8, clef="bass", clef_octave=1)
    muspy.show_score(music=muspy.Music(tracks=[piano_right], resolution=segment.resolution, metadata=segment.metadata), 
                     fig=fig, ax=ax_treble, clef="treble", clef_octave=0)

# Final display
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Remove padding between edges
plt.show()
