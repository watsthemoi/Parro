<div id="user-content-toc">
  <ul align="center" style="list-style: none;">
    <summary>
      <h1>PARRO</h1>
    </summary>
  </ul>
</div>

### *Exploring a Software Solution to Music Theory Analysis and Visualization*
---
Parro is built using the [music21 toolkit for musical analysis and computational musicology](https://github.com/cuthbertLab/music21). The intent of Parro is to assist music theory learning with a hands-on approach, where user's can upload any audio track and receive a rendered composition that can be saved and edited.
Parro utlizes [Spotify's basic-pitch library](https://github.com/spotify/basic-pitch/tree/main) to extract MIDI data from audio files.  

### *Setting Up*
---
Download MuseScore 4 and add the application folder to the /bin folder. This is required to render .musicxml files.
Setup and activate a Python 3.11 environment in Git. Run main.py to initialize the Parro.
