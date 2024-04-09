import pygame
import sys
from resources.helper_functions import *
import random 
import time









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
window = pygame.display.set_mode((1366,768))

WINDOW_WIDTH, WINDOW_HEIGHT = window.get_size()


pygame.display.set_caption("Basic Pygame Example")








# Importing Images
zoomIn_img = pygame.image.load('resources/images/zoom-in.png')
zoomOut_img = pygame.image.load('resources/images/zoom-out.png')

battery_img = pygame.image.load('resources/images/battery.png')
highlighted_battery_img = pygame.image.load('resources/images/highlighted_battery.png')

bulbOn_rawIMG = 'resources/images/bulb_on.png'
bulbOff_rawIMG = 'resources/images/bulb_off.png'
bulbOn_img = pygame.image.load(bulbOn_rawIMG)
bulbOff_img = pygame.image.load(bulbOn_rawIMG)

fanOn_img = pygame.image.load('resources/images/fan_on.gif')
fanOff_img = pygame.image.load('resources/images/fan_off.png')

highlight_img = pygame.image.load('resources/images/highlight.png')






#Creating Linked list
circuit = create_a_linkedlist()

# Initiating the Battery
form_connection(circuit, "PS1", pre_ID1=None, data=(WINDOW_WIDTH*0.8,WINDOW_HEIGHT*0.6, 'resources/images/battery.png'), next_ID2=None)
form_connection(circuit, "NS1", pre_ID1=None, data=None, next_ID2=None)


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
SCALED_GUI_SIZE = (200*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 200*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)
BUTTON_SCALED_SIZE = (200*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 200*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)
#scaled_battery_size =  (1920*WINDOW_WIDTH//20000, 2831*WINDOW_WIDTH//20000)
scaled_battery_size = (131.136, 193.3573)
scaled_tool_size = (131.136, 131.136)
y_highlighted = 385*WINDOW_WIDTH//TOOLS_BUTTON_SIZE

menu_scaled_tool_size = (480*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 480*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)

point_scaled_tool_size = (100*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 100*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)



