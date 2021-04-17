"""
animation of a sine wave from a circle
"""

import os
import sys
import math
import pygame

os.environ["SDL_VIDEO_CENTERED"]='1'

# set up pygame
pygame.init()
width, height = 800, 600
size = (width, height)
fps = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sine Wave')
clock = pygame.time.Clock()

# define color
white = (230, 230, 230)
black = (28, 28, 28)
gray = (100, 100, 100)

# constant
center_x = 150
center_y = 300
radius = 100

dot_x = center_x
dot_y = center_y
dot_radius = 5
angle = 0

wave_dots = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
    
    # set fps and reset screen everyframe
    clock.tick(fps)
    screen.fill(black)

    # main circle
    pygame.draw.circle(screen, white, (center_x, center_y), radius, 2)

    # rotating dot
    dot_x = center_x + (radius * math.cos(math.radians(angle)))
    dot_y = center_y - (radius * math.sin(math.radians(angle)))

    # need to draw line before the dot (cleaner look)
    pygame.draw.line(screen, gray, (dot_x, dot_y), (300, dot_y))

    # line from origin and axis
    pygame.draw.line(screen, gray, (center_x, center_y), (dot_x, dot_y))
    pygame.draw.line(screen, gray, (dot_x, dot_y), (dot_x, center_y))

    pygame.draw.circle(screen, white, (dot_x, dot_y), dot_radius)

    if angle >= 360:
        angle = 2
    angle += 3

    # draw axis
    pygame.draw.line(screen, gray, (center_x - radius, center_y), (width, center_y))

    # draw a dot at the end of the line
    pygame.draw.circle(screen, white, (300, dot_y), 5)

    new_dot = [300, dot_y] # [x_pos, y_pos]

    wave_dots.insert(0, new_dot)

    # move all the dots to the right and draw them
    for dot in wave_dots:
        dot[0] += 3 # x += 3
        pygame.draw.circle(screen, white, (dot[0], dot[1]), 5)
        
    # remove dot if exceed 1000 dots
    if len(wave_dots) > 200:
        wave_dots.pop()

    # draw on screen
    pygame.display.flip()