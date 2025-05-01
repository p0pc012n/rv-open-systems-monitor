# MicroPython main script
from machine import Pin, ADC
import utime
from Pico_ePaper_2_9 import EPD_2in9_Portrait
from trailhat import TrailScreen
from panel_base_x24 import x24_image_data as panel_x24
from panel_base_x26 import x26_image_data as panel_x26

# Configure power switch (True = rocker/toggle switch, Fasle = momentary rocker switch)
constant_power = False

# Configure pins to system sensors
gray_water_pin = ADC(Pin(26))
fresh_water_pin = ADC(Pin(27))
battery_pin = ADC(Pin(29))

# PD 4655L Wildkat battery levels
# Boost Mode 14.4 Volts
# Normal Mode 13.6 Volts
# Storage Mode 13.2 Volts
# Desulfation Mode 14.4 Volts every 21 hours for a period of 15 minutes to prevent battery stratification

# Pico Battery Status:
# Charge: >= 3.08 V
# Full: 2.98 <= V < 3.08
# 2/3:  2.805 V < 2.98
# 1/3:2.63 <= V < 2.805
# empty: V < 2.63

# KIB M-Panel readout
# Battery Charge 12.7 to 12.85
# Battery Good 12.10 to 12.15
# Battery Fair 11.60 to 11.65
# Battery Low 6.0 to --

# KIB M-Panel tanks readout
# Orange Full: 0 Ohms
# Green 2/3: 68k Ohms
# Yellow 1/3: 188k Ohms
# Red Signal
# White Ground

# Fresh Tank Status:
# Ground: > 2.72 V empty
# Yellow:  1.81 < V <= 2.72 1/3
# Green: 0.91 < V <= 1.81 2/3
# Orange: V <= 0.91 full

# Gray Tank Status:
# Ground: > 2.72 V empty
# Yellow:  1.81 < V <= 2.72 1/3
# Green: 0.91 < V <= 1.81 2/3
# Orange: V <= 0.91 full


def read_voltage(pico_pin):
    raw = pico_pin.read_u16()
    voltage = raw * 3.3 / 65535
    return voltage


def tank_level(voltage):
    if voltage > 2.72:
        return "0"
    elif 1.81 < voltage <= 2.72:
        return "1"
    elif 0.91 < voltage <= 1.81:
        return "2"
    elif voltage <= 0.91:
        return "3"


def battery_level(voltage):
    if voltage < 2.63:
        return "0"
    elif 2.63 <= voltage < 2.81:
        return "1"
    elif 2.81 <= voltage < 2.98:
        return "2"
    elif 2.98 <= voltage < 3.08:
        return "3"
    elif voltage >= 3.08:
        return "4"


def format_tank(pico_voltage):
    scaled_volt = pico_voltage * (8200 + 5760) / 5760
    rounded_volt = round(scaled_volt, 2)
    # format_volt = "{:.2f}".format(rounded_volt)
    return rounded_volt


def format_battery(pico_voltage):
    scaled_volt = pico_voltage * (34800 + 10200) / 10200
    rounded_volt = round(scaled_volt, 2)
    # format_volt = "{:.2f}".format(rounded_volt)
    return rounded_volt


def get_status(panel_x24, panel_x26, gray_water_pin, fresh_water_pin, battery_pin):
    # initialize class
    start_screen = TrailScreen(panel_x24, panel_x26)

    # read pins
    read_gray = read_voltage(gray_water_pin)
    read_fresh = read_voltage(fresh_water_pin)
    read_battery = read_voltage(battery_pin)

    # debug
    # read_gray = 0.5
    # read_fresh =0.5
    # read_battery =3.09

    # scale voltage
    gray_volt = format_tank(read_gray)
    fresh_volt = format_tank(read_fresh)
    battery_volt = format_battery(read_battery)

    # determine status
    gray_status = tank_level(read_gray)
    fresh_status = tank_level(read_fresh)
    battery_status = battery_level(read_battery)

    return (
        gray_volt,
        fresh_volt,
        battery_volt,
        gray_status,
        fresh_status,
        battery_status,
    )


def update_display(
    gray_status, fresh_status, battery_status, gray_volt, fresh_volt, battery_volt
):
    start_screen.process_gray(gray_status)
    start_screen.process_fresh(fresh_status)
    start_screen.process_battery(battery_status)

    start_screen.process_voltage_readings(gray_volt, fresh_volt, battery_volt)

    get_x24, get_x26 = start_screen.get_screen()

    # call epd driver and write to screen
    epd = EPD_2in9_Portrait()
    epd.Clear(0xFF)
    epd.fill(0xFF)
    epd.init_4Gray()
    epd.display_Gray_Image(get_x24, get_x26)
    epd.sleep()


def clear_display():
    epd = EPD_2in9_Portrait()
    epd.init()
    epd.Clear(0xFF)
    epd.fill(0xFF)
    epd.Clear(0xFF)
    epd.sleep()


if constant_power:
    clear_display()
    # Time to clear display for storage and cycle power off
    utime.sleep(1000)
    g_volt, f_volt, b_volt, g_status, f_status, b_status = get_status(
        panel_x24, panel_x26, gray_water_pin, fresh_water_pin, battery_pin
    )
    previous_g_status = g_status
    previous_f_status = f_status
    previous_b_status = b_status
    update_display(
        gray_status, fresh_status, battery_status, gray_volt, fresh_volt, battery_volt
    )
    # Checks status every 20 minutes
    while constant_power:
        g_volt, f_volt, b_volt, g_status, f_status, b_status = get_status(
            panel_x24, panel_x26, gray_water_pin, fresh_water_pin, battery_pin
        )
        if (
            previous_g_status != g_status
            or previous_f_status != f_status
            or previous_b_status != b_status
        ):
            previous_g_status = g_status
            previous_f_status = f_status
            previous_b_status = b_status
            update_display(
                gray_status,
                fresh_status,
                battery_status,
                gray_volt,
                fresh_volt,
                battery_volt,
            )
        utime.sleep(1200000)

else:
    current_time = utime.ticks_ms()
    while current_time < 1500:
        g_volt, f_volt, b_volt, g_status, f_status, b_status = get_status(
            panel_x24, panel_x26, gray_water_pin, fresh_water_pin, battery_pin
        )
        update_display(
            gray_status,
            fresh_status,
            battery_status,
            gray_volt,
            fresh_volt,
            battery_volt,
        )
    clear_display()
