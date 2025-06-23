from flask import Flask
from Endpoints import routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/process-video": {"origins": "*"}})
    app.register_blueprint(routes.routes)
    return app

if  __name__ == "__main__":
    app = create_app()
    app.run(debug=True)