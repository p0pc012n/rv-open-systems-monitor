# python script used to crop image bytearrays to overlay on the panel_base image
import os
from battery_white_x24 import x24_image_data  # import split bytearray to cut

# === file path config ===
parent_dir = os.path.dirname(__file__)
file_name = "battery_white_x24.py"  # Replace with your image filename
file_path = os.path.join(parent_dir, file_name)
base_name = "\\" + file_name[:-4]
old_byte = x24_image_data
print(file_name)

start_byte = 3458  # starting byte index to cut
rows = 64  # num of pixel rows to iterate
num_bytes = 7  # num of bytes per row to cut
new_bytearray = bytearray()
counter = 0  # initiate byte counter
while counter < rows:
    byte_counter = 0
    row_byte = start_byte
    while byte_counter < num_bytes:
        new_bytearray.append(old_byte[row_byte])
        row_byte += 1
        byte_counter += 1
    start_byte += 16
    counter += 1


with open(file_path, "w") as f:
    f.write("x24_image_data = bytearray([\n")
    for i, byte in enumerate(new_bytearray):
        f.write(f"    0x{byte:02x},\n")
    f.write("])\n")
