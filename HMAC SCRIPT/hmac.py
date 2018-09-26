#Author: WekwaChiodza
#HMAC for files and messages
#I have imported the hashlib and my custom modules for hashing files and comparing hash values
#Assignment CRYPTOGRAPHY

import argparse
import hashlib
import deceiveMeNoMore as _files
import hmac_for_text as _hmac

parser = argparse.ArgumentParser(description='Program to show the working principle of HMAC on messages and files')
parser.add_argument('--run',
    action='store_true',
    help='Run the program to see how the HMAC works' )

args = parser.parse_args()

if args.run:

    print("Please choose an option \n\n1. Deal with files \n2. Deal with plaintext messages")

    option=int(input(""))

    if option==1:
        print("You have selected option 1 which deals with files")
        _files.introMsg()
        _selectedOption=_hmac.decision()
        if _selectedOption==1:
            print("YOU HAVE SELECTED TO HASH A FILE OPTION")

            #call the hashfile function
            _files.hashfile()
            
        elif _selectedOption==2:
            print("YOU HAVE SELECTED THE SECOND OPTION")
            print("Please input the Original hash value of the Downloaded file or Existing file hashed:")
            md5_hash=input()

            print("\nHash the File you have.")
            result=_files.hashfile_for_option2()                         #save the result of the _files.hashfile_for_option2 to result
            if result == md5_hash:                                       #compare result and md5_hash values
                print("Dont worry mate your files are intact!!")

            else:
                print("Suspicious File.. Hash Values that do not match!!!")
                exit()


            
            
    elif option==2:
        print("You have selected option 2 which deals with plainText messages")
        _hmac._msg()
        _selectedOption=_hmac.decision()
        if _selectedOption==1:
            print("Input your message to hash here")
            msg = input("")
            something=msg.encode()
            x=something
            print(_hmac._hash(x))

        elif _selectedOption==2:
            #checking file text integrity
            _thevalue=_hmac._hash(x)
            print("Please paste/input the hash value you have below to check for integrity")
            info=input("")
            x=info.encode()
            text_Of_Interest=_hmac._hash(x)
            _hmac.hash_compare(_thevalue, text_Of_Interest)
        else:
            print("Your input is not that which we can process")
            exit()



    else:
        print("Oooopsss !! That is embarassing, you selected a wrong option please select 1 or 2")
        exit()

else:
    print("Why did you have to type that my guy, please type --run to run this good program")

