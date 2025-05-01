from battery_1_3_x24 import x24_image_data as b13_x24
from battery_1_3_x26 import x26_image_data as b13_x26
from battery_2_3_x24 import x24_image_data as b23_x24
from battery_2_3_x26 import x26_image_data as b23_x26
from battery_charge_x24 import x24_image_data as bc_x24
from battery_charge_x26 import x26_image_data as bc_x26
from battery_empty_x24 import x24_image_data as be_x24
from battery_empty_x26 import x26_image_data as be_x26
from battery_white_x24 import x24_image_data as bw_x24
from battery_white_x26 import x26_image_data as bw_x26
from gray_full_x24 import x24_image_data as gf_x24
from gray_full_x26 import x26_image_data as gf_x26
from gray_1_3_x24 import x24_image_data as g13_x24
from gray_1_3_x26 import x26_image_data as g13_x26
from gray_2_3_x24 import x24_image_data as g23_x24
from gray_2_3_x26 import x26_image_data as g23_x26
from gray_empty_x24 import x24_image_data as ge_x24
from gray_empty_x26 import x26_image_data as ge_x26
from fresh_1_3_x24 import x24_image_data as f13_x24
from fresh_1_3_x26 import x26_image_data as f13_x26
from fresh_2_3_x24 import x24_image_data as f23_x24
from fresh_2_3_x26 import x26_image_data as f23_x26
from fresh_empty_x24 import x24_image_data as fe_x24
from fresh_empty_x26 import x26_image_data as fe_x26
from fresh_full_x24 import x24_image_data as ff_x24
from fresh_full_x26 import x26_image_data as ff_x26
from zero_x24 import x24_image_data as zero_x24
from zero_x26 import x26_image_data as zero_x26
from one_x24 import x24_image_data as one_x24
from one_x26 import x26_image_data as one_x26
from two_x24 import x24_image_data as two_x24
from two_x26 import x26_image_data as two_x26
from three_x24 import x24_image_data as three_x24
from three_x26 import x26_image_data as three_x26
from four_x24 import x24_image_data as four_x24
from four_x26 import x26_image_data as four_x26
from five_x24 import x24_image_data as five_x24
from five_x26 import x26_image_data as five_x26
from six_x24 import x24_image_data as six_x24
from six_x26 import x26_image_data as six_x26
from seven_x24 import x24_image_data as seven_x24
from seven_x26 import x26_image_data as seven_x26
from eight_x24 import x24_image_data as eight_x24
from eight_x26 import x26_image_data as eight_x26
from nine_x24 import x24_image_data as nine_x24
from nine_x26 import x26_image_data as nine_x26
from point_x24 import x24_image_data as point_x24
from point_x26 import x26_image_data as point_x26
from volt_x24 import x24_image_data as volt_x24
from volt_x26 import x26_image_data as volt_x26


