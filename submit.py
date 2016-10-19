#Run this script at the end when you are ready to submit your homework to the autograder.

import hw4  # imports your hw4 module
import requests

submissionFile=open('hw4.py','r')
postParams=hw4.yourSubmission()
del postParams["output"] 
postData={"output":hw4.yourSubmission()["output"]}
postHeaders={'content-type': 'application/octet-stream'}

tokenFile=open('token','a+')
token=tokenFile.read();

if len(token)<6: 
	tokenResponse=requests.post("https://script.google.com/macros/s/AKfycbyiAaZXZHG0PzuWNHSl5gPXTCa2i15tTmavDSA3wAHz11DOnqbM/exec",data={'requestingToken':1,'email':postParams["email"]});
	token=tokenResponse.text;
	tokenFile.write(token)

postParams["token"]=token
postParams["submission"]=submissionFile.read()
subResponse=requests.post("https://script.google.com/macros/s/AKfycbyiAaZXZHG0PzuWNHSl5gPXTCa2i15tTmavDSA3wAHz11DOnqbM/exec",params=postParams,data=postData,headers = postHeaders)
responseFile=open('submissionResponse.txt','w+')
responseFile.write(subResponse.text.encode('utf8'))
print subResponse.text
