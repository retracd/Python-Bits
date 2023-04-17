from math import sqrt

numrange = input("What number(s) would you like square roots of (ie 8 for 8, or 5 8 for 5 thru 8):")
nums = numrange.split(' ', 1)
for i in list(range(int(nums[0]), int(nums[1]) + 1)):
        print(f"The square root of {i} is {round(sqrt(i), 3)}")

"""
try: 
    for i in list(range(int(nums[0]), int(nums[1]) + 1)):
        print(f"The square root of {i} is {round(sqrt(i), 3)}")
except:
    if (int(nums[1]) <= int(nums[0])):
        print("ERROR: Range is negative!")
        exit()
    if(len(nums) == 1):
        if(not nums[0].isnumeric()):
            print("ERROR: Invalid Digits")
            exit()
    else:
        if(not nums[0].isnumeric() or not nums[1].isnumeric()):
            print("ERROR: Invalid Digits")
            exit()
"""