import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys

# Initialize Pygame
pygame.init()

# Set up display
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glViewport(0, 0, display[0], display[1])

# Set up perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Set up clear color
glClearColor(0.0, 0.0, 0.0, 1.0)

# Enable depth testing
glEnable(GL_DEPTH_TEST)

# Initial car parameters
car_speed = 0.0
car_turn_angle = 0.0
car_pos = [0.0, 0.0, 0.0]
car_direction = 0.0

# Function to draw the car
def draw_car():
    glBegin(GL_QUADS)

    # Car body
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, -1.0)

    # Car top
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, 1.0)
    glVertex3f(0.0, 1.0, 1.0)
    glVertex3f(0.0, 1.0, -1.0)

    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(0.0, 1.0, -1.0)
    glVertex3f(0.0, 1.0, 1.0)

    glEnd()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard input handling
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                car_speed += 0.1  # Accelerate
            elif event.key == pygame.K_s:
                car_speed -= 0.05  # Decelerate (half as fast)
            elif event.key == pygame.K_a:
                car_turn_angle += 5.0  # Turn left
            elif event.key == pygame.K_d:
                car_turn_angle -= 5.0  # Turn right

    # Limit speed to a maximum of 1
    car_speed = min(max(car_speed, 0), 1)

    # Update car direction based on turn angle
    car_direction += car_turn_angle * 0.01  # Reduce turn angle impact

    # Update car position based on speed and direction
    car_pos[0] += car_speed * math.sin(math.radians(car_direction))
    car_pos[2] += car_speed * math.cos(math.radians(car_direction))

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset transformations
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)
    glTranslatef(car_pos[0], car_pos[1], car_pos[2])
    glRotatef(car_direction, 0, 1, 0)

    # Draw the car
    draw_car()

    # Update display
    pygame.display.flip()

    # Pause briefly to control frame rate
    pygame.time.wait(10)
