import dazl
import pickle
import json

network = dazl.Network()
network.set_config(url='http://localhost:6865')


towerGuard = network.simple_party('towerGuard')


@towerGuard.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
def addToMap(event):
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    dict['towerGuard'] = event.cid
    #print(dict)
    with open('datafile.txt', 'wb') as fh:
       	pickle.dump(dict, fh)
    
@towerGuard.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
def automate_l2(event):
    print('towerGuard')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'towerGuard' != event.cdata['userPartyId']:
    	print("HERE")
    	towerGuard.submit_exercise(dict['towerGuard'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
@towerGuard.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
def automate_l1(event):
    print('Created L2Moderatedanger')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'towerGuard' != event.cdata['userPartyId']:
    	towerGuard.submit_exercise(dict['towerGuard'], 'CreateLowInfectectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    


network.run_forever()
