# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:16:37 2018

@author: NTPU
"""
from random import choice
from mcpi.minecraft import Minecraft
tricia=Minecraft.create()

block = [14,15,16,56,73,129]

r = choice(block)
myID = tricia.getPlayerEntityId("tricia2015")
x,y,z = tricia.entity.getTilePos(myID)

tricia.setBlock(x,y,z,r)