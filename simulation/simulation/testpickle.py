import pickle

mylist = {}
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)



pickle_off = open ("datafile.txt", "rb")
emp = pickle.load(pickle_off)
print(emp)
