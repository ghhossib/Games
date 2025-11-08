from app.Models.Base import *
from app.Models.Genre import Genre

class Game(Base):
    id = PrimaryKeyField()
    title = CharField(max_length=100)
    developer = CharField(max_length=100)
    releaseYear = TextField(null=True)
    genres = ManyToManyField(Genre, backref='games')
if __name__ == "__main__":
    connect_db().create_tables([Game])