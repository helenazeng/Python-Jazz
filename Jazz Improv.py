
from music import *

# theme (notice how we line up corresponding pitches and rhythms)
pitches1   = [C4, E4, B4, A4, C4, E4, B4, A4]
durations1 = [QN, QN,  QN,  EN,  QN,  EN,  QN,  QN] 


pitches3   = [[F4, D2], A3, D4, F4, D4, A3, [A4, C2], A3, E4, A4, E4, A3, [D5, B1], D3, A4, D5, A4, D3, 
               [D3, A1], A3, E3, A3, F3, A3, [E5, G1], E3, B4, E4, B4, E3,[D5, G1], F3, B4, D5, B4, F3]
durations3 = [QN,       QN, QN, QN, QN, QN,  QN,      QN, QN, QN, QN, QN,  QN,      QN, QN, QN, QN, QN, 
               QN,      QN,  QN, QN, QN, QN, QN,      QN,  QN, QN, QN, QN, QN,      QN,  QN, QN, QN, QN]

pitches4  = [[C4, A2, A1], E2, A3, C3, A3, E2, [F4, A1, A2], A3, C3, F3, C3, A3, [E4, B2, B1], G2, C3, E3, C3, G2,
            [F4, D2], A3, D4, F4, D4, A1]
durations4 = [QN,       QN, QN, QN, QN, QN,  QN,      QN, QN, QN, QN, QN,  QN,      QN, QN, QN, QN, QN, 
               QN,      QN,  QN, QN, QN, QN]
# create an empty phrase, and construct theme using pitch/rhythm data
theme = Phrase()   
theme.addNoteList(pitches1, durations1)
Mod.repeat(theme, 5)
theme.addNoteList(pitches3, durations3)
Mod.accent(theme, 1)
theme.addNoteList(pitches4, durations4)
Mod.accent(theme, 1)

# set the instrument and tempo for the theme
theme.setInstrument(SYNTH_BASS_2)
theme.setTempo(160)

# play it
Play.midi(theme)
