import dazl
import pickle
import json

network = dazl.Network()
network.set_config(url='http://localhost:6865')


gateGuard = network.simple_party('gateGuard')


@gateGuard.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
def addToMap(event):
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    dict['gateGuard'] = event.cid
    #print(dict)
    with open('datafile.txt', 'wb') as fh:
       	pickle.dump(dict, fh)
    
@gateGuard.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
def automate_l2(event):
    print('gateGuard')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'gateGuard' != event.cdata['userPartyId']:
    	print("HERE")
    	gateGuard.submit_exercise(dict['gateGuard'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
@gateGuard.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
def automate_l1(event):
    print('Created L2Moderatedanger')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'gateGuard' != event.cdata['userPartyId']:
    	gateGuard.submit_exercise(dict['gateGuard'], 'CreateLowInfectectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    

network.run_forever()
