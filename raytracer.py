import pygame as pg
from pygame.locals import *
from rt import Raytracer
from figures import *
from materials import *
from lights import *


width = 512
height = 512

pg.init()

screen = pg.display.set_mode((width, height), pg.DOUBLEBUF | pg.HWACCEL | pg.HWSURFACE)
screen.set_alpha(None)

raytracer = Raytracer(screen=screen)

raytracer.envMap = pg.image.load("envMap.jpg")
earthTex = pg.image.load("earth.bmp")

raytracer.rtClearColor(0.25, 0.25, 0.25)

grass = Material(diffuse=(0.4, 1, 0.4), specular=32, ks=0.1)
water = Material(diffuse=(0.4, 0, 1), specular=256, ks=0.2)
mirror = Material(diffuse=(0.9, 0.9, 0.9), specular=64, ks=0.2, matType=REFLECTIVE)
blueMirror = Material(diffuse=(0.4, 0.4, 0.9), specular=32, ks=0.15, matType=REFLECTIVE)
earth = Material(texture=earthTex)

""" raytracer.scene.append(Sphere(position=(1, 1, -5), radius=0.5, material=grass))
raytracer.scene.append(Sphere(position=(0, 0, -7), radius=2, material=mirror))
raytracer.scene.append(Sphere(position=(0.5, -1, -5), radius=0.3, material=water)) """

raytracer.scene.append(Sphere(position=(-2, 0, -7), radius=1.5, material=mirror))
raytracer.scene.append(Sphere(position=(2, 0, -7), radius=2, material=earth))
raytracer.scene.append(Sphere(position=(0, -1, -5), radius=0.5, material=blueMirror))


#Lights
raytracer.lights.append(AmbientLight(0.1))
raytracer.lights.append(DirectionalLight(direction=(-1, -1, -1), intensity=0.7))
raytracer.lights.append(PointLight(point=(1.5, 0, -5), intensity=1, color=(1, 0, 1)))


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
