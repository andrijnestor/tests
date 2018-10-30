# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    list_of_studends.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anestor <anestor@student.unit.ua>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/29 23:18:33 by anestor           #+#    #+#              #
#    Updated: 2018/10/30 09:05:44 by anestor          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys, requests
import simplejson as json
import time

f = open("testfile", "a")
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
#'filter[campus_id]=8',
'page=1'
#'sort[user_id]=true'
#'filter[active]=true'
	]


n = 1
while True:
    status = requests.get("https://api.intra.42.fr/v2/campus/8/users?{}".format("&".join(args)))
    #print status
    time.sleep(0.5)
    response2 = status.json()
 #   r = requests.head(link)
  #  print r.headers['link']
 #   print response2
    if len(response2) > 0:
        for test in response2:
         #   print test["campus_id"]
         #   print test["user"]["login"]
         #   print test["host"]
        #    print test['login']
            f.write(test['login'] + "\n")
        print "Page: " + str(n)
        n = n + 1
        args[2] = "page=" + str(n)
    else:
        f.close()
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
