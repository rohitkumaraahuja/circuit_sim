import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode()

WINDOW_WIDTH, WINDOW_HEIGHT = window.get_size()


pygame.display.set_caption("Basic Pygame Example")

# Set up colors
WHITE = (255, 255, 255)
OFF_WHITE = (200,200,200)
RED = (255, 0, 0)
LIGHT_BLUE = (64, 64, 128)

# Set up the rectangle
tools_width = 100
tools_height = 100
tools_x = WINDOW_WIDTH*0.1 //1 - tools_width*0.1 // 1
tools = 5
rect_speed = 5


box_color = OFF_WHITE

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the rectangle
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    
    # if mouse[0] and mouse_pos[0] >= tools_x and mouse_pos[1] >= tools_y and mouse_pos[0] <= rect_x + rect_width and mouse_pos[1] <= rect_y + rect_width:
    #     box_color = RED








    # Fill the background
    window.fill(OFF_WHITE)

    # Draw the side element tab
    pygame.draw.rect(window, LIGHT_BLUE, (0, 70, WINDOW_WIDTH*0.2, WINDOW_HEIGHT-70))


    # Draw Elements Tab
    for i in range(tools):
        pygame.draw.rect(window, OFF_WHITE, (WINDOW_WIDTH*0.07, (WINDOW_HEIGHT/(tools+1))*(i+1), tools_width, tools_height))


    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
