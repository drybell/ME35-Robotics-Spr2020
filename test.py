import requests
import json 

def Get_SL(Tag):
    Key = "j2m40Z2Dd2MyPJcsmCSh586VCtvx68ltYwJjZCHujB"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    urlValue = urlBase + Tag + "/values/current"
    try:
        value = requests.get(urlValue,headers=headers).text
        data = json.loads(value)
        #print(data)
        result = data.get("value").get("value")
    except Exception as e:
        print(e)
        result = 'failed'
    return result

def Put_SL(Tag, Type, Value):
    Key = "j2m40Z2Dd2MyPJcsmCSh586VCtvx68ltYwJjZCHujB"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    urlValue = urlBase + Tag + "/values/current"
    propValue = {"value":{"type":Type,"value":Value}}
    try:
        reply = requests.put(urlValue,headers=headers,json=propValue).text
    except Exception as e:
        print(e)         
        reply = 'failed'
    return reply

def Get_SL2(Tag):
    Key = "bvd8X9LweQY9o2eP1NYL-p8mLL9wMAk6YYOnYSiIo0"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    urlValue = urlBase + Tag + "/values/current"
    try:
        value = urequests.get(urlValue,headers=headers).text
        data = ujson.loads(value)
        #print(data)
        result = data.get("value").get("value")
    except Exception as e:
        print(e)
        result = 'failed'
    return result

def Put_SL2(Tag, Type, Value):

    Key = "bvd8X9LweQY9o2eP1NYL-p8mLL9wMAk6YYOnYSiIo0"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    urlValue = urlBase + Tag + "/values/current"
    propValue = {"value":{"type":Type,"value":Value}}
    try:
        reply = urequests.put(urlValue,headers=headers,json=propValue).text
    except Exception as e:
        print(e)         
        reply = 'failed'
    return reply

Put_SL2("Start29", "BOOLEAN", "True")
Put_SL2("Start28", "BOOLEAN", "False")
Put_SL("start","STRING", "True")
# Put_SL("start","STRING", "False")
Put_SL("stage1","STRING", "True")
# Put_SL("stage1","STRING", "False")
print("done")


