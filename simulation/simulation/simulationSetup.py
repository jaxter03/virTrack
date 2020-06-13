import dazl
import pickle
import time




with dazl.simple_client('http://localhost:6865', 'boy') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'boy' , 'personalDetails' : {'name' : 'Alice' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})



with dazl.simple_client('http://localhost:6865', 'towerGuard') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'towerGuard' , 'personalDetails' : {'name' : 'Himesh' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})



with dazl.simple_client('http://localhost:6865', 'gateGuard') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'gateGuard' , 'personalDetails' : {'name' : 'Feroz' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})



with dazl.simple_client('http://localhost:6865', 'colleague1') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'colleague1' , 'personalDetails' : {'name' : 'Upanshu' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})



with dazl.simple_client('http://localhost:6865', 'colleague2') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'colleague2' , 'personalDetails' : {'name' : 'Nishchal' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})



with dazl.simple_client('http://localhost:6865', 'securityHead') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'securityHead' , 'personalDetails' : {'name' : 'Srinivasan' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})



with dazl.simple_client('http://localhost:6865', 'guard1') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'guard1' , 'personalDetails' : {'name' : 'Somnath' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})



with dazl.simple_client('http://localhost:6865', 'guard2') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'guard2' , 'personalDetails' : {'name' : 'Bhola' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})



with dazl.simple_client('http://localhost:6865', 'resident1') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'resident1' , 'personalDetails' : {'name' : 'Gajendra' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})



with dazl.simple_client('http://localhost:6865', 'resident2') as client:
	client.ready()
	client.submit_create_and_exercise('ContactRelatedContracts.PersonalContract',{'userPartyId' : 'resident2' , 'personalDetails' : {'name' : 'Rupesh' , 'phoneNo' : '00000' , 'address' : 'address' }}, 'CreateContactConfirmationContract',{})














	