#Function Constant
clicked = False





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
    




























    # Importing Images
            
    # Zoom In and Out
    
    scaled_ZoomIn_img = pygame.transform.scale(zoomIn_img, SCALED_GUI_SIZE)
    scaled_ZoomOut_img = pygame.transform.scale(zoomOut_img, SCALED_GUI_SIZE)


    # Battery Images
    
    scaled_battery_img = pygame.transform.scale(battery_img, scaled_battery_size)
    highlighted_scaled_battery_img = pygame.transform.scale(highlighted_battery_img, scaled_battery_size)


    # Bulb Images

    
    scaled_bulbOn_img = pygame.transform.scale(bulbOn_img, scaled_tool_size)
    scaled_bulbOff_img = pygame.transform.scale(bulbOff_img, scaled_tool_size)
    menu_scaled_bulbOn_img = pygame.transform.scale(bulbOn_img, menu_scaled_tool_size)
    menu_scaled_bulbOff_img = pygame.transform.scale(bulbOff_img, menu_scaled_tool_size)


    # Fan Images
    
    scaled_fanOn_img = pygame.transform.scale(fanOn_img, scaled_tool_size)
    scaled_fanOff_img = pygame.transform.scale(fanOff_img, scaled_tool_size)
    menu_scaled_fanOn_img = pygame.transform.scale(fanOn_img, menu_scaled_tool_size)
    menu_scaled_fanOff_img = pygame.transform.scale(fanOff_img, menu_scaled_tool_size)



    #Highlight Image
    scaled_highlight_img = pygame.transform.scale(highlight_img, menu_scaled_tool_size)
    point_scaled_highlight_img = pygame.transform.scale(highlight_img, point_scaled_tool_size)
    button_highlight_img = pygame.transform.scale(highlight_img, BUTTON_SCALED_SIZE)
    
        

    



    # Fill the background
    window.fill(OFF_WHITE)





   







    #Draw Zoom In and Zoom Out
    window.blit(scaled_ZoomIn_img, (WINDOW_WIDTH*0.85,WINDOW_HEIGHT*0.9))
    ZoomIn_size = scaled_ZoomIn_img.get_size()
    if is_hovering(((WINDOW_WIDTH*0.85,WINDOW_HEIGHT*0.9),(WINDOW_WIDTH*0.85+ZoomIn_size[0],WINDOW_HEIGHT*0.9+ZoomIn_size[1] )) ,mouse_pos):
        window.blit(button_highlight_img, (WINDOW_WIDTH*0.85,WINDOW_HEIGHT*0.9))
    if is_clicked(((WINDOW_WIDTH*0.85,WINDOW_HEIGHT*0.9),(WINDOW_WIDTH*0.85+ZoomIn_size[0],WINDOW_HEIGHT*0.9+ZoomIn_size[1] )) ,mouse_pos, mouse):
        scaled_battery_size = (scaled_battery_size[0]*1.5,scaled_battery_size[1]*1.5)
        scaled_tool_size = (scaled_tool_size[0]*1.5,scaled_tool_size[1]*1.5)
        point_scaled_tool_size = (point_scaled_tool_size[0]*1.5,point_scaled_tool_size[1]*1.5)

    window.blit(scaled_ZoomOut_img, (WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.9))
    ZoomOut_size = scaled_ZoomOut_img.get_size()
    if is_hovering(((WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.9),(WINDOW_WIDTH*0.9+ZoomOut_size[0],WINDOW_HEIGHT*0.9+ZoomOut_size[1] )) ,mouse_pos):
        window.blit(button_highlight_img, (WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.9))
    if is_clicked(((WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.9),(WINDOW_WIDTH*0.9+ZoomOut_size[0],WINDOW_HEIGHT*0.9+ZoomOut_size[1] )) ,mouse_pos, mouse):
        scaled_battery_size = (scaled_battery_size[0]/1.5,scaled_battery_size[1]/1.5)
        scaled_tool_size = (scaled_tool_size[0]/1.5,scaled_tool_size[1]/1.5)
        point_scaled_tool_size = (point_scaled_tool_size[0]/1.5,point_scaled_tool_size[1]/1.5)



    # Draw batteries
    # window.blit(scaled_battery_img, (WINDOW_WIDTH*0.8,WINDOW_HEIGHT*0.6))


    print(circuit)




    

    # Draw the side element tab
    if menu_open:
        pygame.draw.rect(window, LIGHT_BLUE, (0, WINDOW_HEIGHT*0.05,WINDOW_WIDTH*0.2, WINDOW_HEIGHT), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_x, menu_btn_y))

        # Draw Tools on Tab

        
        window.blit(menu_scaled_bulbOn_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1))
        
        if is_hovering(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1),(WINDOW_WIDTH*0.05+menu_scaled_tool_size[0], (((WINDOW_HEIGHT-70)/(tools+1))*1) + menu_scaled_tool_size[1])), mouse_pos):
            window.blit(scaled_highlight_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1))
        if is_clicked(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1),(WINDOW_WIDTH*0.05+menu_scaled_tool_size[0], (((WINDOW_HEIGHT-70)/(tools+1))*1) + menu_scaled_tool_size[1])), mouse_pos,mouse):
            clicked = True


            if 'B1' not in circuit:
                add_connection(circuit, "PS1", 'B1', (last_element(circuit)[0]+100-131, last_element(circuit)[1]+13.5-104, 'resources/images/bulb_off_withWire.png'))
            else:
                count = random.randint(1, 500)
                while "B" + str(count) in circuit.keys():
                    count = random.randint(2, 500)    
                add_connection(circuit, "PS1", 'B'+str(count), (last_element(circuit)[0]+100-131, last_element(circuit)[1]+13.5-104, 'resources/images/bulb_off_withWire.png'))
            time.sleep(0.5)


        window.blit(menu_scaled_fanOn_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*2))
        if is_hovering(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*2),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*2) + scaled_tool_size[1])), mouse_pos):
            window.blit(scaled_highlight_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*2))
        if is_clicked(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*2),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*2) + scaled_tool_size[1])), mouse_pos,mouse):
            clicked = True

    else:
        pygame.draw.rect(window, LIGHT_BLUE, (0, WINDOW_HEIGHT*0.05, WINDOW_WIDTH*0.06, WINDOW_HEIGHT), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_close_x, menu_btn_y))



    if clicked:
        window.blit(highlighted_scaled_battery_img, (WINDOW_WIDTH*0.8,WINDOW_HEIGHT*0.6))



    for i in circuit:
        if circuit[i][1] != None:
            img = pygame.image.load(circuit[i][1][2])
            scaled_img = pygame.transform.scale(img, (131,131))
            window.blit(scaled_img, (circuit[i][1][0], circuit[i][1][1]))


    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(30)








