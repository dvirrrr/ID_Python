import os
import time

def change_resolution():
    # Check the current screen resolution
    current_resolution = os.popen('dumpsys display | grep mDisplayInfo').read()
    if '1080p-59.94hz' in current_resolution:
        # Change the screen resolution to 1080p-50hz
        os.system('wm size 1920x1080')
        os.system('wm density 320')
        os.system('settings put system display_mode 1080p-50hz')
    elif '1080p-50hz' in current_resolution:
        # Change the screen resolution to 1080p-59.94hz
        os.system('wm size 1920x1080')
        os.system('wm density 320')
        os.system('settings put system display_mode 1080p-59.94hz')
    else:
        print('Error: Unsupported screen resolution')

# Wait for the device to boot up
time.sleep(30)

# Change the screen resolution
change_resolution()
