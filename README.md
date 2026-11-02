# RaspberryPiPicoW.HID
A Raspberry Pi Pico W project that uses USB Human Interface Device (HID) keyboard emulation to open a link, such as a LinkedIn profile, on macOS

**Overview**
This is a personal project in which a Raspberry Pi Pico W and CircuitPython are demonstrating an USB HID keyboard emulation, and when connected to a MacBook, the Pico acts as a keyboard and automatically enters commands to open a link, in my case my LinkedIn profile. 

The Raspberry Pi Pico is programmed to send keyboard inputs to a MacBook, first opening Spotlight Search, launches Terminal, and then enters commands to open my LinkedIn profile in a search browser. 

**What you need: **

Hardware:
- Raspberry Pi Pico W

Software and Libraries:
- CircuitPython
- Python
- Adafruit HID library
- macOS

**How it works:**
1. The Raspberry Pi Pico W connects to the MacBook through USB, in which most will require an adapter from USB to USB-C.
2. The computer will recognize the Pico as a USB Human Interface Device (HID)keyboard.
3. The program sends commands to open Spotlight Search, types, then launches Terminal.
4. It enters a command to open a URL, such as LinkedIn Profile, in a browser.

**How to setup:**
1. Install CircuitPython on Raspberry Pi Pico W.
2. Download the Adafruit HID library and add to the Pico's library folder.
3. Save the Python program as code.py and copy it to the Pico's CIRCUITPY drive.
4. Connect the Pico to a MacBook through the USB (or USB-C adapter).
5. Once plugged in, the program will run automatically when the Pico starts.

**What I Learned:**
Through this personal project, I learned about USB HID communications and how computers are able to recognize a device as a trusted HID. I gained expierence using CircuitPython, Adafruit HID library, and basic hardware automation.

**Cybersecurity Focus:**
I learned about the project in light of my personal interest in Cybersecurity. This project demonstrates how easy it can be to use emulation to allow MacBooks to trust unknown USB devices and raises awareness about why we should be cautious when using unknown devices. 

**Acknowledgment:**
This project was inspired by Steven Hainley's LinkedIN BasUSB project: https://github.com/stevenhainley/Steves-LinkedIn-BadUSB. 
I used the general concept as a starting point, and then created a simplified implementation using CircuitPython and the Adafruit HID library. 

