def intersection(lst1,lst2):
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3

lst1 = [0,1,2,3,4,5]
lst2 = [0,3,5,7]
print(intersection(lst1,lst2))
