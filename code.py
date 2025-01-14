import pwmio
import board
import neopixel
import digitalio
import asyncio
import time

from core import *
from notes import *


# Main coroutine to create and manage tasks
async def main():
    # Create tasks for each function
    asyncio.create_task(monitor_button())
    asyncio.create_task(update_onboard_neopixel())
    asyncio.create_task(play_music_and_update_leds())
    asyncio.create_task(white_keys_rainbow())  

    # Keep the event loop alive
    while True:
        await asyncio.sleep(0)  # Allow other tasks to run

# Start the asyncio event loop
asyncio.run(main())