import hashlib
import random
import string

def hash(inputs):
    outputs=hashlib.sha512(inputs.encode()).hexdigest()
    return (outputs)
#print (hash("test"))
username="drew"
password="abc123"
salt="%4$bct"
whatsinthedatabase=hash(username+password+salt)
def checkpassword(randstr,shouldbe):
    print(randstr +"\n -->this would be a capatchea")
    capatchea=input("What does it say?\n -->")
    uname=input("whats your username\n -->")
    pword=input("whats your password\n -->")
    salty=salt
    return(shouldbe==hash(capatchea+hash(uname+password+salty)))
while(True):
    randomstring=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(7))
    if(checkpassword(randomstring,hash(randomstring+whatsinthedatabase))):
        print("authenticated")
    else:
        print("The username password or capatchea was incorrect")
