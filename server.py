import google.generativeai as genai
import time
import socket

def start_local_server():

  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  host = '127.0.0.1'
  port = 65432
  server_socket.bind((host, port))
  server_socket.listen(5)
  print(f"Server listening on {host}:{port}")

  while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    data = client_socket.recv(8192).decode('utf-8')
    print(f"Received: {data}")
    response = callAPI(data)
    response = str(response)
    client_socket.send(response.encode('utf-8'))
    client_socket.close()


def callAPI(input):
  
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
  
  if input == "":
    return

  timeS = time.time()
  response = chat_session.send_message(input)
  rtext = response.text
  timeR = time.time()
  
  prompt = input
  msg = rtext

  dic = {
    "Prompt": prompt, 
    "Message": msg, 
    "TimeSent": timeS, 
    "TimeRecvd": timeR, 
    "Source": "Gemini"
  }

  return dic

start_local_server()
'''
{
    "Prompt": "What is an operating system?", 
    "Message": "An operating system is computer program that organizes a number of other programs at the same time", 
    "TimeSent": 1724610170, 
    "TimeRecvd": 1724610183, 
    "Source": "ChatGPT"}
	
'''

