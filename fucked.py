import muspy
import matplotlib.pyplot as plt

# Load the MIDI file
music_data = muspy.read_midi('bach_846.mid')

# Function to segment by measures (same as before)
def segment_measures(music_data, beats_per_measure, measures_per_segment=4):
    ticks_per_beat = music_data.resolution
    ticks_per_measure = beats_per_measure * ticks_per_beat
    ticks_per_segment = ticks_per_measure * measures_per_segment

    segments = []
    start_tick = 0
    max_tick = max(note.time for track in music_data.tracks for note in track.notes)

    while start_tick < max_tick:
        segment = muspy.Music(tracks=[], resolution=music_data.resolution, metadata=music_data.metadata)
        for track in music_data.tracks:
            new_track = muspy.Track(program=track.program, is_drum=track.is_drum)
            new_track.notes = [note for note in track.notes if start_tick <= note.time < start_tick + ticks_per_segment]
            segment.tracks.append(new_track)
        segments.append(segment)
        start_tick += ticks_per_segment

    return segments

# Parameters
beats_per_measure = 4  # Assuming 4/4 time signature
measures_per_segment = 4  # 3 measures per segment

# Segment the music data
segments = segment_measures(music_data, beats_per_measure, measures_per_segment)

# Create a single figure
fig, ax = plt.subplots(figsize=(20, len(segments)*2))  # Adjust height dynamically based on number of segments


for i, segment in enumerate(segments):
    # Pass the same figure but shift the axis vertically
    ax = fig.add_subplot(len(segments), 1, i+1)  # Create subplots in one figure, stacked vertically
    muspy.show_score(segment, fig=fig, ax=ax, font_scale=180)  # Use the customized ax
    # Ensure all axis elements are removed

# Final display
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.show()
