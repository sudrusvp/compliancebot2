from watson_developer_cloud import ConversationV1

def conversation():
	
	conversation = ConversationV1(
	username='81cae901-ee0e-4066-b333-c6d9cc5532ec',
	password='NCdy2rD8GQ5N',
	version='2017-02-03')
	
	conv_workspace_id = 'e5fa2b42-e839-4e1b-9c6d-4d3ca9a93330'
    
    temp={ "x": conversation,"y": conv_workspace_id }
    return_json=JSON.stringify(temp);

	return return_json