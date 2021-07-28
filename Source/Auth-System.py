source = open(input('Enter Python File Name: '), "r").read()
auth = r'''
import subprocess, requests, time, os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()'''
auth2 = f"\nreq = requests.get('{input('Enter Your Pastebin Link: ')}').text"

auth3 = """
try:
    if hwid in req:
        pass
    else:
        print('[-] HWID Not in database')
        print(f'HWID: {hwid}') 
        time.sleep(5)
        exit()
except:
    print('[-] Failed to connect to database')
    time.sleep(5) 
    exit() 
    
print('Welcome')
"""
with open("AuthDone.py", "w") as m:
    m.write(f"{auth}\n{auth2}\n{auth3}\n{source}")
