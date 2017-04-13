from watson_developer_cloud import ToneAnalyzerV3

def tone_analyze():

	tone_analyzer = ToneAnalyzerV3(
	username = '20c2903e-48a9-4fd5-8f0b-5e699fa5343e',
	password = 'ZC2WBeLbXUXs',
	version = '2016-05-19')
    
	return tone_analyzer