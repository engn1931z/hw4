# Homework 2 Template Code
#
# This initial helper code will contact the server to request a list of desired angles, and will turn these comma separated values into a python list called desiredAngles.
#
# Your goal is to produce a command sequence that will:
#  - First home the stage
#  - Then move the stage to each position in the desiredAngle list
#  - Finally query the position of the stage at its final position.
#
# Pass your commands to the variable named commandSequence, and it will be save to a file unscrambledText.txt
# 
# When you have a final answer, you can submit your assignment to the autograde by running the submit.py script 

##################################################################
### HELPER CODE TO REQUEST DESIRED ANGLES FROM SERVER
##################################################################
import requests
serverRequest=requests.get("https://goo.gl/Y83I1i").text
desiredAngles=[float(x) for x in serverRequest.split(',')]
##################################################################
### YOUR BRIEF TEXT EXPLANATION OF YOUR DETECTIVE WORK
##################################################################

# Please provide a brief text explanation of how you decoded the stage commands
#
#
#
#
#
#
#

##################################################################
### YOUR CODE TO CREATE THE COMMAND SEQUENCE SHOULD GO BELOW HERE
##################################################################


# import anything else you might need here 

email= "YOUR_EMAIL_GOES_HERE@brown.edu" #REPLACE THIS



commandSequence='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER

##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':2,'input':serverRequest,'output':commandSequence}