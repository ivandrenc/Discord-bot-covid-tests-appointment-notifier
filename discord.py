import requests #dependency

url = "https://discordapp.com/api/webhooks/914235861762179093/sn5tVSc4KKuAc4y5ixx_zlG_QN9nTOUzn77LHyxPhgRdLOQgFzKdwMFhmUa0fHQXqvNP" #webhook url, from here: https://i.imgur.com/f9XnAew.png

def sendSignal(link):
    data = {
        "content": "@everyone "+link,
        "username": "Arnold Schwarzenegger",
    }
    result = requests.post(url, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
pass
