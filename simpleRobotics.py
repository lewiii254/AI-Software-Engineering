# Import necessary libraries
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Robot Simulation")

# Set up the robot
robot = pygame.Rect(400, 300, 50, 50)
robot_color = (0, 128, 255)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the robot based on key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        robot.y -= 5
    if keys[pygame.K_DOWN]:
        robot.y += 5
    if keys[pygame.K_LEFT]:
        robot.x -= 5
    if keys[pygame.K_RIGHT]:
        robot.x += 5

    # Draw the robot
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, robot_color, robot)
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)