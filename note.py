from dataclasses import dataclass
from typing import Literal

from static import *

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
        if (self.octave-1)*12 + NOTES.index(self.name) + self.accidental < 0:
            raise ValueError(f"Flat results in an invalid note: '{self.name}' with accidental {self.accidental}, lower than C1")
    
    def return_equivalent_note(self) -> 'Note':
        
        new_index = (NOTES.index(self.name) + self.accidental)
        new_octave = self.octave + (new_index // 12)
        
        new_name = NOTES[new_index%12]
        
        return Note(new_name, new_octave)
    
    

        
        
    
    def distance(self, other: 'Note') -> int:
        """
        Calculate the distance in semitones between this note and another note.
        """
        semitone_distance = (other.octave - self.octave) * 12 + NOTES.index(other.name) + other.accidental - NOTES.index(self.name) - self.accidental
        return semitone_distance

    def frequency(self) -> float:
        """
        Calculate the frequency of this note.
        """
        semitone_distance = self.distance(Note('A', 4))
        frequency = A4 * (2 ** (semitone_distance / 12))
        return frequency

    def get_interval(self, other: 'Note') -> tuple[str,str]:
        """
        Returns the interval between this note and another note.
        """
        semitone_distance = self.distance(other)
        interval = semitone_distance % 12
        if semitone_distance < 0:
            return INTERVALS[interval], f'-{self.octave-other.octave}'
        return INTERVALS[interval], f'+{self.octave-other.octave}'

def test():
    n1 = Note('D', 6, 1)
    n2 = Note('A', 4)
    
    print(f"{n1.name}{n1.octave}")
    interval, octave_diff = n1.get_interval(n2)
    print(f"Interval: {interval}, Octave Difference: {octave_diff}")
    freq = n1.frequency()
    print(f"Frequency of {n1.name}{n1.octave}: {freq} Hz")
    freq = n2.frequency()
    print(f"Frequency of {n2.name}{n2.octave}: {freq} Hz")
    
# Χρήση:
if __name__ == "__main__":
    n = Note('A', 4)  # Έγκυρο
    print(n)
    print(f"{n.name}{n.octave}")
    # Note('X', 4)  # Εγείρει ValueError
    # Note('A', -1) # Εγείρει ValueError