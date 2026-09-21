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

def get_octave(note: str) -> int:
    """
    Returns the octave of a given note.
    """
    # Extract the octave from the note string
    octave = int(note[-1])
    return octave


def get_interval(note1, note2): 
    """
    Returns the interval between two notes.
    """
    octave1 = get_octave(note1)
    octave2 = get_octave(note2)
    
    # Calculate the number of semitones between the two notes
    semitone_distance = NOTES.index(note2) - NOTES.index(note1)
    
    interval = semitone_distance % 12  # Ensure the interval is within one octave
    octave_difference = (octave2 - octave1) * 12 if octave1 is not None and octave2 is not None else 0
    # Return the corresponding interval
    return INTERVALS[interval]