from flask_restful import Resource
import urllib2
import json
import redis

class Laundry(Resource):
    def get(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        #print str(json.load(response))
        
        output = json.loads(r.get('app.tasks.laundry'))
        return output
