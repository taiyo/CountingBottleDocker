#!/usr/bin/env python
import bottle
import subprocess
import os
import counting

p1 = subprocess.Popen(['ip','addr','show','eth0'],stdout=subprocess.PIPE)
p2 = subprocess.Popen(['sed','-rn',r's/\s*inet\s(([0-9]{1,3}\.){3}[0-9]{1,3}).*/\1/p'],stdin=p1.stdout,stdout=subprocess.PIPE)
p1.stdout.close()
ip_addr = p2.communicate()[0].strip()
p1.wait()

app = bottle.app()

@bottle.route('/')
def root_index():
    return bottle.template('index',ip_addr = ip_addr)

@bottle.route('/json')
def json_reply():
    heads = bottle.request.headers
    bottle.response.content_type = 'application/json'

    response = {'headers':dict(heads),
            'environment':dict(os.environ),
            'response':dict(bottle.response.headers)}
    return response

@bottle.route('/counting')
def create_counting():
    fileName = counting.screenshot()
    counting.crop(fileName)
    os.remove(fileName)
    url = counting.uploadGyazo()
    print url

    heads = bottle.request.headers
    bottle.response.content_type = 'application/json'
    response = {'url':url}
    return response

if __name__=='__main__':
    bottle.debug(True)
    bottle.run(app=app,host='localhost',port=8080)
