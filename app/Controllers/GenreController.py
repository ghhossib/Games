from app.Models.Genre import Genre
from app.Models.GameGenre import GameGenre


class GenreController:

    @classmethod
    def add(cls, name):
        Genre.create(name=name)

    @classmethod
    def get(cls):
        return Genre.select()

    @classmethod
    def show(cls, id):
        return Genre.get_by_id(id)

    @classmethod
    def update(cls, id, **fields):
        Genre.update(**fields).where(Genre.id == id).execute()

    @classmethod
    def delete(cls, id):
        Genre.delete_by_id(id)

    @classmethod
    def get_games_by_genre(cls, genre_id):
        """Получить все игры жанра"""
        from app.Models.Game import Game
        return (Game
                .select()
                .join(GameGenre)
                .where(GameGenre.genre == genre_id))