import requests
import os
import time

webhook = input("[~] Webhook; ")
text = input("[~] Message; ")
data = {
    "content": text 
}
def send(i):
    res = requests.post(webhook, data=data)
    try:
        print("getting ratelimited, waiting")
        time.sleep(res.json()["retry_after"]/1000)
        res = ("waited")
    except:
        i += 1
        res = "Sent message " + "Successful."
    print('Amount of messages already sent:')
    return i
i = 0
while True:
   i = send(i)

os.system("pause")
