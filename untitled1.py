# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:32:28 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
tricia=Minecraft.create()


x,y,z = tricia.player.getTilePos

tricia.setBlock(x,y-1,z,36)
time.sleep(0.2)
tricia.setBlock(x,y-1,z,36)
time.sleep(0.2)
tricia.setBlock(x,y-1,z,36)
time.sleep(0.2)
tricia.setBlock(x,y-1,z,36)
time.sleep(0.2)
tricia.setBlock(x,y-1,z,36)
time.sleep(0.2)
tricia.setBlock(x,y-1,z,36)
time.sleep(0.2)
tricia.setBlock(x,y-1,z,36)
time.sleep(0.2)
tricia.setBlock(x,y-1,z,36)