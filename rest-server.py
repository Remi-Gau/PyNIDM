from flask import Flask, request
from flask_restful import Resource, Api
import glob
from nidm.experiment.tools.rest import RestParser
from flask_cors import CORS
import simplejson

def getTTLFiles():
    return list(glob.glob('/opt/project/ttl/**/*.ttl', recursive=True))

class NIDMRest(Resource):
    def get(self, all):

        query_bits = [f"{a}={request.args.get(a)}" for a in request.args.keys()]
        query = "&".join(query_bits)

        files = getTTLFiles()
        if len(files) == 0:
            return ({'error' : 'No NIDM files found. You may need to add NIDM ttl files to ~/PyNIDM/ttl'})
        restParser = RestParser(output_format=RestParser.OBJECT_FORMAT, verbosity_level=5)

        json_str = simplejson.dumps(restParser.run(files, f"{all}?{query}"), indent=2)
        return app.response_class(
            response=json_str, status=200, mimetype='application/json'
        )

class Instructions(Resource):
    def get(self):

        return {
            'message': f'You probably want to start at {request.url_root}projects  See instructions at PyNIDM/docker/README.md for details on the API and loading data.'
        }



app = Flask(__name__)
CORS(app)
api = Api(app)
api.add_resource(Instructions, '/')
api.add_resource(NIDMRest, '/<path:all>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')