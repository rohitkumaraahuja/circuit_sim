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


# Importing Images

battery_img = pygame.image.load('resources/images/battery.png')
battery_img_size = battery_img.get_size()
scaled_battery_img = pygame.transform.scale(battery_img, (battery_img_size[0]*0.08, battery_img_size[1]*0.08))

bulbOn_img = pygame.image.load('resources/images/bulb_on.png')
bulbOff_img = pygame.image.load('resources/images/bulb_off.png')
bulb_img_size = bulbOn_img.get_size()
scaled_bulbOn_img = pygame.transform.scale(bulbOn_img, (bulb_img_size[0]*0.15,bulb_img_size[1]*0.15))
scaled_bulbOff_img = pygame.transform.scale(bulbOff_img, (bulb_img_size[0]*0.15,bulb_img_size[1]*0.15))


# Menu Button
menuIcon_img = pygame.image.load('resources\images\menu_icon.png')
menuIcon_img_size = menuIcon_img.get_size()
scaled_menuIcon_img = pygame.transform.scale(menuIcon_img, (menuIcon_img_size[0]*0.2, menuIcon_img_size[1]*0.2))
scaled_menuIcon_img_size = scaled_menuIcon_img.get_size()
menu_btn_x = WINDOW_WIDTH*0.01
menu_btn_y = WINDOW_HEIGHT*0.1
menu_btn_close_x = WINDOW_WIDTH*0.01
menu_btn_open_x = WINDOW_WIDTH*0.15
menu_open = False



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



    # Interactivity of menu button
    
    if mouse[0] and mouse_pos[0] >= menu_btn_x and mouse_pos[1] >= menu_btn_y and mouse_pos[0] <= menu_btn_x + scaled_menuIcon_img_size[0] and mouse_pos[1] <= menu_btn_y + scaled_menuIcon_img_size[1]:
        menu_open = not menu_open
        if menu_btn_x == menu_btn_open_x:
            menu_btn_x = menu_btn_close_x
        elif menu_btn_x == menu_btn_close_x:
            menu_btn_x = menu_btn_open_x








    # Fill the background
    window.fill(OFF_WHITE)


    #Draw menu button



    # Draw battary
    window.blit(scaled_battery_img, (WINDOW_WIDTH*0.8,WINDOW_HEIGHT*0.6))


    # Draw the side element tab
    if menu_open:
        pygame.draw.rect(window, LIGHT_BLUE, (0, 70, WINDOW_WIDTH*0.2, WINDOW_HEIGHT-70), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_x, menu_btn_y))

        # Draw Bulb on Tab
        window.blit(scaled_bulbOn_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1))


    else:
        pygame.draw.rect(window, LIGHT_BLUE, (0, 70, WINDOW_WIDTH*0.06, WINDOW_HEIGHT-70), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_close_x, menu_btn_y))


    


    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(5)
