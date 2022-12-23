import traceback

from flask import Flask
from flask import Response
from flask import request
from flask_restful import Resource, Api

import schedule
from Runner import ServerJob

from FlaskOperations import Operations

from LogErrors import LogErrors


app = Flask(__name__)
api = Api(app)
instance_of_runner = ServerJob()


class CostsToday(Resource):
    def post(self):
        if bool(Operations.getJsonPriceContents()):
            return Operations.getJsonPriceContents()
        else:
            return Response({'Contents': None}, content_type='application/json')


class ErrorsToday(Resource):
    def post(self):
        return Operations.getErrorContents()


api.add_resource(CostsToday, '/')
api.add_resource(ErrorsToday, '/errors')
LogErrors.logError('Testing start')

schedule.every(20).seconds.do(instance_of_runner.run)
app.run(debug=False)
