def condiComp():
    arr = [1,2,3,4,5,6,7,8,9,10]
    print([i **2 if i % 2 == 0 else i for i in arr])


condiComp()