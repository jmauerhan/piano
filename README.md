# LED Piano with Speaker: Audio Visual Art

## Overview
This project uses NeoPixel LED animations and PWM-based tone playback functionality, designed to replicate the nostalgic audio experience of early video game technology, to create an audiovisual work of art. 

This was designed as a gift for my daughter's piano teacher, who is so kind and has encouraged my daughter and brightened our lives. He always gives her a very generous Christmas gift. My daughter asked me to make something for him using my laser cutter for a Christmas gift. She was thinking some art for his walls, and specified that he likes Mario and Zelda. I originally was imagining a cutout of a Mario platformer style scene, then thought about adding LEDs, since I've creating LED powered wall art with Mandalas. Then I had the idea of a piano playing the Mario theme song with LEDs showing the notes, and it turned into this project - I was so happy to be able to take our idea to the next level and create a truly unique gift for her teacher that incorporates things they both love.

When powered on, the piano keys light up and slowly transition through the rainbow. When the button on the side is pressed, it plays a random song from the list programmed, and the correct key lights up as the tone plays. Pressing the button again stops the music and shuffles to another song for the next play. I included song files for Mario, Zelda, Pacman, Tetris, Für Elise and Ode to Joy. (Disclaimer: I am only confident in the Mario, Für Elise and Ode to Joy music, the others I had trouble with and got ChatGPT to generate). 

This project was a great opportunity for me to experiment with new ideas, and I learned a lot. While I didn’t have time to implement everything I imagined, and I would definitely change things if I did it again, for now, I’m thrilled with how it turned out, and I hope this inspires others to create their own versions. You are welcome to recreate this as is following my documentation here, build upon it with your own ideas, or take insipiration to make something else entirely. If you do, please share your project with me! 

I hope this inspires others to create.

