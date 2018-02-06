#Run this script at the end when you are ready to submit your homework to the autograder.

import hw_sniffing  # imports your hw_sniffing module
import requests

submissionFile=open('hw_sniffing.py','r')
postParams=hw_sniffing.yourSubmission()
del postParams["output"] 
postData={"output":bytes(hw_sniffing.yourSubmission()["output"],encoding='iso-8859-1')}
postHeaders={'content-type': 'application/octet-stream'}

tokenFile=open('token','a+')
token=tokenFile.read();

if len(token)<6: 
	tokenResponse=requests.post("https://script.google.com/a/brown.edu/macros/s/AKfycbyiAaZXZHG0PzuWNHSl5gPXTCa2i15tTmavDSA3wAHz11DOnqbM/exec",data={'requestingToken':1,'email':postParams["email"]});
	token=tokenResponse.text;
	tokenFile.write(token)

postParams["token"]=token
postParams["submission"]=submissionFile.read()

subResponse=requests.post("https://script.google.com/a/brown.edu/macros/s/AKfycbyiAaZXZHG0PzuWNHSl5gPXTCa2i15tTmavDSA3wAHz11DOnqbM/exec",params=postParams,data=postData,headers = postHeaders)
responseFile=open('submissionResponse.txt','wb')
responseFile.write(subResponse.text.encode('utf-8'))
print(subResponse.text)