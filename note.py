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
        if NOTES.index(self.name) + self.accidental < 0 and self.octave == 1:
            raise ValueError(f"Flat results in an invalid note: '{self.name}' with accidental {self.accidental}, lower than C1")
    
    
# Χρήση:
if __name__ == "__main__":
    n = Note('A', 4)  # Έγκυρο
    print(n)
    print(f"{n.name}{n.octave}")
    # Note('X', 4)  # Εγείρει ValueError
    # Note('A', -1) # Εγείρει ValueError