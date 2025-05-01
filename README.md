# rv-open-systems-monitor
ePaper Systems Information Display for RVs, Powered by Raspberry Pi

Open Source solution to provide a drop in replacement to system monitor panels in RVs (Motorhomes, Travel Trailers, Campers)
This started as a personal project after i got tired checking the LEDS and trying to remember what the last status was. The ePaper display will retain the system status image even when powered off.
The intended folder structure is set up in anticipation if this project is picked up and other RV system monitor configurations are added. The goal is to aim for modularity.

This system ePaper display is powered by a Raspberry Pi Pico 2 W. There is potential for wireless notfications, but I have not gotten around to it.
The display is a Waveshare 2.9in Four Color Grayscale ePaper display for Pico, and must be used in order for this code to work.
The STL files are a retrofitted display bezel to allow the assembly to clip into the existing system monitor frame and use the existing wiring harness.

Testing is underway, however I am only able to test this on my travel trailer configuration. 3D Models will vary from system monitor panels. Voltage values may vary wildly between RVs, system monitors, installed batteries, power control boards, etc.

In Testing:
KIB System Monitor found in 2006 Trailmanor model years. Voltage values may be tuned for 12V LifePo4 battery and PD Wildkat board.

