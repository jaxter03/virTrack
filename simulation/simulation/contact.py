import dazl
import pickle
import time

while (True):
	first,second = input("************** :- ").split()
	with dazl.simple_client('http://localhost:6865', first) as client:
		client.ready()
		pickle_off = open ("datafile.txt", "rb")
		dict = pickle.load(pickle_off)
		client.submit_exercise(dict[first], 'UpdateContactList', {'contactedPartyId' : second})

	time.sleep(4)

	with dazl.simple_client('http://localhost:6865', second) as client:
		client.ready()
		pickle_off = open ("datafile.txt", "rb")
		dict = pickle.load(pickle_off)
		client.submit_exercise(dict[second], 'UpdateContactList', {'contactedPartyId' : first})
