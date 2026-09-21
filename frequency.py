import math
from static import *


# returns frequency of given note in specific octave
def get_frequency(note: Note) -> int:
    # Calculate the number of semitones from A4
    semitone_distance = (note.octave - 4) * 12 + NOTES.index(note.name) - NOTES.index('A')
    # Calculate the frequency using the formula
    frequency = A4 * (2 ** (semitone_distance / 12))
    return frequency

def get_note_from_frequency(frequency: float) -> str:
    """
    Returns the note corresponding to a given frequency.
    """
    # Calculate the number of semitones from A4
    semitone_distance = round(12 * (math.log2(frequency / A4)))
    # Calculate the note and octave
    note_index = (semitone_distance + NOTES.index('A')) % 12
    octave = 4 + ((semitone_distance + NOTES.index('A')) // 12)
    return f"{NOTES[note_index]}{octave}"



