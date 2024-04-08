def create_a_linkedlist(): # Creates the linked list:
    return {}

def form_connection(linked_list, ID, pre_ID1, next_ID2): # Connects two components:
    linked_list[ID] = (pre_ID1, False, next_ID2)

def remove_connection(linked_list, ID): # Removes connections of the whole circuit:
    current_ID = ID
    while linked_list[current_ID][2] != None:
        next_ID = linked_list[current_ID][2]
        if type(next_ID) == tuple:
            remove_connection(linked_list, next_ID[0])
            remove_connection(linked_list, next_ID[1])
        if type(next_ID) != tuple:
            linked_list[current_ID][1] = False
            current_ID = next_ID

def get_a_node(linked_list, ID): # Returns data of a particular component with key ID:
    return linked_list[ID]

def length_of_linkedlist(linked_list): # Returns the number of components in the system:
    return len(linked_list.keys())

def source_linked_list(linked_list): # Returns the source supply component:
    return linked_list["Head"]
    
def place_a_transmitter(linked_list, pre_ID, T_ID, next_IDs):
    linked_list[T_ID] = (pre_ID, False, next_IDs)

def place_a_receiver(linked_list, pre_IDs, R_ID, next_ID):
    linked_list[R_ID] = (pre_IDs, False, next_ID)

def remove_a_transmitter(linked_list, T_ID):
    remove_connection(linked_list, T_ID)

def remove_a_receiver(linked_list,R_ID):
    next_ID = linked_list[R_ID[0]][2]
    if type(next_ID) == tuple:
        remove_connection(linked_list, next_ID[0])
        remove_connection(linked_list, next_ID[1])
    linked_list[R_ID[0]][1] = False
    linked_list[R_ID[1]][1] = False

def display_the_linked_list(linked_list):
    current_ID = linked_list["Head"]
    lst = [["Head"]]
    while current_ID[2] != None:
        current_ID = linked_list[current_ID[2]]
        lst.append(current_ID)
    return lst
        
