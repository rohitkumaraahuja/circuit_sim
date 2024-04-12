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
        

def near_division_multiple(division, number):
    a = number
    if a%division >= division//2:
        while a%division != 0:
            a+=1
        return a
    else:
        while a%division != 0:
            a-=1
        return a
























# Initialize Pygame
pygame.init()

# Set up the window

window = pygame.display.set_mode()
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





circuit = {
    'PS1': ('NS1', (700, 700, 'resources/images/on_0_ps_img.png'), None)
}


#Function Constant
component_selected = False
component = ''
init_mouse_pos = (0,0)
line_ending_point = (0,0)
division = 70
create_line = False
WIRE_COLOR = (0,0,0)
GRID_COLOR = (180,180,180)




bulb_image = pygame.image.load('resources/images/off_180_b_img.png')
scaled_bulb_image = pygame.transform.scale(bulb_image, (140, 140))

# Initiating the Battery
# form_connection(circuit, "PS1", pre_ID1=None, data=(WINDOW_WIDTH*0.8,WINDOW_HEIGHT*0.6, 'resources/images/battery.png'), next_ID2=None)
# form_connection(circuit, "NS1", pre_ID1=None, data=None, next_ID2=None)


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
# scaled_battery_size =  (1920*WINDOW_WIDTH//20000, 2831*WINDOW_WIDTH//20000)
scaled_battery_size = (131.136, 193.3573)
# scaled_tool_size = (1920*WINDOW_WIDTH//20000, 1920*WINDOW_WIDTH//20000)
scaled_tool_size = (131.136, 131.136)

y_highlighted = 385*WINDOW_WIDTH//TOOLS_BUTTON_SIZE

menu_scaled_tool_size = (480*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 480*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)

point_scaled_tool_size = (100*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 100*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)









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



    # Draw Grid
    temp325 = 1
    while division*temp325 <= WINDOW_WIDTH:
        pygame.draw.line(window, GRID_COLOR, 
                [division*temp325, 0], 
                [division*temp325, WINDOW_HEIGHT], 5)
        pygame.draw.line(window, GRID_COLOR, 
                [0, division*temp325], 
                [WINDOW_WIDTH, division*temp325], 5)
        temp325 += 1
   







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











