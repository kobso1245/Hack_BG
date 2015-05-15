from Client import *


def register_new_client(firstname, middlename, lastname, EGN):
    cl = Client(firstname=firstname,
           secondname=middlename,
           lastname=lastname,
           EGN=EGN)
    try:
        cl.add()
    except Exception:
        print("dadada")
        return {"result": False,
                "reason": "Client already exist"
                }
def register_new_account(username, password, email, firstname, middlename, lastname, EGN):
    if Client(firstname=firstname,
              secondname=middlename,
              lastname=lastname,
              EGN=EGN):
        pass
    else:
        return False



cl1 = Client(firstname="Kaloyan", secondname="Rumenov", lastname="Evtimov", EGN="9408066345")
cl1.add()
print(cl1.exists())
cl2 = Client(firstname="Kaloyan", secondname="Rumenov", lastname="Evtimov", EGN="9408066346")
print(cl2.exists())

