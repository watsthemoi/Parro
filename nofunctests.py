import muspy
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.axes import Axes

# Load the MIDI file
music_data = muspy.read_midi('bach_846.mid')

muspy.show_score(music_data)

# Final display
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Remove padding between edges
plt.show()