## Requirements
As mentioned, I was working only with supplies I already had on hand - you may need to adapt things, please feel free to use this as a guide and adapt your project to your materials. I have provided links to the exact products I used - *none* of these are affiliate links, just links to what I used.
### Piano / Case
- CO2 Laser Cutter (A Diode laser may not be capable of cutting the acrylic as it is semi-transparent, and opaque acrylic will not work for this project). 
- 3mm (1/4") Plywood (I used xTool brand basswood sheets, I prefer basswood over birch plywood for laser)
- 3mm Walnut Veneer Plywood [Amazon: ROBOTIME 6-Pack 1/8" Walnut Plywood Sheets](https://www.amazon.com/gp/product/B0CYLW48ZV)
- 3mm Black LED Cast Acrylic [Custom Made Better: 1/8" Black LED Cast Acrylic)[https://www.custommadebetter.com/products/black-led-cast-acrylic-sheets]
- 3mm Frosted White Cast Acrylic [Custom Made Better: 1/8" Frosted White Cast Acrylic Sheets](https://www.custommadebetter.com/products/1-8-matte-milky-white-acrylic-sheet)

### Hardware
#### Board, LEDs, Speaker:
- CircuitPython-compatible microcontroller board
  - For V1 / Prototype, I used [Adafruit ESP32 Feather V2](https://www.adafruit.com/product/5400)
  - For V2 I used [Adafruit KB2040](https://www.adafruit.com/product/5302)
- ~1 meter High Density WS2812B LED Strip (Neopixels), ideally 160 leds/m, 2.7mm width. 
  - These are the only 2.7mm ones I've found, and they are extremely difficult to solder the connections, but the strip does come with a connector already soldered. The strip is also very fragile, so be careful - after multiple bends, one of my connections broke and I did have to tin the connection pad to restore the connection. [Amazon: Xnbada WS2812B WS2812 2.7mm Ultra Narrow LED Strip,DC5V 160LEDs/m](https://www.amazon.com/gp/product/B0CYGHHR96). 
   - If you plan to use wider strips (5, 10, 12mm), I highly recommend the BTF-Lighting Brand: [Amazon: BTF-Lighting 144LED/m](https://www.amazon.com/gp/product/B01CDTEJR0) - you will need to adjust the case design.
- Class D Amplifier & Speaker OR piezo buzzer (not tested, but should work in theory)
  - I used the [Adafruit STEMMA speaker](https://www.adafruit.com/product/3885) which has a Class D amplifier on board. The only downside is not being able to easily adjust the volume once the entire project is assembled. 
- Panel Mount Momentary Button [Amazon: Momentary Push Buttons](https://www.amazon.com/gp/product/B0DB5PMLBH)

#### Power & Assembly:
- Power: 
  - USB-C Power Male Pigtail: [Amazon](https://www.amazon.com/gp/product/B0BFHXWCS9)
  - Option: USB-C Port
    - Mini Rocker Switch [Amazon: DaierTek Mini Rocker Switch](https://www.amazon.com/gp/product/B07S2QJKTX) 
    - USB-C Female Socket Connector with Pigtail [Amazon](https://www.amazon.com/gp/product/B0D1K23RTG)
  - Option: DC 2.1mm port
    - DC Power 5.5mm x 2.1mm Pigtail Barrel Plug Connector Cable [Amazon](https://www.amazon.com/gp/product/B072BXB2Y8)
    - Inline DC Power Switch: [Amazon: Inline Switch,Low Voltage Switch, Manual Inline DC Power Switch Extension Cable](https://www.amazon.com/gp/product/B099S33P7F)
    - 5V 1A Power Supply Wall Adapter: [Amazon: 5V 1A Power Supply](https://www.amazon.com/gp/product/B0915SN2QN)

- Perma-Proto Board or Solderable Prototype Breadboard
  - [Adafruit Perma-Proto Board](https://www.adafruit.com/product/1609)
  - [Amazon: ElectroCookie](https://www.amazon.com/ElectroCookie-Solderable-Breadboard-Electronics-Gold-Plated/dp/B081MSKJJX)
- 3-pin and 2-pin 5mm or 2.54mm terminal blocks
- Optional: Quick-connect wire connectors
- Soldering iron
- CA Glue
- Hot Glue

# Instructions

## Circuit Python Code

### Install Circuit Python
1. Install Circuit Python on the board. I used [9.2.2 for the KB2040](https://circuitpython.org/board/adafruit_kb2040/)
2. Download the [Circuit Python Library Bundle](https://circuitpython.org/libraries) and copy the neopixel.mpy file onto your board
3. Download and copy over the code in this repository. 

### Configure for your board
Update the [config.py]() file with the appropriate pins for your board, if needed. The example in this repo is for the KB2040 and the pins I chose to use. 
```python
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
```

## Wiring Diagram

I first tested out the wiring on a breadboard, then transferred that to a solderable prototype breadboard, and added terminal blocks for the speaker, button and LED strip. I used 5mm terminal blocks because the 2-3 pin ones do fit easily on a breadboard, and I struggled to turn the tiny screws on the 2.54mm size.



## Laser Cutting & Piano Assembly
- Cut the Piano Top out of the Walnut Veneer Plywood
- Cut the white_keys from the Frosted White Cast Acrylic
- Cut the black_keys from the Black LED Cast Acrylic
- Cut all other files using 3mm basswood.

*Fixes/Notes*
- The acrylic keys have been adjusted, so the white piece is slightly bigger, and the black keys are slightly taller. This allows for space to adhere to the wood case, and place the LED holder.
- The LED holder has also been resized, you may notice in my photos the LED holder is slightly smaller than they keyboard. I have uploaded only the fixed correct size.

### Keyboard
#### Acrylic
- Test fit the black keys into the white keys, be sure all of your black keys have the same side facing up if your acrylic has two different textures. I accidentally installed all of mine with the glossy side down :( I suggest going glossy-side up.
- Use CA glue to attach the black keys to the white keys.
- Lay the walnut piano top piece face down, and line up the keys on it - again, face down.
- Check the alignment - tape the acrylic to the walnut and flip it back over to be sure the black keys line up with the walnut lines. Make sure both are facing the right direction. 
- Flip it back over and apply a small amount of CA glue to attach the keys to the top. 

#### LED holder
*Note*: In my version, the LED holder is slightly smaller than intended. The SVG file I've uploaded in this repository is the correct fixed size.
- If using taller LEDs, you can either cut the LED holder out of thicker plywood, or cut a few layers of it. The middle prongs on the holder should line up with the bottom of the black keys.
- Stick the LED strip to the holder, wrapping from the middle around the entire perimeter of the shape.
- Attach the LED holder to the acrylic (I suggest either hot glue or crafting "sticky dots" rather than CA glue, in case you need to adjust this part or have a problem with the LEDs due to the fragile connection pads.
- Attach the LED back to the LED holder - again ideally using hot glue rather than CA glue.

#### Main Case Body
- Test fit / Friction Fit the main body - the sides should fit tightly into the back, and the flat side faces up. Do not glue anything yet.
- Insert the momentary push button and the rocker switch into the appropriate holes.
- Fit the USB-C female port into the hole, attach using screws or CA glue.
- Wire up the USB-C input, rocker switch, and USB-C pigtail for the board. (I used quick wire connectors for these)
- Wire the speaker, button and LED connector to the appropriate terminal blocks.
- Test the circuits!
- Assuming everything works, attach the perma-proto board to the case, I used the "sticky dots", nylon screws would work as well. The speaker can be stuck to the back of the case as well.
- Gently squeeze a small amount of CA glue into the finger joints of the sides and the back - don't overdo it!

### Front
- Line up the top (which includes the LEDs) over the case, the bottom and sides of the case should line up with the piano top, and the walls should fit snugly around the LED housing.
- Plug in before glueing and confirm everything is working and ready!
- If everything looks good, apply a small amount of CA glue on top of all the walls, then place the top back on.

### Back with Hanger Holes
This is the last piece, and when I attached mine I glued it on backwards despite checking it several times before glueing. Oh well! I decided it made it artsy and added an acrylic music note. 
- Line it up with the back of the case and glue - either direction! :D 
