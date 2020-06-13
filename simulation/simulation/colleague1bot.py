import dazl
import pickle
import json

network = dazl.Network()
network.set_config(url='http://localhost:6865')

colleague1 = network.simple_party('colleague1')


@colleague1.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
def addToMap(event):
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    dict['colleague1'] = event.cid
    #print(dict)

    with open('datafile.txt', 'wb') as fh:
       	pickle.dump(dict, fh)
    
@colleague1.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
def automate_l2(event):
    print('colleague1')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    if 'colleague1' != event.cdata['userPartyId']:
    	print("HERE")
    	colleague1.submit_exercise(dict['colleague1'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
@colleague1.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
def automate_l1(event):
    print('Created L2Moderatedanger')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'colleague1' != event.cdata['userPartyId']:
    	colleague1.submit_exercise(dict['colleague1'], 'CreateLowInfectectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    

network.run_forever()
