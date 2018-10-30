import os, sys, requests
import simplejson as json

class term_colors:
	BLUE = '\033[94m'
	RED = '\033[91m'
	GREEN = '\x1b[6;30;42m'
	END = '\x1b[0m'

debug = False;

if len(sys.argv) > 1:
	with open(sys.argv[1]) as f:
		names = f.readlines()
	if len(sys.argv) > 2 and sys.argv[2] == "debug":
		debug = True;
else:
	print "Usage: python hind.c <login names file> [debug]"
	sys.exit()

args = [
	'grant_type=client_credentials',
	'client_id=' + "d44086fe266348e6ec1a6fd07682ace51387bc78f670c5970062f4d66a7d8912",
	'client_secret=' + "f1f09e447fa0f778248ae1a1fc268aeab0b4b14b4c83e3599e8c45e5e7a562ef",
	]

status = requests.post("https://api.intra.42.fr/oauth/token?{}".format("&".join(args)))
response = status.json() #token print response

if status.status_code == 200:
	print "***********************"
	print term_colors.BLUE + "Connected to the 42 API" + term_colors.END;
	print "***********************"
else:
	print "You are not connecting to the 42 API please check README.md"
	sys.exit()

if debug:
	print "Token: " + response['access_token']

args = [
'access_token={}'.format(response['access_token']),
'token_type=bearer',
'filter[campus_id]=8'
#'filter[active]=true'
	]
"""
for name in names:
	if name.strip() != "":
		status = requests.get("https://api.intra.42.fr/v2/users/" + name.strip() + "/locations?{}".format("&".join(args)))
		response = status.json()
		if len(response) > 0:
			if debug:
				print str(json.dumps(response, indent=4, sort_keys=True))
                     #   print response
                     #   print "999999\n"
			print name.strip() + " is at computer " + term_colors.GREEN + response[0]['host'] + term_colors.END
		else:
			if status.status_code == 200:
				print name.strip() + " is not showing up on a computer," + term_colors.BLUE + " ask around!" + term_colors.END
			else:
				print term_colors.RED + name.strip() + term_colors.END + " is not a student login on the 42 API"
                                
"""

status = requests.get("https://api.intra.42.fr/v2/locations?{}".format("&".join(args)))
response2 = status.json()
for test in response2:
    #print test.items()
    print test["campus_id"]
    print test["user"]["login"]
    print test["host"]
#print str(json.dumps(response, sort_keys=True))

print "\n\n\n"
status = requests.get("https://api.intra.42.fr/v2/cursus_users?{}".format("&".join(args)))
response3 = status.json()
for test in response3:
    print test["user"]["login"]
    print test["level"]

print "\n\n\n"
args = [
'access_token={}'.format(response['access_token']),
'token_type=bearer'
	]
status = requests.get("https://api.intra.42.fr/v2/users?{}".format("&".join(args)))
response4 = status.json()
for test in response4:
    print test["login"]
#    print test["level"]
#print response4
