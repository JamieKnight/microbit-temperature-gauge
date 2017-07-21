from microbit import *

while True:
    # Settings
    target_temp = 24
    trim = 6  # See Readme.

    # Show trimmed temp when button pressed.
    trimmed_temp = temperature() - trim

    if button_a.is_pressed():
        display.scroll(str(trimmed_temp) + 'c')

    # Subtract target tempreture from trimmed tem.
    remainder = trimmed_temp - target_temp  # Trimmed to '0'

    # Display the relevant icon based on remainder.
    if remainder < 0:
        display.show(Image.TSHIRT)
        sleep(2000)
    elif remainder == 0:
        display.show(Image.YES)
        sleep(2000)
    elif remainder > 0 and remainder < 3:
        display.show(Image.NO)
        sleep(2000)
    elif remainder >= 3:
        display.show('!' + str(remainder))
        sleep(500)
