import peewee
from flask import Blueprint, jsonify, request
from app.Controllers.GenreController import GenreController

genre_bp = Blueprint('genre', __name__, url_prefix='/genre')



@genre_bp.route('/', methods=['GET'])
def get_genres():
    genres = GenreController.get()
    genres_list = []
    for genre in genres:
        genres_list.append({
            'id': genre.id,
            'name': genre.name,
        })
    return jsonify({
        'success': True,
        'genres': genres_list
    }), 200



@genre_bp.route('/', methods=['POST'])
def add_genre():
    try:
        data_genre = request.get_json()
        name = data_genre['name']
        GenreController.add(name=name)
        return jsonify({
            'success': True,
            'message': 'Жанр добавлен',
        }), 200
    except peewee.IntegrityError as error:
        return jsonify(
            {
                'success': False,
                'message': 'жанр не добавлен',
                'error': str(error)
            }
        ),400



@genre_bp.route('/<int:genre_id>/games', methods=['GET'])
def get_genre_games(genre_id):
    games = GenreController.get_games_by_genre(genre_id)

    games_list = []
    for game in games:
        games_list.append({
            'id': game.id,
            'title': game.title,
            'developer': game.developer,
            'releaseYear': game.releaseYear
        })

    return jsonify({
        'success': True,
        'genre_id': genre_id,
        'games': games_list
    }), 200