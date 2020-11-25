import _pickle
mylist = [1,2,3,4]

ser = _pickle.dumps(mylist)
print(ser)