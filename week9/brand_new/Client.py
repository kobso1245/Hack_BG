from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
#from start import session

Base = declarative_base()
class Client(Base):
    __tablename__ = "Clients"
    username = Column(String)
    balance = Column(Float)
    id = Column(Integer, primary_key=True)
    message = Column(String)
    email = Column(String)
    last_logged_in = Column(DateTime)
    last_loging_attempt = Column(DateTime)

    def add(self):
        session.add(self)
        session.commit()

    def get_username(self):
        return self.username

    def get_balance(self):
        return self.balance

    def get_id(self):
        return self.id

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

    def set_message(self, new_message):
        self.message = new_message

    def get_email():
        return


engine = create_engine("sqlite:///bank.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)

