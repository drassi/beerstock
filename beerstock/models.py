from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    )

from zope.sqlalchemy import ZopeTransactionExtension

from datetime import datetime

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class ItemType(Base):

    __tablename__ = 'item_type'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    added = Column(DateTime, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.added = datetime.utcnow()

class Item(Base):

    __tablename__ = 'item'

    id = Column(Text, primary_key=True)
    item_type_id = Column(Integer, ForeignKey('item_type.id'), nullable=False)
    added = Column(DateTime, nullable=False)

    item_type = relationship(ItemType, backref='items')

    def __init__(self, id, item_type):
        self.id = id
        self.item_type = item_type
        self.added = datetime.utcnow()
