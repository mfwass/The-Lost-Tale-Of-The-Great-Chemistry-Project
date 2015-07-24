# George Mrsich, Michael Wass & Michael Vanyo
# 5/27/2015
# Chemistry Project

# Importing a class runs anything before the
# game window opens.
print(":ClientStart: Starting the game...")
print(":ClientStart: Preloading window...")
import ClientPreloader
# Import the base class that opens the game window.
import ClientBase
print(":ClientStart: Creating game window...")
# Open the game window
ClientBase.ClientBase()

if not base.win:
    raise StandardError("Main window failed to open! Please check your computer graphics.")

base.run()