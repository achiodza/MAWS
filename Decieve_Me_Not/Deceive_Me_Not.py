import hashlib
BLOCKSIZE = 65536 #set block size which the huge files and any other files will use to save your run from being used up by a single process

print("\n\t\t************************************************************")
print("\t\t************************************************************")
print("\t\t***********  Author:         @WekwaChiodza   ***************")
print("\t\t**If you have any questions contact wekwachiodza@gmail.com**")
print("\t\t************************************************************")
print("\t\t************************************************************\n")

print("\t\t*************************************************************")
print("\t\t****************PLEASE CHOOSE AN OPTION !********************")
print("\t\t*************************************************************\n\n")

print("1. HASH A FILE")
print("2. COMPARE HASH VALUES")

def hashfile():
    #input the file directory and append the file name at the end e.g var/www/html/test.txt
    chosen_file=input()


    with open(chosen_file, 'rb') as a_file:             #open the file specified by the directory given above and fed in 'chosen_file' in binary format
        buffered_file = a_file.read(BLOCKSIZE)          #break down the file in chunks that fits in the BLOCKSIZE save t to buffered_file
        while len(buffered_file) > 0:
            (hashlib.md5()).update(buffered_file)       #update the buffered_file with the other chunks remaining if they are.
            buffered_file = a_file.read(BLOCKSIZE)
    print((hashlib.md5()).hexdigest())                  #print the hashed value

#edited to be used for option two otherwise similar to the first one. just tweeked on the return.
def hashfile_for_option2():
    #input the file directory and append the file name at the end e.g var/www/html/test.txt
    chosen_file=input()


    with open(chosen_file, 'rb') as a_file:
        buffered_file = a_file.read(BLOCKSIZE)
        while len(buffered_file) > 0:
            (hashlib.md5()).update(buffered_file)
            buffered_file = a_file.read(BLOCKSIZE)

            return((hashlib.md5()).hexdigest()) #just return the hash digest value


#input one of the choices to bigin either option 1 or option 2
choice=input("Your choice pliz:")

if choice == '1':
    print("YOU HAVE SELECTED TO HASH A FILE OPTION")

#call the hashfile function
    hashfile()


if choice == '2':
    print("YOU HAVE SELECTED THE SECOND OPTION")
    print("Please input the Original hash value Downloaded or Existing:")
    md5_hash=input()

    print("\nHash the File you have.")
    result=hashfile_for_option2()                         #save the result of the hashfile_for_option2 to result
    if result == md5_hash:                                #compare result and md5_hash values
        print("Dont worry mate your files are intact!!")

    else:
        print("Suspicious File.. Has Values that do not match!!!")


#------------------------------------------------------------------------------------------------------------------------------------------
