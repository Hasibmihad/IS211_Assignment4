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
    sequential_search_dict={}
    ordered_sequential_search_dict={}
    binary_search_iterative_dict={}
    binary_search_recursive_dict={}


    
    for sizeList in sizesOfList:
        totaltimeForSequential=0
        totaltimeForSeqOrdered=0
        totaltimeForBinaryIte=0
        totaltimeForBinaryRec=0
        for countlist in range (numberOfList):
            random_list = []
            for i in range(0, sizeList):
                random_list.append(random.randint(0, 1000000))
            found,time_taken=sequential_search(random_list,-1)
            totaltimeForSequential+=time_taken

            random_list.sort()

            found,time_taken=ordered_sequential_search(random_list,-1)
            totaltimeForSeqOrdered+=time_taken

            found,time_taken=binary_search_iterative(random_list,-1)
            totaltimeForBinaryIte+=time_taken

            found,time_taken=binary_search_recursive(random_list,-1)
            totaltimeForBinaryRec+=time_taken


        averageTime=totaltimeForSequential/sizeList
        sequential_search_dict[sizeList]=averageTime

        averageTime=totaltimeForSeqOrdered/sizeList
        ordered_sequential_search_dict[sizeList]=averageTime

        averageTime=totaltimeForBinaryIte/sizeList
        binary_search_iterative_dict[sizeList]=averageTime

        averageTime=totaltimeForBinaryRec/sizeList
        binary_search_recursive_dict[sizeList]=averageTime


        print

    print(f"Sequential Search took {sequential_search_dict[500]:10.7f} seconds to run, on average for size 500")

    print(f"Sequential Search took {sequential_search_dict[1000]:10.7f} seconds to run, on average for size 1000")

    print(f"Sequential Search took {sequential_search_dict[10000]:10.7f} seconds to run, on average for size 10000")


    print("Ordered Sequential Search:")
    print(ordered_sequential_search_dict)

    print("Binary Search Iterative:")
    print(binary_search_iterative_dict)

    print("Binary Search Recursive:")
    print(binary_search_recursive_dict)


if __name__=="__main__":
    main()