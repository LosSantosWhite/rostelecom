from sqlalchemy import Column, Integer, String, BigInteger

from servicedb.db import Base


class Appeal(Base):
    __tablename__ = "appeal"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String, index=True)
    second_name = Column(
        String,
    )
    phone_number = Column(BigInteger, index=True)
    text = Column(String, index=True)
