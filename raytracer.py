import pygame as pg
from pygame.locals import *
from rt import Raytracer
from figures import *
from materials import *
from lights import *


width = 768
height = 640

pg.init()

screen = pg.display.set_mode((width, height), pg.DOUBLEBUF | pg.HWACCEL | pg.HWSURFACE)
screen.set_alpha(None)

raytracer = Raytracer(screen=screen)

raytracer.envMap = pg.image.load("environmentMap.jpg")
fireTex = pg.image.load("fire.bmp")

raytracer.rtClearColor(0.25, 0.25, 0.25)

grass = Material(diffuse=(0.4, 1, 0.4), specular=32, ks=0.1)
fire = Material(texture=fireTex)
glass = Material(diffuse=(0.9, 0.9, 0.9), specular=64, ks=0.2, ior=1.5, matType=REFLECTIVE)
silver = Material(diffuse=(0.5, 0.5, 0.5), specular=128, ks=0.15, ior=1, matType=REFLECTIVE)
diamon = Material(diffuse=(0.9, 0.9, 0.9), specular=64, ks=0.2, ior=2.417, matType=TRANSPARENT)
water = Material(diffuse=(0.4, 0.4, 1.0), specular=128, ks=0.2, ior=1.33, matType=TRANSPARENT)

raytracer.scene.append(Sphere(position=(-2, 1, -5), radius=1, material=grass))
raytracer.scene.append(Sphere(position=(-2, -1, -5), radius=1, material=fire))
raytracer.scene.append(Sphere(position=(0, 1, -5), radius=1, material=glass))
raytracer.scene.append(Sphere(position=(0, -1, -5), radius=1, material=silver))
raytracer.scene.append(Sphere(position=(2, 1, -5), radius=1, material=diamon))
raytracer.scene.append(Sphere(position=(2,-1, -5), radius=1, material=water))


#Lights
raytracer.lights.append(AmbientLight(0.1))
raytracer.lights.append(DirectionalLight(direction=(-1, -1, -1), intensity=0.9))


isRunning = True
while(isRunning):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isRunning = False
            elif event.key == pg.K_s:
                pg.image.save(screen, "image.bmp")
    raytracer.rtClear()
    raytracer.rtRender()
    pg.display.flip()



pg.quit()
