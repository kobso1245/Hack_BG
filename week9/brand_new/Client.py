from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
#from start import session

Base = declarative_base()
class Account(Base):
    __tablename__ = "Accounts"
    account_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("Clients.client_id"))
    username = Column(String)
    balance = Column(Float) 
    password = Column(String)
    message = Column(String)
    email = Column(String)
    last_logged_in = Column(DateTime)
    last_login_attempt = Column(DateTime)
    login_attempts = Column(Integer)
    #clients = relationship("Client")


    def add(self):
        session.add(self)
        session.commit()

    def get_username(self):
        return self.username

    def get_balance(self):
        return self.balance

    def get_id(self):
        return self.id

    def change_message(self, message):
        self.message = message
        session.commit()

    def change_password(self,old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            session.commit()
        else:
            return {"result": False,
                    "reason": "Wrong password!"
                    }

    def withdraw_money(self, ammount):
        if self.balance < ammount:
            return {"result": False,
                    "reason": "Trying to withdraw more than you have!"
                    }
        else:
            self.balance -= ammount
            session.commit()
            return {"result": True,
                    "reason": ""
                    }

    def deposit_money(self, ammount):
        if ammount <= 0:
            return {"result": False,
                    "reason": "Not possitive value!"
                    }
        else:
            self.balance += ammount
            session.commit()
            return {"result": True,
                    "Reason": ""
                    }


    def get_message(self):
        return self.message


    def get_email(self, email):
        return self.email

    def change_email(self, email):
        self.email = email
        session.commit()

    def get_last_logged_in(self):
        return last_logged_in

    def set_last_logged_in(self, time):
        self.last_logged_in = time
        session.commit()


    def get_last_login_attempt(self):
        return self.last_login_attempt

    def set_last_logged_in_attempt(self, time):
        self.last_login_attempt = time
        session.commit()

    def get_login_attempts(self):
        return self.login_attempts

    def incr_login_attempts(self):
        self.login_attempts += 1
        session.commit()

class Client(Base):
    __tablename__ = "Clients"
    client_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    secondname = Column(String)
    lastname = Column(String)
    EGN = Column(String, unique=True)

    def add(self):
        session.add(self)
        session.commit()


    def exists(self):
        try:
            session.query(Client).filter(Client.firstname==self.firstname,
                                          Client.secondname==self.secondname,
                                          Client.lastname==self.lastname,
                                          Client.EGN==self.EGN).one()
        except NoResultFound:
            return False
        return True
    def get_client_id(self):
        return self.client_id

    def get_name(self):
        return self.firstname + ' ' +self.lastname

    def get_info(self):
        return self.get_name() + ' ' + self.EGN

engine = create_engine("sqlite:///bank.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)
