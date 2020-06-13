import dazl
import pickle
import json

network = dazl.Network()
network.set_config(url='http://localhost:6865')


guard2 = network.simple_party('guard2')


@guard2.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
def addToMap(event):
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    dict['guard2'] = event.cid
    #print(dict)
    with open('datafile.txt', 'wb') as fh:
       	pickle.dump(dict, fh)
    
@guard2.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
def automate_l2(event):
    print('guard2')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'guard2' != event.cdata['userPartyId']:
    	print("HERE")
    	guard2.submit_exercise(dict['guard2'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
@guard2.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
def automate_l1(event):
    print('Created L2Moderatedanger')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'guard2' != event.cdata['userPartyId']:
    	guard2.submit_exercise(dict['guard2'], 'CreateLowInfectectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    

network.run_forever()
