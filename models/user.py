#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This is the class for user attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
<<<<<<< HEAD
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
=======
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

<<<<<<< HEAD
    places = relationship('Place', cascade='all, delete' backref='user')
    reviews = relationship('Review', cascade='all, delete' backref='user')
=======
    places = relationship('Place', cascade='all, delete', backref='user')
    reviews = relationship('Review', cascade='all, delete', backref='user')
    
>>>>>>> 80c254acfcdcca816045c7346fab87d9c735758e
>>>>>>> 45191c419fa45eb59f0d5b67ad4de6bcba7379ff
