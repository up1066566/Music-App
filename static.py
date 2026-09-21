from dataclasses import dataclass
from typing import Literal

A4 = 440

INTERVALS = ('1', 'b2', '2', 'b3', '3', '4', 'b5', '5', 'b6', '6', 'b7', '7')
NOTES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')

NATURALS = ('C', 'D', 'E', 'F', 'G', 'A', 'B')

FLATS_TO_SHARPS = {'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#', 'Bb': 'A#'}
SHARPS_TO_FLATS = {'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab', 'A#': 'Bb'}


# Main Parent Scales
DEGREES_MAJOR = ('1', '2', '3', '4', '5', '6', '7')
DEGREES_MINOR = ('1', '2', 'b3', '4', '5', 'b6', 'b7')
DEGREES_HARMONIC_MINOR = ('1', '2', 'b3', '4', '5', 'b6', '7')
DEGREES_MELODIC_MINOR = ('1', '2', 'b3', '4', '5', '6', '7')

# Extra Heptatonic Parent Scales
DEGREES_HARMONIC_MAJOR = ('1', '2', '3', '4', '5', 'b6', '7')
DEGREES_DOUBLE_HARMONIC_MAJOR = ('1', 'b2', '3', '4', '5', 'b6', '7')

# Non-Heptatonic Parent Scales
DEGREES_PENTATONIC_MAJOR = ('1', '2', '3', '5', '6')
DEGREES_WHOLE_TONE = ('1', '2', '3', 'b5', 'b6', 'b7')
DEGREES_DIMINISHED_HW = ('1', 'b2', 'b3', '3', 'b5', '5', '6', 'b7')

NoteName = Literal[*NOTES]
NaturalNoteName = Literal[*NATURALS]


@dataclass(frozen=True)
class Note:
    name: NoteName # type: ignore
    octave: int
    accidental: int = 0

    def __post_init__(self):
        if self.name not in NOTES:
            raise ValueError(f"Invalid note name: '{self.name}'. Must be one of {NOTES}")
        if self.octave <= 0:
            raise ValueError(f"Octave must be a positive integer, got {self.octave}")
        if NOTES.index(self.name) + self.accidental < 0 and self.octave == 1:
            raise ValueError(f"Flat results in an invalid note: '{self.name}' with accidental {self.accidental}, lower than C1")
        
# Χρήση:
if __name__ == "__main__":
    n = Note('A', 4)  # Έγκυρο
    print(n)
    print(f"{n.name}{n.octave}")
    # Note('X', 4)  # Εγείρει ValueError
    # Note('A', -1) # Εγείρει ValueError