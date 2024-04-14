# given a list of numbers in descreasing oder return the index of target number while ascessing minimum number of indexs

# sol1: ascess all possible indexes until u find the target or u reach the end of the list

def locate_num(my_list, target):
    for x in range(len(my_list)):
        if target == my_list[x]:
            return x
    return None

# sol2: pick one middle ele and chop down half of the array based on if the current number is greater or smaller or same as target
def locate_num1(my_list, target):
    if my_list:
        list_start = 0
        list_end = len(my_list) - 1
        while list_start<=list_end:
            mid = (list_start + list_end)//2
            mid_ele = my_list[mid]
            if mid_ele == target:
                return mid
            elif mid_ele>target:
                list_start = mid + 1
            elif mid_ele<target:
                list_end = mid - 1   
    return None

mylist = [9, 7, 5, 4, 2, 1]
target_ele = 7

print(locate_num1(mylist, target_ele))