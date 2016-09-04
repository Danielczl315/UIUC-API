from __future__ import absolute_import






import urllib2
import json
import redis
from tasks.celery import app


@app.task(name='laundry.update')
def laundry_update():
    request_url = "http://23.23.147.128/homes/mydata/urba7723"
    response = urllib2.urlopen(request_url)
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
#    st = json.dumps(json.load(response))
#r.set('app.tasks.laundry', st)
#print str(json.load(response))

#output = json.loads(r.get('app.tasks.laundry'))
#print output
