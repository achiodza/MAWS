usage:
python hmac.py --run [-h]

CREATED:
deceiveMeNoMore.py which has functions to hash files.
-you need to use the path of the file to hash it e.g C:\users\name_of_user\Desktop\filename

hmac_for_text.py which has functions to hash the text messages only.
-prompts you to enter text or paste a message


Please note that l did not include the use of a password or key:
some of you might start saying so where is the hmac of the hmac,

adding a key as a string only add characters to the message which is ultimately the message too in the end.

def generate_hash(message):

    key=generate_key()

    message=message+str(key)

    message_key= message.encode()

    print ("Key used is:", key)

    sha256=hashlib.sha256()

    sha256.update(message_key)

    msg_digest=sha256.digest()

    hash_code=msg_digest.hex()

    return(hash_code)

Clearly l can write that. :-)

So if you want to add it you can to spice things up. and we are taking suggestions too.


YOU CAN ALSO USE THE HMAC MODULES THAT COMES WITH PYTHON TOO IT COMES IN HANDY.
This was my feeble attempt to create my version of it.