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
        list_end = len(my_list)
        while True:
            temp_list = my_list[list_start:list_end]
            mid_ele = temp_list[len(temp_list)//2]
            if mid_ele == target:
                return len(temp_list)//2
            elif mid_ele>target:
                list_start = len(temp_list)//2
            elif mid_ele<target:
                list_end = len(temp_list)//2
            return
    return None

mylist = [9, 7, 5, 4, 2, 1]
target_ele = 2

print(locate_num1(mylist, target_ele))