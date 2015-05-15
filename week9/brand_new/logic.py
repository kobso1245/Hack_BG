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

    return {"result": True,
            "reason": "Client registered successfully!"
            }

def register_new_account(username, password, email, firstname, middlename, lastname, EGN):
    cl_id = Client(firstname=firstname,
              secondname=middlename,
              lastname=lastname,
              EGN=EGN)
        
    if cl_id:
        acc = Account(client_id=cl_id, username=username,
                      password=password, email=email)
        try:
            acc.add()
        except Exception:
            return {"result": False,
                    "reason": "Username already exist!"
                    }

        return {"result": True,
                "reason": "Account created successfully!"
                }

    else:
        return {"result": False,
                "reason": "No client with this information found!"
                }


cl1 = Client(firstname="Kaloyan", secondname="Rumenov", lastname="Evtimov", EGN="9408066345")
cl1.add()
print(cl1.exists())
cl2 = Client(firstname="Kaloyan", secondname="Rumenov", lastname="Evtimov", EGN="9408066346")
print(cl2.exists())

