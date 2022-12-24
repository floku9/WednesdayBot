from Init.init import config
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from enum import Enum


engine = create_engine(config['Database']['Path'], connect_args={"check_same_thread": False})
Base = declarative_base()


class RoleType(Enum):
    user = 'user'
    admin = 'admin'
    moderator = 'moderator'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users", enable_typechecks=False)


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    users = relationship("User", back_populates="role")


class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    sender_id = Column(String, ForeignKey("users.id"))
    checker_id = Column(String, ForeignKey("users.id"))
    approve_status = Column(String)
    sender = relationship("User", foreign_keys=sender_id)
    checker = relationship("User", foreign_keys=checker_id)


Base.metadata.create_all(bind=engine)
Session = sessionmaker(autoflush=False, bind=engine)
session = Session()

# Add roles from Enum if they are not in table yet
session.bulk_insert_mappings(Role, [
    {'name': role.value} for role in RoleType
    if role.value not in [str(name[0]) for name in session.query(Role.name).all()]
])

session.commit()