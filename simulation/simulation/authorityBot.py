import dazl
import pandas as pd

network = dazl.Network()
network.set_config(url='http://localhost:6865')

authority = network.simple_party('authority')

def addToDb(pincode, infectionLevel):
	df = pd.read_csv('/home/knoldus/Desktop/knolTrack/knolTrackFinal/dataset/dataset.csv')
	newdf=df.set_index('pincode')
	newdf.at[pincode,infectionLevel] = newdf.at[pincode,infectionLevel] + 1
	newdf.to_csv('/home/knoldus/Desktop/knolTrack/knolTrackFinal/dataset/dataset.csv')

@authority.ledger_created('ContactRelatedContracts.PersonalDetailsSharingContract')
def eventListner(event):
	addToDb(event.cdata['personalDetails']['pincode'],event.cdata['infectionDegree'])


network.run_forever()
	





