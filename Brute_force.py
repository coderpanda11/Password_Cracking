import random
import pyautogui

#Writing all the characters required for the password cracking
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$'

#Changing all those characters in a list
allChars = list(chars)

#Using an interactive GUI for the users to enter their password
pwd = pyautogui.password("Enter your password: ")
sample_pwd = ''

#Using while loop for cracking the password from the list of all characters
while (sample_pwd!=pwd):
    sample_pwd = random.choices(allChars,k=len(pwd))
    print (str(sample_pwd))
    if (sample_pwd == list(pwd)):
        print ("The Password is: "+ "".join(sample_pwd))