def create_a_linkedlist(): # Creates the linked list:
    return {}

def insert_a_tuple(linked_list, ID, status, data, connection = None): # Inserts data for a particular component with key ID:
    linked_list[ID] = (status, data, connection)

def remove_node(linked_list, ID): # Removes data of a particular component with key ID:
    for c in linked_list:
        if linked_list[c][2] == ID:
            linked_list[c] = (linked_list[c][0], linked_list[c][1], None)
    tup = linked_list[ID]
    del linked_list[ID]
    return tup

def get_a_node(linked_list, ID): # Returns data of a particular component with key ID:
    return linked_list[ID]

def length_of_linkedlist(linked_list): # Returns the number of components in the system:
    return len(linked_list.keys())

def source_linked_list(linked_list): # Returns the source supply component:
    return linked_list["Head"]

def form_connection(linked_list, ID1, ID2): # Connects two components:
    linked_list[ID1] = (linked_list[ID1][0], linked_list[ID1][1], ID2)

def remove_connection(linked_list, ID1): # Removes connections:
    if linked_list[ID1][2] == None:
        print("No connection found")
    else:
        if ID1 == source_linked_list(linked_list): # When the source is being removed
            current_ID = ID1
            while linked_list[current_ID][2] != None:
                next_ID = linked_list[current_ID][2]
                linked_list[current_ID][2] = None
                current_ID = next_ID
        else:
            # Logic yet to be made.
            pass   
                
