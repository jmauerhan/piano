import pwmio
import board
import neopixel
import digitalio
import asyncio
import time

from config import *

from notes import *
from custom_shuffle import *
from song_list import *

# Setup Song List
song_list = list(songs.keys())
custom_shuffle(song_list)
current_song_index = 0  # Start at the first shuffled so ng
current_song = songs[song_list[current_song_index]]["song"]
current_tempo = songs[song_list[current_song_index]]["tempo"]
note_index = 0  # Start at the first note of the song

# Configure NeoPixel strip
pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=0.5, auto_write=False)

# Configure the onboard NeoPixel
onboard_pixel = neopixel.NeoPixel(ONBOARD_PIXEL_PIN, 1, brightness=0.25, auto_write=True)

# Configure music toggle button
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# State variables
music_playing = False
note_index = 0
color_position = 0  # Initialize color position at the start of the song
last_color_update = time.monotonic()
last_note_update = time.monotonic()
color_update_interval = 0.5

async def white_keys_rainbow():
    global music_playing
    
    # Spread the rainbow colors across the white keys
    num_keys = len(white_keys)
    base_color_positions = {note: (i * (256 // num_keys)) % 256 for i, note in enumerate(white_keys)}

    while True:
        if not music_playing:
            for note in white_keys:
                if note in note_to_pixel:
                    # Get the pixel indices for the current note
                    pixels_list = note_to_pixel[note]

                    # Update the color for the current note
                    current_color_position = base_color_positions[note]

                    for pixel_index in pixels_list:
                        if 0 <= pixel_index < NUM_PIXELS:
                            # Set the pixel to the calculated color
                            pixels[pixel_index] = wheel(current_color_position)
                        else:
                            print(f"Warning: Pixel index {pixel_index} is out of range.")

                    # Increment the base color position for the note
                    base_color_positions[note] = (current_color_position + COLOR_CHANGE) % 256

            # Show updated colors on the strip
            pixels.show()

        await asyncio.sleep(0.02)  # Adjust speed of the animation


# Async function to handle music playback and LED strip updates
async def play_music_and_update_leds():
    global note_index, current_song, current_tempo, music_playing

    # Play the song once
    while True:
        if music_playing and note_index < len(current_song):
            # Play the current note
            note, duration = current_song[note_index]
            duration_in_sec = duration_in_seconds(duration, current_tempo)

            pixels.fill((0, 0, 0))  # Turn off all pixels
            if note in note_to_pixel:
                # Generate a unique color for the current note
                note_color = wheel((note_index * 15) % 256)  # Adjust the multiplier for smoother transitions
                for led in note_to_pixel[note]:
                    pixels[led] = note_color
            pixels.show();

            # Play the tone asynchronously
            await play_tone(BUZZER_PIN, note, duration_in_sec)

            pixels.fill((0, 0, 0))  # Turn off all pixels
            pixels.show()
            # Move to the next note
            note_index += 1
            await asyncio.sleep(0.01)  # Prevent CPU overload
        
        if music_playing and note_index is len(current_song):
            # Once the song is finished, turn off the LEDs
            pixels.fill((0, 0, 0))
            pixels.show()
            # Optionally, you can set music_playing to False to indicate the song has finished
            music_playing = False

        await asyncio.sleep(0.01)  # Prevent CPU overload


# Async function to update the onboard NeoPixel
async def update_onboard_neopixel():
    global color_position

    while True:
        if music_playing:
            onboard_pixel.fill(wheel(color_position % 256))
            color_position += 1
        else:
            onboard_pixel.fill((0, 0, 0))
        await asyncio.sleep(0.5)  # Update every 0.5 seconds

# Generate rainbow colors using a wheel effect
def wheel(pos):
    # Input a value 0 to 255 to get a color.
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)


async def play_tone(pin, frequency, duration):
    if frequency == NOTE_REST:
        await asyncio.sleep(duration)
        return

    audio_pwm = pwmio.PWMOut(pin, duty_cycle=2**15, frequency=frequency)
    await asyncio.sleep(duration)
    audio_pwm.deinit()


async def monitor_button():
    global music_playing, current_song_index, current_song, current_tempo, note_index, song_list

    last_button_state = True

    while True:
        current_button_state = button.value
        if last_button_state and not current_button_state:  # Button just pressed
            if music_playing:
                # Turn off music
                music_playing = False
                print("Music stopped.")
                
                # Prepare for next song
                current_song_index += 1  

                # Shuffle if needed
                if current_song_index >= len(song_list):  # If we've played all songs
                    custom_shuffle(song_list)
                    current_song_index = 0  # Reset index
                    print("Song list shuffled.")
         
                # Select the next song
                current_song = songs[song_list[current_song_index]]["song"]
                current_tempo = songs[song_list[current_song_index]]["tempo"]
            else:
                # Reset to the start of the song
                note_index = 0
                print(f"Playing: {song_list[current_song_index]} at {current_tempo} BPM.")
                music_playing = True

            await asyncio.sleep(0.2)  # Debounce delay

        last_button_state = current_button_state
        await asyncio.sleep(0.01)
