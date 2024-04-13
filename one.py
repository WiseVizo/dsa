# given a list of numbers in descreasing oder return the index of target number while ascessing minimum number of indexs

# sol1: ascess all possible indexes until u find the target or u reach the end of the list

def locate_num(my_list, target):
    for x in range(len(my_list)):
        if target == my_list[x]:
            return x
    return None
mylist = [9, 7, 5, 4, 2, 1]
target_ele = 6

print(locate_num(mylist, target_ele))