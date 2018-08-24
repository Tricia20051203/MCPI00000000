# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:36:15 2018

@author: """

from mcpi.minecraft import Minecraft
tricia=Minecraft.create()

weather = 1
x,y,z = tricia.player.getTilePos()
for i in range(number):
    tricia.spawnEntity(x,y,z,60)
number =number*2