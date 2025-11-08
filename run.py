from flask import Flask,jsonify,request
import locale

from app.Routes.GameRoute import game_bp
from app.Routes.GenreRoute import genre_bp

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
application = Flask(__name__)

application.register_blueprint(game_bp)
application.register_blueprint(genre_bp)


if __name__ == "__main__":
    application.run(debug=True,port=5111)
