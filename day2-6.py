# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:39:33 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
blockid=int(input("你要放的方塊:"))
mc.setBlock(x+1,y,z,blockid)
