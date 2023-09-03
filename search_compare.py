import time 
import random



def sequential_search(a_list,item):
    start= time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
         found = True
        else:
            pos = pos+1
    end=time.time()        
    return found,end-start
 


def ordered_sequential_search(alist,item):
    
    pos = 0
    found = False
    stop = False
    start= time.time()
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    end=time.time()        
    return found,end-start
    


def binary_search_iterative(a_list, item):
    
    first = 0
    last = len(a_list) - 1
    found = False
    start=time.time()
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end=time.time()        
    return found,end-start
   



def binary_search_recursive(a_list, item):
    start = time.time()
    result = binary_search_recursive_operation(a_list, item)
    end = time.time()
    timeTaken = end - start
    return result, timeTaken

def binary_search_recursive_operation(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive_operation(a_list[:midpoint], item)
        else:
            return binary_search_recursive_operation(a_list[midpoint + 1:], item)








def main():


    numberOfList = 100
    sizesOfList = [500, 1000, 10000]
    random_list = []

    for i in range(0, 500):
        random_list.append(random.randint(0, 1000000))
        #print(random_list)
    
    found,time_taken=sequential_search(random_list,-1)

    #print (found,time_taken)

if __name__=="__main__":
    main()