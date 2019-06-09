#
main.py
import webapp2
from google.cloud import pubsub
class WatchPage(webapp2.RequestHandler):
    def get(self):
    pubsub_client = pubsub.Client()
topic = pubsub_client.topic('api-scheduler')
message_id = topic.publish('ping'.encode('utf-8'))
self.response.write(message_id)
app = webapp2.WSGIApplication([
    ('/watch', WatchPage),
], debug = True)