The images used for the display were made in GIMP using a four color grayscale scheme that resulted in RGB values of black (0,0,0), dark gray (23, 23, 23), light gray (103, 103, 103), and white (255, 255, 255) explicitly. The png files were exported at full resolution no scaling in 8bit RGB. I did not use the GIMP export setting for grayscale.

I found the waveshare display driver for the pico version of the 2.9 in grayscale display to be problematic. The original waveshare display unpacks a bytearray and splits it into two images to send to the display and are overlaid.
I forked the original waveshare driver to insert a simple function in the driver, ane then wrote a python script to process my png files on a pc and then send the final bytearrays to the raspberry pi pico.
My forked waveshare driver can be found here: https://github.com/p0pc012n/pico_epaper_image/blob/main/python/Pico_ePaper-2.9.py
My python script for converting .png to bytearrays with more detailed instruction can be found here: https://github.com/p0pc012n/PNG_to_epaper_converter

The main.py combines bytearrays depending on the system status to generate the final image in real time. I implemented further post-processing of the bytearrays except for the base GUI image. I used clean_byte.py to crop all the images representing different system statuses. This allow the main.py to overwrite the bytes at each of the status positions on the display for gray water tank, fresh water tank, and battery respectively. 
