from flask import Response
from src import app


@app.route('/_health_check', methods=['GET'])
def check():
    resp = Response(status=200, mimetype='application/json')
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
