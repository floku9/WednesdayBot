from Init.init import config
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine(config['Database']['Path'], connect_args={"check_same_thread": False})
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship("User", back_populates="role")


class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    sender_id = Column(String, ForeignKey("users.id"))
    checker_id = Column(String, ForeignKey("users.id"))
    sender = relationship("User", foreign_keys=sender_id)
    checker = relationship("User", foreign_keys=checker_id)


Base.metadata.create_all(bind=engine)
LocalSession = sessionmaker(autoflush=False, bind=engine)


