#!/usr/bin/env python3

if __name__ == '__main__':
    pass

import sys


count = len(sys.argv)
mean = sys.argv[1:]
total = 0

while count > 1:
	count -= 1
	total += float(sys.argv[count])
      
if not len(sys.argv) > 1:
      print("No arguments were passed")
      

print(f"The total is {total}")
print(f"The avarage is {total / len(mean)}")


