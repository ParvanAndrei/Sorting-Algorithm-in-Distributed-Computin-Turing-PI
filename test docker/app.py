from flask import Flask
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

class sayHello(Resource):
    def get(self):
        return {'hello': 'world'}
class sayHello3(Resource):
    def get(self):
        return {'hello':'cox'}
api.add_resource(sayHello3, '/worker3')
api.add_resource(sayHello, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))