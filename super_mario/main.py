import pygame, sys
from pygame.math import Vector2 as vector
from settings import *
from support import *

from pygame.image import load

from editor import Editor
from level import Level

from os import walk

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock=pygame.time.Clock()
        self.imports()


        self.editor_active=True
        self.transition=Transition(self.toggle)
        self.editor=Editor(self.land_tiles,self.switch)
    
        #cursor
        surf=load('super_mario/graphics/cursor/mouse.png').convert_alpha()
        cursor=pygame.cursors.Cursor((0,0),surf)
        pygame.mouse.set_cursor(cursor)
        
    def imports(self):
        #terrain graphics
        self.land_tiles=import_folder_dict('super_mario/graphics/terrain/land_1')
        self.water_bottom=load('super_mario/graphics/terrain/water/water_bottom.png').convert_alpha()
        self.water_top_animation=import_folder('super_mario/graphics/terrain/water/animation')

        #coins graphics
        self.gold=import_folder('super_mario/graphics/items/gold')
        self.silver=import_folder('super_mario/graphics/items/silver')
        self.diamond=import_folder('super_mario/graphics/items/diamond')
        self.particle=import_folder('super_mario/graphics/items/particle')

        #palm trees graphics
        self.palms={folder:import_folder(f'super_mario/graphics/terrain/palm/{folder}') for folder in list(walk('super_mario/graphics/terrain/palm'))[0][1]}


        #enemies graphics
        self.spikes=load('super_mario/graphics/enemies/spikes/spikes.png').convert_alpha()
        self.tooth={folder:import_folder(f'super_mario/graphics/enemies/zombie/{folder}') for folder in list(walk('super_mario/graphics/enemies/zombie'))[0][1]}
        self.shell={folder:import_folder(f'super_mario/graphics/enemies/shell_left/{folder}') for folder in list(walk('super_mario/graphics/enemies/shell_left'))[0][1]}
        self.pearl=load('super_mario/graphics/enemies/pearl/pearl.png').convert_alpha()


        #player graphics
        self.player_graphics={folder:import_folder(f'super_mario/graphics/player_1/{folder}') for folder in list(walk('super_mario/graphics/player_1'))[0][1]}

        #clouds
        self.clouds=import_folder('super_mario/graphics/cloud')

        #music
        self.level_sounds={
            'coin':pygame.mixer.Sound('super_mario/audio/coin.wav'),
            'hit':pygame.mixer.Sound('super_mario/audio/hit.wav'),
            'jump':pygame.mixer.Sound('super_mario/audio/jump.wav'),
            'music':pygame.mixer.Sound('super_mario/audio/SuperHero.ogg'),
            
        }

    def toggle(self):
        self.editor_active= not self.editor_active
        if self.editor_active:
            self.editor.editor_music.play()

    def switch(self,grid=None): #for display graphics in the actual level
        self.transition.active=True
        if grid:
            self.level=Level(
                grid,
                self.switch,{
                'land':self.land_tiles,
                'water bottom':self.water_bottom,
                'water top':self.water_top_animation,
                'gold':self.gold,
                'silver':self.silver,
                'diamond':self.diamond,
                'particle':self.particle,
                'palms':self.palms,
                'spikes':self.spikes,
                'tooth':self.tooth,
                'shell':self.shell,
                'player':self.player_graphics,
                'pearl':self.pearl,
                'clouds':self.clouds},
            self.level_sounds)

    def run(self):
        while True:
            dt=self.clock.tick()/1000

            if self.editor_active:
                self.editor.run(dt)
            else:
                self.level.run(dt)
            self.transition.display(dt)
            pygame.display.update()


class Transition:
    def __init__(self,toggle):
        self.display_surface=pygame.display.get_surface()
        self.toggle=toggle
        self.active=False

        self.border_width=0
        self.direction=1
        self.center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
        self.radius=vector(self.center).magnitude()
        self.threshold=self.radius+100

    def display(self,dt):
        if self.active:
            self.border_width+=100*dt*self.direction
            if self.border_width>=self.threshold:
                self.direction=-1
                self.toggle()

            if self.border_width<0:
                self.active=False
                self.border_width=0
                self.direction=1
            pygame.draw.circle(self.display_surface,'black',self.center,self.radius,int(self.border_width))

if __name__=='__main__':
    main=Main()
    main.run()
