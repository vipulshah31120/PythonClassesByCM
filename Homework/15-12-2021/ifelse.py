import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    
if n%2!=0 :
    print("Wierd")
        
elif n%2==0 and n in range(2,6) :
    print("Not Wierd")
        
elif n%2==0 and n in range (6,21) :
    print("Wierd")
    
elif n%2==0 and n>20 :
    print("Not Wierd")