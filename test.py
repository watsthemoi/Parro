import muspy
import fluidsynth
import matplotlib.pyplot as plt

# Load the MIDI file
music_data = muspy.read_midi('bach_846.mid')

def segment_measures(music_data, beats_per_measure, measures_per_segment=3):
    # Get the resolution (ticks per beat)
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

# Parameters for segmentation
beats_per_measure = 4  # Assuming 4/4 time signature
measures_per_segment = 3  # You want 3 measures per segment

# Segment the music data into segments of 3 measures each
segments = segment_measures(music_data, beats_per_measure, measures_per_segment)

# Plot all segments as one continuous score
for segment in segments:
    muspy.show_score(segment)
    plt.show() 