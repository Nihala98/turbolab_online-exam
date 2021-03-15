def SplitString(str, n): 
    str_size = len(str) 
    if str_size % n != 0: 
        print ("Invalid Input: String size is not divisible by n")
        return
    part_size = str_size/n 
    a = 0
    for i in str: 
        if a%part_size==0: 
            print ("\n")
        print(i) 
        a += 1
str = "i love python program"
SplitString(str,3) 
    