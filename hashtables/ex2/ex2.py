#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    dest = "NONE"
    
    """
    YOUR CODE HERE
    """
    
    for ticket in tickets:
        s=ticket.source
        d=ticket.destination
        hash_table_insert(hashtable,s, d)

    for idx in range(len(route)):
        dest = hash_table_retrieve(hashtable, dest)
        route[idx] = dest


        
        

        #route[int(idx)] = hashtable[int(idx)-1]

    return route
