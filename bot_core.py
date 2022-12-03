from Database.interaction import Interactor
import Database.core as db_core
from sqlalchemy.orm import Session


class BotCore:
    def __init__(self, db_session: Session):
        self.db_interactor = Interactor(db_session)

    def add_new_user(self, user_id):
        common_user_role = self.db_interactor.find(db_core.Role, name="user")

        new_user = db_core.User(telegram_id=user_id, role=common_user_role)
        self.db_interactor.create(new_user)
