import board

# Board Specific Config

# Speaker / Buzzer
BUZZER_PIN = board.D2

# Neopixel Strip
PIXEL_PIN = board.D4
NUM_PIXELS = 180

# lower = less/slower color change
# higher = more/faster color change
COLOR_CHANGE = 2

# lower sleep = faster color movement
# higher sleep = slower color movement
COLOR_CHANGE_SLEEP = 0.01

# Music Toggle Button
BUTTON_PIN = board.D7

# Onboard Neopixel (for debugging)
ONBOARD_PIXEL_PIN = board.NEOPIXEL