class TrailScreen:
    def __init__(self, panel_base_x24, panel_base_x26):
        # initialize image bytearrays
        self.panel_base_x24 = panel_base_x24
        self.panel_base_x26 = panel_base_x26
        
        self.fresh_x24 = [fe_x24, f13_x24, f23_x24, ff_x24]
        self.fresh_x26 = [fe_x26, f13_x26, f23_x26, ff_x26]

        self.gray_x24 = [ge_x24, g13_x24, g23_x24, gf_x24]
        self.gray_x26 = [ge_x26, g13_x26, g23_x26, gf_x26]

        self.battery_x24 = [be_x24, b13_x24, b23_x24, bw_x24, bc_x24]
        self.battery_x26 = [be_x26, b13_x26, b23_x26, bw_x26, bc_x26]

        self.digits_x24 = [
            zero_x24,
            one_x24,
            two_x24,
            three_x24,
            four_x24,
            five_x24,
            six_x24,
            seven_x24,
            eight_x24,
            nine_x24,
        ]
        self.digits_x26 = [
            zero_x26,
            one_x26,
            two_x26,
            three_x26,
            four_x26,
            five_x26,
            six_x26,
            seven_x26,
            eight_x26,
            nine_x26,
        ]

        self.point_x24 = point_x24
        self.point_x26 = point_x26

        self.volt_x24 = volt_x24
        self.volt_x26 = volt_x26
        
    #Overlay fresh tank status on system GUI
    def process_fresh(self, fresh_value):
        start_byte = 1810
        fresh_status_x24 = self.fresh_x24[int(fresh_value)]
 
        fresh_status_x26 = self.fresh_x26[int(fresh_value)]
 
        current_byte = 0
        for _ in range(52):
            row_byte = start_byte
            
            for _ in range(7):
                #print(f"row_byte: {row_byte}, old: {self.panel_base_x24[row_byte]},  new: {fresh_status_x24[current_byte]}")
                self.panel_base_x24[row_byte] = fresh_status_x24[current_byte]
                self.panel_base_x26[row_byte] = fresh_status_x26[current_byte]
                current_byte += 1
                row_byte += 1
            start_byte += 16
            
    #Overlay gray tank status on system GUI
    def process_gray(self, gray_value):
        print(gray_value)
        start_byte = 322
        gray_status_x24 = self.gray_x24[int(gray_value)]
        gray_status_x26 = self.gray_x26[int(gray_value)]
        current_byte = 0
        for _ in range(56):
            row_byte = start_byte
            for _ in range(6):
                self.panel_base_x24[row_byte] = gray_status_x24[current_byte]
                self.panel_base_x26[row_byte] = gray_status_x26[current_byte]
                row_byte += 1
                current_byte += 1
            start_byte += 16
            
    #Overlay battery status on system GUI
    def process_battery(self, battery_value):
        if battery_value == "3":
            pass
        else:
            start_byte = 3458
            battery_status_x24 = self.battery_x24[int(battery_value)]
            battery_status_x26 = self.battery_x26[int(battery_value)]
            current_byte = 0
            for _ in range(64):
                row_byte = start_byte
                for _ in range(7):
                    self.panel_base_x24[row_byte] = battery_status_x24[current_byte]
                    self.panel_base_x26[row_byte] = battery_status_x26[current_byte]
                    row_byte += 1
                    current_byte += 1
                start_byte += 16
                
    #Generate Voltage Value Image
    def _process_voltage_digits(self, voltage_str, start_index):
        parts = voltage_str.split(".")
        integer_part = list(parts[0])
        decimal_part = list(parts[1])

        digits = list(integer_part) + ["."] + list(decimal_part)
        print(digits)
        current_index = start_index
        # integer
        self.panel_base_x24[current_index] = 0x00
        self.panel_base_x26[current_index] = 0x00
        current_index += 16
        for digit in integer_part:

            byte_counter = 0

            while byte_counter < 3:
                self.panel_base_x24[current_index] = self.digits_x24[int(digit)][
                    byte_counter
                ]
                self.panel_base_x26[current_index] = self.digits_x26[int(digit)][
                    byte_counter
                ]
                current_index += 16
                print(current_index)
                byte_counter += 1

            self.panel_base_x24[current_index] = 0x00
            self.panel_base_x26[current_index] = 0x00
            current_index += 16
        # decimal point
        byte_counter = 0
        while byte_counter < 3:
            self.panel_base_x24[current_index] = self.point_x24[byte_counter]
            self.panel_base_x26[current_index] = self.point_x26[byte_counter]
            current_index += 16
            print(current_index)
            byte_counter += 1

        # decimal part
        self.panel_base_x24[current_index] = 0x00
        self.panel_base_x26[current_index] = 0x00
        current_index += 16

        for digit in decimal_part:

            byte_counter = 0

            while byte_counter < 3:
                self.panel_base_x24[current_index] = self.digits_x24[int(digit)][
                    byte_counter
                ]
                self.panel_base_x26[current_index] = self.digits_x26[int(digit)][
                    byte_counter
                ]
                current_index += 16
                print(current_index)
                byte_counter += 1
            self.panel_base_x24[current_index] = 0x00
            self.panel_base_x26[current_index] = 0x00
            current_index += 16


        self.panel_base_x24[current_index] = 0x00
        self.panel_base_x26[current_index] = 0x00
        current_index += 16
        byte_counter = 0
        # voltage unit
        while byte_counter < 3:
            self.panel_base_x24[current_index] = self.volt_x24[byte_counter]
            self.panel_base_x26[current_index] = self.volt_x26[byte_counter]
            current_index += 16
            print(current_index)
            byte_counter += 1

        self.panel_base_x24[current_index] = 0x00
        self.panel_base_x26[current_index] = 0x00
        
    #Overlay Voltage Numbers on system GUI
    def process_voltage_readings(self, adc26_value, adc27_value, adc29_value):
        def format_voltage(voltage):
            formatted = "{:.2f}".format(voltage)
            if formatted.startswith("."):
                formatted = "0" + formatted
            return formatted

        formatted_adc26 = format_voltage(adc26_value)
        formatted_adc27 = format_voltage(adc27_value)
        formatted_adc29 = format_voltage(adc29_value)

        self._process_voltage_digits(formatted_adc26, 596)
        self._process_voltage_digits(formatted_adc27, 2037)
        self._process_voltage_digits(formatted_adc29, 3765)
        
    #Returns the two processed system GUI to write to display
    def get_screen(self):
        return self.panel_base_x24, self.panel_base_x26
