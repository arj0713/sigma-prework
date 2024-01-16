def maxmin(int_list):
    max = int_list[0]
    min = int_list[0]
    for i in int_list:
        if i > max:
            max = i
        if i < min:
            min = i
    return [min,max]


test1 = [2,4,1,0,2,-1]
test2 = [20,50,12,6,14,8]
test3 = [100,-100]

print(maxmin(test1))
print(maxmin(test2))
print(maxmin(test3))