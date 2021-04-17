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
sine_start_x = 300
cosine_start_y = 400

center_x = 150
center_y = 500
radius = 50

dot_x = center_x
dot_y = center_y
dot_radius = 5
angle = 0

sine_dots = []
cosine_dots = []

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
    pygame.draw.line(screen, gray, (dot_x, dot_y), (sine_start_x, dot_y))
    pygame.draw.line(screen, gray, (dot_x, dot_y), (dot_x, cosine_start_y))


    # line from origin and triangle
    pygame.draw.line(screen, gray, (center_x, center_y), (dot_x, dot_y))
    pygame.draw.line(screen, gray, (dot_x, dot_y), (dot_x, center_y))
    pygame.draw.line(screen, gray, (center_x, center_y), (dot_x, center_y))

    pygame.draw.circle(screen, white, (dot_x, dot_y), dot_radius)

    if angle >= 360:
        angle = 2
    angle += 5

    # draw a dot at the end of the line
    pygame.draw.circle(screen, white, (sine_start_x, dot_y), 5)
    pygame.draw.circle(screen, white, (dot_x, cosine_start_y), 5)


    new_sine_dot = [sine_start_x, dot_y] # [x_pos, y_pos]
    new_cosine_dot = [dot_x, cosine_start_y]

    sine_dots.insert(0, new_sine_dot)
    cosine_dots.insert(0, new_cosine_dot)

    # move all the dots to the right and draw them
    for dot in sine_dots:
        dot[0] += 3 # x += 3
        pygame.draw.circle(screen, white, (dot[0], dot[1]), 5)

    # move all the dots up and draw
    for dot in cosine_dots:
        dot[1] -= 3 # x += 3
        pygame.draw.circle(screen, white, (dot[0], dot[1]), 5)
        
    # remove dot if exceed 200 dots
    if len(sine_dots) > 200:
        sine_dots.pop()

    # remove dot if exceed 200 dots
    if len(cosine_dots) > 200:
        cosine_dots.pop()

    # draw on screen
    pygame.display.flip()