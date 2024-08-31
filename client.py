
import json
import socket

def start_local_client(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 65432
    client_socket.connect((host, port))
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(8192).decode('utf-8')
    response = eval(response)
    print("received response")
    client_socket.close()
	
    return response


fileobject = open("inputt.txt")
jarray = []
while fileobject:
	input = fileobject.readline()
	if input == "":
		break
	response = start_local_client(input)
	jarray.append(response)
	
fileobject.close()

json_object = json.dumps(jarray, indent=4)
with open("llmdata.json", "w+") as outfile:
	outfile.write(json_object)