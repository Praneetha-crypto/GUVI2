def countTotalBits(N): 
      
     # convert number into it's binary and  
     # remove first two characters 0b. 
     binary = bin(N)[2:] 
     print(len(binary))  
  
# Driver program 
#if __name__ == "__main__": 
N =int(input("enter the num"))
countTotalBits(N)
