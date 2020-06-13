import dazl
import pickle
import json

network = dazl.Network()
network.set_config(url='http://localhost:6865')


boy = network.simple_party('boy')


@boy.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
def addToMap(event):
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    dict['boy'] = event.cid
    #print(dict)
    with open('datafile.txt', 'wb') as fh:
       	pickle.dump(dict, fh)
    
@boy.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
def automate_l2(event):
    print('boy')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    	
    if 'boy' != event.cdata['userPartyId']:
    	print("HERE")
    	boy.submit_exercise(dict['boy'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
@boy.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
def automate_l1(event):
    print('Created L2Moderatedanger')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    	
    if 'boy' != event.cdata['userPartyId']:
    	boy.submit_exercise(dict['boy'], 'CreateLowInfectectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    

network.run_forever()
