"""
Contains the SQLAlchemy models for the API
"""

import api

from sqlalchemy import Table, Column, DateTime
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

group_team_table = Table("group_team_table", Base.metadata,
                         Column("gid", String, ForeignKey("group.gid")),
                         Column("tid", String, ForeignKey("team.tid")))

class Group(Base):
    __tablename__ = 'group'

    gid = Column(String(50), primary_key=True)
    name = Column(String(50))

    owner = Column(String, ForeignKey('teacher.uid'))
    members = relationship("Team", secondary=group_team_table, backref="groups")

class Team(Base):
    __tablename__ = 'team'

    tid = Column(String(50), primary_key=True)
    name = Column(String(50), unique=True)

    password = Column(String(50))
    school = Column(String(42))

    size = Column(Integer())
    eligible = Column(Boolean())

    members = relationship("Competitor", backref="team", single_parent=True)

    def __repr__(self):
        return '<Team %r>' % self.name

class User(Base):
    __tablename__ = 'user'

    uid = Column(String(50), primary_key=True)
    name = Column(String(50), unique=True)
    password_hash = Column(String(42))

    disabled = Column(Boolean())

    role = Column(String(20))

    background = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    country = Column(String(50))
    email = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.disabled = False

    def __repr__(self):
        return '<User %r>' % self.name

class Teacher(User):
    __tablename__ = 'teacher'

    uid = Column(String, ForeignKey('user.uid'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
    }

    def __init__(self, **kwargs):
        super(Teacher, self).__init__(**kwargs)
        self.role = self.__class__.__name__

    def __repr__(self):
        return '<Teacher %r>' % self.name

class Competitor(User):
    __tablename__ = 'competitor'

    uid = Column(String, ForeignKey('user.uid'), primary_key=True)
    tid = Column(String, ForeignKey("team.tid"))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
    }

    def __init__(self, **kwargs):
        super(Competitor, self).__init__(**kwargs)
        self.role = self.__class__.__name__

    def __repr__(self):
        return '<Competitor %r>' % self.name
