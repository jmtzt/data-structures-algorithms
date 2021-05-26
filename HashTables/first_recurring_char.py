# Google Question
# Given an array, return the first recurring character
# Example1 : array = [2,1,4,2,6,5,1,4]
# It should return 2
# Example 2 : array = [2,6,4,6,1,3,8,1,2]
# It should return 6

def frc(arr):
    dictionary = dict()
    for item in arr:
        if item not in dictionary:
            dictionary[item] = True
        elif item in dictionary:
            return item
    return None


print(frc([2,1,1,2,3,5,1,2,4]))
print(frc([2,1,2,4,1,5,2,6]))
