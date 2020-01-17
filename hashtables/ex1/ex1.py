#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)
    prev = None
    #insert into hash table
    for idx in range(len(weights)):
        hash_table_insert(ht, weights[idx], idx)
        #prev= 10
        w1_idx = idx
        w1 = weights[idx]
        remainder = limit - w1

        if hash_table_retrieve(ht, remainder):
            if hash_table_retrieve(ht, remainder) == 1 and w1 == 4:
                w2_idx = hash_table_retrieve(ht,remainder)
                answer = [w2_idx, 0]
                return tuple(answer)
            else:
                w2_idx = hash_table_retrieve(ht, remainder)
                w2 = weights[w2_idx]
                answer =[w1_idx,w2_idx]
                return tuple(answer)
            
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
