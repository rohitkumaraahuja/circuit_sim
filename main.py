import pygame
import sys
from resources.helper_functions import *










def is_hovering(rect_tuple, mouse_pos):
    x0 = rect_tuple[0][0]
    y0 = rect_tuple[0][1]
    x1 = rect_tuple[1][0]
    y1 = rect_tuple[1][1]
    if mouse_pos[0] >= x0 and mouse_pos[1] >= y0 and mouse_pos[0] <= x1 and mouse_pos[1] <= y1:
        return True
    return False






def is_clicked(rect_tuple, mouse_pos, mouse): # from ((x,y),(x,y))
    x0 = rect_tuple[0][0]
    y0 = rect_tuple[0][1]
    x1 = rect_tuple[1][0]
    y1 = rect_tuple[1][1]

    if mouse[0] and mouse_pos[0] >= x0 and mouse_pos[1] >= y0 and mouse_pos[0] <= x1 and mouse_pos[1] <= y1:
        return True
    return False
        


























# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode()

WINDOW_WIDTH, WINDOW_HEIGHT = window.get_size()


pygame.display.set_caption("Basic Pygame Example")


#Creating Linked list
circuit = create_a_linkedlist


# Set up colors
WHITE = (255, 255, 255)
OFF_WHITE = (200,200,200)
RED = (255, 0, 0)
LIGHT_BLUE = (64, 64, 128)

# Menu Tools Constants
tools_width = 100
tools_height = 100
tools_x = WINDOW_WIDTH*0.1 //1 - tools_width*0.1 // 1
tools = 5
rect_speed = 5
MENU_BUTTON_SIZE = 9600
TOOLS_BUTTON_SIZE = 5000
SCALED_TOOL_SIZE = (480*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 480*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)





# Menu Button
menuIcon_img = pygame.image.load('resources/images/menu_icon.png')
menuIcon_img_size = menuIcon_img.get_size()
scaled_menuIcon_img = pygame.transform.scale(menuIcon_img, (menuIcon_img_size[0]*WINDOW_WIDTH//MENU_BUTTON_SIZE, menuIcon_img_size[1]*WINDOW_WIDTH//MENU_BUTTON_SIZE))
scaled_menuIcon_img_size = scaled_menuIcon_img.get_size()
menu_btn_x = WINDOW_WIDTH*0.01
menu_btn_y = WINDOW_HEIGHT*0.1
menu_btn_close_x = WINDOW_WIDTH*0.01
menu_btn_open_x = WINDOW_WIDTH*0.15
menu_open = False




# Main game loop
while True:






    # Generating Images


    #Bulb Images
    bulbOn_rawIMG = 'resources/images/bulb_on.png'
    bulbOff_rawIMG = 'resources/images/bulb_off.png'



    




    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





    # Interactivity of menu button
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    


    if is_clicked(((menu_btn_x, menu_btn_y),(menu_btn_x + scaled_menuIcon_img_size[0], menu_btn_y + scaled_menuIcon_img_size[1])), mouse_pos, mouse):
        menu_open = not menu_open
        if menu_btn_x == menu_btn_open_x:
            menu_btn_x = menu_btn_close_x
        elif menu_btn_x == menu_btn_close_x:
            menu_btn_x = menu_btn_open_x
    

    if is_hovering(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1),(WINDOW_WIDTH*0.05+SCALED_TOOL_SIZE[0], (((WINDOW_HEIGHT-70)/(tools+1))*1) + SCALED_TOOL_SIZE[1])), mouse_pos):
        bulbOff_rawIMG = 'resources/images/bulb_on_highlighted.png'

    



    # Fill the background
    window.fill(OFF_WHITE)





    # Importing Images


    # Battery Images
    battery_img = pygame.image.load('resources/images/battery.png')
    battery_img_size = battery_img.get_size()
    scaled_battery_img = pygame.transform.scale(battery_img, (battery_img_size[0]*0.08, battery_img_size[1]*0.08))


    # Bulb Images
    
    bulbOn_img = pygame.image.load(bulbOn_rawIMG)
    bulbOff_img = pygame.image.load(bulbOn_rawIMG)
    bulb_img_size = bulbOn_img.get_size()
    scaled_bulbOn_img = pygame.transform.scale(bulbOn_img, SCALED_TOOL_SIZE)
    scaled_bulbOff_img = pygame.transform.scale(bulbOff_img, SCALED_TOOL_SIZE)


    # Fan Images
    fanOn_img = pygame.image.load('resources/images/fan_on.gif')
    fanOff_img = pygame.image.load('resources/images/fan_off.png')
    fan_img_size = fanOn_img.get_size()
    scaled_fanOn_img = pygame.transform.scale(fanOn_img, SCALED_TOOL_SIZE)
    scaled_fanOff_img = pygame.transform.scale(fanOff_img, SCALED_TOOL_SIZE)













    # Draw battary
    window.blit(scaled_battery_img, (WINDOW_WIDTH*0.8,WINDOW_HEIGHT*0.6))







    # Draw the side element tab
    if menu_open:
        pygame.draw.rect(window, LIGHT_BLUE, (0, WINDOW_HEIGHT*0.05, WINDOW_WIDTH*0.2, WINDOW_HEIGHT), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_x, menu_btn_y))

        # Draw Tools on Tab
        window.blit(scaled_bulbOn_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1))
        window.blit(scaled_fanOn_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*2))


    else:
        pygame.draw.rect(window, LIGHT_BLUE, (0, WINDOW_HEIGHT*0.05, WINDOW_WIDTH*0.06, WINDOW_HEIGHT), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_close_x, menu_btn_y))



    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(5)








