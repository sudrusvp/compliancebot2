from watson_developer_cloud import ConversationV1
from json import JSONEncoder

def conversation_fun():
	
	conversation = ConversationV1(
	username='81cae901-ee0e-4066-b333-c6d9cc5532ec',
	password='NCdy2rD8GQ5N',
	version='2017-02-03')

	return conversation