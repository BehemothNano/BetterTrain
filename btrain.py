!#usr/bin/python3
"""
A silly little thing to entertain you while your model trains.
Your training script must be written in python for this to work, if it isn't, 
c for example, make a small python script that runs your non-python training 
script, and use that when running this.

Copyright (C) 2023-2024 Dylan Buchanan

To play: 
    btrain <training script name>
    Args (optional): 
        -pyv <python version>, --python_version # Specifies the python version that should be used when running your training script.

"""

import actors
import world
import regen
import pathfind
import player
import inventories
import engine
import graphics
