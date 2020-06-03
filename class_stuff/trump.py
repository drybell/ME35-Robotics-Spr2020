import requests


Key = 	#hidden because i dont trust like that																	'xFXBfS_CWn75o_jHyTQWZ5TaU6GWD6sdUhUDfYVFMK'
     
urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
headers1 = {"Accept":"application/json","x-ni-api-key":Key}

url = "https://joke3.p.rapidapi.com/v1/joke"

headers = {
    'x-rapidapi-host': "joke3.p.rapidapi.com",
    'x-rapidapi-key': "fd1c2f68f0msh0af8fa70c8a8662p146e2cjsn93778d346e95"
    }

response = requests.request("GET", url, headers=headers)

dict1 = response.json()

value = dict1["content"]
		
urlValue = urlBase + "Trump" + "/values/current"
propValue = {"value":{"type":"STRING","value":value}}
reply = requests.put(urlValue,headers=headers1,json=propValue).text
print(dict1["content"])
