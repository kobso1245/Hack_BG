from Client import *
import hashlib
import smtplib
from sending_settings import RECEIVER_EMAIL, SENDER_EMAIL, SENDER_PASSWORD, SERVER, PORT
import random
from sqlalchemy.orm.exc import NoResultFound
import string


def generate_new_password():
    n = random.randint(15, 20)
    return ''.join(
        random.SystemRandom().choice(
            string.ascii_uppercase +
            string.digits) for _ in range(n))


def wrapper_reset_password(username, email):
    new_pass = generate_new_password()
    try:
        logged_user = Account(
            username=username,
            email=email).exists_with_email()
    except NoResultFound:
        return {'result': False,
                'reason': "No account found!"}
    logged_user.password = hash_them_things(new_pass)
    send_reset_password(logged_user.email, new_pass)
    return {'result': True,
            'reason': "Password resetted sucessfully!"
            }


def send_reset_password(receiver, new_password):
    TO = receiver
    SUBJECT = "New password"
    TEXT = "Your new passowrd is  {}".format(new_password)
    server = smtplib.SMTP(SERVER, PORT)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, [TO], TEXT)


def hash_them_things(thing):
    hash_object = hashlib.sha512(thing.encode())
    return hash_object.hexdigest()


def register_new_client(firstname, middlename, lastname, EGN):
    cl = Client(firstname=firstname,
                secondname=middlename,
                lastname=lastname,
                EGN=EGN)
    try:
        cl.add()
    except Exception:
        return {"result": False,
                "reason": "Client already exist"
                }

    return {"result": True,
            "reason": "Client registered successfully!"
            }


def register_new_account(
        username,
        password,
        email,
        firstname,
        middlename,
        lastname,
        EGN):
    cl_id = Client(firstname=firstname,
                   secondname=middlename,
                   lastname=lastname,
                   EGN=EGN)

    exist = cl_id.exists()
    if exist:
        acc = Account(client_id=exist, username=username,
                      password=password, email=email, login_attempts=0)
        try:
            acc.add()
        except Exception as exc:
            return {"result": False,
                    "reason": exc
                    }

        return {"result": True,
                "reason": "Account created successfully!"
                }

    else:
        return {"result": False,
                "reason": "No client with this information found!"
                }
