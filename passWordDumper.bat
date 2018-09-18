#script to view and dump passwords in a file or removable media
#view profiles and save them in a text file. you can type this command in the command prompt and see what it shows you.
netsh wlan show profiles >profiles.txt


#for future dev: code to read the profiles and feed the names to the code below.

#view password and save it in plaintext in a textfile
netsh wlan show profiles name="Name_Of_Network" key="clear" >PasswordsDetails.txt