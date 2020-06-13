import dazl
import pickle
import json

# Hello World program in Python
while (True):
    network = dazl.Network()
    network.set_config(url='http://localhost:6865')
    pickle_off = open ("datafile.txt", "rb")
    dict = pickle.load(pickle_off)
    alice = network.simple_party('alice')
    bob = network.simple_party('bob')
    boy = network.simple_party('boy')
    towerGuard = network.simple_party('towerGuard')
    gateGuard = network.simple_party('gateGuard')
    colleague1 = network.simple_party('colleague1')
    colleague2 = network.simple_party('colleague2')
    securityHead = network.simple_party('securityHead')
    guard1 = network.simple_party('guard1')
    guard2 = network.simple_party('guard2')
    resident1 = network.simple_party('resident1')
    resident2 = network.simple_party('resident2')
    
    
    ####################################################ALICE################################################################################################
    @alice.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToDict(event):
    	dict['alice'] = event.cid
    	print(event)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @alice.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l1(event):
    	print('ksr1')
    	
    	if 'alice' != event.cdata['userPartyId']:
    		alice.submit_exercise(dict['alice'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @alice.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'alice' != event.cdata['userPartyId']:
    		alice.submit_exercise(dict['alice'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    #####################################################BOB##################################################################################################333
    	
    @bob.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['bob'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @bob.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('ksr2')
    	
    	if 'bob' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['bob'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @bob.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'bob' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['bob'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    #####################################################boy##################################################################################################333
    	
    @boy.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['boy'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @boy.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('boy')
    	
    	if 'boy' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['boy'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @boy.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'boy' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['boy'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    #####################################################towerGuard##################################################################################################333
    	
    @towerGuard.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['towerGuard'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @towerGuard.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('towerGuard')
    	
    	if 'towerGuard' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['towerGuard'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @towerGuard.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'towerGuard' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['towerGuard'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    
    #####################################################gateGuard##################################################################################################333
    	
    @gateGuard.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['gateGuard'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @gateGuard.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('gateGuard')
    	
    	if 'gateGuard' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['gateGuard'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @gateGuard.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'gateGuard' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['gateGuard'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    #####################################################colleague1##################################################################################################333
    	
    @colleague1.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['colleague1'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @colleague1.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('colleague1')
    	
    	if 'colleague1' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['colleague1'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @colleague1.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    
    	if 'colleague1' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['colleague1'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    #####################################################colleague2##################################################################################################333
    	
    @colleague2.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['colleague2'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @colleague2.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('colleague2')
    	
    	if 'colleague2' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['colleague2'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @colleague2.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'colleague2' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['colleague2'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    #####################################################securityHead##################################################################################################333
    	
    @securityHead.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['securityHead'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @securityHead.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('securityHead')
    	
    	if 'securityHead' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['securityHead'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @securityHead.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'securityHead' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['securityHead'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    #####################################################guard1##################################################################################################333
    	
    @guard1.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['guard1'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @guard1.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('guard1')
    	
    	if 'guard1' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['guard1'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @guard1.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'guard1' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['guard1'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    #####################################################guard2##################################################################################################333
    	
    @guard2.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['guard2'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @guard2.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('guard2')
    	
    	if 'guard2' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['guard2'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @guard2.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'guard2' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['guard2'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    #####################################################resident1##################################################################################################333
    	
    @resident1.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['resident1'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @resident1.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('resident1')
    	
    	if 'resident1' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['resident1'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @resident1.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'resident1' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['resident1'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    #####################################################resident2##################################################################################################333
    	
    @resident2.ledger_created('ContactRelatedContracts.ContactConfirmationContract')
    def addToMap(event):
    	dict['resident2'] = event.cid
    	#print(dict)
    	with open('datafile.txt', 'wb') as fh:
       		pickle.dump(dict, fh)
    
    @resident2.ledger_created('ContactRelatedContracts.L1HighInfectionDangerContract')
    def automate_l2(event):
    	print('resident2')
    	
    	if 'resident2' != event.cdata['userPartyId']:
    		print("HERE")
    		bob.submit_exercise(dict['resident2'], 'CreateModerateInfectionDanger', {'hospital' : 'hospital' , 'govAuthority' : 'authority' , 'infectedParty' : event.cdata['userPartyId']})
    
    @resident2.ledger_created('ContactRelatedContracts.L2ModerateInfectionDangerContract')
    def automate_l1(event):
    	print('Created L2Moderatedanger')
    	
    	if 'resident2' != event.cdata['userPartyId']:
    		bob.submit_exercise(dict['resident2'], 'CreateLowInfectectionDanger', {'infectedParty' : event.cdata['userPartyId']})
    
    
    
    network.run_forever()
