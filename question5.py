def inter(l1, l2):
    lst3 =list (i for i in l1 if i in l2)
    return lst3
lst1 = [4, 9, 3, 17, 11, 26, 12, 54, 69]
lst2 = [9, 9, 2, 45, 12, 63, 28, 26]
print(inter(lst1, lst2))
