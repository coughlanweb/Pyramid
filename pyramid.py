# import the minecraft python library
from mcpi.minecraft import Minecraft

# make a connection to our game
mc = Minecraft.create()

# set what block we want to use
block = 24  # sandstone

# set the height of our pyramid
height = 10

# set how many levels our pyramid will have. It uses the range function with the input of the height variable
levels = reversed(range(height))

# We then get the players position in the game using the X, Y and Z coordinates
pos = mc.player.getTilePos()

# We then have to make sure the player isnt stuck inside the pyramid, so we add the height variable to the x coordinate
x, y, z = pos.x + height, pos.y, pos.z


# The for loop then iterates over each level in the levels variable ( if we set it at 10, its starts and 1, then 2 etc )  and builds a square
for level in levels:
    mc.setBlocks(x - level, y, z - level, x + level, y, z + level, block)

    # after each squares is built, we add one to the y axis to move the structure up 1 block 
    y += 1
