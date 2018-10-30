# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    list_of_studends.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anestor <anestor@student.unit.ua>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/29 23:18:33 by anestor           #+#    #+#              #
#    Updated: 2018/10/29 23:43:49 by anestor          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys, requests
import simplejson as json

if len(sys.argv) != 1:
    sys.exit()
else:
    print "Hello\n"

args = [
	'grant_type=client_credentials',
	'client_id=' + "d44086fe266348e6ec1a6fd07682ace51387bc78f670c5970062f4d66a7d8912",
	'client_secret=' + "f1f09e447fa0f778248ae1a1fc268aeab0b4b14b4c83e3599e8c45e5e7a562ef",
	]

status = requests.post("https://api.intra.42.fr/oauth/token?{}".format("&".join(args)))
response = status.json()

if status.status_code == 200:
	print "***********************"
	print "Connected to the 42 API"
	print "***********************"
else:
	print "You are not connecting to the 42 API please check README.md"
	sys.exit()

args = [
'access_token={}'.format(response['access_token']),
'token_type=bearer',
'filter[campus_id]=8',
'page=1'
#'filter[active]=true'
	]
n = 1

while True:
    status = requests.get("https://api.intra.42.fr/v2/locations?{}".format("&".join(args)))
    response2 = status.json()
    if len(response2) > 0:
        for test in response2:
            print test["campus_id"]
            print test["user"]["login"]
            print test["host"]
        n = n + 1
        args[3] = "page=" + n
    else:
        break

"""
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
"""
