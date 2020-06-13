import dazl
import pickle
import json

network = dazl.Network()
network.set_config(url='http://localhost:6865')

guard1 = network.simple_party('guard1')


@guard1.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
def addToMap(event):
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    dict['guard1'] = event.cid
    #print(dict)
    with open('datafile.txt', 'wb') as fh:
       	pickle.dump(dict, fh)
    
@guard1.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
def automate_l2(event):
    print('guard1')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'guard1' != event.cdata['userPartyId']:
    	print("HERE")
    	guard1.submit_exercise(dict['guard1'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
@guard1.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
def automate_l1(event):
    print('Created L2Moderatedanger')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'guard1' != event.cdata['userPartyId']:
    	guard1.submit_exercise(dict['guard1'], 'CreateLowInfectectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    

network.run_forever()
