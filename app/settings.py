# settings file
# By Sanix-darker

def open_ressources(file_path):
    return [item.replace("\n", "") for item in open(file_path).readlines()]


# GLOBAL CONSTANT VARIABLES -------
# list of potential incorrect message in the page if it doesn't succeed
INCORRECT_MESSAGE = open_ressources('./ressources/incorrectMessage.txt')
# list of potential success message in the page if it succeed
SUCCESS_MESSAGE = open_ressources('./ressources/successMessage.txt')
# Getting list of potentials password
PASSWORDS = open_ressources('./ressources/passwords.txt')
# Getting list of user to test with
USERS = open_ressources('./ressources/users.txt')
# Limit of trying connections
LIMIT_TRYING_ACCESSING_URL = 7
