for logic import register_new_client, register_new_account

def wrapped_reset_password(logged_user):
    new_pass = generate_new_password()
    change_password_query(logged_user.get_username(),
                          sql_manager.hash_them_things(new_pass))
    send_reset_password(get_email(logged_user.get_username()), new_pass)

def wrapped_withdraw(logged_user):
    ammount =  float(input("Please select ammount of money you would like to withdraw: "))
    balance = get_balance(logged_user.get_username())
    if ammount > balance:
        print("Can't withdraw more than you have...")
    else:
        withdraw_money(logged_user.get_username(), balance-ammount)
        print("Money successfully withdrawn!")


def wrapped_deposit(logged_user):
    deposit = float(input("Enter the ammount you would like to deposit: "))
    if deposit <= 0:
        print("Please enter positive value: ")
    else:
        balance = get_balance(logged_user.get_username())
        withdraw_money(logged_user.get_username(), balance + deposit)
        print("Money deposited successfully!")




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

def register_account_info():
    username = input("Please write down the username you would like to use: ")
    password = input("Please write down the password you would like to use: ")
    email = input("Please write down the email you would like to use: ")
    firstname = input("Please write down your first name: ")
    middlename = input("Please write down your middle name: ")
    lastname = input("Please write down your last name: ")
    EGN = input("Please write down your EGN: ")

    return {"username": username
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
                                       result['password'],
                                       result['email'],
                                       result['firstname'],
                                       result['middlename'],
                                       result['lastname'],
                                       result['EGN'])
            print(reg['reason'])

        elif command == 'register-client':
            result = register_client_info()
            reg = register_new_client(result['firstname'],
                                      result['middlename'],
                                      result['lastname'],
                                      result['EGN'])
            print(reg['reason'])

        elif command == 'login':
            result = print_username_password()
            username = result['username']
            password = result['password']

            can_log_in = True
            try:
                logged_user = Account(username=username,
                                      password=password).exists()
                logged_user = convert_to_Account(logged_user)
                logged_user.incr_login_attempts()
            except Exception:
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





def send_reset_password(receiver, new_password):
    TO = receiver
    SUBJECT = "New password"
    TEXT = "Your new passowrd is  {}".format(new_password)
    server = smtplib.SMTP(SERVER, PORT)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, [TO], TEXT)


def generate_new_password():
    n = random.randint(15, 20)
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))

def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print_info()

        elif command == 'changepass':
            old_pass = input("Please enter your old password: ")
            new_pass = input("Enter your new password: ")
            inp = logged_user.change_password(old_pass, new_pass)
            print(inp['reason'])

        elif command == 'reset-password':
            wrapped_reset_password(logged_user)
        
        elif command == 'set-email':
            mail = input("Please enter your email: ")
            logged_user.change_email(mail)

        elif command == 'show-email':
            print(logged_user.get_email())

        elif command == 'show-balance':
            print("Current balance is: {}".format(logged_user.get_balance())

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
def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
