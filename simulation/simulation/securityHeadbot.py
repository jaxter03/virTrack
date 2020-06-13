import dazl
import pickle
import json

network = dazl.Network()
network.set_config(url='http://localhost:6865')


securityHead = network.simple_party('securityHead')


@securityHead.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
def addToMap(event):
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    dict['securityHead'] = event.cid
    #print(dict)
    with open('datafile.txt', 'wb') as fh:
       	pickle.dump(dict, fh)
    
@securityHead.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
def automate_l2(event):
    print('securityHead')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'securityHead' != event.cdata['userPartyId']:
    	print("HERE")
    	securityHead.submit_exercise(dict['securityHead'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
@securityHead.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
def automate_l1(event):
    print('Created L2Moderatedanger')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)	
    if 'securityHead' != event.cdata['userPartyId']:
    	securityHead.submit_exercise(dict['securityHead'], 'CreateLowInfectectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    

network.run_forever()
