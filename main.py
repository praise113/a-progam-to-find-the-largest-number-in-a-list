# Largest number in a list

def largestNumber(list):
    list.sort()
    print("Largest number is ", list[-1])

list = [1, 2, 3, 4]
largestNumber(list)