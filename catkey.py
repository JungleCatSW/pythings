import colorsys
import random

from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()


print("Found {} Razer devices".format(len(device_manager.devices)))
print()

# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
device_manager.sync_effects = False

# Helper funciton to generate interesting colors

red = (255,8,8)
green = (100,255,0)
blue = (0,0,255)
lightblue = (128,128,255)
yellow = (255,255,0)
purple = (255,0,255)
mint = (0,255,255)
orange = (255,80,0)
white = (255,255,255)

def random_color():
    rgb = colorsys.hsv_to_rgb(random.uniform(0, 1), random.uniform(0.5, 1), 1)
    return tuple(map(lambda x: int(256 * x), rgb))

# Set random colors for each zone of each device
for device in device_manager.devices:
    rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

    for row in range(rows):
        for col in range(cols):
            device.fx.advanced.matrix[row, col] = red
    # f1 keys
    device.fx.advanced.matrix[0, 1] = white
    device.fx.advanced.matrix[0, 2] = blue
    device.fx.advanced.matrix[0, 3] = purple
    device.fx.advanced.matrix[0, 4] = purple
    device.fx.advanced.matrix[0, 9] = yellow
    device.fx.advanced.matrix[0, 10] = yellow
    device.fx.advanced.matrix[0, 11] = lightblue
    device.fx.advanced.matrix[0, 12] = lightblue
    device.fx.advanced.matrix[0, 14] = white
    device.fx.advanced.matrix[0, 15] = yellow
    #number keys
    device.fx.advanced.matrix[1, 1] = orange
    device.fx.advanced.matrix[1, 12] = orange
    device.fx.advanced.matrix[1, 13] = orange
    device.fx.advanced.matrix[1, 14] = yellow
    #first row letter keys
    #tab
    device.fx.advanced.matrix[2, 0] = lightblue
    #device.fx.advanced.matrix[2, 1] = lightblue
    device.fx.advanced.matrix[2, 12] = lightblue
    device.fx.advanced.matrix[2, 13] = lightblue
    # caps
    device.fx.advanced.matrix[3, 0] = white
    device.fx.advanced.matrix[3, 11] = purple
    device.fx.advanced.matrix[3, 12] = purple
    device.fx.advanced.matrix[3, 14] = green
    device.fx.advanced.matrix[3, 15] = green
    #shift rows
    device.fx.advanced.matrix[4, 0] = mint
    device.fx.advanced.matrix[4, 1] = mint

    device.fx.advanced.matrix[4, 11] = orange
    device.fx.advanced.matrix[4, 10] = orange
    device.fx.advanced.matrix[4, 9] = orange
    device.fx.advanced.matrix[4, 14] = mint
    #ctrl
    device.fx.advanced.matrix[5, 0] = yellow
    device.fx.advanced.matrix[5, 1] = purple
    device.fx.advanced.matrix[5, 2] = white
    device.fx.advanced.matrix[5, 3] = blue
    device.fx.advanced.matrix[5, 9] = blue
    device.fx.advanced.matrix[5, 10] = purple
    device.fx.advanced.matrix[5, 11] = yellow
    device.fx.advanced.matrix[5, 12] = white
    device.fx.advanced.matrix[5, 14] = white
    device.fx.advanced.draw()
