# rv-open-systems-monitor
ePaper Systems Information Display for RVs, Powered by Raspberry Pi

Open Source solution to provide a drop in replacement to system monitor panels in RVs (Motorhomes, Travel Trailers, Campers)
This started as a personal project after i got tired checking the LEDS and trying to remember what the last status was. The ePaper display will retain the system status image even when powered off.
The intended folder structure is set up in anticipation if this project is picked up and other RV system monitor configurations are added. The goal is to aim for modularity.

This system ePaper display is powered by a Raspberry Pi Pico 2 W. There is potential for wireless notfications, but I have not gotten around to it.
The display is a Waveshare 2.9in Four Color Grayscale ePaper display for Pico, and must be used in order for this code to work.
The STL files are a retrofitted display bezel to allow the assembly to clip into the existing system monitor frame and use the existing wiring harness.

Getting Started:
1. Flash Raspberry Pi Pico 2 (2 or 2W) with latest firmware from official source. (Older Pico may work, but it's untested)
2. Download the folder "Pico" in the intended display size for the system monitor.
3. Download Thonny or a similar micropython IDE that can communicate with the Raspberry Pi Pico 2 (RP).
3. After Flashing Firmware to the RP, open Thonny and connect to the RP.
4. Using Thonny, Upload the "main.py" from the "Pico" folder on your PC to the RP.
5. Using Thonny, Upload the folder "lib" from the "Pico" folder on your PC to the RP.
6. The file structure in the root folder of your RP should now only contain the "main.py" and the folder "lib".
7. If you have trouble, uploading the "lib" folder, you can always move all files one at a time, however this will be very time consuming.
8. Download the Wavehsare driver for the ePaper display and rename it to remove hyphens (-) and extra periods (.) because micropython will have problems (the main.py for the 2.9 display expects it to be named "Pico_ePaper_2_9.py").
9. Using the same method above, upload driver to the "lib" folder on the RP.
Note: For the 2.9in four color grayscale display, use the driver from this fork: [python/Pico_ePaper-2.9.py](https://github.com/p0pc012n/pico_epaper_image/blob/main/python/Pico_ePaper-2.9.py)

Assembly Notes:
1. The Waveshare 2.9 ePaper display has a ribbon cable from the display to the blue display pcb. Ensure that when installing the RP onto the display board headers that the RP microUSB port and the epaper display ribbon cable are on the same side.
2. The 3D Printed Bezel has a cutout for the ePaper display ribbon cable. Ensure the display is oriented on the 3D Printed bezel so that the ribbon cable is in the cutout.

Testing is underway, however I am only able to test this on my travel trailer configuration. 3D Models will vary from system monitor panels. Voltage values may vary wildly between RVs, system monitors, installed batteries, power control boards, etc.

In Testing:
KIB System Monitor found in 2006 Trailmanor model years. Voltage values may be tuned for 12V LifePo4 battery and PD Wildkat board.

Currently Supported: