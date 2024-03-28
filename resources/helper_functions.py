def create_a_linkedlist():
    return {}

def insert_a_tuple(linked_list, ID, status, data, connection = None):
    linked_list[ID] = (status, data, connection)

def remove_node(linked_list, ID):
    for c in linked_list:
        if linked_list[c][2] == ID:
            linked_list[c] = (linked_list[c][0], linked_list[c][1], None)
    tup = linked_list[ID]
    del linked_list[ID]
    return tup

def length_of_linkedlist(linked_list):
    return len(linked_list.keys())

def print_linked_list(linked_list):
    pass # returns the head of the list. 
