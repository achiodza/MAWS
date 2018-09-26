import hashlib

def _msg():
    print("Select 1 for Hashing your Message")
    print("Select 2 to check integrity your Message")

def decision():
    number=int(input())
    return(number)


#Function to hash
def _hash(x):
    sha256 = hashlib.sha256()
    sha256.update(x)
    msg_digest=sha256.digest()
    _thevalue=msg_digest.hex()
    
    return(_thevalue)
    

#Function to compare the hash values
def hash_compare(_thevalue, text_Of_Interest):
    if _thevalue==text_Of_Interest:
        print("The message is unaltered !! The Hash Values Match")
    else:
        print("DANGER!!!!!!!!!! Files compromised")
        

