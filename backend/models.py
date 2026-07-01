from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from database import Base
import enum


class WoWClasses(enum.Enum):
    dk = "Death Knight"
    dh = "Demon Hunter"
    druid = "Druid"
    evoker = "Evoker"
    hunter = "Hunter"
    mage = "Mage"
    monk = "Monk"
    paladin = "Paladin"
    priest = "Priest"
    rogue = "Rogue"
    shaman = "Shaman"
    warlock = "Warlock"
    warrior = "Warrior"


class Members(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    realm = Column(String)
    class_ = Column(Enum(WoWClasses), nullable=False)
    whose = Column(Integer, ForeignKey("members.id"), nullable=False)


