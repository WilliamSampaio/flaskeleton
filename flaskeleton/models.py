from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DoDoStatus(Base):
    __tablename__ = 'to_do_status'

    id = Column(Integer, primary_key=True)
    description = Column(String(50), nullable=False)


class ToDoList(Base):
    __tablename__ = 'to_do_list'

    id = Column(Integer, primary_key=True)
    description = Column(String(50), nullable=False)
    to_do_status_id = Column(
        Integer, ForeignKey('to_do_status.id'), nullable=False
    )
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=True)
