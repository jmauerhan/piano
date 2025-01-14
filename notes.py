# notes.py

# Define notes as constants
NOTE_REST = 0

NOTE_C4 = 262
NOTE_C4_SHARP = 277
NOTE_D4 = 294
NOTE_D4_SHARP = 311
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_F4_SHARP = 370
NOTE_G4 = 392
NOTE_G4_SHARP = 415
NOTE_A4 = 440
NOTE_A4_SHARP = 466
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_C5_SHARP = 554
NOTE_D5 = 587
NOTE_D5_SHARP = 622
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_F5_SHARP = 740
NOTE_G5 = 784
NOTE_G5_SHARP = 831
NOTE_A5 = 880
NOTE_A5_SHARP = 932
NOTE_B5 = 988

# Mapping of # Mapping of notes to NeoPixel indices (groups of LEDs)
note_to_pixel = {
    NOTE_C4: 		[20,21,22,23,24,25,26,27,28, 65, 66, 67, 68, 69, 70, 71, 72, 73],  # Example groups
    NOTE_C4_SHARP:	[18, 19, 29, 30],
    NOTE_D4: 		[17, 31, 62, 63, 64, 74, 75],
    NOTE_D4_SHARP:	[15, 16, 32,33],
    NOTE_E4: 		[13, 14, 34,35, 59, 60, 61, 76, 77, 78],
    NOTE_F4: 		[12, 11, 36,37, 56, 57, 58, 79, 80, 81],
    NOTE_F4_SHARP:	[10, 9, 38,39],
    NOTE_G4: 		[8, 40, 54, 55, 82, 83, 84],
    NOTE_G4_SHARP:	[6, 7, 41, 42],
    NOTE_A4: 		[5, 42,43, 50, 51, 85, 86],
    NOTE_A4_SHARP:	[4, 44,45],
    NOTE_B4: 		[3, 2, 45,46, 47, 48, 49, 87, 88, 89, 90],
    NOTE_C5: 		[90, 91, 92, 131, 132, 133, 134, 177, 178, 179],
    NOTE_C5_SHARP:	[135, 136, 176],
    NOTE_D5:			[93, 94, 95, 128, 129, 130, 137, 174, 175],
    NOTE_D5_SHARP:	[138, 139, 173],
    NOTE_E5:			[96, 97, 98, 125, 126, 127, 140, 141, 171, 172],
    NOTE_F5: 		[99, 100, 101, 122, 123, 124, 142, 143, 169, 170],
    NOTE_F5_SHARP:	[144, 145, 167, 168],
    NOTE_G5:			[102, 103, 104, 119, 120, 121, 146, 166],
    NOTE_G5_SHARP:	[147, 165],
    NOTE_A5:			[105, 106, 107, 116, 117, 118, 149, 163, 164],
    NOTE_A5_SHARP:	[150, 161, 162],
    NOTE_B5:			[108, 109, 110, 111, 112, 113, 114, 115, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160],
}

# white keys (not sharp/flat black keys) for resting animation
white_keys = [
    NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4,
    NOTE_C5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_G5, NOTE_A5, NOTE_B5
]
