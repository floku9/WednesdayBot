from Database.interaction import Interactor
from Database.core import *
from sqlalchemy.orm import Session
from abc import ABC
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

class AbstractUser(ABC):
    def __init__(self, user_info: User):
        self.user_info = user_info

    def get_keyboard(self) -> ReplyKeyboardMarkup:
        pass


class RegularUser(AbstractUser):
    def get_keyboard(self) -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.add(KeyboardButton("Dude"))
        return markup


class AdminUser(AbstractUser):
    def get_keyboard(self) -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup()
        markup.add(KeyboardButton("Dude"))
        markup.add(KeyboardButton("Make it wednesday"))
        return markup


def define_user_class(user_from_db: User) -> AbstractUser:
    if user_from_db.role.name == "admin":
        return AdminUser(user_from_db)
    else:
        return RegularUser(user_from_db)


class BotCore:
    def __init__(self, db_session: Session):
        self.db_interactor = Interactor(db_session)

    def add_new_user(self, user_id):
        common_user_role = self.db_interactor.find(Role, name="user")

        new_user = User(telegram_id=user_id, role=common_user_role)
        self.db_interactor.create(new_user)

    def get_keyboard_for_user(self, user_id):
        db_user = self.db_interactor.find(User, telegram_id=user_id)
        user_class = define_user_class(db_user)
        return user_class.get_keyboard()
