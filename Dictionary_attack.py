import hashlib

pass_found=0

i_hash = input("Enter the hash of your password: ")

print ("\n<==========PASSWORD FILE EXAMPLE=========>")
print ("For windows: A:/password/password_list.txt")
print ("For Linux or Mac: /usr/share/wordlists/rockyou.txt")
p_hash = input("\nEnter your password file with its path: ")

p_file = open(p_hash,'r')

for word in p_file:
    enc_word = word.encode('utf-8')
    hash_word = hashlib.md5(enc_word.strip())
    digest = hash_word.hexdigest()
    
    if digest == i_hash:
        print ("Password found: ", word)
        pass_found = 1
        break

    if not pass_found:
        print ("Password not found")
