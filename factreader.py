"""
Program to read facts from file and post them to Slack
Developed by: Anand Nandakumar
"""

import requests
import json

def factreader(factfile,linelist):
	lines_old = []
	lines_new = []
	i=0
	with open(linelist,'rt') as line_file:
		for line in line_file:
			lines_old=line
	with open(factfile,'rt') as in_file:
		for line in in_file:
			i+=1
			if str(i) not in lines_old and len(lines_new)==0:
				print(line)
				url='https://hooks.slack.com/services/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'
				payload = {"channel": "#dev", "username": "FactBot", "text": line}
				headers = {'Content-type': 'application/json'}
				requests.post(url, data=json.dumps(payload), headers=headers)
				
				lines_new.append(lines_old)
				lines_new.append(i)
				
	line_file = open(linelist,'w')
	line_file.truncate()
	line_file.write(str(lines_new))
	line_file.close()
factfile='facts.txt'
linelist='lines.txt'
factreader(factfile,linelist)
