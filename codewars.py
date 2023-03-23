def arrange(s: list):
    lst = s
    result = []
    for x in range(len(lst)):
        if len(lst) != len(result):
            result.append(lst[x])
            lst.reverse()
            if len(lst) != len(result):
                result.append(lst[x])
    return result
   
print(arrange([4, 9, 7, -8, -4, 9, 0, -2, 8, 6, 3, 2, -8, 5, 7, -1, 9, 8, 1, 4, -8, -4, 0, 9, -2, -6, -5, 1, 2, 8, 6, -1, -9, -1, -1, 10, -6, 9, 3, -10, -9, -3, -1, 8, -2, -3, -7, 7, -7, -10, 7, -4, 6, 3, 8, 3, 3, -3, 0, 8, -10, -8, -2, 3, 1, -3, -8, -7, 7, 6, 8, 0, -4, 7, 4, 9, 9, -3, 1, -3, -8, -5, 7, 8, 7, 5, -8, 0, -7, 3, 7, -6, 3, 2, 7, 10, -2, -7]))
test1 = [1, 5, 6, -3, 5, 8, -2, 7, 9, 0]


test = [1, -1, -2, 2, 3, -3, -4, 4, 5]
