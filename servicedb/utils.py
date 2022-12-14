from sqlalchemy.orm import Session
from servicedb.models import Appeal
import json


def create_appeal(data, db):
    appeal = Appeal(
        name=data["name"],
        last_name=data["last_name"],
        second_name=data["second_name"],
        phone_number=int(data["phone_number"]),
        text=data["text"],
    )
    db.add(appeal)
    db.commit()
