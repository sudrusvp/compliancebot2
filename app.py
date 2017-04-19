import json
import urllib
import os
import os.path
import sys
import logging
from os.path import join, dirname
from conversation import conversation_fun
from text_to_speech import text_to_speech_fun
from speech_to_text import speech_to_text_fun
from tone_analyze import tone_analyze_fun
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def main_page():

	if request.method == 'GET':
		return render_template("index2.html")

	elif request.method == 'POST':
		
		tone_analyzer1 = tone_analyze_fun()
		tone = tone_analyzer1.tone( text = request.form['message'])
		#print(json.dumps(tone,indent=2))
#		temp_context = {}
#		json.dumps(temp_context)
#		if os.path.isfile("static/doc/context_file.json") and os.path.getsize("static/doc/context_file.json")>0:
#			print("*******************")
#			print("file found")
#			with open('static/doc/context_file.json', 'r') as cf:
#				temp_context = json.load(cf)
#				print("*******************")
#				print(json.dumps(temp_context,indent=2))
#				print("*******************")
#				print(type(temp_context))
#			
#		else:
#			print("*******************")
#			print("file not found")
		

		
		context = {
			"user":tone['document_tone']['tone_categories']
		}
		
		#for emotion tone
		i = 0
		j = 0
		max = 0.0
		while i != 5:
			temp = round(context['user'][0]['tones'][i]['score'],2)
			if temp >= max:
				max = temp
				j = i
			i+=1
		
#		final_emotiontone = str(context['user'][0]['tones'][j]['tone_name']) + "-" + str(round(context['user'][0]['tones'][j]['score'],2))
		context["current"]=str(context['user'][0]['tones'][j]['tone_name'])
#		context["next_node"]="name"
#		context["next_node2"]="name2"
#		context["name"]="name"
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


#		print("*******************")
#		print(context)
#		if os.path.isfile("static/doc/context_file.json") and os.path.getsize("static/doc/context_file.json")>0:
#			context["temp_context"]=temp_context

		#print(json.dumps(context['user'][1]['category_name'],indent=4))
		conv_workspace_id = 'e5fa2b42-e839-4e1b-9c6d-4d3ca9a93330'

		response = conversation_fun().message(workspace_id = conv_workspace_id, message_input={'text': request.form['message']},context = context)
		
#		with open('static/doc/context_file.json', 'w') as f:
#			f.seek(0)
#			f.truncate()
#			json.dump(response['context'], f)
#			f.close()
		
#		print("*******************")
		print(json.dumps(response,indent=4))
		file = open('static/media/output.wav','wb+')
#		file.seek(0)
#		file.truncate()
		file.write(text_to_speech_fun().synthesize(str(response['output']['text'][0]),accept='audio/wav',voice='en-US_LisaVoice'));
		file.close()
		
		
		with open(join(dirname(__file__), 'static/media/mySound.wav'),'rb') as file2:
			print("start printing speech to text output")
			print(json.dumps(speech_to_text_fun().recognize(file2, content_type='audio/wav', timestamps=True,word_confidence=True),indent=2))
			file2.close()
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
		

		script1 = """<html><head><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
			</head>
			<body>
			<hr>
			<a href='#' class='btn btn-info btn-lg' onclick='yes()'>
          	<span class='glyphicon glyphicon-thumbs-up'></span> Yes
        	</a>
			<a href='#' class='btn btn-info btn-lg' onclick='no()'>
          	<span class='glyphicon glyphicon-thumbs-down'></span> No
        	</a>
			</body>
			</html>"""

		script2 = """ <html><head>
			<style>
			.button {
			  display: inline-block;
			  padding: 15px 25px;
			  font-size: 15px;
			  cursor: pointer;
			  text-align: center;
			  text-decoration: none;
			  outline: none;
			  color: #fff;
			  background-color: #ADD8E6;
			  border: none;
			  border-radius: 12px;
			  box-shadow: 0 9px #fff;
			}
			
			.button:hover {background-color: #00BFFF}
			
			.button:active {
			  background-color: #00BFFF;
			  box-shadow: 0 5px #666;
			  transform: translateY(4px);
			}
			</style>
			<script type='text/javascript'>
			var src = "static/media/output.wav?cache-buster=" + new Date().getTime()
			var audio = new Audio(src);
			audio.play();
			function play(){
				audio.play();
			}
			function pause(){
				audio.pause();
			}
			</script>
			</head>
			<hr>
			<input class="button button5" type="button" value="PLAY" onclick="play()">
			<input class="button button5" type="button" value="PAUSE" onclick="pause()">
			</html>"""
			
		if response['intents'] and response['intents'][0]['confidence']:
			confidence = str(round(response['intents'][0]['confidence'] * 100))
			response = str(response['output']['text'][0] + "\n" + "<HTML><BODY><hr style='height: 7px;border: 0;box-shadow: 0 10px 10px -10px white inset;width:270px;margin-left:0px'></body></html>I'm "  + confidence + "% certain about this answer!")
			newline = "<html><body><br></body></html>"
			response = response + newline + a + " " + b + " "+ c + " "+ d + " "+ e 
			response = response + newline + f + " " + g + " "+ h
			response = response + newline + i + " " + j + " "+ k + " "+ l + " "+ m
#			response = response + newline + " detected " + final_emotiontone + newline + " detected " + final_langtone + newline + " detected " + final_socialtone
			response = response + newline
			
			response = response + script1+script2
			return str(response)
		
		response = str(response['output']['text'][0])
		newline = "<html><body><br></body></html>"
		response = response + "<html><hr></html>" + newline + a + " " + b + " "+ c + " "+ d + " "+ e 
		response = response + newline + f + " " + g + " "+ h
		response = response + newline + i + " " + j + " "+ k + " "+ l + " "+ m
		response = response + script2
		return str(response)
		

if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
	
	

