import traceback

from flask import Flask
from flask_restful import Resource, Api

import schedule
from Runner import ServerJob

from FlaskOperations import Operations

from LogErrors import LogErrors


app = Flask(__name__)
api = Api(app)
SERVERJOB = ServerJob()


class CostsToday(Resource):
    def get(self):
        SERVERJOB.run()
        return Operations.getJsonPriceContents()


class ErrorsToday(Resource):
    def get(self):
        return Operations.getErrorContents()


api.add_resource(CostsToday, '/')
api.add_resource(ErrorsToday, '/errors')
LogErrors.logError('Testing start')


app.run(debug=False)
