from flask import Blueprint, jsonify, request
from app.Controllers.GameController import GameController

game_bp = Blueprint('game', __name__, url_prefix='/game')



@game_bp.route('/', methods=['GET'])
def get_games():
    games = GameController.get()
    games_list = []
    for game in games:
        # Получаем жанры для каждой игры
        genres = GameController.get_game_genres(game.id)
        genres_list = []
        for genre in genres:
            genres_list.append({
                'id': genre.id,
                'name': genre.name
            })

        games_list.append({
            'id': game.id,
            'title': game.title,
            'developer': game.developer,
            'releaseYear': game.releaseYear,
            'genres': genres_list  # Добавляем жанры
        })
    return (jsonify
        ({
        'success': True,
        'games': games_list
    }), 200)



@game_bp.route('/', methods=['POST'])
def add_game():
    data_game = request.get_json()
    title = data_game['title']
    developer = data_game['developer']
    releaseYear = data_game['releaseYear']
    GameController.add(title=title, developer=developer, releaseYear=releaseYear)
    return (jsonify
            ({
            'success': True,
            'message': 'Игра добавлена'
            }),200)



@game_bp.route('/<int:id>', methods=['GET'])
def get_game(id):
    game = GameController.show(id)
    return jsonify({
        'success': True,
        'game': {
            'id': game.id,
            'title': game.title,
            'developer': game.developer,
            'releaseYear': game.releaseYear
        }
    }), 200



@game_bp.route('/<int:game_id>/genres/<int:genre_id>', methods=['POST'])
def assign_genre_to_game(game_id, genre_id):
    GameController.add_genre_to_game(game_id, genre_id)
    return jsonify({
        'success': True,
        'message': 'Жанр назначен игре'
    }), 200



@game_bp.route('/<int:game_id>/genres', methods=['GET'])
def get_game_genres(game_id):
    genres = GameController.get_game_genres(game_id)

    genres_list = []
    for genre in genres:
        genres_list.append({
            'id': genre.id,
            'name': genre.name
        })

    return jsonify({
        'success': True,
        'game_id': game_id,
        'genres': genres_list
    }), 200