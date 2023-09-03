import time 
import random

def insertion_sort(alist):
   start= time.time()
   
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
   end=time.time()  
   return alist,end-start
   


def shell_sort(alist):
    start= time.time()
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      #print("After increments of size",sublistcount,"The list is",alist)

      sublistcount = sublistcount // 2
    end=time.time()        
    return alist,end-start
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue




def python_sort(alist):
   start= time.time()
   alist.sort()
   end=time.time()        
   return alist,end-start
           

def main():
    sizesOfList = [500, 1000, 10000]

    for size in sizesOfList:
        random_list=[]
        for i in range(0, size):
            random_list.append(random.randint(0, 1000000))
        print ("\n")
        print (f"..........................FOR SIZE {size}...............................")
        print ("\n")
        sorted_list, insertion_sort_time = insertion_sort(random_list)
        print(f"Insertion Sort took {insertion_sort_time:10.7f} seconds to run, on average for size {size}")
        print ("\n")
        sorted_list, shell_sort_time = shell_sort(random_list)
        print(f"Shell Sort took {shell_sort_time:10.7f} seconds to run, on average for size {size}")
        print ("\n")
        sorted_list, python_sort_time = python_sort(random_list)
        print(f"Python Sort took {python_sort_time:10.7f} seconds to run, on average for size {size}")  
        


if __name__=="__main__":
    main()