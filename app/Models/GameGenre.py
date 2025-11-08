from app.Models.Base import *
from app.Models.Game import Game
from app.Models.Genre import Genre
from datetime import datetime


class GameGenre(Base):
    id = PrimaryKeyField()
    game = ForeignKeyField(Game, backref='game_genres')
    genre = ForeignKeyField(Genre, backref='genre_games')
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'game_genre'

if __name__ == "__main__":
    connect_db().create_tables([GameGenre])