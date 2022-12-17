import traceback

from flask import Flask
from flask_restful import Resource, Api

from apscheduler.schedulers.background import BackgroundScheduler
from Runner import ServerJob

from FlaskOperations import Operations

from LogErrors import LogErrors


app = Flask(__name__)
api = Api(app)


class CostsToday(Resource):
    def get(self):
        return Operations.getJsonPriceContents()


class ErrorsToday(Resource):
    def get(self):
        return Operations.getErrorContents()


api.add_resource(CostsToday, '/')
api.add_resource(ErrorsToday, '/errors')
LogErrors.logError('Testing start')


if __name__ == '__main__':
    try:
        SERVERJOB = ServerJob()
        schedule = BackgroundScheduler(daemon=True)
        schedule.add_job(SERVERJOB.run, 'interval', seconds=20)
        schedule.start()
        LogErrors.logError('Testing startup')
    except:
        print(traceback.print_exc())
        LogErrors.logError('Error happened')
    app.run(debug=False)
