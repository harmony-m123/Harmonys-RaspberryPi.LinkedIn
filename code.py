import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Read PICO as a keyboard
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Wait for Mac to recognize the PICO
time.sleep(4)

# Open search
keyboard.press(Keycode.GUI, Keycode.SPACE)
keyboard.release_all()

time.sleep(0.5)

# Search for terminal
layout.write("terminal")
keyboard.send(Keycode.ENTER)

# Wait for terminal to open
time.sleep(1.5)

# Open my LinkedIn profile
layout.write("open https://www.linkedin.com/in/harmony-martin-809303334/")
keyboard.send(Keycode.ENTER)
