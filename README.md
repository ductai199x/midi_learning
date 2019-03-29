# midi_learning
This project aims at learning how to do digital signal processing with sound waves. Since MIDI is discrete in frequencies (notes are ranged from 0-127), it is easier to do simulation and to verify results

The ultimate goal is to be able to take a melody + a bunch of spoken words and produce a song with such melody and such words as lyrics

Just imagine singing any song with any lyrics!! <!--:stuck_out_tongue_winking_eye:-->

# learning goals
1. Understand how MIDI works
2. Be able to get a frequency vs time graph from a provided midi/wav file
3. Be able to produce an fft of an input sound wave
4. Extract spoken syllables from a sound file
5. Assume 1 midi note corresponds to 1 syllable, do signal processing on that syllable so that it has the tone and the pitch of the midi note
6. Use crossfading techniques to smooth out the transition between processed syllables
7. String the syllables together, do some more signal processing so that the tempo of the syllables matches the tempo of the input midi song
8. Add the syllables to the input song
9. Output the finished product
10. Do testing to verify the performance of the implemented algorithms

# learning resources
- https://mido.readthedocs.io/en/latest/lib.html
- https://pages.mtu.edu/~suits/NoteFreqCalcs.html
- https://www.cs.cmu.edu/~music/cmsip/readings/MIDI tutorial for programmers.html
- http://web.mit.edu/music21/doc/usersGuide/index.html
- https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
- https://stackoverflow.com/questions/19727261/how-to-count-the-number-of-spoken-syllables-in-an-audio-file
- http://www.fon.hum.uva.nl/praat/

# learning milestones (date - task - % )
- 03/25/19 - Understanding MIDI - 50%
- 03/26/19 - Understanding MIDI - 100%
- 03/27/19 - Producing a freq vs time graph of midi file - 40%
- 03/28/19 - Got the freq vs time graph + its fft - 100%
- 03/29/19 - Researching how to get syllables from sound file - 30%