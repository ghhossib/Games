from app.Models.Base import *

class Genre(Base):
    id = PrimaryKeyField()
    name = CharField(max_length=100)
if __name__ == "__main__":
    connect_db().create_tables([Genre])