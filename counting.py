# coding: utf-8

import ConfigParser
import glob
import os
import slackweb
from gyazo import Api

conf = ConfigParser.SafeConfigParser()
conf.read('./setting.conf')

def crop(file):
    x = 0
    y = 70
    width = 500
    height = 280

    cmd = "convert %s -crop '%dx%d+%d+%d' counting.png"%(file, width, height, x, y)
    print cmd
    os.system(cmd)

def screenshot():
    url = conf.get('Counting', 'url')
    cmd = "webkit2png -x 1280 1024 -o countingfull.png " + url
    print cmd
    os.system(cmd)
    files = glob.glob('./*full.png')
    return files[0]

def uploadGyazo():
    token = conf.get('Gyazo', 'access_token')
    api = Api(access_token=token)

    url = ""
    with open('./counting.png', 'rb') as f:
        image = api.upload_image(f)
        dict = image.to_dict()
        url = dict['url']
    return url

def postSlack(image_url):
    url = conf.get('Slack', 'url')
    slack = slackweb.Slack(url=url)
    attachments = []
    attachment = {'image_url': image_url,'text': 'test'}
    attachments.append(attachment)
    slack.notify(attachments=attachments)

if __name__ == '__main__':
    file = screenshot()
    crop(file)
    os.remove(file)
    url = uploadGyazo()
    print url
    #postSlack(url)

