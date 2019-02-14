import requests
import json

url = "https://api.dominos.com/bot-service/conversation"
query = "get started"

headers = {
	"Authorization": "Bearer 6dc47ffe-d5e0-11e7-af10-e2174a70c3f9",
	"Content-Type": "application/json; charset=utf-8"
}

#I don't think we need these :)
#cookies = {
#	"utag_main": "v_id:0168eda8deba001f64d4f09872220004e002900d00e50$_sn:1$_ss:1$_st:1550177293819$ses_id:1550175493819%3Bexp-session$_pn:1%3Bexp-session", 
#	"AMCV_1F046398524DCCF80A490D44%40AdobeOrg": "-2017484664%7CMCMID%7C91497838094242808067000420431404102199%7CMCAID%7CNONE"
#}

rjson = {
	"query": query,
	"user": {
		"id": "5dbed01a-61f8-42e8-8d09-9f80fe4f3eaf",
		"token": "null"
	}
}

def update_query():
	global rjson, query
	rjson = {
		"query": query,
		"user": {
			"id": "5dbed01a-61f8-42e8-8d09-9f80fe4f3eaf",
			"token": "null"
		}
	}
	
def get_options(list):
	options = []
	for i in range(0, len(list)):
		options.append(list[i]["title"])
	options = str(options).translate(None, "[]\'u")
	return options

while query != "exit":
	r = requests.post(url, headers=headers, json=rjson)
	pr = json.loads(r.text)
	print("Domino's: " + pr["display"])
	#print("Options: " + get_options(pr["media"][0]["buttons"]))
	#print(rjson)
	
	query = raw_input("You: ")
	update_query()