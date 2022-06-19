import random
from alive_progress import alive_bar
import time

#The lists for teh status lines
#To change these, simply add/delete the words/phrases you want and hit save
action = ["Hacking", "Retrieving", "Encrypting", "Decrypting", "Encoding", "Generating", "Forging", "Calculating", "Creating", "Cracking", "Pinging", "Sending", "Requesting", "Spoofing"]
actioned = ["Hacked", "Retrieved", "Encrypted", "Decrypted", "Encoded", "Generated", "Forged", "Calculated", "Created", "Cracked", "Requested", "Sent", "Spoofed"]
thing = ["Log Files", "Security Key", "Algorithm", "Module", "Floating Point Numbers", "Private Key", "System Logs", "SSD", "Cookie"]
place = ["CIA Database", "Deep Web", "Dataset", "Operating System", "Target", "Web", "TappStudios.serveirc.com", "Interpol", "G94&*-98uj;KJHp9uhf38P98.onion", "Host Server"]

a=len(action)-2
t=len(thing)-2
p=len(place)-2


def loading():
    for i in range(packets):
        ... # process items as usual.
        yield  # insert this :)
wait=0.00000001
length=random.randint(5,25)

#The main code
for i in range(length):
    bytes=random.randint(1,9)
    size=random.randbytes(bytes)
    loadbar=random.randint(0,3)
    packets=random.randint(100, 550)
    string=random.randint(1,8)
    
    if string==1:
        act=random.randint(1,a)
        tng=random.randint(1,t)
        thg=random.randint(1,t)
        print(">_",action[act], place[tng], thing[thg], "...")
        if loadbar==1:
            fail=random.randint(1,2)
            if fail==1:
                print("     Action Failed...")
            time.sleep(0.5)
        else:
            with alive_bar(packets) as bar:
                for i in loading():
                    time.sleep(wait)
                    bar()

    if string==2:
        tng=random.randint(1,t)
        act=random.randint(1,a)
        print(">_",thing[tng], actioned[act], "...")
        if loadbar==1:
            fail=random.randint(1,2)
            if fail==1:
                print("     Action Failed...")
            time.sleep(0.5)
        else:
            with alive_bar(packets) as bar:
                for i in loading():
                    time.sleep(wait)
                    bar()

    if string==3:
        act=random.randint(1,a)
        tng=random.randint(1,t)
        plc=random.randint(1,p)
        print(">_",action[act], thing[tng], "From", place[plc], "...")
        if loadbar==1:
            fail=random.randint(1,2)
            if fail==1:
                print("     Action Failed...")
            time.sleep(0.5)
        else:
            with alive_bar(packets) as bar:
                for i in loading():
                    time.sleep(wait)
                    bar()

    if string==4:
        act=random.randint(1,a)
        plc=random.randint(1,p)
        tng=random.randint(1,t)
        print(">_",action[act], place[plc], thing[tng], "...")
        if loadbar==1:
            fail=random.randint(1,2)
            if fail==1:
                print("     Action Failed...")
            time.sleep(0.5)
        else:
            with alive_bar(packets) as bar:
                for i in loading():
                    time.sleep(wait)
                    bar()
 
    if string==5:
        plc=random.randint(1,p)
        tng=random.randint(1,t)
        act=random.randint(1,a)
        print(">_",place[plc],thing[tng], actioned[act], "...")
        if loadbar==1:
            fail=random.randint(1,2)
            if fail==1:
                print("     Action Failed...")
            time.sleep(0.5)
        else:
            with alive_bar(packets) as bar:
                for i in loading():
                    time.sleep(wait)
                    bar()
        
    if string==6:
        act=random.randint(1,a)
        tng=random.randint(1,t)
        plc=random.randint(1,p)
        print(">_ Pinging", place[plc], "...")
        if loadbar==1:
            fail=random.randint(1,2)
            if fail==1:
                print("     Action Failed...")
            time.sleep(0.5)
        else:
            with alive_bar(packets) as bar:
                for i in loading():
                    time.sleep(wait)
                    bar()
            print("     ",place[plc], "responded", size)
        
    if string==7:
        act=random.randint(1,a)
        print(">_", action[act], size, "...")
        if loadbar==1:
            fail=random.randint(1,2)
            if fail==1:
                print("     Action Failed...")
            time.sleep(0.5)
        else:
            with alive_bar(packets) as bar:
                for i in loading():
                    time.sleep(wait)
                    bar()
                    
    if string==8:
        act=random.randint(1,a)
        plc=random.randint(1,p)
        print(">_", actioned[act], size, "from", place[plc],"...")
        if loadbar==1:
            fail=random.randint(1,2)
            if fail==1:
                print("     Action Failed...")
            time.sleep(0.5)
        else:
            with alive_bar(packets) as bar:
                for i in loading():
                    time.sleep(wait)
                    bar()

        
