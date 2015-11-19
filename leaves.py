from music import *

##### define the data structure (score, parts, and phrases)
autumnLeaves = Score(140) 

goblinsPart = Part(GOBLINS, 0)       
pianoPart  = Part(PIANO, 1)          
bassPart    = Part(GUNSHOT, 2)

melodyPhrase = Phrase()   # holds the melody
chordPhrase  = Phrase()   # holds the chords
bassPhrase   = Phrase()   # holds the bass line

##### create musical data
# melody
melodyPitch1 = [REST, A4, B4, C5, F5, REST, G4, A4, B4, E5,  E5] 
melodyDur1   = [QN,   QN, QN,  QN, WN, EN,   DQN,QN, QN,  DQN, HN+EN]
melodyPitch2 = [REST, F4, G4, A4, D5, REST, E4, D5, C5, A4]
melodyDur2   = [QN,   QN, QN, QN, WN, EN,   DQN, QN, QN, 6.0]

melodyPhrase.addNoteList(melodyPitch1, melodyDur1) # add to phrase
melodyPhrase.addNoteList(melodyPitch2, melodyDur2)

# chords
chordPitches1   = [REST, [A3, C3, D3, F4], [A3, C3, D3, F4], REST, 
                    [B3, D4, F4]]
chordDurations1 = [WN,    HN,               QN,              QN,    
                    QN]           
chordPitches2   = [REST, [G3, B3, C4, E4], [G3, B3, C4, E4]]
chordDurations2 = [DHN,  HN,                QN]               
chordPitches3   = [REST, [F3, A3, C4, E4], REST, [A3, B3, D4, F4], 
                    [A3, B3, D4, F4]]
chordDurations3 = [QN,   QN,               DHN,  HN,                
                    QN]
chordPitches4   = [REST, [GS3, B3, D4, E3], REST, [A2, C3, E3], 
                   [GS3, B3, D3, E3]]
chordDurations4 = [QN,   QN,                 DHN,  HN,           
                   QN]
chordPitches5   = [REST, [A2, C3, E3], REST]
chordDurations5 = [QN,   HN,           HN]

chordPhrase.addNoteList(chordPitches1, chordDurations1)  # add them
chordPhrase.addNoteList(chordPitches2, chordDurations2)
chordPhrase.addNoteList(chordPitches3, chordDurations3)
chordPhrase.addNoteList(chordPitches4, chordDurations4)
chordPhrase.addNoteList(chordPitches5, chordDurations5)

# bass line
bassPitches1   = [REST, D2, REST, D2, A2, G2, REST, G2, D2, C3, REST, 
                   G2, G2, F2] 
bassDurations1 = [WN,   QN, EN,   EN, HN, QN, EN,   EN, HN, QN, EN,   
                   EN, HN, QN] 
bassDurations2 = [EN,   EN, HN, QN,  EN,   EN,  HN, QN, EN,   EN, HN,  
                   QN]
bassPitches2   = [REST, F2, C2, B2, REST, B2, F2, E1, REST, E1, B2, 
                   A2] 
bassPitches3   = [REST, A2, A2, E1, A2, REST]
bassDurations3 = [EN,   EN, QN, QN, HN, HN]

bassPhrase.addNoteList(bassPitches1, bassDurations1)  # add them
bassPhrase.addNoteList(bassPitches2, bassDurations2)
bassPhrase.addNoteList(bassPitches3, bassDurations3)

##### combine musical material
goblinsPart.addPhrase(melodyPhrase) # add phrases to parts
pianoPart.addPhrase(chordPhrase)
bassPart.addPhrase(bassPhrase)

autumnLeaves.addPart(goblinsPart) # add parts to score
autumnLeaves.addPart(pianoPart)
autumnLeaves.addPart(bassPart)

Play.midi(autumnLeaves)  # play music
