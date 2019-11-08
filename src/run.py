from flask import Flask, Response

from src.insrastructure import DB
from src.routes.restaurant import restaurant
from src.routes.tables import tables
from src.routes.city import CityView

from flask_restful import Resource, Api



def setup_db():
    DB['restaurant'] = []
    DB['table'] = []
    DB['city'] = []


def create_app():
    setup_db()
    app = Flask(__name__, instance_relative_config=False)
    api = Api(app)

    # api.add_resource(CityView, '/city')
    api.add_resource(CityView, '/city/<string:id_>') #- here?


    with app.app_context():
        app.register_blueprint(restaurant)
        app.register_blueprint(tables)
        return app


app = create_app()


@app.route('/_health_check', methods=['GET'])
def check():
    resp = Response(status=200, mimetype='application/json')
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
