

import os
import google.generativeai as genai
import json
import time

fileobject = open("inputt.txt")

genai.configure(api_key="AIzaSyBgKOWbufgSnHbPceVVsJ6thftiv1pt_A8")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)



jarray = []

while fileobject:
  line = fileobject.readline()
   
  if line == "":
    break

  timeS = time.time()
  response = chat_session.send_message(line)
  rtext = response.text
  timeR = time.time()
  
  prompt = line
  msg = rtext

  dic = {
    "Prompt": prompt, 
    "Message": msg, 
    "TimeSent": timeS, 
    "TimeRecvd": timeR, 
    "Source": "Gemini"
  }
  jarray.append(dic)
  
  print("appended")


json_object = json.dumps(jarray, indent=4)
with open("llmdata.json", "w+") as outfile:
	#outfile.seek(0,2)
	outfile.write(json_object)
	print("wohoo saved")
    
fileobject.close()

'''
{
    "Prompt": "What is an operating system?", 
    "Message": "An operating system is computer program that organizes a number of other programs at the same time", 
    "TimeSent": 1724610170, 
    "TimeRecvd": 1724610183, 
    "Source": "ChatGPT"}
	
'''

