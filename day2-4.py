# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:27:20 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
while True:
    flower=random.randrange(9)
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z+1,9,flower)