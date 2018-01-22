# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2017 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA  02110-1301, USA.
"""
This script shows the basic use of the MotionCommander class.

Simple example that connects to the crazyflie at `URI` and runs a
sequence. This script requires some kind of location system, it has been
tested with (and designed for) the flow deck.

Change the URI variable to your Crazyflie configuration.
"""
import sys
import logging
import time
import pygame

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

def key_ctrl(mc):

    print 'WASD for throttle & yaw; arrow keys for left/right/forward/backward' 
    print 'Spacebar to land'

    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    mc.up(0.3)

                elif event.key == pygame.K_SPACE:  
                    print 'Space pressed, landing'
                    pygame.quit()
                    sys.exit(0)

                elif event.key == pygame.K_a:
                    mc.start_turn_left(30)

                elif event.key == pygame.K_s:
                    mc.down(0.3)

                elif event.key == pygame.K_d:
                    mc.start_turn_right(30)

                elif event.key == pygame.K_UP:
                    mc.start_forward(0.3)   

                elif event.key == pygame.K_DOWN:
                    mc.start_back(0.3)

                elif event.key == pygame.K_LEFT:
                    mc.start_left(0.3)

                elif event.key == pygame.K_RIGHT:
                    mc.start_right(0.3)

                elif event.key == pygame.K_RCTRL:
                    mc.stop()
                

            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_w:
                    mc.start_up(0)

                elif event.key == pygame.K_a:
                    mc.start_turn_left(0)

                elif event.key == pygame.K_s:
                    mc.start_down(0)

                elif event.key == pygame.K_d:
                    mc.start_turn_right(0)

                elif event.key == pygame.K_UP:
                    mc.start_forward(0)   

                elif event.key == pygame.K_DOWN:
                    mc.start_back(0)

                elif event.key == pygame.K_LEFT:
                    mc.start_left(0)

                elif event.key == pygame.K_RIGHT:
                    mc.start_right(0)



if __name__ == '__main__':

    try:

        cflib.crtp.init_drivers(enable_debug_driver=False)


        with SyncCrazyflie(URI) as scf:

            print 'Spacebar to start'
            raw_input()
            pygame.display.set_mode((400, 300))
            # We take off when the commander is created
            with MotionCommander(scf) as mc:
                time.sleep(1)
                
                key = threading.Thread(target = key_ctrl)
                key.start()
                


       
    except Exception:
        print('\nShutting down...')
                
        pygame.quit()
        sys.exit(0) 
    
