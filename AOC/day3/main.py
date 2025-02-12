'''
Code for day 3 of AOC
'''
import re
'''General input.txt opener function'''
def get_data() -> str:
    with open("./input.txt", "r") as file:
        # Read and process all lines, splitting into two sorted arrays
        data = "" # initializing empty string variable
        for line in file:
            data = data+str(line) # concatenating each .txt file line as string
    if not data:
        raise ValueError("Failed: Input data is empty or invalid") # Error output 
    return data

mstring = get_data() #Calling get_data() to variable in main

''' Function to eliminate "Don't()" parts of the string'''
def sep_enabled(text) -> str:
    do = "do()"
    dont = "don't()"
    ans = ""
    stat = 1
    while len(text)>0:
        if stat == 1:
            try:
                tval, separator, text = text.partition(dont)
                stat = 0
                ans += tval
            except:
                text = ""
        else:
            try:
                tval, separator, text = text.partition(do)
                stat = 1
            except:
                text = ""
    return ans

'''Part 1 of day 3'''
pattern = r'mul\((\d+),(\d+)\)' # defining Reg Expression formula to catch mul(*,*) form
matches = re.findall(pattern, mstring) # getting matches from RegEx (RE) function
sval = 0 #cum sum variable initiated at 0
for nums in matches: # iterating over all matches
    sval += int(nums[0])*int(nums[1]) #multiplying then adding to cum sum varaible
print(sval) #printing result

'''Part 2 of day 3'''
sep_text = sep_enabled(mstring) #calling function to eliminate don'ts 
sval = 0
matches = re.findall(pattern, sep_text)# finding matches again
sval = 0 #'''
for nums in matches: #'''
    sval += int(nums[0])*int(nums[1]) #'''
print(sval) #'''