# Draw Wire
    if menu_open:
        if is_clicked(((WINDOW_WIDTH*0.2, 0), (WINDOW_WIDTH, WINDOW_HEIGHT)), mouse_pos, mouse) and component_selected == False:
            if create_line:
                id = random.randint(2,10000)
                while "L" + str(id) in circuit:
                    id = random.randint(2, 10000)
                id = 'L'+str(id)
                

                # For Tail
                start = None
                for i in circuit:
                    if i[0] == 'B':
                        if circuit[i][1][2][21] == '1' or circuit[i][1][2][20] == '1':
                            if circuit[i][1][0]+140 == init_mouse_pos[0] and circuit[i][1][1]+70 == init_mouse_pos[1]:
                                circuit[i] = (circuit[i][0], circuit[i][1], id)
                                start = i
                                break
                    if i[0] == 'P':
                        if circuit[i][1][2][20] == '0':
                            print()
                            if circuit[i][1][0]+140 == init_mouse_pos[0] and circuit[i][1][1]+70 == init_mouse_pos[1]:
                                circuit[i] = (circuit[i][0], circuit[i][1], id)
                                start = i
                                break
                    if i[0] == 'L':
                        if circuit[i][1][2] == init_mouse_pos[0] and circuit[i][1][3] == init_mouse_pos[1]:
                            circuit[i] = (circuit[i][0], circuit[i][1], id)
                            start = i
                            break
                

                # For Head
                end = None
                for i in circuit:
                    if i[0] == 'B':
                        if circuit[i][1][2][21] == '1' or circuit[i][1][2][20] == '1':
                            if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1]+70 == line_ending_point[1]:
                                circuit[i] = (id, circuit[i][1], circuit[i][2])
                                end = i
                                break
                    if i[0] == 'P':
                        if circuit[i][1][2][20] == '0':
                            if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1]+70 == line_ending_point[1]:
                                circuit[i] = (id, circuit[i][1], circuit[i][2])
                                end = i
                                break
                    if i[0] == 'L':
                        if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][2] == line_ending_point[1]:
                            circuit[i] = (id, circuit[i][1], circuit[i][2])
                            end = i
                            break
                
                circuit[id] = (start, (init_mouse_pos[0], init_mouse_pos[1], line_ending_point[0], line_ending_point[1]), end)


            create_line = not create_line
            init_mouse_pos = (near_division_multiple(division, mouse_pos[0]), near_division_multiple(division, mouse_pos[1]))
            time.sleep(0.2)
    else:
        if is_clicked(((WINDOW_WIDTH*0.06, 0), (WINDOW_WIDTH, WINDOW_HEIGHT)), mouse_pos, mouse) and component_selected == False:
            if create_line:
                id = random.randint(2,10000)
                while "L" + str(id) in circuit:
                    id = random.randint(2, 10000)
                id = 'L'+str(id)
                

                # For Tail
                start = None
                for i in circuit:
                    if i[0] == 'B':
                        if circuit[i][1][2][21] == '1' or circuit[i][1][2][20] == '1':
                            if circuit[i][1][0]+140 == init_mouse_pos[0] and circuit[i][1][1]+70 == init_mouse_pos[1]:
                                circuit[i] = (circuit[i][0], circuit[i][1], id)
                                start = i
                                break
                    if i[0] == 'P':
                        if circuit[i][1][2][20] == '0':
                            if circuit[i][1][0]+140 == init_mouse_pos[0] and circuit[i][1][1]+70 == init_mouse_pos[1]:
                                circuit[i] = (circuit[i][0], circuit[i][1], id)
                                start = i
                                break
                    if i[0] == 'L':
                        if circuit[i][1][2] == init_mouse_pos[0] and circuit[i][1][3] == init_mouse_pos[1]:
                            circuit[i] = (circuit[i][0], circuit[i][1], id)
                            start = i
                            break
                

                # For Head
                end = None
                for i in circuit:
                    if i[0] == 'B':
                        if circuit[i][1][2][21] == '1' or circuit[i][1][2][20] == '1':
                            if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1]+70 == line_ending_point[1]:
                                circuit[i] = (id, circuit[i][1], circuit[i][2])
                                end = i
                                break
                    if i[0] == 'P':
                        if circuit[i][1][2][20] == '0':
                            if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1]+70 == line_ending_point[1]:
                                circuit[i] = (id, circuit[i][1], circuit[i][2])
                                end = i
                                break
                    if i[0] == 'L':
                        if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][2] == line_ending_point[1]:
                            circuit[i] = (id, circuit[i][1], circuit[i][2])
                            end = i
                            break
                
                circuit[id] = (start, (init_mouse_pos[0], init_mouse_pos[1], line_ending_point[0], line_ending_point[1]), end)

            create_line = not create_line
            init_mouse_pos = (near_division_multiple(division, mouse_pos[0]), near_division_multiple(division, mouse_pos[1]))
            time.sleep(0.2)


    if create_line:
        line_ending_point = (near_division_multiple(division, mouse_pos[0]), near_division_multiple(division, mouse_pos[1]))
        if abs(line_ending_point[0] - init_mouse_pos[0]) < abs(line_ending_point[1] - init_mouse_pos[1]):
            line_ending_point = (init_mouse_pos[0], line_ending_point[1])
        else:
            line_ending_point = (line_ending_point[0], init_mouse_pos[1])
        
        pygame.draw.line(window, WIRE_COLOR, 
                [init_mouse_pos[0], init_mouse_pos[1]], 
                [line_ending_point[0], line_ending_point[1]], 5)













    

    # Draw the side element tab
    if menu_open:
        pygame.draw.rect(window, LIGHT_BLUE, (0, WINDOW_HEIGHT*0.05,WINDOW_WIDTH*0.2, WINDOW_HEIGHT), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_x, menu_btn_y))

        # Draw Tools on Tab

        
        window.blit(menu_scaled_bulbOn_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1))
        
        # Menu Bulb
        if is_hovering(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1),(WINDOW_WIDTH*0.05+menu_scaled_tool_size[0], (((WINDOW_HEIGHT-70)/(tools+1))*1) + menu_scaled_tool_size[1])), mouse_pos):
            window.blit(scaled_highlight_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1))
        if is_clicked(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1),(WINDOW_WIDTH*0.05+menu_scaled_tool_size[0], (((WINDOW_HEIGHT-70)/(tools+1))*1) + menu_scaled_tool_size[1])), mouse_pos,mouse):
            component_selected = True
            component = 'bulb'
            mouse = (False, mouse[1], mouse[2])
            time.sleep(0.1)


        window.blit(menu_scaled_fanOn_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*2))
        # if is_hovering(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*2),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*2) + scaled_tool_size[1])), mouse_pos):
        #     window.blit(scaled_highlight_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*2))
        # if is_clicked(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*2),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*2) + scaled_tool_size[1])), mouse_pos,mouse):
        #     component_selected = True

    else:
        pygame.draw.rect(window, LIGHT_BLUE, (0, WINDOW_HEIGHT*0.05, WINDOW_WIDTH*0.06, WINDOW_HEIGHT), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_close_x, menu_btn_y))





   
        
        

        



    # Draw Component
    if component_selected:
        create_line = False
        if component == 'bulb':
            window.blit(scaled_bulb_image, (near_division_multiple(division, mouse_pos[0]-70), near_division_multiple(division, mouse_pos[1]-70)))
        

   
        if mouse[0] == True:
            component_selected = False

            if component == 'bulb':
                id = random.randint(2,10000)
                while "B" + str(id) in circuit:
                    id = random.randint(2, 10000)
                id = 'B'+str(id)
                position = (near_division_multiple(division, mouse_pos[0]-70), near_division_multiple(division, mouse_pos[1]-70))

                start = None
                for i in circuit:
                    if i[0] == 'B':
                        if circuit[i][1][2][21] == '1' or circuit[i][1][2][20] == '1':
                            if circuit[i][1][0]+140 == position[0] and circuit[i][1][1] == position[1]:
                                circuit[i] = (circuit[i][0], circuit[i][1], id)
                                start = i
                                break
                    if i[0] == 'P':
                        if circuit[i][1][2][21] == '0' or circuit[i][1][2][20] == '0':
                            if circuit[i][1][0]+140 == position[0] and circuit[i][1][1] == position[1]:
                                circuit[i] = (circuit[i][0], circuit[i][1], id)
                                start = i
                                break
                    if i[0] == 'L':
                        if circuit[i][1][2] == position[0] and circuit[i][1][3] == position[1]+70:
                            circuit[i] = (circuit[i][0], circuit[i][1], id)
                            start = i
                            break

                end = None
                for i in circuit:
                    if i[0] == 'B':
                        if circuit[i][1][2][21] == '1' or circuit[i][1][2][20] == '1':
                            if circuit[i][1][0] == position[0]+140 and circuit[i][1][1] == position[1]:
                                circuit[i] = (id, circuit[i][1], circuit[i][2])
                                end = i
                                break
                    if i[0] == 'P':
                        if circuit[i][1][2][21] == '0' or circuit[i][1][2][20] == '0':
                            if circuit[i][1][0] == position[0]+140 and circuit[i][1][1] == position[1]:
                                circuit[i] = (id, circuit[i][1], circuit[i][2])
                                end = i
                                break
                    if i[0] == 'L':
                        if circuit[i][1][0] == position[0]+140 and circuit[i][1][1] == position[1]+70:
                            circuit[i] = (id, circuit[i][1], circuit[i][2])
                            end = i
                            break
                            

                circuit[id] = (start, (position[0], position[1], 'resources/images/off_180_b_img.png'), end)

            component = '' 
            time.sleep(0.2)
    

  



    for i in circuit:
        if i[0] == 'L':

            pygame.draw.line(window, WIRE_COLOR, 
                [circuit[i][1][0], circuit[i][1][1]], 
                [circuit[i][1][2], circuit[i][1][3]], 5)

        elif circuit[i][1] != None:

            img = pygame.image.load(circuit[i][1][2])
            scaled_img = pygame.transform.scale(img, (140,140))
            window.blit(scaled_img, (circuit[i][1][0], circuit[i][1][1]))


    

    print(circuit)


    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(30)








