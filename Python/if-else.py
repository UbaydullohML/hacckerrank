#!/bin/python3

import math
import os
import random
import re
import sys
    
if __name__ == '__main__':      # This block ensures the code below only runs when the script is executed directly,
    # not when imported as a module.
  
    n = int(input().strip())      # Get user input, convert it to an integer, and remove any leading/trailing spaces.

    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0 and 2 <= n >= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Weird')
    elif n > 20:
        print("Not Weird")


# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
