import json
import time
from urllib.request import Request, urlopen
from discord import sendSignal
import datetime

def start(links):
    count = 0
    while True:
        for link in links:
            if(link[0] == False):
                print("Checking availability...")
                time.sleep(1.5)
                req = urlopen(Request(link[1], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}))
                content = json.loads(req.read())
                print(content)
                x = datetime.datetime.now()
                if ((x.hour == 17 and x.minute == 30) or x.hour == 18 or x.hour == 9 or x.hour == 14):
                    for i in content["data"][""]:
                        if content["data"][""][i] > 0:
                            sendSignal(str(content["data"][""][i]) + " Termin verfügbar: um " + i + link[1])
                    
                count = count +1
                print("No termin available..."+ str(count))
pass

link1 = [False, "https://sbj-teststation-munich.de/de/testcenter/1/ajax/verfuegbare-timeslots/", "https://sbj-teststation-munich.de/de/landsberger-strasse"]


links = [link1]
start(links)

