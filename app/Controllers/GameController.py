from app.Models.Game import Game
from app.Models.Genre import Genre
from app.Models.GameGenre import GameGenre
from datetime import datetime


class GameController:

    @classmethod
    def add(cls, title, developer, releaseYear):
        Game.create(
            title=title,
            developer=developer,
            releaseYear=releaseYear
        )

    @classmethod
    def get(cls):
        return Game.select()

    @classmethod
    def show(cls, id):
        return Game.get_by_id(id)

    @classmethod
    def add_genre_to_game(cls, game_id, genre_id):

        GameGenre.create(game=game_id, genre=genre_id, created_at=datetime.now())

    @classmethod
    def get_game_genres(cls, game_id):
        return (Genre.select().join(GameGenre).where(GameGenre.game == game_id))

    @classmethod
    def remove_genre_from_game(cls, game_id, genre_id):

        query = GameGenre.delete().where(
            (GameGenre.game == game_id) & (GameGenre.genre == genre_id)
        )
        return query.execute()