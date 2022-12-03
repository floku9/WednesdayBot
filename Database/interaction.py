from Database.core import Base
from sqlalchemy.orm import Session


class Interactor:
    def __init__(self, db_session: Session):
        self.session = db_session

    def create(self, db_object: Base):
        self.session.add(db_object)
        self.session.commit()

    def find(self, db_table: Base, **find_parameters):
        satisfy_objects = self.session.query(db_table).filter_by(**find_parameters).scalar()
        return satisfy_objects
