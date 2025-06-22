from flask import Flask
from Endpoints import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes.routes)
    return app


if  __name__ == "__main__":
    app = create_app()
    app.run(debug=True)