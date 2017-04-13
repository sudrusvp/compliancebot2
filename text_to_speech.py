from watson_developer_cloud import TextToSpeechV1

def text_to_speech():

	text_to_speech = TextToSpeechV1(
    username='8921eb13-5eb4-4286-9add-5a7870ba4ecf',
    password='tKJBMhuw42nL',
    x_watson_learning_opt_out=True)
    
    return text_to_speech