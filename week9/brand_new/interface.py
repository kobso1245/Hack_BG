from logic import register_new_client, register_new_account
import getpass as gp
from Client import Account, convert_to_Account
import random
import string
import smtplib
from sending_settings import RECEIVER_EMAIL, SENDER_EMAIL, SENDER_PASSWORD, SERVER, PORT
from logic import hash_them_things, send_reset_password, wrapper_reset_password


def print_username_password():
    username = input("Enter your username: ")
    password = gp.getpass(prompt="Enter your password: ")
    return {"username": username,
            "password": password
            }


def print_help():
    print("login - for logging in!")
    print("register - for creating new account!")
    print("exit - for closing program!")


def print_info():
    print("You are: " + logged_user.get_username())
    print("Your id is: " + str(logged_user.get_id()))
    print("Your balance is:" + str(logged_user.get_balance()) + '$')


def print_all_commands():
    print("info - for showing account info")
    print("changepass - for changing passowrd")
    print("change-message - for changing users message")
    print("show-message - for showing users message")


def print_reset_password():
    username = input("Please write down your username: ")
    email = input("Please write down your email: ")
    return {'username': username,
            'email': email}


def register_account_info():
    username = input("Please write down the username you would like to use: ")
    password = input("Please write down the password you would like to use: ")
    email = input("Please write down the email you would like to use: ")
    firstname = input("Please write down your first name: ")
    middlename = input("Please write down your middle name: ")
    lastname = input("Please write down your last name: ")
    EGN = input("Please write down your EGN: ")

    return {"username": username,
            "password": password,
            "email": email,
            "firstname": firstname,
            "middlename": middlename,
            "lastname": lastname,
            "EGN": EGN
            }


def register_client_info():
    firstname = input("Please write down your first name: ")
    middlename = input("Please write down your middle name: ")
    lastname = input("Please write down your last name: ")
    EGN = input("Please write down your EGN: ")

    return {"firstname": firstname,
            "middlename": middlename,
            "lastname": lastname,
            "EGN": EGN
            }


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register-account':
            result = register_account_info()
            reg = register_new_account(result['username'],
                                       hash_them_things(result['password']),
                                       result['email'],
                                       result['firstname'],
                                       result['middlename'],
                                       result['lastname'],
                                       hash_them_things(result['EGN']))
            print(reg['reason'])

        elif command == 'register-client':
            result = register_client_info()
            reg = register_new_client(result['firstname'],
                                      result['middlename'],
                                      result['lastname'],
                                      hash_them_things(result['EGN']))
            print(reg['reason'])

        elif command == 'reset-password':
            result = print_reset_password()
            username = result['username']
            email = result['email']

            res = wrapper_reset_password(username, email)
            print(res['reason'])

        elif command == 'login':
            result = print_username_password()
            username = result['username']
            password = result['password']

            can_log_in = True
            try:
                logged_user = Account(
                    username=username,
                    password=hash_them_things(password)).exists()
                logged_user.incr_login_attempts()
            except Exception as exc:
                print(exc)
                can_log_in = False

            if can_log_in:
                logged_menu(logged_user)
            else:
                print("Login failed")
###############################################################
        elif command == 'help':
            print_help()
        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print_info()

        elif command == 'changepass':
            old_pass = input("Please enter your old password: ")
            new_pass = input("Enter your new password: ")
            inp = logged_user.change_password(hash_them_things(old_pass),
                                              hash_them_things(new_pass))
            print(inp['reason'])

        elif command == 'reset-password':
            wrapper_reset_password(logged_user)

        elif command == 'set-email':
            mail = input("Please enter your email: ")
            logged_user.change_email(mail)

        elif command == 'show-email':
            print(logged_user.get_email())

        elif command == 'show-balance':
            print("Current balance is: {}".format(logged_user.get_balance()))

        elif command == 'withdraw':
            ammount = input("Please enter the ammount to withdraw: ")
            logged_user.withdraw_money(ammount)

        elif command == 'deposit':
            ammount = input("Please enter the ammount to deposit: ")
            logged_user.deposit_money(ammount)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            logged_user.change_message(new_message)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == "logout":
            return

        elif command == 'help':
            print_all_commands()
##############################################################

if __name__ == '__main__':
    print("da")
    main_menu()
