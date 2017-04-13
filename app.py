import urllib
import os
import os.path
import sys
import logging
import conversation
import text_to_speech
import tone_analyze
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def main_page():

	if request.method == 'GET':
		return render_template("index2.html")

	elif request.method == 'POST':
		
		tone_analyzer1 = tone_analyze()
		tone = tone_analyzer1.tone( text = request.form['message'])
		#print(json.dumps(tone,indent=2))
		context = {
			"user":tone['document_tone']['tone_categories']
		}
		#print(json.dumps(context['user'][1]['category_name'],indent=4))
		conv1 = conversation()['x']
		conv2 = conversation()['y']
		response = conv1.message(workspace_id = conv2, message_input={'text': request.form['message']},context = context)
		
		file = open('static/media/output.wav','wb+')
		file.seek(0)
		file.truncate()
		file.write(text_to_speech().synthesize(str(response['output']['text'][0]),accept='audio/wav',voice='en-US_LisaVoice'));
		file.close()
		
		a = str(context['user'][0]['category_name']) + "--->" + str(context['user'][0]['tones'][0]['tone_name']) + "-" + str(round(context['user'][0]['tones'][0]['score'],2))
		b = str(context['user'][0]['tones'][1]['tone_name']) + "-" + str(round(context['user'][0]['tones'][1]['score'],2))
		c = str(context['user'][0]['tones'][2]['tone_name']) + "-" + str(round(context['user'][0]['tones'][2]['score'],2))
		d = str(context['user'][0]['tones'][3]['tone_name']) + "-" + str(round(context['user'][0]['tones'][3]['score'],2))
		e = str(context['user'][0]['tones'][4]['tone_name']) + "-" + str(round(context['user'][0]['tones'][4]['score'],2))
		
		f = str(context['user'][1]['category_name']) + "--->" +str(context['user'][1]['tones'][0]['tone_name']) + "-" + str(round(context['user'][1]['tones'][0]['score'],2))
		g = str(context['user'][1]['tones'][1]['tone_name']) + "-" + str(round(context['user'][1]['tones'][1]['score'],2))
		h = str(context['user'][1]['tones'][2]['tone_name']) + "-" + str(round(context['user'][1]['tones'][2]['score'],2))
		
		i = str(context['user'][2]['category_name']) + "--->" +str(context['user'][2]['tones'][0]['tone_name']) + "-" + str(round(context['user'][2]['tones'][0]['score'],2))
		j = str(context['user'][2]['tones'][1]['tone_name']) + "-" + str(round(context['user'][2]['tones'][1]['score'],2))
		k = str(context['user'][2]['tones'][2]['tone_name']) + "-" + str(round(context['user'][2]['tones'][2]['score'],2))
		l = str(context['user'][2]['tones'][3]['tone_name']) + "-" + str(round(context['user'][2]['tones'][3]['score'],2))
		m = str(context['user'][2]['tones'][4]['tone_name']) + "-" + str(round(context['user'][2]['tones'][4]['score'],2))
		
#		#for emotion tone
#		i = 0
#		j = 0
#		max = 0.0
#		while i != 5:
#			temp = round(context['user'][0]['tones'][i]['score'],2)
#			if temp >= max:
#				max = temp
#				j = i
#			i+=1
#		
#		final_emotiontone = str(context['user'][0]['tones'][j]['tone_name']) + "-" + str(round(context['user'][0]['tones'][j]['score'],2))
#		
#		#for language tone
#		i = 0
#		j = 0
#		max = 0.0
#		while i != 3:
#			temp = round(context['user'][1]['tones'][i]['score'],2)
#			if temp >= max:
#				max = temp
#				j = i
#			i+=1
#		
#		final_langtone = str(context['user'][1]['tones'][j]['tone_name']) + "-" + str(round(context['user'][1]['tones'][j]['score'],2))
#		
#		#for social tone
#		i = 0
#		j = 0
#		max = 0.0
#		while i != 5:
#			temp = round(context['user'][2]['tones'][i]['score'],2)
#			if temp >= max:
#				max = temp
#				j = i
#			i+=1
#		
#		final_socialtone = str(context['user'][2]['tones'][j]['tone_name']) + "-" + str(round(context['user'][2]['tones'][j]['score'],2))
		
		if response['intents'] and response['intents'][0]['confidence']:
			confidence = str(round(response['intents'][0]['confidence'] * 100))
			response = str(response['output']['text'][0] + "\n" + "<HTML><BODY><hr style='height: 7px;border: 0;box-shadow: 0 10px 10px -10px white inset;width:270px;margin-left:0px'></body></html>I'm "  + confidence + "% certain about this answer!")
			newline = "<html><body><br></body></html>"
			response = response + newline + a + " " + b + " "+ c + " "+ d + " "+ e 
			response = response + newline + f + " " + g + " "+ h
			response = response + newline + i + " " + j + " "+ k + " "+ l + " "+ m
#			response = response + newline + " detected " + final_emotiontone + newline + " detected " + final_langtone + newline + " detected " + final_socialtone
			response = response + newline + "<html><body><hr></body></html>"
			script1 = """<html><head><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
			</head>
			<body>
			<a href='#' class='btn btn-info btn-lg' onclick='yes()'>
          	<span class='glyphicon glyphicon-thumbs-up'></span> Yes
        	</a>
			<a href='#' class='btn btn-info btn-lg' onclick='no()'>
          	<span class='glyphicon glyphicon-thumbs-down'></span> No
        	</a>
			</body>
			</html>"""
			
			response = response + script1
			
			script2 = """ <html><head><script type='text/javascript'>
			var src = "static/media/output.wav?cache-buster=" + new Date().getTime()
			var audio = new Audio(src);
			audio.play();
			</script>
			</head>
			</html>"""
			
			response = response + script2
			return str(response)
			
		#else
			#return str(response)
			
		print(json.dumps(response,indent=2))
		return str(response['output']['text'][0])
		

if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
	
	

